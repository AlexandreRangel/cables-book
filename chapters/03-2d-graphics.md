# 2D Graphics in Cables.gl

## Introduction to 2D Drawing

Cables.gl excels at creating stunning 2D graphics and animations, from simple shapes to complex generative art. This comprehensive chapter covers fundamental 2D drawing operations, advanced transformations, interactive elements, feedback loops, post-processing effects, and professional techniques for creating production-ready 2D visuals.

Whether you're creating data visualizations, interactive installations, or generative art, this chapter will give you the tools and knowledge to master 2D graphics in cables.gl.

## Basic Shapes

### Circle

The `Circle` op is one of the most common 2D primitives.

**Key Parameters:**

- `Radius` - Size of the circle
- `Segments` - Smoothness (more segments = smoother circle)
- `Inner Radius` - Creates a ring when > 0

### Rectangle

The `Rectangle` op draws rectangular shapes.

**Key Parameters:**

- `Width` - Horizontal size
- `Height` - Vertical size
- `Pivot` - Origin point for positioning

### RoundedRectangle

A rectangle with smooth corners.

**Key Parameters:**

- `Width` / `Height` - Dimensions
- `Corner Radius` - How rounded the corners are

### Polygon

Create regular polygons (triangles, pentagons, etc.)

**Key Parameters:**

- `Sides` - Number of sides (3 = triangle, 5 = pentagon, etc.)
- `Radius` - Size of the polygon

### Line / Lines

Draw single or multiple lines.

**Key Parameters:**

- Start and End coordinates
- Line width
- Line style (solid, dashed)

## Color and Appearance

### SetColor

Changes the drawing color for subsequent shapes.

```
MainLoop -> BasicMaterial -> Circle
```

Connect `SetColor` output to `BasicMaterial`'s color input ports (r, g, b, a) to set the color.

**Color Modes:**
- RGB (Red, Green, Blue)
- HSB (Hue, Saturation, Brightness)
- Hex values

### SetAlpha

Controls transparency.

```
MainLoop -> BasicMaterial -> Shape
```

Connect `SetAlpha` output to `BasicMaterial`'s alpha (a) input port to control transparency.

Values range from 0 (invisible) to 1 (fully opaque).

### Gradients

Use texture-based gradients or shader-generated gradients for smooth color transitions.

## Transformations

### Transform

The `Transform` op modifies position, rotation, and scale of all following shapes.

```
TRANSFORM PIPELINE
MainLoop
BasicMaterial
Transform
+-> Position (X, Y, Z)
+-> Rotation (X, Y, Z)
+-> Scale
Shape (Circle, Rectangle, etc.)
```

**Parameters:**
- `TranslateX`, `TranslateY`, `TranslateZ` - Position
- `RotateX`, `RotateY`, `RotateZ` - Rotation (degrees)
- `Scale` - Uniform scaling

### Transformation Order Matters!

Transformations are applied in order. These produce different results:

**Rotate then Translate:**
```
ROTATE THEN TRANSLATE
Original Position
o
Step 1: Rotate 45 degrees
o
(rotate)
Step 2: Translate Right
-> o
Result: Object rotates around origin, then moves
```

```
Transform (rotate) -> Transform (translate) -> Shape
```

**Translate then Rotate:**
```
TRANSLATE THEN ROTATE
Original Position
o
Step 1: Translate Right
-> o
Step 2: Rotate 45 degrees (around new position)
(rotate) o
Result: Object moves first, then rotates around new origin
```

```
Transform (translate) -> Transform (rotate) -> Shape
```

### Nested Transforms

Create hierarchies by chaining transforms:

```
Transform (parent)
Transform (child)
Shape
```

The child inherits and adds to the parent's transformations.

## Blending Modes

### SetBlending

Controls how colors combine when shapes overlap.

**Common Modes:**
- `Normal` - Standard opacity blending
- `Add` - Colors add together (great for glow effects)
- `Multiply` - Colors multiply (darkening effect)

### Depth Testing

For 2D, you often want to disable depth testing:

```
MainLoop -> BasicMaterial -> DepthTest (disabled) -> Your 2D Content
```

This ensures draw order matches your connection order.

## Patterns and Repetition

### IteratorLoop

Create patterns by repeating shapes:

```
MainLoop -> IteratorLoop -> [Your Shape Setup]
```

Use the iterator index to offset position, color, or other properties.

### ArrayIterator

Iterate over data arrays to position multiple shapes.

## Text Rendering

### DrawText

Display text in your patches.

