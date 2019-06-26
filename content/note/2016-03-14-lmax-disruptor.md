---
layout: post
title: LMAX Disruptor
categories: blog
tags:
  - queues
  - concurrency
  - threads
  - asynchronous
  - events
  - patterns
  - disruptor
excerpt: The Disruptor is a general-purpose pattern for building low-latency, high-throughput event processing queues.
---

## Contents
{:.no_toc}

- TOC
{:toc}

## The Design of the LMAX Disruptor
- queues conflate several data-storage concerns for handling the needs of producers and consumers. The Disruptor separates these concerns.
- Ensure that any data are owned by only one thread for write access, eliminating write contention. This is the Disruptor design.
- At the heart of the disruptor is a pre-allocated bounded data structure in the form of a ring buffer. Data is added to the ring buffer through one or more producers, and processed by one or more consumers.

### The Class Diagram
This is my attempt to recreate the original class diagram. My skills with the [dot tool](http://graphviz.org/) aren't quite up to the task (though, it may be that's just not the right tool to use to create a SVG version of a class diagram).

<figure>
  <img class="content-image"
       src="/img/disruptor.svg">
  <figcaption>
    <strong>Fig. 1 | </strong> The Disruptor class relationships.
  </figcaption>
</figure>

Another thing to note is that the implementation of the LMAX disruptor has drifted away from this diagram. For one thing, the code no longer refers to `Entry` objects, but `Event` objects instead.

It may be best to refer to the [LMAX Disruptor Wiki](https://github.com/LMAX-Exchange/disruptor/wiki/Introduction). The introduction provides several important definitions:

Ring Buffer
:   The Ring Buffer is often considered the main aspect of the Disruptor, however from 3.0 onwards the Ring Buffer is only responsible for the storing and updating of the data (Events) that move through the Disruptor. And for some advanced use cases can be completely replaced by the user.

Sequence
:   The Disruptor uses `Sequence`s as a means to identify where a particular component is up to. Each consumer (`EventProcessor`) maintains a `Sequence` as does the Disruptor itself. The majority of the concurrent code relies on the movement of these `Sequence` values, hence the Sequence supports many of the current features of an `AtomicLong`. In fact the only real difference between the two is that the Sequence contains additional functionality to prevent false sharing between `Sequence`s and other values.

Sequencer
:   The `Sequencer` is the *real* core of the Disruptor. The two implementations of this interface (single producer and multi-producer) define all of the concurrent algorithms used for fast, correct passing of data between producers and consumers.

Sequence Barrier
:   The Sequence Barrier is produced by the `Sequencer` and contains references to the main published `Sequence` from the `Sequencer` and the `Sequence`s of any dependent consumer. It contains the logic to determine if there are any events available for the consumer to process.

Wait Strategy
:   The Wait Strategy determines how a consumer will wait for events to be placed into the Disruptor by a producer.

Event
:   The unit of data passed from producer to consumer. There is no specific code representation of the Event as it defined entirely by the user.

`EventProcessor`
:   The main event loop for handling events from the Disruptor and has ownership of consumer's `Sequence`. There is a single representation called `BatchEventProcessor` that contains an efficient implementation of the event loop and will call back onto a user supplied implementation of the `EventHandler` interface.

`EventHandler`
:   An interface that is implemented by the user and represents a consumer for the Disruptor.

Producer
:   This is the user code that calls the Disruptor to enqueue `Events`. This concept also has no representation in the code.

<figure>
<img class="content-image" src="/img/LMAX-Disruptor-Models.png">
<figcaption>
    <strong>Fig. 2 | </strong> Relationships among the main classes and interfaces.
</figcaption>
</figure>

### The Ring Buffer
A ring buffer can store either an array of pointers to entries (which are really messages or events to pass among threads in the same process), or an array of objects (instances of a structure) representing the entries. Pre-allocating entries eliminates issues in languages that support garbage collection, since the entries will be reused and live for the duration of the Disruptor instance.

In Java, entries in ring buffers must be pointers to objects. On creation of the ring buffer, the Disruptor utilizes the Abstract Factory pattern to pre-allocate the entries. When an entry is claimed, a producer can copy its data into it.

In C++, entries can be items in a `std::array` and a move assignment operator can be used by the producer to copy its data into the claimed entry.

Like any good moving target, things change. Trisha Gee's article [Dissecting The Disruptor](http://trishagee.github.io/post/dissecting_the_disruptor_demystifying_memory_barriers/) references a file called `AbstractEntry.java`, where I presume the `Entry` interface from the class diagram above is defined. That file no longer exists. Perhaps it's been refactored into the Event* files (`EventFactory.java`, `EventHandler.java`, etc.). Nevertheless, the current implementation has moved on from her original description.

Now that I've looked at some of the code, it may be that only the terminology changed, moving from *entries* to *events*. Also, note that the `RingBuffer` class implements [Cursored](#cursored-interface), [EventSequencer](#eventsequencer-interface) and [EventSink](#eventsink-interface).

The `RingBuffer` in the LMAX Disruptor contains the following fields:

```java
    // Padding to prevent cache-line sharing
    protected long p1, p2, p3, p4, p5, p6, p7;

    // Fields to enforce some initialization and scaling constraints
    private static final int BUFFER_PAD;
    private static final long REF_ARRAY_BASE;
    private static final int REF_ELEMENT_SHIFT;
    private static final Unsafe UNSAFE = Util.getUnsafe();

    // Data fields
    private final long indexMask;
    private final Object[] entries;
    protected final int bufferSize;
    protected final Sequencer sequencer;
```

Associated with those fields is a static block (which is a block of statements that will be executed when the RingBufferFields class is first loaded into the JVM), a constructor, and two methods:

```java
    // Initialization of class static values
    static
    {
        final int scale = UNSAFE.arrayIndexScale(Object[].class);
        if (4 == scale)
        {
            REF_ELEMENT_SHIFT = 2;
        }
        else if (8 == scale)
        {
            REF_ELEMENT_SHIFT = 3;
        }
        else
        {
            throw new IllegalStateException("Unknown pointer size");
        }
        BUFFER_PAD = 128 / scale;
        // Including the buffer pad in the array base offset
        REF_ARRAY_BASE = UNSAFE.arrayBaseOffset(Object[].class) + (BUFFER_PAD << REF_ELEMENT_SHIFT);
    }

    // The fields constructor (details elided)
    RingBufferFields(EventFactory<E> eventFactory, Sequencer sequencer) {...}

    // Used by the constructor to initialize the entries array by callling the eventFactory's
    // newInstance() method.
    private void fill(EventFactory<E> eventFactory) {...}

    // Enables the RingBuffer to access an entry in the entries array.
    protected final E elementAt(long sequence) {...}
```

The `EventFactory` is just an interface template that has one function, `newInstance`, which returns an instance of its template argument, which should be a type of Event.

```java
public interface EventFactory<T>
{
    T newInstance();
}
```

The `EventFactory` could be implemented in C++ in a number of ways. One set of implementations could be created through policy-based class design as proposed by Andrei Alexandrescu in his book "Modern C++ Design: Generic Programming and Design Patterns Applied." Here are the creation policies from his book with the `Create` method renamed to `newInstance`:

```cpp
template <typename T>
struct OpNewCreator
{
    static T* newInstance()
    {
        return new T;
    }

protected:
    /**
     * Avoid the overhead of a virtual destructor in policy classes.
     * Host classes often publically inherit from policy classes. A protected
     * destructor will ensure that users can't convert a pointer to a host-class
     * object into a pointer to a policy-class object and then attempt to delete
     * the host object through that pointer.
     */
    ~OpNewCrator() {}
};

template <typename T>
struct MallocCreator
{
    static T* newInstance()
    {
        void *buf = std::malloc(sizeof(T));
        if (!buf) return 0;

        // Execute T's constructor
        return new(buf) T;
    }

protected:
    /**
     * Avoid the overhead of a virtual destructor in policy classes.
     * Host classes often publically inherit from policy classes. A protected
     * destructor will ensure that users can't convert a pointer to a host-class
     * object into a pointer to a policy-class object and then attempt to delete
     * the host object through that pointer.
     */
    ~MallocCreator() {}
};

template <typename T>
struct PrototypeCreator
{
    PrototypeCreator(T* obj = 0) : prototype_(obj) {}

    T* newInstance()
    {
        // If we have a prototype, clone it.
        return prototype_ ? prototype_->clone() : 0;
    }

    T* getPrototype() {return prototype_;}

    void setPrototype(T* obj) {prototype_ = obj;}

private:
    T* prototype_;

protected:
    /**
     * Avoid the overhead of a virtual destructor in policy classes.
     * Host classes often publically inherit from policy classes. A protected
     * destructor will ensure that users can't convert a pointer to a host-class
     * object into a pointer to a policy-class object and then attempt to delete
     * the host object through that pointer.
     */
    ~PrototypeCreator() {}
};
```

Stop the presses! The Java-based ring buffer is an array of pointers to some type of event object. In C++, we don't have to use pointers, so we don't need a factory method to create instances of an event and we don't need a `fill` method to populate the entries in the ring buffer. All we need to create an array of events is a class that has a default constructor.

If we can't have a default constructor, then it might be possible to clone a prototype object, or define another method for initialization. In this case, we don't want a factory so much as an initializer. In the end, it's the same idea as the factory, but the method should be named `initializeEvent` instead of `newInstance`.

```cpp
template <typename T>
struct EmptyInitializer
{
    void initializeEvent(T event) {}

protected:
    /**
     * Avoid the overhead of a virtual destructor in policy classes.
     * Host classes often publically inherit from policy classes. A protected
     * destructor will ensure that users can't convert a pointer to a host-class
     * object into a pointer to a policy-class object and then attempt to delete
     * the host object through that pointer.
     */
    ~EmptyInitializer() {}
};

template <typename T>
struct DoInitInitializer
{
    void initializeEvent(T& event) {event.doInit();}

protected:
    /**
     * Avoid the overhead of a virtual destructor in policy classes.
     * Host classes often publically inherit from policy classes. A protected
     * destructor will ensure that users can't convert a pointer to a host-class
     * object into a pointer to a policy-class object and then attempt to delete
     * the host object through that pointer.
     */
    ~DoInitInitializer() {}
};

template <typename T typename A>
struct DoInitArgInitializer
{
    void initializeEvent(T& event, A& arg) {event.doInit(arg);}
    void initializeEvent(T& event, const A& arg) {event.doInit(arg);}

protected:
    /**
     * Avoid the overhead of a virtual destructor in policy classes.
     * Host classes often publically inherit from policy classes. A protected
     * destructor will ensure that users can't convert a pointer to a host-class
     * object into a pointer to a policy-class object and then attempt to delete
     * the host object through that pointer.
     */
    ~DoInitArgInitializer() {}
};
```

The `RingBuffer` constructor first checks that the size is both at least 1 and is a power of 2. If these conditions aren't met, it throws an `IllegalArgumentException`.

The constructor is passed an `EventFactory`, which it uses to populate the `RingBuffer`'s array of entries. The `RingBuffer` doesn't hold on to the supplied factory. However, the constructor is also passed an instance of a `Sequencer`, to which it does keep a reference.

It seems to me the RingBuffer interface in C++ looks like:

```cpp
// An arbitrary default size for a RingBuffer
constexpr size_t DefaultRingBufferCapacity = 1024;

template<class Config_, size_t Capacity = DefaultRingBufferCapacity>
class RingBuffer : public Config_
{
public:
    typedef Config_                             Config;
    typedef typename Config::Event              Event;
    typedef typename Config::EventInitializer   EventInitializer;
    typedef typename Config::Sequencer          Sequencer;

    RingBuffer(EventInitializer& initializer)
    {
        for (size_t i = 0; i < Capacity; ++i)
        {
            initializer.initializeEvent(entries[i]);
        }
    }

    /**
     * Cursored interface.
     * Get the current cursor value.
     *
     * @return current cursor value
     */
     i64 getCursor() {return sequencer.getCursor();}

     constexpr size_type capacity() const {return Capacity;}

protected:
    Sequencer   sequencer;

private:
    const size_type                   next_{0};
    const std::array<value_type, Capacity> entries_{};

    DISALLOW_COPY_MOVE_AND_ASSIGN(RingBuffer);
};
```

### The Sequence Class

```java
public class Sequence extends RhsPadding
{
    static final long INITIAL_VALUE = -1L;
    private static final Unsafe UNSAFE;
    private static final long VALUE_OFFSET;

    static
    {
        UNSAFE = Util.getUnsafe();
        try
        {
            VALUE_OFFSET = UNSAFE.objectFieldOffset(Value.class.getDeclaredField("value"));
        }
        catch (final Exception e)
        {
            throw new RuntimeException(e);
        }
    }

    // Create a sequence initialized to -1.
    public Sequence() {this(INITIAL_VALUE);}

    // Create a sequence with a specific initial value
    public Sequence(final long initialValue) {...}

    // Volatile read of the sequence.
    public long get() {return value;}

    // Ordered write. Place a Store/Store barrier between this write and any previous write.
    public void set(final long value) {...}

    // Volatile write. Place a Store/Store barrier between this write and any previous write,
    // and a Store/Load barrier between this write and any subsequent volatile read.
    public void setVolatil(final long value) {...}

    // Perform a compare and set (CAS) operation on the sequence
    public boolean compareAndSet(final long expectedValue, final long newValue) {...}

    // Atomically increment the sequence by one
    public long incrementAndGet() {return addAndGet(1L);}

    // Atomic add the supplied value
    public long addAndGet(final long increment) {...}
    public String toString() {return Long.toString(get());}
}
```

### The Sequencer Class
The `Sequencer` is defined as an interface that extends [Cursored](#cursored-interface) and [Sequenced](#sequenced-interface). It is the *real* core of the Disruptor. The two implementations of this interface (single producer and multi-producer) define all of the concurrent algorithms used for fast, correct passing of data between producers and consumers.

So, the entire interface for a `Sequencer` is:

```java
public interface Cursored
{
    long getCursor();
}

public interface Sequenced
{
    int getBufferSize();
    boolean hasAvailableCapacity(final int requiredCapacity);
    long remainingCapacity();
    long next();
    long next(int n);
    long tryNext() throws InsufficientCapacityException;
    long tryNext(int n) throws InsufficientCapacityException;
    void publish(long sequence);
    void publish (long lo, long hi);
}

public interface Sequencer extends Cursored, Sequenced
{
    // We add the following declarations to Cursored and Sequenced interfaces.
    long INITIAL_CURSOR_VALUE = -1L;
    void claim(long sequence);
    boolean isAvailable(long sequence);
    void addGatingSequences(Sequence... gatingSequences);
    boolean removeGatingSequence(Sequence sequence);
    SequenceBarrier newBarrier(Sequence... sequencesToTrack);
    long getMinimumSequence();
    long getHighestPublishedSequence(long nextSequence, long availableSequence);
    <T> EventPoller<T> newPoller(DataProvider<T> provider, Sequence... gatingSequences);
}

// Let's see which methods of Sequencer are implemented by AbstractSequencer
public abstract class AbstractSequencer implements Sequencer
{
    // We have a few private and protected data members
    private static final AtomicReferenceFieldUpdater<AbstractSequencer, Sequence[]> SEQUENCE_UPDATER =
        AtomicReferenceFieldUpdater.newUpdater(AbstractSequencer.class, Sequence[].class, "gatingSequences");

    protected final int bufferSize;
    protected final WaitStrategy waitStrategy;
    protected final Sequence cursor = new Sequence(Sequencer.INITIAL_CURSOR_VALUE);
    protected volatile Sequence[] gatingSequences = new Sequence[0];

    // We have a constructor
    public AbstractSequencer(int bufferSize, WaitStrategy waitStrategy) {...}

    // From the Cursored interface
    public final long getCursor() {return cursor.get();}
}
```

### Cursored Interface
The `Cursored` interface declares a single function `long getCursor();` to get the current value of the cursor.

### Sequenced Interface
The `Sequenced` interface is larger. Each consumer (aka, EventProcessor) maintains a `Sequence` as does the Disruptor itself. The majority of the concurrent code relies on the movement of these `Sequence` values, hence the `Sequence` acts very much like an `AtomicLong`.

- `int getBufferSize();`: returns the capacity of the ring buffer.
- `boolean hasAvailableCapacity(final int requiredCapacity);`: return true if the buffer has the capacity to allocate the next sequence, otherwise return false.
- `long remainingCapacity();`: get the remaining capacity for this Sequencer.
- `long next();`: claim the next event in the sequence for publishing. It returns the value of the claimed sequence.
- `long next(int n);`: for producing a batch of events; claim the next `n` events in the sequence for publishing.
- `long tryNext() throws InsufficientCapacityException;`: Attempt to claim the next event in sequence for publishing. This will return the number of the slot if there is at least `requiredCapacity` slots available.
- `long tryNext(int n) throws InsufficientCapacityException;`: Attempt to claim the next `n` events in sequence for publishing. It returns the highest numbered slot if there is at least `requiredCapacity` slots available.
- `void publish(long sequence);`: Publishes a sequence. Call when the event has been filled.
- `void publish(long lo, long hi);`: Batch publish a range of events. Called when all of the events have been filled.

The `Sequencer` interface coordinates the process of claiming sequences for access to a data structure while tracking dependent `Sequence`s. This interface declares the following in addition to the functions declared in the `Cursored` and `Sequenced` interfaces:

- `long INITIAL_CURSOR_VALUE = -1L;`: intended to be the sequence starting point. It seems odd to start it at `-1`. I suppose the cursor represents the index of the currently claimed slot, so `-1` indicates no slots have yet been claimed.
- `void claim(long sequence);`: Claim a specific sequence. Only used if initializing the ring buffer to a specific value.
- `boolean isAvailable(long sequence);`: Confirms if a sequence is published and the event is available for use. This is a non-blocking function.
- `void addGatingSequences(Sequence... gatingSequences);`: Add the specified gating sequences to this instance of the Disruptor. They will safely and atomically be added to the list of gating sequences. The parameter is the sequences to add. I suppose this essentially *subscribes* one or more instances of a `Sequence` to the ring buffer.

### EventSequencer Interface
This is a simple interface that adds no function declarations. It only extends [DataProvider](#dataprovider-interface) and [Sequenced](#sequenced-interface).

### DataProvider Interface
This interface declares only one function: `T get(long sequence);`, which presumably is used to retrieve an event based on its location in the sequence.

### EventSink Interface
The `EventSink` interface defines an API for publishing events to the ring buffer. It consists of an amazingly ugly array of variations on `void publishEvent(EventTranslator<E> translator);` and `boolean tryPublishEvent(EventTranslator<E> tranlator);`. Each variation consists of one to three user-supplied arguments and versions with a variable number of arguments. Here it is:

`void publishEvent(EventTranslator<E> translator);`
: Publishes an event to the ring buffer. It handles claiming the next sequence, getting the current (uninitialized) event from the ring buffer and publishing the claimed sequence after translation. It's argument is the user-specified translation for the event.

`boolean tryPublishEvent(EventTranslator<E> translator);`
: Attempts to publish an event to the ring buffer. It handles clamining the next sequence, getting the current (uninitialized) event from the ring buffer and publishing the claimed sequence after translation. It will return true if the value was published, and false if there was insufficient capacity.

`<A> void publishEvent(EventTranslatorOneArg<E, A> translator, A arg0);`
: Publishes an event with one user-supplied argument. The `translator` is the user-specified translation for the event, and `arg0` is a user-supplied argument.

`<A> boolean tryPublishEvent(EventTranslatorOneArg<E, A> translator, A arg0);`
: This is the same idea as `publishEvent`, above.

`<A, B> void publishEvent(EventTranslatorOneArg<E, A> translator, A arg0, B arg1);`
: Same idea with two user-supplied arguments.

`<A, B> boolean tryPublishEvent(EventTranslatorOneArg<E, A> translator, A arg0, B arg1);`
: Same idea with two user-supplied arguments.

`<A, B, C> void publishEvent(EventTranslatorOneArg<E, A> translator, A arg0, B arg1, C arg2);`
: Same idea with three user-supplied arguments.

`<A, B, C> boolean tryPublishEvent(EventTranslatorOneArg<E, A> translator, A arg0, B arg1, C arg2);`
: Same idea with three user-supplied arguments.

`void publishEvent(EventTranslatorVararg<E> translator, Object... args);`
: Same idea with a variable number of arguments.

`void tryPublishEvent(EventTranslatorVararg<E> translator, Object... args);`
: Same idea with a variable number of arguments.

`void publishEvents(EventTranslator<E>[] translators);`
: Publish multiple events to the ring buffer. It handles claiming the next sequence, getting the current (uninitialized) event from teh ring buffer and publishing the claimed sequence after translation. With this call, the data that is to be inserted into the ring buffer will be a field (either explicitly or captured anonymously), therefore this call will require an instance of the translator for each value that is to be inserted into the ring buffer. The `translators` parameter contains the user-specified translation for each event.

`void publishEvents(EventTranslator<E>[] translators, int batchStartsAt, int batchSize);`
: Attempts to publish multiple events to the ring buffer. It handles claiming the next sequence, getting the current (uninitialized) event from teh ring buffer and publishing the claimed sequence after translation. With this call, the data that is to be inserted into the ring buffer will be a field (either explicitly or captured anonymously), therefore this call will require an instance of the translator for each value that is to be inserted into the ring buffer. The `batchStartAt` parameter is the first element of the array which is within the batch, and the `batchSize` parameter is the actual size of the batch.

`boolean tryPublishEvents(EventTranslator<E>[] translators);`
: Attempts to publish multiple events to the ring buffer; `translators` is the array of user-specified translators for the events. The function returns true if the values were published and false if there was insufficient capacity.

`boolean tryPublishEvents(EventTranslator<E>[] translators, int batchStartsAt, int batchSize);`
: The same boring idea as above.


`<A> void publishEvents(EventTranslatorOneArg<E, A> translator, A[] arg0);`
: Really? Again?

`<A> void publishEvents(EventTranslatorOneArg<E, A> translator, int batchStartsAt, int batchSize, A[] arg0);`
: Really? Again?

`<A> void tryPublishEvents(EventTranslatorOneArg<E, A> translator, A[] arg0);`
: Really? Again?

`<A> void tryPublishEvents(EventTranslatorOneArg<E, A> translator, int batchStartsAt, int batchSize, A[] arg0);`
: Really? Again?


`<A, B> void publishEvents(EventTranslatorTwoArg<E, A, B> translator, A[] arg0, B[] arg1);`
: Really? Again?

`<A, B> void publishEvents(EventTranslatorTwoArg<E, A, B> translator, int batchStartsAt, int batchSize, A[] arg0, B[] arg1);`
: Really? Again?

`<A, B> void tryPublishEvents(EventTranslatorTwoArg<E, A, B> translator, A[] arg0, B[] arg1);`
: Really? Again?

`<A, B> void tryPublishEvents(EventTranslatorTwoArg<E, A, B> translator, int batchStartsAt, int batchSize, A[] arg0, B[] arg1);`
: Really? Again?


`<A, B, C> void publishEvents(EventTranslatorThreeArg<E, A, B, C> translator, A[] arg0, B[] arg1, C[] arg2);`
: Really? Again?

`<A, B, C> void publishEvents(EventTranslatorThreeArg<E, A, B, C> translator, int batchStartsAt, int batchSize, A[] arg0, B[] arg1, C[] arg2);`
: Really? Again?

`<A, B, C> void tryPublishEvents(EventTranslatorThreeArg<E, A, B, C> translator, A[] arg0, B[] arg1, C[] arg2);`
: Really? Again?

`<A, B, C> void tryPublishEvents(EventTranslatorThreeArg<E, A, B, C> translator, int batchStartsAt, int batchSize, A[] arg0, B[] arg1, C[] arg2);`
: Really? Again?


`void publishEvents(EventTranslatorVararg<E> translator, Object[]... args);`
: ...

`void publishEvents(EventTranslatorVararg<E> translator, int batchStartsAt, int batchSize, Object[]... args);`
: ...

`boolean tryPublishEvents(EventTranslatorVararg<E> translator, Object[]... args);`
: ...

`boolean tryPublishEvents(EventTranslatorVararg<E> translator, int batchStartsAt, int batchSize, Object[]... args);`
: ...


### Gating Sequence
The core part of the LMAX Disruptor is the `Sequencer` and its `Sequence`s. The `RingBuffer` implements those interfaces. Each gating sequence acts as a cursor to each `Sequencer` that is "subscribed" to the target. This is how a `Sequencer` can have multiple cursors for its connected `Sequencer`s and let them touch the next `sequence` by just calling `tryNext()`.

## Motivation
I'm learning as much as I can about the LMAX Disruptor because I thought I might need a queue to create a work-item pipeline using ZeroMQ.

By the way, I've briefly looked into [nanomsg](http://nanomsg.org/), but that seems to be [unsupported](http://hintjens.com/blog:112) (see [here as well](http://sealedabstract.com/rants/nanomsg-postmortem-and-other-stories/)). Perhaps I could take the crazy idea at the conclusion and "clone nanomsg, move to ZeroMQ organization, relicense as MPL, support ZMTP, only new socket types and expose CZMQ API." I'm not sure what that would entail, but maybe I could get a non-GPL/LGPL licensed message queue with a reasonable API out of the deal.

## Overview
The Disruptor pattern was created by the [LMAX Exchange](https://www.lmax.com/) as part of their efforts to build a high performance financial exchange. They found that the compute-time in their processing pipelines were dominated by the cost of queuing of events between stages. The Disruptor is the result of their work to build a concurrent structure that separates the concerns for producers, consumers and their data storage.

## False Sharing of Cache Lines Among Threads
See [Avoiding and Identifying False Sharing Among Threads](https://software.intel.com/en-us/articles/avoiding-and-identifying-false-sharing-among-threads).

To what part or parts of the disruptor do we have to be concerned about false sharing?

### Techniques to Avoid False Sharing
The goal is to ensure variables that could cause false sharing are spaced far enough apart in memory that they cannot reside on the same cache line. One technique is to use compiler directives to force individual variable alignment. The following source code demonstrates the compiler technique using `__declspec (align(n))`, where `n` equals 64 (64-byte boundary) to align the individual variables on the cache-line boundaries:

```cpp
__declspec (align(64)) int thread1_global_variable;
__declspec (align(64)) int thread2_global_variable;
```

Note that Intel's compiler and Microsoft's Visual Studio compiler support `__declspec(align(n))`, where `n` is any power of two from 1 to 8192 bytes. GCC provides `__attribute__((align(n)))` for the same purpose. I assume Clang also provides `__attribute__((align(n)))`.

When using an array of data structures, pad the structure to the end of a cache line to ensure that the array elements begin on a cache-line boundary. If you cannot ensure that the array is aligned on a cache-line boundary, pad the data structure to twice the size of a cache line. The following source code demonstrates padding a data structure to a cache line boundary and ensuring the array is also aligned using the compiler directive `__declspec (align(n))`. If the array is dynamically allocated, you can increase the allocation size and adjust the pointer to align with a cache-line boundary.

```cpp
struct ThreadParams
{
    // For the following 4 variables: 4*4 = 16 bytes
    unsigned long thread_id;
    unsigned long v; // Frequent read/write access variable
    unsigned long start;
    unsigned long end;

    // expand to 64 bytes to avoid false sharing
    // (four unsigned long variables + 12 padding) * 4 = 64
    int padding[12];
};

__declspec (align(64)) struct ThreadParams Array[10];
```

It is also possible to reduce the frequency of false sharing by using thread-local copies of data. The thread-local copy can be read and modified frequently and only when complete, copy the result back to the data structure. The following source code demonstrates using a local copy to avoid false sharing.

```cpp
struct ThreadParams
{
    // For the following 4 variables: 4*4 = 16 bytes
    unsigned long thread_id;
    unsigned long v; // Frequent read/write access variable
    unsigned long start;
    unsigned long end;
};

void threadFunc(void *parameter)
{
    ThreadParams *p = (ThreadParams*) parameter;

    // local copy for read/write access variable
    unsigned long local_v = p->v;

    for (local_v = p->start; local_v < p->end; local_v++)
    {
        // Functional computation
    }

    p->v = local_v; // Update shared data structure only once
}
```

### Comparing the Disruptor to Other Models
There's a nice [comparison of the Disruptor](http://stackoverflow.com/questions/6559308/how-does-lmaxs-disruptor-pattern-work) to a queue, the Actor model and the Staged Event-Driven Architecture (SEDA) on stackoverflow, by Michael Barking.

#### Comparison to a Queue
The Disruptor is similar to a queue in that it enables one thread, a producer, to pass a message to other threads, the consumers, waking them up if necessary. The three differences are:

1. The user of the Disruptor defines how messages are stored by extending the Entry class interface and providing a factory to pre-allocate memory for the ring buffer. This allows for either memory reuse through copying, or an instance of the Entry class interface could contain a reference to another object.
2. Putting messages into the Disruptor is a 2-phase process. First a slot is claimed in the ring buffer, which provides the user with the Entry that can be filled with the appropriate data. Second, the entry must be committed. This 2-phase approach is necessary to allow for the flexible use of memory mentioned above. It is the commit that makes the message visible to the consumer threads.
3. It is the responsibility of the consumer to keep track of the messages that have been consumed from the ring buffer. Moving this responsibility away from the ring buffer itself helped reduce the amount of write contention as each thread maintains its own counter.

#### Comparison to the Actor Model
The Disruptor is close to the Actor model, especially if you use the BatchConsumer/BatchHandler classes that are provided. These classes hide all of the complexities of maintaining the consumed sequence numbers and provide a set of simple callbacks to handle important events. However, there are a couple of subtle differences.

1. The Disruptor uses a 1-thread - 1-consumer model, where Actors use an N:M model. That is, you can have as many actors as you like and they will be distributed across a fixed number of threads (generally 1 thread per core).
2. The BatchHandler interface provides an additional (and very important) callback `onEndOfBatch()`. This allows for slow consumers. For example, those doing I/O to batch events together to improve throughput. It is possible to do batching in other Actor frameworks, however as  nearly all other frameworks don't provide a callback at the end of the batch, you need to use a timeout to determine the end of the batch, resulting in poor latency.

#### Comparison to SEDA
LMAX built the Disruptor pattern to replace a SEDA-based approach.

1. The main improvement that it provided over SEDA was the ability to do work in parallel. To do this the Disruptor supports multi-casting the same messages (in the same order) to multiple consumers. This avoids the need for fork stages in the pipeline.
2. We also allow consumers to wait on the results of other consumers without having to put another queuing stage between them. A consumer can simply watch the sequence number of a consumer that it depends on. This avoids the need for join stages in the pipeline.

#### Comparison to Memory Barriers
Another way to think about it is as a structured, ordered memory barrier. The producer barrier forms the write barrier and the consumer barrier is the read barrier.

Memory barriers are necessary, because modern CPUs can reorder loads and stores to optimize performance. These optimizations are normally not an issue in a single thread of execution. However, in concurrent programs and device drivers in multiprocessor systems, they can cause unpredictable results.

Memory barriers are expensive operations, so they must be used only where necessary. They invalidate CPU caches and cause the CPU to read or write main memory, which is orders of magnitude slower than the caches.

There seem to be three categories of memory barriers, also known as fences. There's the full fence, which ensures that all load and store operations before to the fence will have been committed prior to any loads and stores issued following the fence. Some architectures provide separate 'acquire' and 'release' memory barriers, which address the visibility of read-after-write operations from the point of view of a reader (sink, consumer) or a writer (source, producer), respectively.

### Definitions
- concurrency: two or more tasks running in parallel that contend for access to resources.
- mutual exclusion: managing contended updates to some resource.
- visibility of change: controlling when such changes are made visible to other threads.

"The most costly operation in any concurrent environment is a contended write access. To have multiple threads write to the same resource requires complex and expensive coordination. Typically this is achieved by employing a locking strategy of some kind."

### Memory Allocation and Garbage Collection
All memory for the ring buffer is pre-allocated on start up. A ring buffer can store either an array of pointers to entries, or an array of structures representing the entries. In Java, entries in ring buffers must be pointers to objects. This pre-allocation of entries eliminates issues in languages that support garbage collection, since the entries will be reused and live for the duration of the Disruptor instance.

Under heavy load queue-based systems can back up, which can lead to a reduction in the rate of processing, and results in the allocated objects surviving longer than they should, thus being promoted beyond the young generation with generational garbage collectors. This has two implications: first, the objects have to be copied between generations which cause latency jitter; second, these objects have to be collected from the old generation which is typically a much more expensive operation and increases the likelihood of “stop the world” pauses that result when the fragmented memory space requires compaction. In large memory heaps this can cause pauses of seconds per GB in duration.

### Teasing Apart the Concerns
The following concerns are conflated in all queue implementations, to the extent that this collection of distinct behaviors tend to define the interfaces that queues implement:

1. Storage if items being exchanged.
2. Coordination of producers claiming the next sequence for exchange.
3. Coordination of consumers being notified that a new item is available.

When designing a low-latency pipeline in a language that uses garbage collection, too much memory allocation can be problematic. This concern eliminates linked-list backed queues from consideration. Garbage collection is minimized if the entire storage for the exchange of data between processing stages can be pre-allocated. Furthermore, if this allocation can be performed in a uniform chunk, then traversal of that data will be done in a manner that is very friendly to the caching strategies employed by modern processors.

A data-structure that meets this requirement is an array with all the slots pre-filled. On creation of the ring buffer, the Disruptor utilizes the Abstract Factory pattern to pre-allocate the entries. When an entry is claimed, a producer can copy its data into the pre-allocated structure. I'm thinking that move-constructors and move-assignment operators are needed in a C++ implementation.

Note that the size of a ring buffer should be a power of 2 to reduce the cost of calculating the remainder on a sequence number to get the correct index.

In general, bounded queues suffer from contention at the head and tail. The ring buffer data structure is free from this contention and concurrency primitives, because these concerns have been teased out into producer and consumer barriers through which the ring buffer must be accessed. The logic for these barriers is described below:

In the case where there is only one producer (such as when the producer is reading a file or listening to a network connection), there is no contention on sequence/entry allocation. In cases where there are multiple producers, producers will race one another to claim the next entry in the ring buffer. Contention on claiming the next available entry can be managed with a simple Compare-And-Swap (CAS) operation on the sequence number for that slot.

Once a producer has copied the relevant data to the claimed entry it can make it public to consumers by committing the sequence. This can be done without CAS by a simple busy-spin until the other producers have reached this sequence in their own commit. This producer then advances the cursor signifying the next available entry for consumption. Producers can avoid wrapping the ring by tracking the sequence of the consumers as a simple read operation before they write to the ring buffer.

Consumers wait for a sequence to become available in the ring buffer before they read the entry. Various strategies can be employed while waiting. If CPU resource is precious, they can wait on a condition variable within a lock that gets signaled by the producers. This obviously is a point of contention and only to be used when CPU resource is more important than latency or throughput. The consumers can also loop, checking the cursor which represents the currently available sequence in the ring buffer. This could be done with or without a thread yield by trading CPU resource against latency. This scales very well as we have broken the contended dependency between the producers and consumers if we do not use a lock and condition variable. Lock-free multi-producer and multi-consumer queues do exist, but they require multiple CAS operations on the head, tail, and size counters. The Disruptor does not suffer this CAS contention.

### Sequencing
Sequencing is the core concept to how concurrency is managed in the Disruptor. Each producer and consumer works off of a strict sequencing concept for how it interacts with the ring buffer. Producers claim the next slot in sequence when claiming an entry in the ring. This can be a simple counter in the case of only one producer, or an atomic counter updated using CAS operations in the case of multiple producers.

Once a sequence value is claimed, this entry in the ring buffer is available to be written to by the producer that claimed it.

## Memory Barriers
In his post titled [Memory Barriers Are Like Source Control Operations](http://preshing.com/20120710/memory-barriers-are-like-source-control-operations/), Jeff Preshing presented four types of memory barriers. They are:

- `LoadLoad`
- `LoadStore`
- `StoreLoad`
- `StoreStore`

Each type of memory barrier is named after the type of memory reordering it's designed to prevent. For example, `StoreLoad` is designed to prevent the reordering of a store followed by a load.

### LoadLoad
A `LoadLoad` barrier effectively prevents reordering of loads performed before the barrier with loads performed after the barrier. There is no guarantee that the `LoadLoad` barrier will get the latest value from memory. It could be that no other CPU has marked the shared memory as modified (per the [MESI cache-coherence protocol](https://en.wikipedia.org/wiki/MESI_protocol)), The value is only guaranteed to be *at least as new as the newest value which was cached from main memory to the current CPU on which the thread is running*.

The classic example is where a consumer-thread checks a shared flag to see if some data has been published by a producer-thread. If the flag is true, then the consumer thread issues a `LoadLoad` barrier before reading the published value:

```cpp
if (isPublished)
{
    LoadLoadFence();
    return sharedValue;
}
```

Note that for this to work, we don't need to ensure `sharedValue` is an atomic value. It can be any kind of value, including a large structure or array.
### StoreStore
A `StoreStore` barrier prevents reordering of stores performed before the barrier with stores performed after the barrier. There is no guarantee that `StoreStore` barriers take effect instantly. They can be performed in an asynchronous manner.

In this case, to ensure the consumer-thread doesn't see any stale data published by the producer-thread, the producer-thread need only to write to shared memory, issue a `StoreStore` barrier and then set the shared flag to true.

```cpp
sharedValue = x;    // publish some data
StoreStoreFence();  // Ensure sharedValue is updated before isPublished
isPublished = true; // set the shared flag to indicate sharedValue is updated.
```

Eventually, the consumer will see the change to `isPublished` and will read `sharedValue`.

### LoadStore
Let's look at this barrier from the perspective of instruction reordering on the publisher thread. Some instructions will load data from the CPU cache to a register, and some will cause register data to be stored back to the cache. The CPU can, under some specific cases, reorder these loads and stores. When the CPU encounters a load, it checks ahead to see if any stores coming up are related to the load it's about to perform. If the stores are completely unrelated, to the current load, the CPU is allowed to skip ahead, do the stores first and then come back to perform the load. The CPU might reorder such loads and stores if, for example, the load caused a cache miss followed by a cache hit on the store.

However, if there is a `LoadStore` barrier between the load and store operations, then the CPU is prevented from reordering these loads and stores. There are two things to note here with real-world CPUs:

1. If only a `LoadLoad` or a `StoreLoad` barrier is used between the load and subsequent store operations, the CPU is still allowed to reorder the loads and stores.
2. If a `LoadStore` barrier is issued, the CPU acts as if at least one of the other two barriers (`LoadLoad` or `StoreStore`) were issued.

### StoreLoad
A `StoreLoad` barrier ensures that all stores performed before the barrier are visible to other processors, and that all loads performed after the barrier receive the latest value that is visible at the time of the barrier.

`StoreLoad` is the only memory barrier that will prevent each processor from delaying the effect of a store past any load from a different location. Pershing provided [example code](http://preshing.com/files/ordering.zip) that showed this sort of memory reordering that occurs when a `StoreLoad` barrier is not used.

### The Full Memory Fence
We can't just use a `StoreStore` barrier followed by a `LoadLoad` barrier to get the same effect. Although a `StoreStore` will ensure values before the barrier are pushed to main memory before any subsequent stores after the barrier, the push might be delayed for an arbitrary number of instructions. Also, `LoadLoad` does **not** guarantee a load instruction will get the latest value from main memory.

If we combine `LoadLoad`, `StoreStore` and `LoadStore` barriers, we get a full memory fence.

Likewise, if we combine a `StoreLoad` with a `LoadStore`, we also get a full memory fence. [Doug Lea point out](http://g.oswego.edu/dl/jmm/cookbook.html) that every instruction on all current processors which act as a `StoreLoad` barrier also act as a full memory fence.

## Acquire and Release Semantics
NOTE: One good reference is the September 13, 2012 article [Acquire and Release Semantics](http://preshing.com/20120913/acquire-and-release-semantics/), by Jeff Preshing. Other references covering subtleties of acquire and release operations and fences (they aren't the same thing) are:

* [Acquire and Release Fences](http://preshing.com/20130922/acquire-and-release-fences/)
* [Acquire and Release Fences Don't Work the Way You'd Expect](http://preshing.com/20131125/acquire-and-release-fences-dont-work-the-way-youd-expect/)
* [Memory Barriers Are Like Source Control Operation](http://preshing.com/20120710/memory-barriers-are-like-source-control-operations/)
* [The Purpose of memory_order_consume in C++11](http://preshing.com/20140709/the-purpose-of-memory_order_consume-in-cpp11/)
* [Double-Checked Locking is Fixed in C++11](http://preshing.com/20130930/double-checked-locking-is-fixed-in-cpp11/)
* [The Synchronizes-With Relation](http://preshing.com/20130823/the-synchronizes-with-relation/)
* [Atomic vs. Non-Atomic Operations](http://preshing.com/20130618/atomic-vs-non-atomic-operations/)
* [The World's Simplest Lock-Free Hash Table](http://preshing.com/20130605/the-worlds-simplest-lock-free-hash-table/)
* [Improved Support for Bidirectional Fences](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2008/n2633.html) from the "Programming Language C++, Library/Concurrency Subgroup" on 2008-05-16.
* [Mintomic](http://mintomic.github.io/), a library provides an API for lock-free programming in C and C++ (no C++11 compilers required).
* [Lockless Programming Considerations for Xbox 360 and Microsoft Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/ee418650.aspx)

An operation has **acquire semantics** if other processors will always see its effect before any subsequent operation's effect. In other words, acquire semantics guarantee the particular operation is completed and is visible to all processors before any subsequent code is executed. The property can only apply to operations which **read** from shared memory, whether they are read-modify-write operations or plain loads. The operation is then considered a **read-acquire**. Acquire semantics prevent memory reordering of the read-acquire with any read or write operation which **follows** it in program order.

An operation has **release semantics** if other processors will see every preceding operation's effect before the effect of the operation itself. In other words, release semantics guarantee all previous operations will be completed and is visible to all processors before the current operation is executed. The property can only apply to operations which **write** to shared memory, whether they are read-modify-write operations or plain stores. The operation is then considered a **write-release**. Release semantics prevent memory reordering of the write-release with any read or write operation which **precedes** it in program order.

There are four memory barrier types:
1. LoadLoad
2. LoadStore
3. StoreLoad
4. StoreStore

The first two, `LoadLoad` and `LoadStore`,  can be used to define acquire semantics, and the `LoadStore` and `StoreStore` barriers can be used to define release semantics. Neither acquire nor release semantics require the use of a `StoreLoad` memory barrier.

Wow! There is a subtle difference between a release operation and a release fence. See Jeff Pershing's November 25, 2013 article [Acquire and Release Fences Don't Work the Way You'd Expect](http://preshing.com/20131125/acquire-and-release-fences-dont-work-the-way-youd-expect/), particularly the section called "Nor Can a Release Operation Take the Place of a Release Fence".

He compared the properties of a release operation:

```cpp
tmp = new Singleton;
m_instance.store(tmp, std::memory_order_release);
```

with a release fence:

```cpp
tmp = new Singleton;
std::atomic_thread_fence(std::memory_order_release);
m_instance.store(tmp, std::memory_order_relaxed);
```

Apparently, a release operation, such as the one above will only prevent preceding memory operations from being reordered past **itself**, but a release fence is more strict. The release fence must prevent preceding memory operations from being reordered past *all subsequent writes*, not just itself. Pershing goes on to show why this distinction is important. Here's his example:

```cpp
Singleton* tmp = new Singleton;
g_dummy.store(0, std::memory_order_release);
m_instance.store(tmp, std::memory_order_relaxed);
```

In this case, the store to `m_instance` is now free to be reordered before the store to `g_dummy`, and possibly before any stores performed by the `Singleton` constructor.

Full fence operations have both acquire and release semantics, so all code preceding the particular operation will be completed and be visible to all processors (release semantics), and the particular operation will be completed and be visible to all processors before any subsequent operation is executed (acquire semantics).

Consider this code:

```cpp
a++;
b++;
c++;
```

From another processor's point of view, the preceding operations can appear to occur in any order. Microsoft Windows provides `Interlocked*` functions that have both acquire and release semantics by default. Some processors, such as the Itanium-based ones, provide instructions that have only acquire or release semantics which are faster than those with both. Therefore, Windows also provides `Interlocked*Acquire` and `Interlocked*Release` version of some of the interlocked functions.

For example, the `InterlockedIncrementAcquire` routine uses acquire semantics. The code above could be rewritten as follows to ensure that other processors would always see the increment of `a` before the increments of `b` and `c` (while the increments of `b` and `c` could be in either order):

```cpp
InterlockedIncrementAcquire(&a);
b++;
c++;
```

Likewise, the `InterlockedIncrementRelease` routine uses release semantics, so we could ensure that other processors saw the increment of `c` after the increments of `a` and `b` (while the increments of `a` and `b` could still be in either order):

```cpp
a++;
b++;
InterlockedIncrementRelease(&c);
```

Note that on x86 processors, which do not have instructions that have only acquire or release semantics, both `InterlockedIncrementAcquire` and `InterlockedIncrementRelease` are equivalent to `InterlockedIncrement`.

### The `volatile` Keyword
One warning about the C/C++ keyword `volatile`. It was intended to allow C and C++ programs to directly access memory-mapped I/O. All it does is ensure that the compiler will emit code such that reads and writes to volatile memory locations happen in the exact order specified and that no read or write is omitted (due to some compiler optimization, for example). The keyword `volatile` does *not* guarantee a memory barrier to enforce cache consistency. It is worth reading the Linux kernel document [Why the "volatile" type class should not be used](https://www.kernel.org/doc/Documentation/volatile-considered-harmful.txt). It highlights problems with the `volatile` keyword.

### Behaviors for Consumers
Generally, consumers can read concurrently and independently. However, we can declare dependencies among consumers. Consumer dependencies can be arbitrary, forming an acyclic graph. If consumer B depends on consumer A, consumer B can't read past consumer A.

Consumer dependency arises because consumer A can annotate an entry, and consumer B depends on that annotation. For example, A does some calculation on an entry, and stores the result in field `a` of the entry. Consumer A then moves on, and now B can read the entry, and the new value of `a`. If reader C does not depend on A, C should not attempt to read `a`.

The Entry objects in the ring buffer are pre-allocated to reduce the cost of garbage collection (or of allocating and releasing memory from the head, in the case of non-garbage collected implementations). Producers and consumers don't insert new entry objects, or delete old ones. Instead, a producer asks for a pre-existing entry, populates its fields and notifies the consumers. This 2-phase action might look like this in code:

```java
setNewEntry(EntryPopulator);
interface EntryPopulator { void populate(Entry existingEntry); }
```

For developers of consumers, note that different annotating consumers should write to different fields to avoid write contention. Actually, they should write to different cache lines. An annotating consumer should not touch anything that other non-dependent consumers may read. This is why we say **annotate** entries instead of **modify** entries.

## Another Explanation of Producers and Consumers
The ring buffer of Entry objects has a sister buffer that amounts to an array (ring buffer) of flags. This flag array is the same size as the ring buffer. Each flag is an integer that indicates the availability of the associated slot in the ring buffer.

There can be any number of producers. When one wants to write to the buffer, it gets the current write position from the buffer and increments it atomically with a Compare And Set instruction, along the lines of the following code:

```java
public final int incrementAndGet() {
    for (;;) {
        int current = get();
        int next = current + 1;
        if (compareAndSet(current, next))
            return next;
    }
}
```

We can refer to this value as a `producerCallId`. In a similar manner, a `consumerCallId` is generated when a consumer **finishes** reading an Entry from the buffer. The most recent `consumerCallId` is accessed. If there are many consumers, the call with the lowest ID is chosen.

These IDs are compared, and if the differences between the two is less than the buffer size, the producer is allowed to write. If the `producerCallId` is greater than the recent `consumerCallId + bufferSize`, then the buffer is full and the producer must wait until an entry becomes available.

The producer is then assigned the entry in the ring buffer based on the value of its `producerCallId` (the index of the entry is `producerCallId mod bufferSize`, and since the `bufferSize` is a power of 2, the index is `producerCallId & (bufferSize - 1)`). It is then free to modify the entry at that location. The actual algorithm is a little more complicated, involving caching the most recent `consumerCallId` in a separate atomic reference for optimization purposes.

When the entry is modified, the change is "published" by updating the respective slot in the flag array. The flag value is the number of the loop (`producerCallId` divided by the `bufferSize`, or simply `producerCallId >> bufferSize`, since `bufferSize` is a power of 2).

In a similar manner, there can be any number of consumers. Each time a consumer wants to access the buffer, a `consumerCallId` is generated. Depending on how consumers were added to the Disruptor, the atomic value used to generate the ID may be shared or separate for each of them. This `consumerCallId` is then compared to the most recent `producerCallId`, and if it is less than the value of that `producerCallId`, the reader is allowed to progress. If they are the same value, then the buffer is empty and the consumer must wait. The manner of waiting is defined by the implementation of the `WaitStrategy` used during the creation of the Disruptor.

For individual consumers, the ones with their own ID generator, the next thing to check is the ability to batch consume. The slots in the buffer are examined in order from the one index by the `consumerCallId` to the one indexed by the recent `producerCallId`. They are examined in a loop by comparing the flag value written in the flag array, against a flag value generated for the consumerCallId. If the flags match it means that the producers filling the slots have committed their changes. If not, the loop is broken, and the highest committed change ID is returned. The slots from `consumerCallId` to received in change ID can be consumed in batch.

If a group of consumers read together (the ones with a shared ID generator), each one only takes a single call ID, and only the slot for that single call ID is checked and returned.

## References
- LMAX Disruptor
    - [LMAX Exchange](https://www.lmax.com/)
    - [A Comparison of the Disruptor](http://stackoverflow.com/questions/6559308/how-does-lmaxs-disruptor-pattern-work) on stackoverflow.
    - [Getting Started with CoralQueue](http://www.coralblocks.com/index.php/2014/06/getting-started-with-coralqueue/) has a description of a Disruptor implementation.
- Memory Barriers
    - [Dissecting the Disruptor: Demystifying Memory Barriers](http://mechanitis.blogspot.com/2011/08/dissecting-disruptor-why-its-so-fast.html).
    - [Memory Barrier](https://en.wikipedia.org/wiki/Memory_barrier) on Wikipedia.
    * [Memory Barriers Are Like Source Control Operation](http://preshing.com/20120710/memory-barriers-are-like-source-control-operations/)
    * [Memory Ordering at Compile Time](http://preshing.com/20120625/memory-ordering-at-compile-time/)
    * [Memory Reordering Caught in the Act](http://preshing.com/20120515/memory-reordering-caught-in-the-act/)
- Memory Barriers and C++
    * [std::memory_order](http://en.cppreference.com/w/cpp/atomic/memory_order) on [cppreference.com](http://en.cppreference.com/w/).
    * [The Purpose of memory_order_consume in C++11](http://preshing.com/20140709/the-purpose-of-memory_order_consume-in-cpp11/)
    * [Double-Checked Locking is Fixed in C++11](http://preshing.com/20130930/double-checked-locking-is-fixed-in-cpp11/)
    * [The Synchronizes-With Relation](http://preshing.com/20130823/the-synchronizes-with-relation/)
    * [Improved Support for Bidirectional Fences](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2008/n2633.html) from the "Programming Language C++, Library/Concurrency Subgroup" on 2008-05-16.
    - [Why the "volatile" type class should not be used](https://www.kernel.org/doc/Documentation/volatile-considered-harmful.txt)
    * [Mintomic](http://mintomic.github.io/), a library that provides an API for lock-free programming in C and C++ (no C++11 compilers required).
- Acquire and Release Semantics
    [Acquire and Release Semantics](http://preshing.com/20120913/acquire-and-release-semantics/), by Jeff Preshing
    * [Acquire and Release Fences](http://preshing.com/20130922/acquire-and-release-fences/)
    * [Acquire and Release Fences Don't Work the Way You'd Expect](http://preshing.com/20131125/acquire-and-release-fences-dont-work-the-way-youd-expect/)
    * [atomic Weapons: The C++ Memory Model and Modern Hardware](http://herbsutter.com/2013/02/11/atomic-weapons-the-c-memory-model-and-modern-hardware/)
* [Atomic vs. Non-Atomic Operations](http://preshing.com/20130618/atomic-vs-non-atomic-operations/)
* [The World's Simplest Lock-Free Hash Table](http://preshing.com/20130605/the-worlds-simplest-lock-free-hash-table/)
* [Lockless Programming Considerations for Xbox 360 and Microsoft Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/ee418650.aspx)
- [Avoiding and Identifying False Sharing Among Threads](https://software.intel.com/en-us/articles/avoiding-and-identifying-false-sharing-among-threads)
