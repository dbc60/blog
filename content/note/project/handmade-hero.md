---
title: Handmade Hero
date: 2017-02-18
draft: true
categories: [project]
tags: [games]
---
Notes on game design and programming from Casey Muratori's Handmade Hero videos.

A good directory layout can help keep files organized. Jekyll does this well. The Go programming language and the simple directory hierarchy Casey Muratori uses for [Handmade Hero](https://handmadehero.org/) are also good models.
<!--more-->

The Handmade Hero model is as simple a directory layout as anyone could ask for. There are four directories. A `/handmade/code` directory for all C source files and headers, `/handmade/misc` for shell scripts, editor configuration and other stuff, `/handmade/data` for test assets and `/build` where all the build results go.

```term
w:\
    handmade\
        code\
        data\
        misc\
    build\
```

The directory `w:\handmade` is where all of the code and scripts go. The directory `w:\build` is where all the build artifacts go.

## The Drudge Work: Starting a Project
When programming on Windows, you can code and build within Visual Studio. Muratori likes to write code within Emacs, and use Visual Studio from the command line to compile, link and debug his code.

Another thing he does is use the `subst` command to map a drive to his project directory. I do the same thing. In fact, I created a small batch script in `C:\Users\Doug\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\dougs.build.env.bat` to set my aliases. It runs every time I logon so my `N:` and `P:` drives are always ready for me.

```shell
@echo
REM Place this file in
REM "C:\Users\Doug\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
REM to set these directory paths to drive letters after login.
subst N: C:\Users\Doug\Notes
subst P: E:\Users\Doug\Projects
```

The first code file Muratori creates is `win32_handmade.cpp` and adds the entry point for Windows. He uses the typical entry point `WinMain`:

```cpp
int CALLBACK WinMain(_In_ HINSTANCE hInstance,
                     _In_ HINSTANCE hPrevInstance,
                     _In_ LPSTR lpCmdLine,
                     int nCmdShow);
```

It's perfectly reasonable to use `int main();` or `int main(int argc, char* argv[]);`. To make a window, you'll need the value `hInstance` that's provided by `WinMain`. You get it by calling `GetModuleHandle(nullptr)`, as in:

```cpp
HMODULE instance = GetModuleHandle(nullptr);
```

Note that `HMODULE` and `HINSTANCE` are the same thing. I use `HMODULE` because that is the exact return type specified by the documentation for `GetModuleHandle`.

Similarly, you might want to get the command line arguments. They are provided by `WinMain` in its `lpCmdLine` parameter, and its value can also be obtained from the `GetCommandLine` function.

```cpp
LPTSTR WINAPI GetCommandLine(void);
```

For a few more details about entry points (including using `wmain`), see [Programming Tips & Snippets](/note/2017-02-02-programming-tips-and-snippets).

## Interface: Platform-Specific vs Platform Nonspecific Code
One of the basic design premises in Handmade hero is that code can be split into functions written for a specific operating system and those that are for the game.

## Exploration Based Architecture
This is from episode 27. He talks about Project State Space. On day zero, your project is in one state, and your goal is to get to a shipping state. However, you have little to no idea what that shipping state looks like or how to get there.

On any given day, you're driving to some new point somewhere in that state space. Over time, you meander toward your goal. How well you do depends on how good you are with dead reconning.

If you do a lot of up-front design, you spend a lot of time potentially heading in the wrong time. Up-front design sets waypoints for a general direction. Those waypoints look good, but may force you in the wrong direction.

Don't look too far ahead. Take an explore and lock approach. Instead of picking a set of things that we think are the directions to go ahead of time (which may turn out to be wrong), we're going to take our current location in the project state space, wherever it is, explore around the space and see what we find in there. When we find something that we feel is along the path to shipping, we will lock that in and make that our new location. We repeat this process.

In summary, we start from where we are, do explorations which amount to writing whatever code comes to mind for the thing we need to implement. We explore the possibilities and see what works in the code. When we find something we are happy with, we'll lock that in and call that the new starting point for the next problem.

As you get more experience as a programmer, you learn to sense the gradient. With each exploration, you get better at course correction to stay in the channel to good architecture and avoid meandering into designs that are merely okay, fair, bad or even awful.

## Game Design
Muratori is a fan of the original Legend of Zelda, because it dropped you into a world with a lot of richness and interest, but few constraints on where you could travel to and what you could do. I think that's why I like Skyrim so much.

So, the main design goal is to minimize the constraints - no hand holding. He wants to be able to make tile maps that give the game a feel of the old classic tile map games, but without using tile map graphics. That is, players aren't constrained to moving from one tile to another. They should move smoothly across the entire map. The graphic elements, such as trees, grass, walls and water, can be constrained (I think) to tiles, but not the player's movements.

The tiles add a constraint about the kinds of puzzles that players can solve. It reduces the degrees of freedome for moving puzzle pieces around - that is, the player can move pushable objects from one tile to another, but limited by tiles with immovable objects. It makes gameplay easier to understand.

The overall goals are:

- Tile map
- Stuff that moves around on the map
- A fancy renderer so the game doesn't look like a tile map, but it's still understandable as a tile map for moving and puzzle solving.
- The world is procedurally generated - maybe only the start or ending screens would be hard coded, but all others would be fresh every time you create a new instance of the game.
- An overworld map that contains lots tile maps
- Dungeons. A dungeon is a lower level of tile maps. Each dungeon can be entered at certain locations on the overworld map.
- Consistent Space. If a dungeon can be entered from two locations, one can enter the dungeon at one location, travel through it and when the player exits it, they are at the other location on the world map. Tiles should always be the same size. So, if the dungeon entries are 27 tiles apart on the world map, the dungeon should be the same size.
- Giant Worlds. No limit to the size of the world, but it's okay if the real limit is so large that a player couldn't travel from one end to another in a week of continuous play.
- Combinatorially rich. His example is fear. If something can become fearful, then if you have a magic scepter that can cast spells on tiles, and be loaded with gems, and it's loaded with a fear gem, then if it casts fear on a tile, and a monster walks on that tile, it becomes fearful. Also, if the rule is that if a monster is both fearful and weak then it immediately runs away. So, if a weak monster walks on a tile with fear cast on it, then it will be both weak and fearful and must run away.

## Rendering
Drawing a simple rectangle on the screen.

```cpp
// A simple rounding function. There's probably a better way using intrinsics.
INTERNAL_FUNCTION s32
Round32ToS32(r32 value) {
    s32 result = static_cast<s32>(value + 0.5f);
}

INTERNAL_FUNCTION s32
RoundR32ToS32(r32 value) {
    s32 result = static_cast<s32>(value + 0.5f);

    return result;
}

INTERNAL_FUNCTION u32
RoundR32ToU32(r32 value) {
    u32 result = static_cast<u32>(value + 0.5f);

    return result;
}


/*
    The min and max values locations on our grid. They will be rounded to
    integer values to represent pixel locations, and we will fill up to, but
    not including the max value.

    This allows us to, for example, fill one rectangle from 10 to 20, and the
    next from 20 to 30. If we had decided to include the max value, then we'd
    have to fill from 10-19 and 20-29. Also, this latter convention combined
    with floating point values makes it difficult to talk about what happens
    between, say, 19 and 20.

    Using the former convention, we can draw two rectangles that perfectly
    abut.

    The color representation will be floating point numbers normalized to 1.0.
    This means that 0.0 is black, and 1.0 is the brightest red, green or blue
    the monitor can display.
*/
INTERNAL_FUNCTION void
DrawRectangle(AppOffscreenBuffer* buffer,
              r32 r32_min_x, r32 r32_min_y, r32 r32_max_x, r32 r32_max_y
              r32 red, r32 green, r32 blue)
{
    s32 min_x = RoundR32ToS32(r32_min_x);
    s32 max_x = RoundR32ToS32(r32_max_x);
    s32 min_y = RoundR32ToS32(r32_min_y);
    s32 max_y = RoundR32ToS32(r32_max_y);

    // Clipping
    if (min_x < ) {
        min_x = 0
    }

    if (min_y < ) {
        min_y = 0
    }

    if (max_x > buffer->width_) {
        max_x = buffer->width_;
    }

    if (max_y > buffer->width_) {
        max_y = buffer->width_;
    }

    // The color bit pattern is 0x AA RR GG BB
    u32 color = (RoundR32ToU32(red * 255.0f) << 16) |
                (RoundR32ToU32(green * 255.0f) << 8) |
                RoundR32ToU32(blue * 255.0f);

    // Set the pointer to the pixel in the buffer where we want to write the
    // top left corner of the rectangle.
    u08* row = reinterpret_cast<u08*>(buffer->memory_ +
                                      min_x * buffer->bytes_per_pixel_ +
                                      min_y * buffer->pitch_);
    for (int y = min_y; y < max_y; ++y) {
        u32* pixel = reinterpret_cast<u32*>(row);
        for (int x = min_x; x < max_x; ++x) {
            // Remember, there are 4 bytes per color
            if ((row >= buffer->memory_) && ((pixel + 4) <= end_of_buffer)) {
                *pixel++ = color;
            }
        }

        // next row
        row += buffer->pitch_;
    }
}
```

## Tile Maps
The tile map we'll start with is a 9x16 array. We'll draw a rectangle on our "board" if the tile map has a 1, and no rectangle (just the background color), if the map has a zero.

```cpp
u32 tile_map[9][17] =
{
    {1, 1, 1, 1,  1, 1, 1, 1,  0, 1, 1, 1,  1, 1, 1, 1, 1},
    {1, 1, 0, 0,  0, 1, 0, 0,  0, 0, 0, 0,  0, 1, 0, 0, 1},
    {1, 1, 0, 0,  0, 0, 0, 0,  1, 0, 0, 0,  0, 0, 1, 0, 1},
    {1, 0, 0, 0,  0, 0, 0, 0,  1, 0, 0, 0,  0, 0, 0, 0, 1},
    {0, 0, 0, 0,  0, 1, 0, 0,  1, 0, 0, 0,  0, 0, 0, 0, 0},
    {1, 1, 0, 0,  0, 1, 0, 0,  1, 0, 0, 0,  0, 1, 0, 0, 1},
    {1, 0, 0, 0,  0, 1, 0, 0,  1, 0, 0, 0,  1, 0, 0, 0, 1},
    {1, 1, 1, 1,  1, 0, 0, 0,  0, 0, 0, 0,  0, 1, 0, 0, 1},
    {1, 1, 1, 1,  1, 1, 1, 1,  0, 1, 1, 1,  1, 1, 1, 1, 1},
};

r32 upper_left_x = -30;
r32 upper_left_y = 0;
r32 tile_width = 60;
r32 tile_height = 60;

// Clear the screen to the background color
DrawRectangle(buffer, 0.0f, 0.0f,
              static_cast<r32>(buffer->width_),
              static_cast<r32>(buffer->height_),
              1.0f, 0.0f, 0.1f);

// Iterate through the tile map drawing a white rectangle where there is a one,
// and a gray rectangle where there is a zero.
for (int row = 0; row < 9; ++row) {
    for (int column = 0; column < 17; ++column) {
        u32 tile_id = tile_map[row][column];
        r32 gray = 0.5f;

        if (1 == tile_id) {
            gray = 1.0f;
        }

        r32 min_x = upper_left_x + static_cast<r32>(column) * tile_width;
        r32 min_y = upper_left_y + static_cast<r32>(row) * tile_height;
        r32 max_x = min_x + tile_width;
        r32 max_y = min_y + tile_height;
        DrawRectangle(buffer, min_x, min_y, max_x, max_y, gray, gray, gray);
    }
}

## Players
The players sprite will be slightly narrower than a tile map width, but the same height. Note that the sprite won't stop when its top hits the bottom of a wall above it. It normally will partially cover a wall tile above it. There's a similar check for left and right, in that the sprite is allowed to continue halfway into a wall to its left or right. The bottom of the sprite is never allowed to cross the top of a wall below it.

The rectangle's upper left corner is provided to the draw function. For collision detection, we'll calculate a point that is the upper left corner, and subtract the player's height from the y coordinate, and add half the player's width to the x coordinate. That will give us a point in the middle of the bottom of the sprite for collision detection.
