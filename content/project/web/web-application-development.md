---
title: Web Application Development
date: 2016-03-16
draft: true
categories: note
tags: [web, development]
---

A collection of issues and concerns related to developing web applications. Eventually, I'll get to writing about some solutions. For now, it's just a list.
<!--more-->

## The List of Concerns
General Concerns

- Rendering HTML templates / JSON.
- Asset compilation / Cache busting.
- Caching.
- Sending email.
- Previewing/Testing email.
- Background job queuing (with failure/retry/backoff).
- Reliable and easy integration/feature testing.
- Connecting to database and modeling data.
- Authentication/Account signup/Confirmation/Forgot password for identity management.
- Authorization to control who can access what data and the kinds of access allowed.
- Encryption to securely transfer and store data.
- Payment handling.
- PDF / Invoice rendering.
- Deployment.
- Binding data posted from a form to a model and validating it.

Advantages that the Go programming language has for web developers:

- Static typing.
- Web sockets.
- Concurrency.
- Unit testing.
- Speed.
- Syntax.
- Formatting tools.

Supposedly, JVM and .NET stacks have those advantages, too. One person asserted that Java, C#, Scala, Clojure, F#, VB.NET, Haskell, OCaml, Erlang and even languages like Ada and Delphi provide the same advantages as Go.

