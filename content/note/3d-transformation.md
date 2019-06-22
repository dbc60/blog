---
title: 3D Transforms
date: 2016-03-07
draft: true
math: true
categories: math
tags: [3d, graphics]
---

Notes on world, view and projection matrices.

3D vertices can be represented as a \\((x, y, z)\\) triplet, but it's far more useful to use a \\((x, y, z, w)\\) vector. According to [Tutorial 3: Matrices](http://www.opengl-tutorial.org/beginners-tutorials/tutorial-3-matrices/), \\(w\)) takes on one of two values that determines how the vector should be interpreted:
<!--more-->

- if `w == 1`, then the vector `(x, y, z, w)` is a position in space.
- if `w == 0`, then the vector `(x, y, z, w)` is a direction.

It doesn't make any difference for rotation. Whether you rotate a point or a direction, you get the same result. For a translation, we can move a point in a certain direction, but there's no such concept for a direction.

Homogeneous coordinates enable us to use a single mathematical formula to deal with these two cases.

## Matrices
In 3D graphics we mostly use \\(4\times 4\\) matrices to enable us to transform our `(x, y, z, w)` vertices. This is done by multiplying a transformation matrix by the vertex (**in the order presented below**).

\\[
  \begin{bmatrix}
    a & b & c & d \\\\\
    e & f & g & h \\\\\
    i & j & k & l \\\\\
    m & n & o & p
  \end{bmatrix}
  \times
  \begin{bmatrix}
    x \\\\\ y \\\\\ z \\\\\ w
  \end{bmatrix} =
  \begin{bmatrix}
    ax + by + cz +dw \\\\\
    ex + fy + gz + hw \\\\\
    ix + jy + kz +lw \\\\\
    mx + ny + oz + pw
  \end{bmatrix}
\\]


