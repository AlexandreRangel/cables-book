# Texturing in Cables.gl

## Introduction to Textures

Textures add detail, color, and realism to your visuals. In cables.gl, textures can come from images, videos, webcams, or be generated procedurally.

## Loading Textures

### ImageTexture

Load images from files or URLs:

```
ImageTexture -> Material (texture input)
```

**Supported Formats:**

- PNG (with transparency)

- JPG

- WebP

- GIF (first frame or animated)

**Key Parameters:**

- `URL` - Path to image

- `Filter` - Nearest (pixelated) or Linear (smooth)

- `Wrap` - Repeat, Clamp, Mirror

### VideoTexture

Use video as a texture:

```
VideoTexture -> Material (texture input)
```

**Key Parameters:**

- `URL` - Path to video file

- `Loop` - Whether to loop playback

- `Playback Rate` - Speed control

- `Volume` - Audio volume

**Supported Formats:**

- MP4 (H.264)

- WebM

### WebcamTexture

Live webcam input as a texture:

```
WebcamTexture -> Material (texture input)
```

**Tip:** Great for interactive installations!

## Texture Mapping

### UV Coordinates

UV coordinates define how textures wrap onto geometry:

```
UV COORDINATE SYSTEM
Texture (Image)
U=0,V=0 U=1,V=0 <- Top edge
U=0,V=1 U=1,V=1 <- Bottom edge
Mapped to 3D Geometry:
U=0,V=0 ------------ U=1,V=0
3D Surface
U=0,V=1 ------------ U=1,V=1
- U = Horizontal (0 to 1, left to right)
- V = Vertical (0 to 1, top to bottom)
```

- **U** = Horizontal position (0 to 1)
- **V** = Vertical position (0 to 1)

Most primitive shapes have automatic UV mapping.

### UV Transform

Modify texture coordinates:

```
UV TRANSFORM OPERATIONS
Original Texture
Texture
Offset U/V: Shift texture position
+---------+
Texture <- Moved right/up
+---------+
Scale U/V: Tile or shrink texture
Tex Tex Tex <- Tiled horizontally
Rotate: Rotate texture around center
/ \
/ Texture \ <- Rotated
\ /
```

```
TextureTransform -> Before texture application
```

**Parameters:**

- `Offset U/V` - Shift the texture

- `Scale U/V` - Tile or shrink

- `Rotate` - Rotate the texture

### Tiling Textures

For seamless repeating:

1. Set wrap mode to `Repeat`
2. Scale UV coordinates > 1

## Advanced Texture Workflow (Production Mindset)

Texturing is where many cables.gl projects move from “cool prototype” to “polished piece”. The two recurring themes are:

- **Correctness**: color space, alpha handling, UVs, aspect ratios, and predictable sampling.
- **Performance**: texture sizes, filtering, mipmaps, compression, and “how many textures are you sampling per pixel”.

### Color Space: sRGB vs Linear (Why Your Colors Look “Off”)

Most images you download (JPG/PNG/WebP) are authored in **sRGB** (gamma corrected). Most lighting and shading math expects **linear** values. If your project mixes lit materials (e.g., PBR) with UI-like textures, you can run into:

- washed-out or too-dark textures
- incorrect blending
- “metal looks wrong” in PBR

**Practical rule of thumb**:

- **Color/albedo** textures are usually **sRGB**.
- **Data** textures (normal maps, roughness/metalness/AO, masks) are usually **linear**.

If a texture looks wrong, verify you’re not treating a data map like a color map (or vice versa).

### Alpha (Transparency) Pitfalls

If you see dark/bright halos around transparent textures (logos, sprites), you’re likely looking at one of these issues:

- The texture was exported with a bad matte color (common in PNGs).
- The pipeline expects **premultiplied alpha** but you provided straight alpha (or the other way around).
- Filtering/mipmaps sample transparent pixels and “bleed” colors into edges.

**Fix strategies**:

- Add padding/bleed around sprites in your source image.
- Prefer power-of-two textures with mipmaps for distant rendering.
- If you have control over asset export, re-export with correct alpha handling.