## Service Oriented Architecture
Someone asked on Stackoverflow [What are the advantages and disadvantages of using services over components?](http://stackoverflow.com/questions/973673/what-is-the-advantages-and-disadvantages-of-using-services-over-components). The accepted answer is fantastic! It looks at Service Oriented Architecture (SOA) by relating services to what a DLL does for components. If you have a DLL that provides a certain set of functions for several applications, you copy that DLL everywhere there is an instance of an application that uses it. Updates to that DLL might require all of the apps to be rebuilt, but at the very least, all of the DLLs have to be replaced for each instance of the application.

If you have a service that provides the same functionality, you can change the service and deploy it anywhere without the applications being affected (assuming other services are available to locate this service).

> The idea is that distinct operations are decoupled from each other so they can be reused and modified without recompiling the apps that use it. Rather than a piece of code in a DLL being modified and copied everywhere, a service can be deployed that represents a single point of access for a particular piece of processing or source of information.

> Say you had a credit card validation component. You may write this code and compile it into a DLL and start including that in all your applications. Nothing wrong with that unless you notice a bug or the rules for CC validation change. Or maybe you want to upgrade it to check it against a blacklist. You can't do any of those things without recompiling the apps that use it.

> If your credit card validation is exposed as a service however, you can make the changes and deploy to one location. Provided the signature is the same (same parameters and response), the applications don't even have to know it's changed.

> Another advantage of using services over components is that the services can be hosted anywhere. They can be on the local server or on the other side of the world.

> Having said this, like everything you should decide the architecture on a case-by-case basis. While the credit-card validation was a good example of when a service is useful, providing a service to render HTML controls doesn't make much sense.

Within a SOA, services use defined porotocols that describe how services pass and parse messages using description metadata. [Web Services Description Language (WSDL)](https://en.wikipedia.org/wiki/Web_Services_Description_Language) is one kind of Interface Definition Language (IDL) used to describe functionality offered by a web service. It is XML-based. There are alternatives to WSDL, such as [RELAX NG](http://relaxng.org/) and [Web Application Description Language (WADL)](https://en.wikipedia.org/wiki/Web_Application_Description_Language), which are also XML-based.

Protocols for SOA services can be described using the [Simple Object Access Protocol (SOAP)](https://en.wikipedia.org/wiki/SOAP).

From what I gleaned reading a few parts of [Learn REST: A Tutorial](http://rest.elkstein.org/), REST is much simpler than SOAP. A SOAP request consists of an XML payload, followed by a reply that also contains an XML payload. A request based on REST consists only of an HTTP GET or POST request to a URL. The reply can be in XML format, as in SOAP, but can also be many other formats, like CSV, JSON or some kind of binary reply. REST is not bound to XML.

## Types of Services in SOA
There are several types of services in SOA, which can be divided into two categories: Business Services and Infrastructure Services.

A very good article on this subject is [Ontology and Taxonomy of Services in a Service-Oriented Architecture](https://msdn.microsoft.com/en-us/library/bb491121.aspx). Most of the notes in the following sub-sections are copied from there.

### Application Services
Application Services are those services that perform specific business functions and are required for the successful completion of a business process. They might also be called Application Sercies, because they are used to develop composite services and business applications that automate business processes.

Application Services can be further divided into:

- Entity Services.
- Capability Services.
- Activity Services.
- Process Services.

Entity Services are the data-centric components of the enterprise system and are responsible for exposing the information stored in back end databases. They can be thought of as the "nouns" of the business process.

Capability Services and Activity Services are the "verbs." They are the action-centric components that implement business capabilities. Capability Services are coarse-grained and provide generic business capability. Activity Services are more fine-grained and provide specific business capability.

Process Services, which contain the business logic and couple the Enttiy, Activity and Capability services via service orchestration to create composite business services.

### Infrastructure Services
The Infrastructure Services, also called Bus Services, are part of a centrally managed infrastructure necessary for the implementation of applications in SOA. Examples include Software as a Service (SaaS) integration, Authentication services, Event Logging, Exception handling,  memory management and I/O handling.

Infrastructure services divide into Communication Services, which provide message-transfer facilities (message routing and publish-subscribe capabilities, for example) and Utility Services, which provide capabilities unrelated to message transfer such as service discovery and identity federation.

#### Communication Services
Communication services transport messages into, out of and within the system without being concerned with the content of the messages. For example, a bridge may move messages back and forth across a network barrier (that is, bridging two otherwise disconnected networks) or across a protocol barrier (such as moving queued messages between different message queuing systems). Examples of Communication Services incluide relays, bridges, routers, gateways, publish-subscribe systems and queues.

Communication Services do not hold any application state, but in many cases they are configured to work in concert with the applications that use them. A particular application may need to instruct or configure a Communication Service on how to move the messages flowing inside that application such that intercomponent communication is made possible in a loosely coupled architecture. For example, a content-based router may require the application to provide routing instructions such that the router will know where to forward messages. Another example may be a publish-subscribe service that will deliver messages to registered subscribers based on a filter that can be applied to the message's content. This filter will be set by the application. In both cases, the Communication Service does not process the content of the message but rather (optionally) uses parts of it as instructed in advance by the application for determining where it should go.

In addition to application-specific requirements, restrictions imposed by security, regulatory, or other sources of constraints may dictate that in order to use the facilities offered by a particular Communication Service, users will need to possess certain permissions. These permissions can be set:

- at the application scope (allowing an application to use the service regardless of which user is using the application)
- at the user scope (allowing a specific user to use the service regardless of which application that the user is using)
- or at both scopes (allowing the specific user to access the service while running a specific application).

For example, a publish-subscribe service may be configured to restrict access to specific topics by only allowing specific users to subscribe to them.

Other application-level facilities that may be offered by Communication Services pertain to monitoring, diagnostics, and business activity monitoring (BAM). Communication Services may provide statistical information about the application such as an analysis of message traffic patterns (how many messages are flowing through a bridge per minute), error rate reports (how many SOAP faults are being sent through a router per day), or business-level performance indicators (how many purchase orders are coming in through a partner's gateway). Although they may be specific to a particular application, these capabilities are not different than the configuration settings used to control message flow. This information is typically provided by a generic feature of the Communication Service, which often needs to be configured by the application. The statistical information being provided typically needs to be consumed by a specific part of the application that knows what to do with it (raise a security alert at the data center, or update a BAM-related chart on the CFO's computer screen, for example). Table 1 summarizes the characteristics of Communication Services.

#### Utility Services
Utility Services provide generic, application-agnostic services that deal with aspects other than transporting application messages. Like Communication Services, the functionality they offer is part of the base infrastructure of an SOA and is unrelated to any application-specific logic or business process. For example, a discovery service may be used by components in a loosely coupled composite application to discover other components of the application based on some specified criteria; for example, a service being deployed into a pre-production environment may look for another service that implements a certain interface that the first service needs and that is also deployed in the pre-production environment. Examples of Utility Services include security and idEntity Services (for example, an Identity Federation Service or a Security Token Service), discovery services (such as a UDDI server), and message-transformation services.

## Core Components of a Service Ecosystem
- Registration service.
- Discovery or Location services for finding the endpoint(s) of registered services.
- Authentication for identifying services and users.
- Authorization for controlling access to data and services.

## Identity Provider Pattern
The [Identity Provider Pattern](http://arnon.me/soa-patterns/identity-provider/) is one answer to the question of "How can you have an efficient authorization and authentication scheme in an SOA?". In it, there is an identity provider which consists of a Provision component and a Token Server component. The Provision component is used by services to get a signed certificate. I consists of components/services that provide for:

- Audit
- Revocation of tokens.
- Provisioning?
- An Identity data store.

It also has a Token Server for use by services to check identity and retrieve signed tokens. It consists of components/services provide for:

- Token conversion?
- Identity verification.
- Token issuing.

## Identity Management & Modern Authentication Protocols
- [OAuth 2.0](http://oauth.net/2/), and its proposed standard [RFC-6749](http://tools.ietf.org/html/rfc6749) (with [errata](https://www.rfc-editor.org/errata_search.php?rfc=6749)).
- [OpenID Connect](http://openid.net/connect/) is a simple identity layer on top of the OAuth2.0 protocol. It allows clients to verify the identity of the end-user based on the authentication performed by an Authorization Server, and to obtain basic profile information about the end-user in an interoperatable and REST-like manner.

See [The Death (and life) of a protocol](https://www.kuppingercole.com/blog/kearns/the-death-and-life-of-a-protocol) from July 31, 2012 by Dave Kearns for more details about how SAML reached its end-of-life, and that OpenID Connect with OAuth 2.0 are the future of of Identity Management. From the article:

> OpenID Connect is a simple JSON/REST-based interoperable identity protocol built on top of the OAuth 2.0 family of specifications. Its design philosophy is “make simple things simple and make complicated things possible”.

> While OAuth 2.0 is a generic access authorization delegation protocol, thus enabling the transfer of arbitrary data, it does not define ways to authenticate users or communicate information about them. OpenID Connect provides a secure, flexible, and interoperable identity layer on top of OAuth 2.0 so that digital identities can be easily used across sites and applications. While enabling a default set of common claims about the user (such as name, e-mail address, and a user identifier enabling SSO) to be easily employed. OpenID Connect also enables participants to exchange any claims relevant to their application using simple JSON-based data structures.

## User Presence and Synchronization
How do we know who's online? The usual solution is to launch a presence server that monitors channel processes, and broadcasts events as users join and leave. When the server gets a "down" message (I'm not sure if it's "connection down", or if it means the particular process that's handling the particular user went down) for a particular user, it broadcasts "leave" and removes the user from its local state.

One problem with this architecture is if the user opens three browser tabs to the application, there will be three duplicate instances of the user "join"-ing the application, but only one instance of the user in the list of users currently online. If the user closes one browser tab, the presence server will broadcast a "leave" message. The user will be removed from the list of online users, but they will still be online.

The user hasn't really left until all of their presence instances terminate. As we can see, there is a unique presence instance for each user connection rather than each user.

Another problem is created when developers new to Erlang and Elixir develop an application on their personal computer, and put the apps' state on a `gen_server`. Once the app is deployed to multiple nodes (hosts), there's a synchronization problem. The state on each node will depend on which node each user connects to. Some developers will then put the Presence state in a shared database like redis.

The shared database partly solves the synchronization problem. Each node can read and write the shared database to stay current with the state of the other nodes in the system (and thus the list of users present on those other nodes). However, if another node goes down, the processes on that node meant to keep the shared database up-to-date are also gone. The remaining nodes will have orphaned data. The users who were connected to that downed node will appear to remain online forever. Solutions with this architecture become convoluted. You might try using expiration times, and managing users who remain online past those expiration times. You might use a heartbeat/gossip protocol, and automatically remove users associated with the downed node (as long as they weren't also connected to another node that's still up).

Summary of the Presence Problem:

- Local-node concerns: we must account for unique presences for the same user
- Mult-node concers:
    - must handle node-down events and clean up local state for presences belonging to downed node
    - must replicate data across the cluster

The ideal solution will

-  have no single source of truth
    - avoid a single point of failure
    - more scalable
    - more fault-tolerant
    - no net-split problem, where the nodes that lose contact with a central (redis) database would be useless.
- CRDT (Conflict-free Replicated Data Type)
- Hearbeat/Gossip protocol ([SWIM: *S* calable *W* eakly-consistent *I* nfection-style Process Group *M* embership Protocol](https://www.cs.cornell.edu/~asdas/research/dsn02-swim.pdf) (PDF), [SWIM Overview](https://www.serfdom.io/docs/internals/gossip.html), and [The SWIM Membership Protocol](http://prakhar.me/articles/swim/)).

CRDTs, used in the Presence module of the Phoenix Framework, have some interesting properties:

- Strong eventual consistency
- Replicate presence join and leave events across the cluster without merge conflicts.
- Conflicts are *mathematically impossible*
- Supports replication without remote synchronization.
    - There's no need for a distributed consensus algorithm.
    - There's no need for a global lock.
    - If data arrives out of order or arrives multiple times, it doesn't matter. If you can fit your problem within the CRDT problem-space, conflicts are mathematically impossible.


See [ElixirConf 2015 - CRDT: Datatype for the Apocalypse by Alexander Songe](https://www.youtube.com/watch?v=txD1tfyIIvY) for a good introduction to them.

A simple solution using a simple heartbeat protocol is to piggyback your join/leave changes on the heartbeat exchanged among nodes. If one node misses a preconfigured number of heartbeats, the other nodes(s) will declare the first as down and cleans up their state locally and broadcast to the users that are connected to the remaining node. Cool! Each node maintains a copy of the global state of which it is aware, and broadcasts the presence (or absense) of all users to those users who are connected to that node. Every node acts independently of the others.

According to [Chris McCord, during his keynote talk at Erlang Factory SF 2016](https://youtu.be/XJ9ckqCMiKk?t=1278), heartbeats will start scaling poorly once you get to hundreds of nodes. At that point, you will want to think about switching to a Gossip protocol.

## Tools
- Vagrant: the command line utility for managing the lifecycle of virtual machines. At it's core, Vagrant is a command-line driven wrapper around Virtualbox or VMware. Some nice features are:
    - Lots of existing images: check [Vagrantboxes](http://www.vagrantbox.es/) for one place to get images.
    - Snapshot and package your current machine to a Vagrant box file.
    - Ability to fine tune settings fo the VM, including theings like RAM, CPU, APIC, etc.
    - Vagrantfiles allows you to setup your box on initialization - install packages, modifying configuration, moving code around, etc.
    - Integration with Configuration Management (CM) tools like Puppet, Chef, Ansible and Salt. See [provisioning](https://www.vagrantup.com/docs/provisioning/) in the Vagrant documentation.

## Problems with RegEx Matching HTML tags

There was a discussion on Stackoverflow about not being able to match HTML tags using regular expressions. [^1] It has an extraodinary answer. Here is a short list of some of the problems highlighted in the answer (which is a wonderful display of descent into madness):

- the unholy child weeps the blood of virgins
- Russian hackers pwn your webapp
- summons tainted souls into the realm of the living
- you give in to THEM and their blasphemous ways which doom us all to inhuman toil for the One whose Name cannot be expressed in the Basic Multilingual Plan
- he comes
- it will liquify the nerves of the sentient whilst you observe your psyche withering n the onslaught of horror
- the transgression of the child ensures regex will consume all living tissue (except for HTML)
- using regex to parse HTML has doomed humanity t an eternity of dread torture and security holes.
- using regex as a tool to process HTML establishes a breach between this world and the dread relam of corrupt entities
- transport a programmer's consciousness into a world of ceaseless screaming
- he comes
- will devour your HTML parser, application and existence for all time
- he comes
- he comes
- his unholy radiance destroying all enlightenment
- HTML tags will leak from your eyes like liquid pain
- extinguishes the voices of mortal man from the sphere
- the pony he comes
- Zalgo is Tony the Pony he comes

## References
- The discussion on Hacker News about [How Go solves so many problems for web developers](https://news.ycombinator.com/item?id=11172284).
- [How Go solves so many problems for web developers](http://ewanvalentine.io/why-go-solves-so-many-problems-for-web-developers/)
- [Service-oriented architecture](https://en.wikipedia.org/wiki/Service-oriented_architecture) on Wikipedia.
- [Learn REST: A Tutorial](http://rest.elkstein.org/).
- [Thoughts on RESTful API Design](http://restful-api-design.readthedocs.org/en/latest/index.html)
- [Ontology and Taxonomy of Services in a Service-Oriented Architecture](https://msdn.microsoft.com/en-us/library/bb491121.aspx)
- [Security Assertion Markup Language (SAML)](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language) is an XML-based data format for exchanging authentication and authorization data beteween parties, in particular, an identity provider and a service provider.
- [Identity Provider Pattern](http://arnon.me/soa-patterns/identity-provider/)
- [SOA Patterns](http://arnon.me/soa-patterns/)
- [Kerberos Might Not Be Dead, but It's Not Feeling Well](http://windowsitpro.com/identity-management/kerberos-might-not-be-dead-its-not-feeling-well)
- [^1]: [RegEx match open tags except XHTML self-contained tags](http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags?answertab=active#tab-top)