**Key Parameters:**

- `Text` - The string to display
- `Font` - Font family
- `Size` - Text size
- `Alignment` - Left, center, right

### TextTexture

Create textures from text for more advanced effects.

## Advanced Transformation Techniques

### Matrix Transformations

For precise control, work directly with transformation matrices:

```
MatrixMultiply -> Combine multiple transformations
MatrixInvert -> Reverse a transformation
```

### Pivot Points

Control the center of rotation and scaling:

```
Transform (set pivot) -> Transform (rotate) -> Shape
```

**Common Pivot Values:**
- `0, 0` - Bottom left corner
- `0.5, 0.5` - Center (default)
- `1, 1` - Top right corner

### Compound Transformations

Build complex motion by layering transforms:

**Example: Orbital Motion**
```
Transform (parent orbit)
Transform (child rotation)
Transform (child offset)
Shape
```

This creates a shape that orbits while rotating on its own axis.

## Interactive 2D Elements

### InteractiveRectangle

Create draggable, clickable UI elements:

```
InteractiveRectangle
    (outputs X, Y, Width, Height on interaction)
Control other ops with mouse input
```

**Use Cases:**

- On-screen sliders
- Draggable controllers
- Interactive buttons
- Touch-enabled interfaces

### Mouse Input

Capture and use mouse position:

```
Mouse -> Map (screen to world coords) -> Visual property
```

**Mouse Ops:**
- `MouseX` / `MouseY` - Cursor position
- `MouseButton` - Click detection
- `MouseWheel` - Scroll input

### Example: Interactive Color Picker

```
MainLoop
MouseX -> Map (0 to 1) -> Hue
MouseY -> Map (0 to 1) -> Brightness
HSBtoRGB -> BasicMaterial (color input)
FullscreenRectangle
```

## Generative Art Techniques

### Feedback Loops

Create evolving, self-referential visuals by feeding output back as input:

**Basic Feedback Setup:**
```
MainLoop
RenderToTexture (previous frame)
ImageCompose (blend with new content)
Transform (slight scale/rotate)
TextureEffects (blur, fade)
Draw new shapes
Output (becomes next frame's input)
```

**Parameters to Experiment With:**
- Feedback decay (fade amount)
- Transformation amount (scale, rotation)
- Blend mode (add, multiply, screen)
- Blur intensity

**Result:** Trails, echoes, and organic growth patterns

### Op Art and Moiré Patterns

Create optical illusions with overlapping patterns:

```
IteratorLoop (creates grid)
Time -> Sin -> Rotation angle
IteratorLoop (nested for lines)
Rectangle (thin line)
```

Vary parameters like:
- Line spacing
- Rotation speed
- Line thickness
- Pattern density

### Procedural Pattern Generation

Use noise and math to create endless variations:

**Perlin Noise-Based Patterns:**
```
IteratorLoop
Position -> NoiseTexture sample
Noise value -> Circle size
Noise value -> Color
```

**Grid Distortion:**
```
IteratorLoop (grid)
Position + (Noise * distortion amount)
Shape
```

## Post-Processing Effects

### Image Composition

Layer multiple render passes for rich effects:

```
RenderToTexture (Pass 1: Shapes)
RenderToTexture (Pass 2: Glow)
RenderToTexture (Pass 3: Noise)
ImageCompose (blend all layers)
Final Output
```

### TextureEffects for 2D

Apply effects to your rendered 2D scene:

**Blur:**
```
RenderToTexture -> TextureEffects (Blur) -> Output
```

**Color Grading:**
```
RenderToTexture -> ColorCorrection
    (adjust hue, saturation, brightness, contrast)
Output
```

**Glow Effect:**
```
Original scene
RenderToTexture (bright pass)
Blur (large radius)
ImageCompose (add to original)
```

### Displacement Mapping

Distort shapes using textures:

```
NoiseTexture -> DisplacementMap -> Shape rendering
```

Creates wavy, distorted effects on 2D graphics.

## Advanced Pattern Techniques

### Recursive Subdivision

Create fractal-like patterns:

```javascript
// Custom op: Recursive shape division
for (depth = 0; depth < maxDepth; depth++) {
    // Draw shape
    // Divide into smaller shapes
    // Recursively apply
}
```

### Particle Systems in 2D

Simple particle engine structure:

```
ArrayLoop (particle count)
Particle data (position, velocity, life)
Physics update (gravity, friction)
Transform -> Circle (particle visual)
```

### Grid-Based Automata

Cellular automata and Game of Life patterns:

```
ArrayIterator (grid cells)
Cell state + neighbor count
Update rules (Conway's rules, etc.)
Visual representation
```

## Data Visualization

### Chart Generation

Create custom charts and graphs:

**Bar Chart:**
```
ArrayIterator (data values)
Index -> X position
Value -> Rectangle height
Rectangle (bar)
```

**Line Chart:**
```
ArrayIterator (data points)
Connect points with Lines op
Add circles for data points
```

### Integration with ECharts

Apache ECharts is a powerful open-source charting library that integrates seamlessly with cables.gl. This combination lets you create professional-grade data visualizations with interactive 3D effects and real-time updates.

**Why ECharts + cables.gl?**

- **Rich Chart Types**: Bar, line, pie, scatter, radar, candlestick, heatmap, treemap, sunburst, and more
- **Interactive Features**: Tooltips, zooming, panning, data selection
- **Real-Time Updates**: Stream live data into animated charts
- **3D Enhancement**: Apply cables.gl effects to chart outputs

**Setup and Integration:**

1. **Load the ECharts Extension** in cables.gl using the `Ops.Extension.ECharts.ECharts` op
2. **Configure Chart Options** using JSON format (same as standard ECharts)
3. **Connect Data Sources** from other cables.gl ops (JSON fetch, WebSocket, etc.)
4. **Apply Visual Effects** using cables.gl post-processing

**Basic ECharts Patch Structure:**

```
MainLoop
ECharts Op
    +-> Option (JSON configuration)
    +-> Width / Height
    +-> Data inputs
ECharts Instance -> Use in other ops
```

**Example: Simple Bar Chart Configuration:**

```json
{
  "xAxis": {
    "type": "category",
    "data": ["Mon", "Tue", "Wed", "Thu", "Fri"]
  },
  "yAxis": {
    "type": "value"
  },
  "series": [{
    "data": [120, 200, 150, 80, 70],
    "type": "bar",
    "color": "#5470c6"
  }]
}
```

**Example: Real-Time Line Chart:**

```
WebSocket (data stream)
ParseJSON -> Extract values
Array (rolling buffer of last N values)
ECharts Op (line chart config)
Render to texture
Apply glow effect
```

**Example: Interactive Pie Chart with Events:**

```
ECharts Op (pie chart)
EChartsEvent Op
    +-> Click event -> Trigger actions
    +-> Hover event -> Show details
Update other visuals based on selection
```

**Combining Charts with 3D:**

```
ECharts Op -> Render to texture
Plane3D (apply texture)
Transform (rotate in 3D space)
Post-processing (glow, bloom)
```

**Advanced Techniques:**

- **Multi-Chart Dashboards**: Use multiple ECharts ops with different configurations
- **Animated Transitions**: ECharts handles smooth data transitions automatically
- **Custom Themes**: Define color palettes that match your cables.gl aesthetic
- **Responsive Charts**: Connect viewport size to chart dimensions

**Performance Tips:**

- Limit data points for smooth animation (< 1000 for real-time)
- Use `notMerge: true` for complete data replacement
- Disable animations for very high-frequency updates
- Cache chart instances when possible

**Resources:**