### Filtering, Mipmaps, and Why Textures “Shimmer”

When a textured surface gets small on screen, the GPU needs mipmaps to avoid shimmer and crawling.

- **Nearest** filtering: crisp pixels, great for pixel-art, terrible for most 3D.
- **Linear** filtering: smoother sampling, better for general use.
- **Mipmaps**: essential for 3D surfaces viewed at varying distances.

If a ground texture “crawls” when the camera moves, you typically need mipmaps and (if available) anisotropic filtering.

### Power-of-Two Sizes (and When It Matters)

Power-of-two textures (256/512/1024/2048/4096) generally behave better for:

- mipmaps
- repeating wrap modes
- GPU compatibility/performance

Non-power-of-two often still works in modern WebGL, but when things behave oddly, returning to power-of-two sizes is a reliable fix.

### Aspect Ratio Correctness (Especially for Video)

Video textures are a frequent source of “why is it stretched?” issues.

- Match the **Plane** aspect ratio to the video’s aspect ratio.
- If you use Fullscreen rectangles, make sure you’re compensating for screen aspect.

## Advanced Techniques and Patch Recipes

These are “building block” patterns you can reuse across many projects.

### Recipe: Masked Texture Blend (Two Textures + a Mask)

Use a mask texture (black/white) to blend between two images.

**Conceptual chain:**

```
ImageTexture (A) -+
                  +-> (blend using mask) -> Material -> Mesh
ImageTexture (B) -+
ImageTexture (Mask)
```

**Notes:**

- The mask should be treated as a data texture (linear).

- Great for dirt overlays, decals, and transitions.

### Recipe: Animated UVs (Scrolling / Parallax)

Scrolling textures are perfect for conveyor belts, moving backgrounds, water normals, etc.

```
Time -> (speed multiply) -> TextureTransform (Offset U/V)
ImageTexture -> Material (texture input)
Material -> Mesh
```

### Recipe: Render-to-Texture for Post-Processing

Render your scene to a texture, apply effects, then output.

```
MainLoop -> Camera -> RenderToTexture
           [Scene]
TextureEffects -> Output
```

**Use Cases:**

- blur/glow chains

- color grading

- stylized distortion

- feedback trails (see next recipe)

### Recipe: Feedback / Trails (Texture Feedback Loop)

Feedback is a signature look in real-time visuals.

High-level structure:

```
Previous Frame Texture
TextureEffects (fade/blur)
Combine with New Frame Content
RenderToTexture (becomes “previous frame” next tick)
```

**Tip:** Keep feedback subtle (small fade each frame). Large blur + high persistence can become very expensive.

### Recipe: Planar “Mirror” Reflection (Render-to-Texture)

To fake a mirror floor:

- Render the scene from a reflected camera to a texture.
- Apply that texture onto a plane.

```
MainLoop
  +-> Camera (main) -> [Scene]
  +-> Camera (reflected) -> RenderToTexture -> Plane Material -> Mirror Plane
```

### Recipe: Environment Reflections (Cubemap/HDRI)

Use an environment texture for reflections and more believable PBR materials.

```
HDRITexture or CubemapTexture -> (environment input) -> PBRMaterial -> Mesh
```

**Tip:** Even simple objects look dramatically better with good environment lighting.

### Recipe: Video Texture “Billboard” (Reliable Playback)

```
VideoTexture -> BasicMaterial -> Plane
```

**Checklist:**

- Use a browser-served URL (avoid `file://` in production).

- Make sure autoplay policies are satisfied (user interaction may be required).

- Use a fallback poster image if video takes time to load.

### Recipe: Webcam Texture (Permissions + UX)

```
WebcamTexture -> BasicMaterial -> Plane
```

**Checklist:**

- Provide a UI prompt (“Click to enable camera”).

- Handle denied permissions gracefully (fallback texture).

- Keep resolution reasonable for performance.

## Texture Types for PBR Materials

### Albedo/Diffuse Map

