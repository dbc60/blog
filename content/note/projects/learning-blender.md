---
title: Learning Blender
date: 2016-11-23
draft: true
categories: [projects]
tags: [blender]
---

I'd really like to learn how to use this marvelous tool.
<!--more-->

## Blender Workflow
I found an inspiring video, [Successfully Developing Artwork in Blender](https://www.youtube.com/watch?v=TEl8Z-Gemro), where Zacharias Reinhardt talks about his workflow for developing static images and short animations in Blender. His general workflow is:

- Preparation
- Research & Testing
- Creating the Artwork
- Feedback & Fine Tuning

Reinhardt starts with setting some personal goals to keep motivated. Reinhardt tries to learn something new (tools or workflow to try), improve techniques and workflows, and tries to meet deadlines.

Reinhardt's workflow:

- Find a good idea
- Create simple concept art
- Create a previsualization, aka blockout. He blocks out his scene with very simple shapes and colors.
- Replace each object in turn with high resolution objects.
- If something doesn't work, try new things.
- Modeling, shading, lighting
- Rendering & Compositing
- Ask for feedback and fine tune the product.


### 1 Preparation
How to start? Start wtih organizing the project folders, so you have a place to put the artwork. Next, find a good idea. Finally, create the concept art and the previsualization.

#### Organize the Project Folder
Where to put the files? This is for a smaller project, like artwork:

- Main Folder with the project name
    - `/fin`    (final artwork)
    - `/lib`    (things to store)
        - `/ref`    (reference images)
        - `/rend`   (rendered images)
        - `/rec`    (video recordings)
        - `/aud`    (audio recordings)
    - `/prod`   (production: things that will be edited, things with versions)
        - 3d        (blender files)
        - tex       (textures)
        - concept   (concept art)

Only create a folder if you need it. So, if you only have a `blend` file and a few textures, then all you need is the production folder.

#### Finding a Good Idea

1. Get a direction -> what is your motivation for creating your artwork? This can be things like add to your portfolio, enter a competition or work to improve your skills.
1. Specify -> What fits your motivation? For example, if you want to improve your skills, you have to find an artwork that requires the techniques you want to work on. If you want to add to your portfolio, then you have to do something you want to show. It might be somthing that will help you get hired. If you want to be a character artists, then do something with characters. If you want to enter a competition, and perhaps the competition has a particular topic, so you want to work on that topic.
1. Do something you like!

To help you find good ideas, or just something to work on, there is a [weekly CG challenge](https://facebook.com/groups/weeklycgc) on Facebook. There is a new topic each Monday. There are nice prizes.

Reinhardt started with still life photos. He also did a short for his series [Movie Scene Creation in Blender 3D](https://www.youtube.com/watch?v=Wd3bz62dDLA). It's a 20 video set on YouTube. It's not for beginners. Nevertheless, the [second video](https://www.youtube.com/watch?v=R2BsIMmRmog) is short and talks about motivation and workflow.

1. Make your project fun
1. Clear your mind
1. Plan. Start with rough milestones, and add detail as you go.
1. Researching and testing. Find good workflows that will allow a one-person shop to do nice things.
1. Test your workflows. Try it on small objects or small areas. Start with a small plane. When things work, apply it to the big scene. Use tools appropriate to the job. Blender isn't necessarily the best tool for all parts of your work.
1. Get feedback - constructive criticism - when you think you're done. Use that information to rework and tune you project.

The most important thing for a good idea is _the story_!. The title can help. He has an image called "The Monster in the Closet" that tells a story of a little monster eating candy spilled on the floor.

#### Creating the Concept Art
Here we create a simple image to use as a reference for our 3D scene. It help by getting the image out of our heads so we can see and analyze better the thing we want to create in 3D.

- Use references as inspiration -> moodboard
- Crate a sketch, a painting or an overpainting. An overpainting is when you paint over another image, like a photo, with some simple strokes and colors to visualize your basic idea. It's helpful when you want to use some elements in the image, but place them in a different scene, for example.
- This is the visual foundation 3D work relies upon

#### Create the Previsualization
This is where we get started in 3D. A previsualization is also called a previs or blockout. The rules are:

- Use the concept art as the foundation.
- Block out your scene with simple objects.
- Test camera perspective and composition.
- Adjust things until you are happy.

This is something that can be done quickly. The first draft might take half-an-hour (if you know how to use Blender). Reinhardt shows a very simple version of his "Memories of the Past" 3d image, and shows how he played with the camera position, aperature and depth of field. He also showed how to add some nice shadows by adding a sun lamp and played with its position, direction and the size and shape of the shadow box it cast. He also added mist, background color; he moved components around as well.

He also showed a simple animation. He modeled everything in the right size, so when he is ready to replace the simple models with high-res components, he knows exactly what size each thing will be.

### 2 Research & Testing
Find ways to do something fast and efficient! What you actually do, depends a lot on the kind of project you're working on. If you aren't a skilled 3d artist, this is a very imprtant step.

- Find better workflows
- Watch and read tutorials/articles
- Find better tools or addons
- Test in small environments. Reinhardt showed an animated tree that he worked on. It is the _only_ thing in the scene. It has nicely rendered bark, leaves and grass on the ground immediately around it. Each of those components were created separately. He experimented with techniques to find a good way to produce each one. He tried lots of different ways to make each part. Sometimes just a simple patch is all you should start with.

### 3 Creating the Artwork
More fun!

- Use the previualization as the foundation.
- Replace low resolution objects with high resolution versions.
- Create only what is needed.
- Cheat!

Reinhardt showed his animation of moving a camera around a box of vegetables. It looks like part of a larger scene with shadows cast by a tree in the distance. When he panned back, the tree wasn't colored and looked like it was just stuck on the side. It's only purpose was to create shadows, so it wasn't colored or textured in any way.

To create the scene, he modeled one box and made six copies of it. He place them between two planes, one horizontal for the ground and another vertical for a back wall. The planes were textured with some kind of displacement function.

He used 2d images to create height maps and textures for the displayment function.

Time to go. Stopped [the video at 36:20](https://youtu.be/TEl8Z-Gemro?t=2180)

### 4 Feedback & Fine Tuning