## Transformation Matrices
Notes from [World, View and Projection Matrix Unveiled](http://web.archive.org/web/20131222170415/http:/robertokoci.com/world-view-projection-matrix-unveiled/).

The **transformation matrix** is a 4x4 homogeneous matrix. The sub-matrix consisting of the first 3 rows and columns defines scaling and rotation for the transformation. The first 3 columns of the last row define the translation along the X, Y and Z axes, the first 3 rows of the last column are set to zero. I'm not sure what the element in the fourth row of the fourth column represents, but I'm sure it's important.

The **identity matrix** is a matrix that when you multiply a vertex by it, nothing changes. It is filled with zeros except along the diagonal from M(0,0) through M(3,3). Those locations hold the value 1.0. Did I mention that all of these values are floating point numbers?

### The Identity Matrix
The identity matrix is a good place to start when you need a transformation matrix. First create one, and then scale, rotate and move it. Here is an identity matrix:

\\[ \text{Matrix4x4}\ I = \begin{bmatrix} 1 & 0 & 0 & 0 \\\\\ 0 & 1 & 0 & 0 \\\\\ 0 & 0 & 1 & 0 \\\\\ 0 & 0 & 0 & 1 \end{bmatrix}\\]

### The World Matrix
When you create an object in your favorite 3D art creation program, the object is in object space. To move (translate), rotate or scale the object you don't change any of its vertices. Instead, you put those values into the object's *world tranformation matrix*, also known as its *world matrix* or simply *transformation matrix*.

Every transformation you do while creating the object, or later in your 3D engine, is in the world transformation matrix. The object never moves.

Note that in the [referenced article](http://web.archive.org/web/20131222170415/http:/robertokoci.com/world-view-projection-matrix-unveiled/), 3D coordinates are left handed and the object and world spaces are viewed down the Y axis with the X axis extending to the right and the Z axis extending up the page.

```
        ^ Z
        |
        |
        |        X
--------+-------->
        |
        |
        |
```

### The View Matrix
The **view matrix**, also known as the **camera matrix** is used to transform the object from the world space to a space where the X direction points to the right, the Y axis points up the page/display and the Z axis is the direction the camera is looking (into the page/display).

### The Projection Matrix
The **projection matrix** is based on near and far view distances,the angle of the view of the camera and your screen resolution in both the X and Y directions. This matrix creates perspective. It transforms view space into projection space.

### Summary
To display an object in 3D, we have three matrices: *world*, *view* and *projection*. We can multiply all these matrices once to create a combined *world-view-projection* matrix. We now can operate on hte vertices of the objects with this combined matrix to place objects on the screen.

The matrix is produced by:

```c
matrix4x4 worldViewProjectionMatrix = world x view x projection
```

where `x` stands for matrix multiplication. It is important that this order of multiplying these matrices is kept, otherwise you will get surprising results.

Note that the presented matrix model corresponds to a DirectX scenario, and a so called *left to right* multiplication order. In OpenGL, it's reversed, so the combined matrix must be:

```c
matrix4x4 projectionViewWorldMatrix = projection x view x world
```

## Other Terms

- distance fields: for every point in space, how far am i from the surface and am I inside or outside the polygon/solid.
- shader toil?
- lists of edits
- primitives
- platonic pieces
  - cubic strokes
  - cylinders
  - cones
  - cuboid
  - ellipsoids
  - triangular prisms
  - toroids / donuts
  - biscuits
  - markoids - super ellipsoids with variable power for x, y and z
  - pyramids
- CSG
- deformation
  - deform low polygon meshes
  - move the edits around and recalculate the entire mesh. However, this process doesn't scale well when an object has 1000 or 8000 edits and the mesh must be recalculated for each frame of animation.
- Pipeline
  - Edit list
  - Compute Shaders of Doom generated from a Voxel space of 1000 x 1000 x 1000 voxels
  - Sparse distance field
  - Find a way to draw that on the screen
    - Mesh?
    - Filter SVO?
    - Scatter Point Cloud?
- Use a hierarchical space and only refine it near the surfaces. This avoids having 100,000 edits in a 1000^3 voxel space (which means calculating the position of 100 billion things).
- No z-brush pushing and pulling
- Better is CSG add and subtract, and a soft version of add and subtract. It made the hierarchical space practical, where z-brush would have been much much more difficult.
- It's important to figure out where to "split".
- L2 distance norm: Pythagorean Theorem. Distances to a square or a sphere is easy, but distances to an ellipsoid is very difficult.
- Paper: "Efficient Max-Norm Distance Computation and Reliable Voxelization". So use the max-norm, which means you measure how far you have to go in each axis and select the largest one. It gives you "flat bits", but makes everything easier.
- Calculate the number of edits that go into each point on the surface of your CSG object. The fewer the number of edits the faster it is to display them.
- Rendering. See the paper "Cultural Learnings For Make Benefit Glorious Polygonalization of Signed Distance Fields," by Anton Kirczenow.
- The mesh can be very dense. Look into Joule (Dual?) Contouring.
- Paper: "Intersection-free Contouring on An Octree Grid." Only problem is your mesh is no longer a "water tight" manifold.
- Paper: "Manifold Dual Contouring" to the rescue. It's very complicated, brings back the manifold, but also brings back the intersections we were trying to get rid of.
- Polygons are the best way of representing a flat surface, a way of defining a 2D manifold in 3D space.
- Alex Evans discovered the artists were gravitating toward assets with a crinkly, wrinkly look. There were no hard, flat surfaces.
- Inspiration Paper: "Volumetric Billboards," by Philippe Decaudin, Fabrice Neyre. The idea is that everything is represented as voxels, but they're fuzzy voxels - like clouds of gas. They render sheets of polygons aligned with the screen cut through your texture. They don't answer lighting nor a bunch of other questions, but they do have some cool contributions around level of detail. They also support multiple overlapping objects, which is effectively order-independent transparency.
- Sparse Gigavoxels. Downside for a game is that there is only one mesh for the whole world.
- Engine 2: The brick engine. See the slides.
- Parallax occlusion mapping. Lost the fog from the fuzzy voxels.

## References

- [World, View and Projection Matrix Unveiled](http://web.archive.org/web/20131222170415/http:/robertokoci.com/world-view-projection-matrix-unveiled/)
- [Tutorial 3: Matrices](http://www.opengl-tutorial.org/beginners-tutorials/tutorial-3-matrices/) from the [OpenGL Tutorial](http://www.opengl-tutorial.org/).
- [Umbra Ignite 2015: Alex Evans / Media Molecule](https://www.youtube.com/watch?v=-3Yu0TCqa3E)