- [Apache ECharts Documentation](https://echarts.apache.org/en/index.html)
- [ECharts Examples Gallery](https://echarts.apache.org/examples/en/index.html)
- [cables.gl ECharts Integration Tutorial](https://quadexcel.com/wp/fast-and-easy-data-visualization-with-cables-gl-and-apache-echarts/)

### Real-Time Data

Visualize live data streams:

```
WebSocket/API -> Parse data
ArrayIterator -> Visualize each value
Smooth/Interpolate for fluid animation
```

## Complex Example Projects

### Example 4: Kaleidoscope Effect

```
MainLoop
BasicMaterial
IteratorLoop (6 segments)
Transform (rotate by index * 60°)
Transform (mirror flip alternating)
Your content (shapes, webcam, etc.)
```

### Example 5: Audio-Reactive Loading Animation

```
AudioAnalyzer (beat detection)
IteratorLoop (circle of dots)
Index + Time -> Rotation
Beat amplitude -> Scale pulse
SetColor (beat changes color)
Circle (dot)
```

### Example 6: Data-Driven Weather Visualization

```
API -> Fetch weather data
Parse JSON -> Extract values
Temperature -> Background color
Humidity -> Particle density
Wind -> Animation speed
Animated scene reflecting weather
```

### Example 7: Feedback Tunnel Effect

```
RenderToTexture (previous frame)
Transform (scale 1.05, center pivot)
SetAlpha (0.98 for fade)
Draw to screen
Add new circles at edges
Feed back into texture
```

Creates an infinite tunnel effect.

### Example 8: Mouse Trail with Fade

```
MousePosition
RenderToTexture (with feedback)
ColorCorrection (reduce brightness)
Draw circle at mouse position
Blend with previous frame
```

Creates smooth, fading trails following the cursor.

## Performance Optimization

### Culling and Clipping

Only draw what's visible:

```
If (shape position in viewport bounds)
    -> Draw shape
Else
    -> Skip
```

### Object Pooling

Reuse shape instances instead of creating new ones:

```javascript
// Maintain pool of inactive shapes
// Activate/deactivate as needed
// Prevents GC thrashing
```

### Level of Detail (LOD)

Simplify distant or small shapes:

```
If (shape size < threshold)
    -> Use simple circle
Else
    -> Use detailed polygon
```

### Batching Draw Calls

Group similar operations:

```
SetColor once
Draw all shapes of same color
SetColor again
Draw next batch
```

Reduces state changes and improves performance.

## Masking and Clipping

### Stencil Buffer Masking

Use shapes as masks for other shapes:

```
EnableStencil
Draw mask shape (Circle)
SetStencilMode (draw only inside)
Draw content (Rectangle)
DisableStencil
```

### Alpha Mask Technique

Use texture alpha for complex masks:

```
MaskTexture -> AlphaMask
Your content (masked by texture)
```

## Color Theory in Practice

### Color Harmonies

Generate pleasing color palettes:

**Complementary:**
```
BaseHue -> SetColor (shape 1)
BaseHue + 180° -> SetColor (shape 2)
```

**Triadic:**
```
BaseHue -> Color 1
BaseHue + 120° -> Color 2
BaseHue + 240° -> Color 3
```

**Analogous:**
```
BaseHue -> Color 1
BaseHue + 30° -> Color 2
BaseHue - 30° -> Color 3
```

### Gradient Creation

Smooth color transitions:

**Linear Gradient:**
```
IteratorLoop (steps)
Index / TotalSteps -> Mix (Color1, Color2, t)
SetColor -> Rectangle strip
```

**Radial Gradient:**
```
Distance from center -> Mix (Inner, Outer, t)
```

## Typography and Text Effects

### Dynamic Text

Animate text properties:

```
Time -> Character spacing
MouseX -> Font size
AudioLevel -> Text opacity
```

### Text as Texture

Use text rendering for effects:

```
TextTexture (render text to texture)
Apply shader effects
Use as sprite or background
```

### Kinetic Typography

Animate individual letters:

```
TextArray (split into chars)
ArrayIterator
Transform (unique per character)
DrawText (single char)
```

## Practical Examples

### Example 1: Pulsing Circle

```
MainLoop
BasicMaterial (set your color)
Time -> Sin -> Scale input
Circle
```

### Example 2: Rotating Grid

```
MainLoop
BasicMaterial
IteratorLoop (10x10)
Transform (position from iterator)
Transform (rotation from Time)
Rectangle
```

### Example 3: Color Gradient Circle

```
MainLoop
IteratorLoop (for each ring)
IteratorIndex -> Map to Hue -> HSBtoRGB -> BasicMaterial (color input)
BasicMaterial
Circle (radius from iterator index)
```

## Debugging and Workflow Tips

### Visualizing Values

See what your ops are outputting:

```
Value -> NumberDisplay
Value -> DrawNumber (on screen)
```

### Color Coding

Use consistent colors to identify different element types:
- Structural elements: Blue
- Interactive elements: Green  
- Data elements: Yellow
- Background: Dark grey

### Naming Convention

Name ops descriptively:
- `TransformRotation_MainShape`
- `Color_Background`
- `Iterator_ParticleGrid`

### Comment Ops

Document complex sections:

```
Comment ("This section creates the feedback loop")
Your complex patch area
```

## Common Patterns and Recipes

### Pattern: Circular Array

Arrange shapes in a circle:

```
IteratorLoop (count)
Index * (360 / count) -> Angle
Angle -> Cos -> X position
Angle -> Sin -> Y position
Transform -> Shape
```

### Pattern: Wave Grid

Create wave motion across a grid:

```
IteratorLoop (rows)
IteratorLoop (columns)
(X + Time) -> Sin -> Y offset
Transform -> Shape
```

### Pattern: Spiral

Generate spiral patterns:

```
IteratorLoop
Index -> Angle (index * goldenAngle)
Index -> Radius (sqrt(index) * spacing)
Polar to Cartesian
Transform -> Shape
```

### Pattern: Responsive Grid

Grid that adapts to screen size:

```
ViewportWidth / CellSize -> Columns
ViewportHeight / CellSize -> Rows
IteratorLoop (columns * rows)
Grid positioning logic
```

## Troubleshooting Common Issues

### "Shapes not appearing"
- Check trigger connections (grey ports)
- Verify MainLoop is connected to BasicMaterial
- Check BasicMaterial alpha isn't 0
- Verify camera/viewport settings

### "Performance is slow"
- Reduce segment count on circles
- Lower particle/iterator counts
- Disable antialiasing if not needed
- Use simpler blend modes
- Check for unnecessary texture reads

### "Colors look wrong"
- Verify color space (RGB vs HSB)
- Check SetColor is before shapes
- Verify alpha values
- Check blend modes

### "Animation is jerky"
- Use Smooth op for value transitions
- Check frame rate in performance monitor
- Reduce complexity during motion
- Pre-calculate expensive operations

## Performance Tips

1. **Reduce Segments** - Circles don't need 100 segments if they're small
2. **Batch Similar Shapes** - Group similar operations together
3. **Use Instancing** - For many identical shapes, use instanced drawing
4. **Limit Transparency** - Overlapping transparent shapes are expensive
5. **Cache Calculations** - Don't recalculate same values each frame
6. **Cull Off-Screen** - Don't draw what's not visible
7. **Simplify Blending** - Complex blend modes are expensive
8. **Optimize Textures** - Use appropriate texture sizes
9. **Limit Feedback Depth** - Don't keep too many feedback history frames
10. **Profile Regularly** - Use performance monitor to identify bottlenecks

## Featured Videos

### Official Tutorials

```vid
https://youtu.be/goO3PhuenBI
Title: First Steps in Cables.gl - Kaleidoscope Webcam Effect
Author: The Interactive & Immersive HQ
```

```vid
https://youtu.be/xnObNRv8n9I
Title: Introduction to cables.gl Data-Driven Gradient from Geo-Located Weather
Author: Kirell Benzi
```

### Additional Resources

- **Generative Op Art Tutorial**: [Class Central Course](https://www.classcentral.com/course/youtube-generative-op-art-using-feedback-in-cables-gl-tutorial-344255) - Learn feedback loops and Op Art
- **Interactive Rectangle Tutorial**: [Blog Post](https://blog.cables.gl/2019/11/22/interactive-rectangle-op-tutorial/) - Create on-screen sliders
- **Post-Processing Guide**: [Official Docs](https://cables.gl/docs/2_intermediate/post-processing_3d_scenes/post-processing_3d_scenes) - Apply effects to scenes
- **Data Visualization**: [Apache ECharts Integration](https://quadexcel.com/wp/fast-and-easy-data-visualization-with-cables-gl-and-apache-echarts/) - Combine with charting libraries
- **Cables.gl Examples**: [Official Examples](https://cables.gl/examples) - Browse community creations
- **Coding with Cables**: [GitHub Repo](https://github.com/cables-gl/coding-with-cables) - Code examples and custom ops

## Exercises

### Beginner

1. Create a colorful loading spinner using rotating circles
2. Build a grid of squares that change color based on mouse position
3. Make a simple particle system with random positions and sizes

### Intermediate

1. Create a kaleidoscope effect with 8 mirrored segments
2. Build an interactive color picker using mouse position
3. Implement a feedback tunnel with infinite zoom effect
4. Create a data visualization showing time-series data as animated bars

### Advanced

1. Build a generative Op Art piece using feedback loops
2. Create a particle system with physics (gravity, collision)
3. Implement a cellular automaton (Game of Life or similar)
4. Create an audio-reactive geometric pattern generator
5. Build a real-time weather visualization using API data

## Project Ideas

1. **Abstract Clock** - Time visualization with geometric shapes
2. **Music Visualizer** - Frequency bands displayed as 2D patterns
3. **Generative Logo** - Company logo with parametric variations
4. **Loading Animations** - Collection of animated loaders
5. **Data Dashboard** - Real-time data display with charts
6. **Interactive Art Installation** - Touch/camera-driven visuals
7. **Typography Animation** - Kinetic text effects
8. **Pattern Generator** - Infinite procedural pattern variations
9. **Mouse-Driven Drawing Tool** - Paint with code
10. **Meditation Visual** - Calming, slowly evolving patterns

