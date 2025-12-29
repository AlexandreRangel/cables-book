# Introduction to Cables.gl

## What is Cables.gl?

![[01-introduction-1766980878670.jpeg]]

**Cables.gl** is a powerful, browser-based visual programming environment for creating interactive 2D and 3D graphics using WebGL. It was created by undev in Berlin and has become a popular tool for creative coding, interactive installations, data visualization, and web-based visual experiences.

Unlike traditional coding environments, cables.gl uses a **node-based** (or "patch-based") approach where you connect visual operators (ops) together to create your projects. This makes it accessible to artists and designers while still being powerful enough for developers.

## A (Brief) History of cables.gl

cables.gl was created by **undev** (Berlin) with the goal of making **real-time WebGL** creation approachable through a node-based workflow—similar in spirit to visual programming environments used in motion design and interactive installations, but built for the browser.

Over time, cables.gl grew from a tool for quick experiments into a full ecosystem:

- **Early days**: a strong focus on rapid prototyping and sharing patches online.
- **Maturing platform**: a steadily growing op library for 2D, 3D, textures, audio, and interaction, plus better tooling (timeline, profiling/debugging utilities, export options).
- **Community-driven growth**: more public patches, tutorials, Discord knowledge-sharing, and reusable patterns (e.g., render-to-texture workflows, post-processing chains, audio-reactive setups).
- **Production use**: cables.gl exports make it viable for deployment in websites, installations, and client work—where performance, asset management, and reliable runtime behavior matter.

If you’re coming from traditional code, it helps to think of cables.gl as a **visual runtime graph**: triggers define *when* things run; value connections define *what data* flows; and the patch as a whole becomes a web-ready app.

## Why Use Cables.gl?

### Visual Programming
- No coding required to get started
- Drag-and-drop interface
- See results in real-time as you build

### Browser-Based
- No installation needed
- Works on any modern browser
- Collaborate and share easily

### High Performance
- Built on WebGL for GPU-accelerated graphics
- Optimized for real-time rendering
- Handles complex 3D scenes smoothly

### Export Options
- Standalone HTML/JS builds
- Embed in websites
- Create offline applications

### Extensible
- Write custom operators (ops) in JavaScript
- GLSL shader support
- Import external libraries

## Key Concepts

### Operators (Ops)
The building blocks of cables.gl. Each op performs a specific function - from drawing shapes to processing audio to handling user input.

### Patches
A patch is your complete project - a collection of ops connected together to create your visual experience.

### Ports
Ops have input and output ports. You connect ports together with "cables" (hence the name!) to pass data between ops.

### Types of Ports
- **Trigger** (grey) - Execution flow, like "when to do something"
- **Number** (green) - Numerical values
- **String** (yellow) - Text values
- **Object** (blue) - Complex data like meshes, textures, arrays
- **Array** (cyan) - Collections of data

## Featured Videos

### Overview and Getting Started

```vid
https://youtu.be/hVxrxXhH7vQ
Title: Cables.gl Standalone (Offline) Build: Create Without Limits!
Author: Decode GL
Thumbnail: https://i.ytimg.com/vi/hVxrxXhH7vQ/mqdefault.jpg
AuthorUrl: https://www.youtube.com/@Decode_gl
```

```vid
https://youtu.be/goO3PhuenBI
Title: First Steps in Cables.gl - Tutorial
Author: The Interactive & Immersive HQ
Thumbnail: https://i.ytimg.com/vi/goO3PhuenBI/mqdefault.jpg
AuthorUrl: https://www.youtube.com/@TheInteractiveImmersiveHQ
```

```vid
https://youtu.be/xnObNRv8n9I
Title: Introduction to cables.gl - Data-Driven Gradient from Geo-Located Weather - Part 0
Author: Kirell Benzi
Thumbnail: https://i.ytimg.com/vi/xnObNRv8n9I/mqdefault.jpg
AuthorUrl: https://www.youtube.com/@kirellbenzi
```

### More Resources

**Note:** There are limited intro-specific YouTube videos for cables.gl, but the platform has excellent resources:
- Browse the [cables.gl Public Patches](https://cables.gl/ops) to see examples
- Check the official [cables.gl YouTube channel](https://www.youtube.com/@cablesgl) for official tutorials
- The [Decode GL channel](https://www.youtube.com/@Decode_gl) has multiple cables.gl tutorials
- Search for "cables.gl" on YouTube for the latest community content
- Many cables.gl creators share their work on social media and personal channels

## Getting Help

- **Official Documentation**: [cables.gl/docs](https://cables.gl/docs)
- **Example Patches**: Browse public patches for inspiration

---

