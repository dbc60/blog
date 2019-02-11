---
layout: post
title: Programming Tips & Snippets
tags:
    - notes
    - software
    - programming
---
Some code. Some notes. Some organization. Some graphics. Some Handmade Hero stuff.

## Contents
{:.no_toc}

- TOC
{:toc}

## Document History

| Date | Author | Summary of Changes |
|-----------:|-----------------:|:---------------|
| 2017.02.02 | Doug Cuthbertson | Initial draft. |

## Keep the Environment Organized
A good directory layout can help keep files organized. Jekyll does this well. The Go programming language and the simple directory hierarchy Casey Muratori uses for [Handmade Hero](https://handmadehero.org/) are also good models.

### Go Workspace
Go code is kept in a _workspace_. A workspace contains _many_ source repositories (that is, `git` or `mercurial` repositories). The Go tool understands the layout of a workspace. You don't need a `Makefile`. The file and directory layout contain all the necessary information.

A Go workspace looks like this:

```terminal
$GOPATH/
    src/
        github.com/user/repo/
            mypkg/
                mysrc1.go
                mysrc2.go
            cmd/mycmd/
                main.go
    bin/
        mycmd
```

Making a workspace is as simple as:

```terminal
mkdir /tmp/gows
GOPATH=/tmp/gows
```

The `GOPATH` environment variable tells the Go tool where your workspace is.

You can find more information about Go workspaces here:

- [Organizing Go Code](https://talks.golang.org/2014/organizeio.slide#1)
- [How to Write Go Code](https://golang.org/doc/code.html)

### Handmade Hero Workspace
Casey Muratori created a simple directory layout for his projects. There are four directories. A `/handmade/code` directory for all C/C++ source files and headers, `/handmade/misc` for shell scripts, editor configuration and other stuff, `/handmade/data` for test assets and `/build` where all the build results go.

```terminal
w:\
    handmade\
        code\
        data\
        misc\
    build\
```

## Windows Main Program
When writing a main routine for a console program in C or C++, the function signature is typically `int main(int argc, char* argv[])` or just `int main()`. There is also a third form for the signature of the main startup routine: `int main(int argc, char* argv[], char*envp[])`, but it is not typically used. While it's supported on Windows and several compilers on Unix-based operating systems, it is not necessarily supported everywhere.

On Window, we can also use either `int wmain()` or `int wmain(int argc, wchar_t* argv[])` so filenames with non-ascii characters can be supported. Again, the third parameter, `wchar_t* envp[]` for environment variables, is supported but not typically used.

To create a main function that interacts with Windows API, the function signature is `int CALLBACK WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)`. The `hInstance` argument is the base address of the in-memory image of the executable. It is primarily used to load resources from the executable. Its value can also be obtained from the `GetModuleHandle` function.

The `hPrevInstance` argument has no meaning. It was used in 16-bit Windows, but is now always zero.

The `lpCmdLine` argument is a Unicode string containing the command-line arguments. Its value can also be obtained from the `GetCommandLine` function.

The `nCmdShow` argument is a flag that specifies whether the main application window will be minimized, maximized or show normally. Its value can also be obtained from the `GetStartInfo` function.

Finally, the return value, an `int`, is not used by the operating system, but you can use it to pass a status code to another program.

According to the docs for the [WinMain entry point](https://msdn.microsoft.com/en-us/library/windows/desktop/ms633559(v=vs.85).aspx), `WinMain` should initialize the application, display its main window and enter a loop to retrieve and dispatch messages. When it receives a `WM_QUIT` message, it should end the message loop and return the exit value contained in the message's `wParam` parameter. If the function ends before entering the message loop, it should return zero. If `WM_QUIT` was received as a result of calling `PostQuitMessage`, the value of `wParam` is the value of the `PostQuitMessage` function's `nExitCode` parameter.

There is a lot of good information in [this Stackoverflow question](http://stackoverflow.com/questions/13871617/winmain-and-main-in-c-extended) about using `main` vs `WinMain`. I've extracted some of it here:

Since the values of the `WinMain` function can be obtained obtained through API function calls, it's not essential to use that signature as the application entry point. The only advantage for this entry point is that it makes the linker in the Microsoft tool chain automatically default to the GUI subsystem. Even the use of `wmain` can be avoided by using `GetCommandLine` and `CommandLineToArgvW` functions to pick up UTF-16 encoded arguments.

To make the Microsoft linker use `main` as the entry point, set the environment variable `LINK` to `/entry:mainCRTStartup`, or specify that option directly when building your application with Microsoft tools. `mainCRTStartup` is the Microsoft runtime library entry point that calls the standard `main` function.

A console subsystem program, or in short just a console program, is one that requires a console window. This is the default subsystem for all Windows linkers I've used (admittedly not a great many), possibly for all Windows linkers period.

For a console program Windows creates a console window automatically if needed. Any Windows process, regardless of subsystem, can have an associated console window, and at most one. Also, the Windows command interpreter waits for a console program program to finish, so that the program's text presentation has finished.

Conversely, a GUI subsystem program is one that doesn't require a console window. The command interpreter does not wait for a GUI subsystem program, except in batch files. One way to avoid the completion wait, for both kinds of program, is to use the `start` command. One way to present console window text from a GUI subsystem program is to redirect its standard output stream. Another way is to explicitly create a console window from the program's code.

## Creating a Window
One of the first things our Windows program needs to do is create a new window. First retrieve the module handle for the application. Next, fill out a `WNDCLASSEX` structure that describes the kind of window we need, and register it with the Windows subsystem. Finally, pass the module handleand a few other arguments to the `CreateWindowEx` function, and it will return a handle to a new window.

```cpp
int main()
{
    int result = ERROR_SUCCESS;
    HMODULE instance;
    WNDCLASSEX winclassex = {};

    instance = GetModuleHandle(nullptr);

    winclassex.cbSize
    winclassex.style = CS_HREDRAW | CS_VREDRAW;
    winclassex.lpfnWndProc = Win32MainWindowCallback;
    winclassex.hInstance = instance;
    winclassex.hCursor = LoadCursor(0, IDC_ARROW);
    //    winclassex.hIcon;
    winclassex.lpszClassName = L"Application";

    if (RegisterClassEx(&winclassex)) {
        HWND window =
            CreateWindowEx(0, // WS_EX_TOPMOST|WS_EX_LAYERED,
                           winclassex.lpszClassName,
                           L"My Application",
                           WS_OVERLAPPEDWINDOW | WS_VISIBLE,
                           CW_USEDEFAULT,
                           CW_USEDEFAULT,
                           CW_USEDEFAULT,
                           CW_USEDEFAULT,
                           0,
                           0,
                           instance,
                           0);
        if (window) {
            // Do more stuff
        }
    }

    return result;
}
```

Note that `winclassex.lpfnWndProc` is set to the address of a function, a [WindowProc callback function](https://msdn.microsoft.com/en-us/library/windows/desktop/ms633573(v=vs.85).aspx). Its signature is `LRESULT CALLBACK WindowProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)`, and it is used to process messages sent to the window.

## WindowProc Callback Function
The `WindowProc` callback function (also referred to as `WndProc`) is an application-defined function that processes messages sent to a window. Its signature is:

```cpp
LRESULT CALLBACK WindowProc(_In_ HWND   hWnd,
                            _In_ UINT   uMsg,
                            _In_ WPARAM wParam,
                            _In_ LPARAM lParam);
```

The value of `hWnd` is a handle to the window to which the message was sent, and `uMsg` identifies the actual message. The meanings of`wParam` and `lParam` depend on the message. The Windows OS produces different messages as a result of various events taking place in the system. Typically, an application processes very few of these messages. To ensure that all messages are processed, Windows provides a default window procedure called `DefWindowProc`. It can be called by an application when it receives a message for which it has no response. It is usually called at the end of the applications own `WindowProc` function to pass all messages the application has not already processed.

See [Window Notifications](https://msdn.microsoft.com/en-us/library/windows/desktop/ff468922(v=vs.85).aspx) for the values that `uMsg` can take, and the definition of each of them. Note that the WM_QUIT message is not associated with a window and therefore will never be received through a window's window procedure. It is retrieved only by the `GetMessage` or `PeekMessage` functions.

It's probably a good idea to review the documentation on messages and queues.

- [About Messages and Queues](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644927(v=vs.85).aspx) describes Windows messages and how they are incorporated into event-driven applications.
- [Using Messages and Queues](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644928(v=vs.85).aspx) has code examples for creating a message loop, examining a message queue, and for posting and sending a message.

## Windows I/O
I think I need to consider all forms of input and output that Windows allows. Off the top of my head, here's a quick list:

- Keyboard and mouse (process Window event messages).
- Game controllers (XInput).
- Tablet and pen input.
- File I/O.
- Audio output. The DirectSound and XAudio2 APIs are built in to Windows. Some people recommend [FMOD.io](http://www.fmod.com/) for sound development.
- Graphical output. Software rendering, DirectX and OpenGL. There's also [Simple DirectMedia Layer](https://www.libsdl.org/), which covers audio, keyboard, mouse, joystick and graphics via OpenGL and Direct3D.
- Memory allocation. This can be done through standard libraries, or one can have the OS allocate a single block and let the application manage its own memory. The final decision depends on how the app uses memory. I'm told that some games grab one large block of memory, and slice it up for graphics and sound on their own via a simple arena allocator. Once memory is segmented, it isn't released until the game ends.
- Network I/O. [RakNet](http://www.jenkinssoftware.com/) was a commercial network engine for game programmers. The company was purchased by [Oculus](https://www.oculus.com/) and is now a cross-platform [open source](https://github.com/OculusVR/RakNet) C++ networking engine for game programmers. That said, the github repo hasn't been touched in 3 years. Other network APIs to consider are:

    - Valve's [SteamWorks](https://partner.steamgames.com/documentation/api)
    - [Google Play Games Services](https://developers.google.com/games/services/common/concepts/realtimeMultiplayer)
    - Microsoft native [network APIs](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365249(v=vs.85).aspx)

Additionally, consider Windows APIs and instrinsics for managing and measuring dates and time.

## Keyboard Input
The simple example I've been following, from Handmade Hero, is too simple for general use of the keyboard. Here are some references for better keyboard handling:

- [About Keyboard Input](https://msdn.microsoft.com/en-us/library/windows/desktop/ms646267(v=vs.85).aspx) is a general overview of the input model, focus and activation, messages, status and character translation.
- [Using Keyboard Input](https://msdn.microsoft.com/en-us/library/windows/desktop/ms646268(v=vs.85).aspx) has sample code for processing keystroke messages and translating character messages.
- [Keyboard Input Reference](https://msdn.microsoft.com/en-us/library/windows/desktop/ff468857(v=vs.85).aspx) has links to documentation about keyboard functions, messages, notifications, structures and constants.

### A Simple Keyboard, Mouse and Game Controller Interface
Windows allows up to four game controllers to be connected at one time. Here we use a simple model where the keyboard is interpreted as a fifth game controller and mouse input is passed to the application along side those five controls. The interface common to both the OS and the app is written in C so the platform-specific (OS) code and platform-non-specific (app) code can be written in any programming language with a C interface.

```cpp
#ifdef __cplusplus
extern "C" {
#endif

typedef struct AppButtonState {
    int half_transition_count_;
    b32 ended_down_;
} AppButtonState;


typedef struct AppControllerInput {
    b32 is_connected_;
    b32 is_analog_;
    r32 stick_average_x_;
    r32 stick_average_y_;

    union {
        // The magic constant in this array must match the number of
        // AppButtonState fields in the struct that follows  (excluding
        // the terminator) so this union will work correctly.
        AppButtonState buttons_[12];
        struct {
            AppButtonState move_up_;
            AppButtonState move_down_;
            AppButtonState move_left_;
            AppButtonState move_right_;

            AppButtonState action_up_;
            AppButtonState action_down_;
            AppButtonState action_left_;
            AppButtonState action_right_;

            AppButtonState left_shoulder_;
            AppButtonState right_shoulder_;

            AppButtonState back_;
            AppButtonState start_;

            // NOTE: All buttons must be added above this line

            AppButtonState terminator_;
        };
    };
} AppControllerInput;


typedef struct AppInput {
    // This is a notional way to pass mouse information to the app. Windows
    // defines five mouse buttons: Left, Middle/wheel, Right, X1 and X2.
    AppButtonState mouse_buttons_[5];
    s32 mouse_x_;   // x (left-right) position
    s32 mouse_y_;   // y (up-down) position
    s32 mouse_z_;   // mouse wheel

    r32 dt_for_frame_;

    AppControllerInput controllers_[5];
} AppInput;

#ifdef __cplusplus
}
#endif
```

In the game-loop, we process the keyboard input first. The keyboard is the first controller in the array of five controllers.

```cpp
// The keyboard is the first controller (index === 0) of the five.
// Note: We can't zero everything because the up/down state will be wrong!!!
AppControllerInput *old_keyboard_controller = GetController(input_old, 0);
AppControllerInput *new_keyboard_controller = GetController(input_new, 0);

// Initialize the new keyboard controller to zero. This ensures, among
// other things that the half transition count is zero at the beginning
// of each frame.
*new_keyboard_controller = {};
new_keyboard_controller->is_connected_ = true;
for (int button_index = 0;
    button_index < ARRAY_COUNT(new_keyboard_controller->buttons_);
    ++button_index) {
    new_keyboard_controller->buttons_[button_index].ended_down_ =
        old_keyboard_controller->buttons_[button_index].ended_down_;
}

Win32ProcessPendingMessages(window, new_keyboard_controller);
```

Assuming the key mapped to the pause-state was _not_ pressed, the OS gets the current state of the mouse.

```cpp
POINT MouseP;
GetCursorPos(&MouseP);
// Map the mouse pointer from the screen to the window
ScreenToClient(window, &MouseP);
input_new->mouse_x_ = MouseP.x;
input_new->mouse_y_ = MouseP.y;
input_new->mouse_z_ = 0; // TODO: Support mousewheel?

// Get the up/down state for the five mouse buttons
// Left mouse button
Win32ProcessKeyboardMessage(&input_new->mouse_buttons_[0],
                            GetKeyState(VK_LBUTTON) & (1 << 15));

// Middle/wheel mouse button
Win32ProcessKeyboardMessage(&input_new->mouse_buttons_[1],
                            GetKeyState(VK_MBUTTON) & (1 << 15));

// Right mouse button
Win32ProcessKeyboardMessage(&input_new->mouse_buttons_[2],
                            GetKeyState(VK_RBUTTON) & (1 << 15));

// X1 mouse button
Win32ProcessKeyboardMessage(&input_new->mouse_buttons_[3],
                            GetKeyState(VK_XBUTTON1) & (1 << 15));

// X2 mouse button
Win32ProcessKeyboardMessage(&input_new->mouse_buttons_[4],
                            GetKeyState(VK_XBUTTON2) & (1 << 15));
```

Next, we figure out how many controllers are connected and poll them for their current state.

```cpp
// TODO: Need to not poll disconnected controllers to avoid
// xinput frame rate hit on older libraries...
// TODO: Should we poll this more frequently?
DWORD MaxControllerCount = XUSER_MAX_COUNT;
if (MaxControllerCount > (ARRAY_COUNT(input_new->controllers_) - 1)) {
    MaxControllerCount = (ARRAY_COUNT(input_new->controllers_) - 1);
}

for (DWORD ControllerIndex = 0;
        ControllerIndex < MaxControllerCount;
        ++ControllerIndex) {
    DWORD OurControllerIndex = ControllerIndex + 1;
    AppControllerInput *OldController = GetController(input_old, OurControllerIndex);
    AppControllerInput *NewController = GetController(input_new, OurControllerIndex);

    XINPUT_STATE ControllerState;
    if (XInputGetState(ControllerIndex, &ControllerState) == ERROR_SUCCESS) {
        NewController->is_connected_ = true;
        NewController->is_analog_ = OldController->is_analog_;

        // NOTE: This controller is plugged in
        // TODO: See if ControllerState.dwPacketNumber increments too rapidly
        XINPUT_GAMEPAD *Pad = &ControllerState.Gamepad;

        // TODO: This is a square deadzone, check XInput to
        // verify that the deadzone is "round" and show how to do
        // round deadzone processing.
        NewController->stick_average_x_ = Win32ProcessXInputStickValue(
            Pad->sThumbLX, XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE);
        NewController->stick_average_y_ = Win32ProcessXInputStickValue(
            Pad->sThumbLY, XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE);
        if ((NewController->stick_average_x_ != 0.0f) ||
            (NewController->stick_average_y_ != 0.0f)) {
            NewController->is_analog_ = true;
        }

        if (Pad->wButtons & XINPUT_GAMEPAD_DPAD_UP) {
            NewController->stick_average_y_ = 1.0f;
            NewController->is_analog_ = false;
        }

        if (Pad->wButtons & XINPUT_GAMEPAD_DPAD_DOWN) {
            NewController->stick_average_y_ = -1.0f;
            NewController->is_analog_ = false;
        }

        if (Pad->wButtons & XINPUT_GAMEPAD_DPAD_LEFT) {
            NewController->stick_average_x_ = -1.0f;
            NewController->is_analog_ = false;
        }

        if (Pad->wButtons & XINPUT_GAMEPAD_DPAD_RIGHT) {
            NewController->stick_average_x_ = 1.0f;
            NewController->is_analog_ = false;
        }

        r32 Threshold = 0.5f;
        Win32ProcessXInputDigitalButton(
            (NewController->stick_average_x_ < -Threshold) ? 1 : 0,
            &OldController->move_left_, 1,
            &NewController->move_left_);
        Win32ProcessXInputDigitalButton(
            (NewController->stick_average_x_ > Threshold) ? 1 : 0,
            &OldController->move_right_, 1,
            &NewController->move_right_);
        Win32ProcessXInputDigitalButton(
            (NewController->stick_average_y_ < -Threshold) ? 1 : 0,
            &OldController->move_down_, 1,
            &NewController->move_down_);
        Win32ProcessXInputDigitalButton(
            (NewController->stick_average_y_ > Threshold) ? 1 : 0,
            &OldController->move_up_, 1,
            &NewController->move_up_);

        Win32ProcessXInputDigitalButton(Pad->wButtons,
                                        &OldController->action_down_, XINPUT_GAMEPAD_A,
                                        &NewController->action_down_);
        Win32ProcessXInputDigitalButton(Pad->wButtons,
                                        &OldController->action_right_, XINPUT_GAMEPAD_B,
                                        &NewController->action_right_);
        Win32ProcessXInputDigitalButton(Pad->wButtons,
                                        &OldController->action_left_, XINPUT_GAMEPAD_X,
                                        &NewController->action_left_);
        Win32ProcessXInputDigitalButton(Pad->wButtons,
                                        &OldController->action_up_, XINPUT_GAMEPAD_Y,
                                        &NewController->action_up_);
        Win32ProcessXInputDigitalButton(Pad->wButtons,
                                        &OldController->left_shoulder_, XINPUT_GAMEPAD_LEFT_SHOULDER,
                                        &NewController->left_shoulder_);
        Win32ProcessXInputDigitalButton(Pad->wButtons,
                                        &OldController->right_shoulder_, XINPUT_GAMEPAD_RIGHT_SHOULDER,
                                        &NewController->right_shoulder_);

        Win32ProcessXInputDigitalButton(Pad->wButtons,
                                        &OldController->start_, XINPUT_GAMEPAD_START,
                                        &NewController->start_);
        Win32ProcessXInputDigitalButton(Pad->wButtons,
                                        &OldController->back_, XINPUT_GAMEPAD_BACK,
                                        &NewController->back_);
    } else {
        // NOTE: The controller is not available
        NewController->is_connected_ = false;
    }
}
```

Now that we've gather all the input data, we can call the function provided by the application that accepts the input state and returns an update graphic buffer.

```cpp
ThreadContext thread_context = {};
AppOffscreenBuffer offscreen_buffer;
global_offscreen_buffer.InitializeAppOffscreenBuffer(offscreen_buffer);
if (app.is_valid_) {
    app.UpdateAndRender_(&thread_context, &app_memory, input_new, &offscreen_buffer);
}
```

We still need sound from the application. Here's a first pass of what needs to be done to acquire a sound buffer from the app. DirectSound runs in the background racing through a circular sound buffer. It has a play cursor indicating where in the buffer it is currently playing sound, and a write cursor indicating where in the buffer an app may write new sound data. We have to calculate how much sound the app needs to write to the sound buffer so we always have the current desired sound available for the current and future update intervals.

```cpp
/****************************************************/
/* SOUND TEST CODE */
/****************************************************/
// NOTE(casey): DirectSound output test
LARGE_INTEGER wall_clock_audio = Win32GetWallClock();
r32 FromBeginToAudioSeconds = Win32GetSecondsElapsed(wall_clock_flip, wall_clock_audio);

DWORD sound_cursor_play;
DWORD sound_cursor_write;
HRESULT ds_result;

ds_result = global_secondary_sound_buffer->GetCurrentPosition(&sound_cursor_play,
                                                                &sound_cursor_write);
if (SUCCEEDED(ds_result)) {
    /* NOTE(casey):

    Here is how sound output computation works.

    We define a safety value that is the number
    of samples we think our game update loop
    may vary by (let's say up to 2ms)

    When we wake up to write audio, we will look
    and see what the play cursor position is and we
    will forecast ahead where we think the play
    cursor will be on the next frame boundary.

    We will then look to see if the write cursor is
    before that by at least our safety value.  If
    it is, the target fill position is that frame
    boundary plus one frame.  This gives us perfect
    audio sync in the case of a card that has low
    enough latency.

    If the write cursor is _after_ that safety
    margin, then we assume we can never sync the
    audio perfectly, so we will write one frame's
    worth of audio plus the safety margin's worth
    of guard samples.
    */
    if (!is_valid_sound) {
        sound_output.running_sample_index_ = sound_cursor_write / sound_output.bytes_per_sample_;
        is_valid_sound = true;
    }

    DWORD byte_to_lock =
        (sound_output.running_sample_index_ * sound_output.bytes_per_sample_)
        % sound_output.secondary_buffer_size_;

    DWORD ExpectedSoundBytesPerFrame =
        static_cast<DWORD>(
            static_cast<r32>(sound_output.samples_per_second_ * sound_output.bytes_per_sample_)
            / app_update_hz);

    r32 SecondsLeftUntilFlip = (target_seconds_per_frame - FromBeginToAudioSeconds);
    DWORD ExpectedBytesUntilFlip =
        static_cast<DWORD>((SecondsLeftUntilFlip / target_seconds_per_frame)
                           * static_cast<r32>(ExpectedSoundBytesPerFrame));
    DWORD ExpectedFrameBoundaryByte = sound_cursor_play + ExpectedBytesUntilFlip;

    DWORD SafeWriteCursor = sound_cursor_write;
    if (SafeWriteCursor < sound_cursor_play) {
        SafeWriteCursor += sound_output.secondary_buffer_size_;
    }

    Assert(SafeWriteCursor >= sound_cursor_play);
    SafeWriteCursor += sound_output.safety_bytes_;

    bool AudioCardIsLowLatency = (SafeWriteCursor < ExpectedFrameBoundaryByte);

    DWORD target_cursor;
    if (AudioCardIsLowLatency) {
        target_cursor = ExpectedFrameBoundaryByte + ExpectedSoundBytesPerFrame;
    } else {
        target_cursor = sound_cursor_write + ExpectedSoundBytesPerFrame +
                        sound_output.safety_bytes_;
    }

    target_cursor = target_cursor % sound_output.secondary_buffer_size_;


    DWORD bytes_to_write;

    if (byte_to_lock > target_cursor) {
        bytes_to_write = sound_output.secondary_buffer_size_ - byte_to_lock;
        bytes_to_write += target_cursor;
    } else {
        bytes_to_write = target_cursor - byte_to_lock;
    }

    AppSoundOutputBuffer sound_buffer = {};
    sound_buffer.samples_per_second_ = sound_output.samples_per_second_;
    sound_buffer.sample_count_ = bytes_to_write / sound_output.bytes_per_sample_;
    sound_buffer.samples_ = sound_samples;
    if (app.GetSoundSamples_) {
        app.GetSoundSamples_(&thread_context, &app_memory, &sound_buffer);
    }

    Win32FillSoundBuffer(&sound_output,
                         byte_to_lock,
                         bytes_to_write,
                         &sound_buffer);
} else {
    wchar_t buf[256];
    _snwprintf_s(buf, ARRAY_COUNT(buf),
                 L"Failed to get current position in sound buffer: 0x%08x\n",
                 ds_result);
    OutputDebugString(buf);
    is_valid_sound = false;
}
/****************************************************/
/* END SOUND TEST CODE */
/****************************************************/
```

### Push, Pull, Polling and Events
The set of structures shown in the section title "A Simple Keyboard, Mouse and Game Controller Interface" was designed by Casey Muratori for Handmade Hero. It works for that game, because fresh data for the state of the keyboard, mouse and any connected game controllers is pushed from the OS to the game 30 to 60 times a second. It is a push model. The OS pushes fresh state at regular intervals to the application code. The application has the remainder of the interval to respond with an update to its state.

I wonder if other apps would be better served by a pull model, where there would be a callback function supplied to the application during initialization. The app would call that function to get the current state of the user input when it needed it.

On one hand, an app could be designed on an event-based model. The OS initializes and waits on I/O events, and when one is triggered, it calls a function to update the app on. However, if the app is processing data and needs to update the user, either it will have to be polled regularly (as in the game model used by Handmade Hero), or it will need one or more callback functions supplied by the OS to be used to provide feedback to the user.

It will be educational to build and test different models.

## Windows Application Manifest
I need to learn how to define an application manifest, and what it does to effect how a program runs on Windows. I do know that different versions of Windows handle uncaught exceptions differently. As of Windows 7 and Server 2008 R2, a 64-bit program running on 64-bit Windows will first terminate the process and then the Program Compatibility Assistant (PCA) offers to fix it then next time you run the application. You can disable the PCA mitigation by adding a Compatibility section to the [application manifest](https://msdn.microsoft.com/en-us/library/dd371711(VS.85).aspx).

References:

- [Application Manifest](https://msdn.microsoft.com/en-us/library/dd371711(VS.85).aspx)

## Windows 32-bit on Windows 64-bit
This is abbreviated as WOW64. It is subsystem of the Windows Operating System capable of running 32-bit applications in the 64-bit versions of Windows. It is an optional subsystem that is not included in Nano Server.

### Nano Server
By the way, Nano Server is one of three installation options in both Windows Server 2016 Standard and Datacenter. The other two are Server with Desktop Experience and Server Core. According to [Wikipedia, Nano Server](https://en.wikipedia.org/wiki/Windows_Server_2016#Nano_Server) is a minimal-footprint headless version of Windows Server. It excludes the graphical user interface, WOW64 (support for 32-bit software) and Windows Installer. It does not support console login, either locally or via Remote Desktop Connection. All management is performed remotely via Windows Management Instrumentation (WMI), Windows Powershell and Remote Server Management Tools (a collection of web-based GUI and command-line tools). However, in Technical Preview 5, Microsoft has re-added the ability to administer Nano Server locally through PowerShell. According to Microsoft engineer Jeffrey Snover, Nano Server has 93% lower VHD size, 92% fewer critical security advisories, and 80% fewer reboots than Windows Server.

Nano Server is only available to customers who subscribe to the [Microsoft Software Assurance](https://www.microsoft.com/en-us/licensing/licensing-programs/software-assurance-default.aspx) program. There is a [Wikipedia page](https://en.wikipedia.org/wiki/Microsoft_Software_Assurance) that summarizes the program.

### References

- [Windows Application Manifest](https://msdn.microsoft.com/en-us/library/dd371711(VS.85).aspx)
- [Microsoft Announces Nano Server for Modern Apps and Cloud](https://blogs.technet.microsoft.com/windowsserver/2015/04/08/microsoft-announces-nano-server-for-modern-apps-and-cloud/)
-[Introducing Server management tools](https://blogs.technet.microsoft.com/servermanagement/2016/02/09/introducing-server-management-tools/)
[Windows Server 2016 new Current Branch for Business servicing options](https://blogs.technet.microsoft.com/windowsserver/2016/07/12/windows-server-2016-new-current-branch-for-business-servicing-option/)
- [Ray Tracing in One Weekend](http://in1weekend.blogspot.com/2016/01/ray-tracing-in-one-weekend.html)
- [Ray Tracing the Next Week](http://in1weekend.blogspot.com/2016/01/ray-tracing-second-weekend.html)
- [Ray Tracing: The Rest of Your Life](http://in1weekend.blogspot.com/2016/03/ray-tracing-rest-of-your-life.html)
- [Revisiting Network I/O APIs: The netmap Framework](http://queue.acm.org/detail.cfm?id=2103536) in the January 17, 2012 issue of ACM Queue magazine (Vol. 10, No. 1).