The base color of the surface.

### Normal Map

Adds surface detail without extra geometry.

```
NormalMap -> PBRMaterial (normal input)
```

**Tip:** Use tangent-space normal maps (blue-purple appearance).

### Roughness Map

Controls surface smoothness per-pixel.

- White = rough
- Black = smooth/shiny

### Metalness Map

Defines metallic vs. non-metallic regions.

- White = metal
- Black = non-metal (dielectric)

### Ambient Occlusion Map

Pre-baked shadow information for crevices.

### Height/Displacement Map

Actual geometry displacement (more expensive).

### Emissive Map

Self-illuminating regions of the surface.

## Procedural Textures

Generate textures with code/nodes:

### Noise Textures

```
NoiseTexture -> Creates Perlin/Simplex noise
```

**Types:**

- Perlin noise

- Simplex noise

- Voronoi

- Fractal/FBM

### Gradient Textures

```
GradientTexture -> Creates color gradients
```

### Pattern Generators

- Checkerboard
- Stripes
- Dots
- Custom math-based patterns

## Render to Texture

Capture your scene as a texture for post-processing or effects:

```
MainLoop -> Camera -> RenderToTexture
           [Scene to capture]
           TextureOutput -> Use elsewhere
```

### Common Uses:

1. **Post-processing effects** - Apply shaders to the entire scene
2. **Mirrors/Reflections** - Render from reflection viewpoint
3. **Dynamic textures** - Use one patch's output in another
4. **Feedback effects** - Feed output back as input

## Texture Effects

### TextureEffects Op

Chain of image processing effects:

```
ImageTexture -> TextureEffects -> Output
```

**Available Effects:**

- Blur

- Sharpen

- Color correction

- Distortion

- Edge detection

- Pixelation

### Custom Shader Effects

Write GLSL for custom texture processing (see Shaders chapter).

## Cubemaps and Environment Maps

### CubemapTexture

Six images forming a surrounding environment:

```
CubemapTexture -> Environment lighting
```

**Uses:**

- Skyboxes

- Reflections

- Image-based lighting (IBL)

### HDRITexture

High Dynamic Range images for realistic lighting:

```
HDRITexture -> IBL/Environment
```

## Texture Compression and Optimization

### File Size Tips:

1. **Use appropriate formats:**

- PNG for transparency

- JPG for photos (no transparency)

- WebP for best compression
2. **Power of 2 sizes:** 256, 512, 1024, 2048, 4096 pixels
3. **Mipmaps:** Enable for textures viewed at varying distances
4. **Compress textures:** Use tools like TinyPNG, Squoosh

### Memory Considerations:

- 512x512: ~1 MB

- 1024x1024: ~4 MB

- 2048x2048: ~16 MB

- 4096x4096: ~64 MB

## Practical Examples

### Example 1: Textured Rotating Cube

```
MainLoop
PerspectiveCamera
DirectionalLight
Time -> RotateY
ImageTexture -> PhongMaterial (texture input)
Cube
```

### Example 2: Video on a Plane

```
MainLoop
VideoTexture -> BasicMaterial
Plane (aspect ratio matching video)
```

### Example 3: Animated Noise Background

```
MainLoop
Time -> NoiseTexture (animate offset)
BasicMaterial
FullscreenRectangle
```

### Example 4: PBR Textured Material

```
ImageTexture (albedo)
ImageTexture (normal)
ImageTexture (roughness)
ImageTexture (metalness)
    (all connected to PBRMaterial)
PBRMaterial
Mesh
```

## Featured Videos

<!-- Add texturing videos here -->

<!-- Example:
```vid
https://youtu.be/XXXXX
Title: Texturing in Cables.gl
Author: Channel Name
Thumbnail: https://i.ytimg.com/vi/XXXXX/mqdefault.jpg
```
-->

## Exercises

1. Create a textured cube that rotates and displays different images on each face
2. Build a video wall with multiple video textures
3. Create a procedural noise-based animated background
4. Apply PBR textures to a loaded 3D model


