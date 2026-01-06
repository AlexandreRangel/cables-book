# 3D Graphics in Cables.gl

## Introduction to 3D

Cables.gl provides powerful tools for creating real-time 3D graphics using WebGL. This chapter covers everything from basic 3D concepts to advanced rendering techniques, scene management, and performance optimization. Whether you're creating simple 3D visualizations or complex interactive experiences, this guide will give you the knowledge to master 3D graphics in cables.gl.

**Official reference:** start with [cables.gl docs](https://cables.gl/docs) and search for **Cameras**, **Lights**, **Materials**, **GLTF**, **Textures**, and **Post Processing**. Operator names and ports can differ between versions, but the underlying concepts stay the same.

Quick links (official):
- GLTF op reference example: [`Ops.Gl.GLTF.GltfScene_v4`](https://cables.gl/op/Ops.Gl.GLTF.GltfScene_v4) (operator pages are often the most direct “what ports exist?” reference)

## The 3D Pipeline

A basic 3D setup requires:

```
3D RENDERING PIPELINE
MainLoop (Frame Start)
Camera (View Setup)
+-> Position (X, Y, Z)
+-> Rotation / LookAt
+-> Projection (Perspective/Orthographic)
Lighting (Optional)
+-> Directional Light
+-> Point Light
+-> Ambient Light
Materials (Surface Properties)
+-> BasicMaterial / StandardMaterial
+-> Color / Texture
+-> Shading Properties
Mesh/Geometry (3D Shapes)
+-> Box, Sphere, Plane, etc.
+-> Custom Models
Rendered Output (Canvas)
```

## Cameras

Cameras define how we view the 3D scene.

### PerspectiveCamera

The most common camera type - mimics human vision with perspective distortion.

**Key Parameters:**

- `FOV` (Field of View) - How wide the view is (typically 45-90 degrees)
- `Near` / `Far` - Clipping planes (objects outside this range aren't rendered)
- `Position X/Y/Z` - Camera location

### OrthographicCamera

No perspective distortion - useful for UI, 2D-style 3D, or technical views.

**Key Parameters:**

- `Zoom` - Scale of the view
- `Near` / `Far` - Clipping planes

### Orbit Controls

Add interactive camera controls:

```
Camera -> OrbitControls
```

Allows users to rotate, zoom, and pan the view.

### LookAt

Point the camera at a specific location or object.

```
Camera -> LookAt (target position)
```

**Use Cases:**

- Follow a moving object
- Create cinematic camera movements
- Focus on specific scene elements

### Camera Animation

Animate camera movement for cinematic effects:

```
Time -> Sin -> Camera Position X
Time -> Cos -> Camera Position Z
Time -> Camera Rotation Y (orbit)
```

### Camera Shake Effect

Add dynamic camera shake:

```
Random -> Multiply (shake intensity) -> Add to Camera Position
```

### First-Person Camera

Create FPS-style camera controls:

```
MouseX -> Camera Rotation Y
MouseY -> Camera Rotation X
WASD Keys -> Camera Position
```

### Camera Path Following

Follow a predefined path:

```
ArrayIterator (path points)
Smooth interpolation between points
Camera Position
```

### Camera Constraints

Limit camera movement:

```
Camera Position -> Clamp (min, max) -> Constrained Position
```

## Lighting

Lighting brings depth and realism to 3D scenes.

### AmbientLight

Uniform light that illuminates everything equally.

```
MainLoop -> Camera -> AmbientLight -> [Rest of scene]
```

**Tip:** Use subtle ambient light to prevent completely black shadows.

### DirectionalLight

Light from a specific direction (like the sun).

**Key Parameters:**

- Direction (X, Y, Z)
- Color
- Intensity

### PointLight

Light emanating from a point in space (like a light bulb).

**Key Parameters:**

- Position (X, Y, Z)
- Color
- Intensity
- Falloff radius

### SpotLight

Focused beam of light (like a flashlight or stage light).

**Key Parameters:**

- Position and direction
- Cone angle
- Falloff

### Shadow Mapping

Enable shadows for more realism:

```
DirectionalLight (shadows enabled) -> ShadowMap -> Scene
```

**Shadow Parameters:**
- `Shadow Map Size` - Resolution (higher = sharper, slower)
- `Shadow Bias` - Prevents shadow acne
- `Shadow Radius` - Softness of shadow edges

**Tip:** Use lower shadow map sizes for better performance. 1024x1024 is usually sufficient.

### Three-Point Lighting Setup

Professional lighting arrangement:

```
MainLoop -> Camera
AmbientLight (subtle, 0.2 intensity) - Fill light
DirectionalLight (main, from top-left) - Key light
PointLight (weaker, opposite side) - Rim light
[Your scene]
```

**Key Light:** Main illumination (brightest)
**Fill Light:** Reduces harsh shadows (ambient or weak directional)
**Rim Light:** Creates edge highlights (back/side lighting)

### Image-Based Lighting (IBL)

Use environment maps for realistic lighting:

```
HDRITexture -> Environment Map -> PBRMaterial
```

Creates reflections and lighting based on real-world environments.

### Light Probes

Place light probes in your scene for accurate local lighting:

```
LightProbe -> Sample nearby lights -> Apply to objects
```

### Volumetric Lighting

Create god rays and atmospheric lighting:

```
DirectionalLight -> VolumetricScattering -> [Scene]
```

### Light Animation

Animate lights for dynamic scenes:

```
Time -> Sin -> Light Intensity (pulsing)
Time -> Rotate -> Light Direction (rotating sun)
AudioAnalyzer -> Light Color (audio-reactive)
```

## Geometry and Meshes

### Primitive Shapes

**Cube** - Basic box shape
```
Parameters: Width, Height, Depth
```

**Sphere** - Perfect sphere
```
Parameters: Radius, Segments (horizontal/vertical)
```

**Cylinder** - Tube shape
```
Parameters: Radius Top/Bottom, Height, Segments
```

**Plane** - Flat surface
```
Parameters: Width, Height
```

**Torus** - Donut shape
```
Parameters: Radius, Tube Radius, Segments
```

### Loading 3D Models

**OBJLoader** - Load .obj format models
```
OBJLoader -> Mesh
```

**GLTFLoader** - Load .gltf/.glb models (recommended)
```
GLTFLoader -> Scene/Mesh
```

**FBXLoader** - Load .fbx models

### Creating Custom Geometry

Use **PointCloud** or **CustomGeometry** ops to build meshes from data.

**PointCloud:**
```
ArrayIterator (positions) -> PointCloud
```

**CustomGeometry:**
```
Vertices Array -> Normals Array -> UVs Array -> CustomGeometry
```

### Procedural Geometry Generation

Create geometry programmatically:

**Example: Procedural Terrain**
```
IteratorLoop (grid)
NoiseTexture (sample at position) -> Height
Calculate vertex positions
Generate normals
CustomGeometry
```

**Example: Parametric Surfaces**
```
U/V parameters -> Math functions -> Vertex positions
CustomGeometry
```

### Geometry Instancing

Render many copies efficiently:

```
Mesh -> InstanceTransform (array of transforms) -> InstancedMesh
```

**Use Cases:**

- Forests of trees
- Crowds of characters
- Particle systems
- Repeating architectural elements

### Geometry Modifiers

Modify existing geometry:

**Subdivision:**
```
Mesh -> Subdivide -> Smoother surface
```

**Displacement:**
```
Mesh -> DisplacementMap -> Deformed geometry
```

**Morphing:**
```
Mesh1 -> Morph -> Mesh2 (blend between shapes)
```

### Boolean Operations

Combine geometries:

```
Mesh1 -> BooleanUnion -> Mesh2
Mesh1 -> BooleanSubtract -> Mesh2
Mesh1 -> BooleanIntersect -> Mesh2
```

## Real-Time Mesh Distortion

Real-time mesh distortion allows you to dynamically modify geometry vertices during rendering, creating effects like bending walls, scaling surfaces, and warping shapes. This is essential for architectural visualization, interactive installations, and dynamic 3D effects.

### Understanding Vertex Manipulation

Mesh distortion works by modifying vertex positions in real-time. Each vertex has:
- **Position** (X, Y, Z) - Where the vertex is located
- **Normal** (NX, NY, NZ) - Which direction the surface faces
- **UV Coordinates** (U, V) - Texture mapping coordinates

```
MESH DISTORTION PIPELINE
Base Mesh (Plane, Box, etc.)
Vertex Data Extraction
+-> Positions Array
+-> Normals Array
+-> UVs Array
Distortion Function
+-> Calculate new positions
+-> Update normals (if needed)
+-> Preserve UVs
CustomGeometry (with distorted vertices)
Material -> Render
```

### Method 1: Node-Based Distortion

Using built-in cables.gl ops to distort meshes.

#### Example 1: Scaling a Wall (Size Transformation)

Transform a plain wall into different sizes using procedural scaling:

```
WALL SCALING SETUP
Plane (Base Wall)
GetVertices -> Positions Array
Scale Factor (X, Y, Z)
ArrayMap (multiply each vertex by scale)
GetNormals -> Normals Array
GetUVs -> UVs Array
CustomGeometry (new positions, normals, UVs)
Material -> Render
```

**Step-by-Step Node Setup:**

1. **Create Base Plane:**
   - Add `Plane` op
   - Set Width: 10, Height: 5
   - Set Segments Width: 20, Segments Height: 10 (for smooth distortion)

2. **Extract Vertex Data:**
   - Add `GetVertices` op
   - Connect Plane -> GetVertices
   - Output: Array of vertex positions

3. **Create Scale Controls:**
   - Add `Slider` ops for X, Y, Z scale
   - Or use `Number` ops with values

4. **Apply Scaling:**
   - Use `ArrayMap` or `ArrayIterator` to multiply each vertex
   - For each vertex: `[x, y, z] * [scaleX, scaleY, scaleZ]`

5. **Rebuild Geometry:**
   - Get original normals and UVs from Plane
   - Add `CustomGeometry` op
   - Connect: Scaled Positions -> CustomGeometry
   - Connect: Original Normals -> CustomGeometry
   - Connect: Original UVs -> CustomGeometry

#### Example 2: Bending a Wall (Curved Distortion)

Bend a plain wall into a curved wall with controllable angle:

```
WALL BENDING SETUP
Plane (Base Wall)
GetVertices -> Positions Array
Bend Angle (Slider/Number)
Bend Center (X position where bend occurs)
ArrayMap (apply bend transformation)
Calculate New Normals (for proper lighting)
CustomGeometry -> Material -> Render
```

**Bending Algorithm (Node-Based):**

For each vertex:
1. Calculate distance from bend center
2. Calculate angle based on distance and bend amount
3. Rotate vertex around bend axis
4. Update position

**Node Setup for Bending:**

```
Plane
GetVertices -> ArrayIterator
For each vertex:
  Vertex X -> Subtract (Bend Center) -> Distance from center
  Distance -> Multiply (Bend Angle) -> Rotation angle
  Vertex Y -> Sin(Rotation) -> New Y position
  Vertex Z -> Cos(Rotation) -> New Z position
  Vertex X -> Keep original
  Combine -> New Vertex Position
ArrayCollect -> All Distorted Vertices
CustomGeometry
```

### Method 2: JavaScript Custom Op for Mesh Distortion

For more control and performance, use a JavaScript custom op to handle distortion.

#### Custom Op: Wall Distorter

Create a custom op that handles both scaling and bending:

```javascript
// Custom Op: WallDistorter
// Distorts a plane mesh with scaling and bending

const inVertices = op.inArray("Input Vertices");
const inNormals = op.inArray("Input Normals");
const inUVs = op.inArray("Input UVs");

// Scale parameters
const inScaleX = op.inFloat("Scale X", 1.0);
const inScaleY = op.inFloat("Scale Y", 1.0);
const inScaleZ = op.inFloat("Scale Z", 1.0);

// Bend parameters
const inBendAngle = op.inFloat("Bend Angle", 0.0); // in radians
const inBendCenter = op.inFloat("Bend Center X", 0.0); // X position of bend
const inBendAxis = op.inSwitch("Bend Axis", ["X", "Y", "Z"], "X");

// Outputs
const outVertices = op.outArray("Distorted Vertices");
const outNormals = op.outArray("Distorted Normals");
const outUVs = op.outArray("Output UVs");

function distortVertices() {
    const vertices = inVertices.get();
    const normals = inNormals.get();
    const uvs = inUVs.get();
    
    // `vertices` may be an Array or a TypedArray depending on where it comes from.
    if (!vertices || vertices.length === 0) {
        outVertices.set([]);
        outNormals.set([]);
        outUVs.set([]);
        return;
    }
    
    const scaleX = inScaleX.get();
    const scaleY = inScaleY.get();
    const scaleZ = inScaleZ.get();
    const bendAngle = inBendAngle.get();
    const bendCenter = inBendCenter.get();
    const bendAxis = inBendAxis.get();
    
    const distortedVertices = [];
    const distortedNormals = [];
    
    for (let i = 0; i < vertices.length; i += 3) {
        let x = vertices[i];
        let y = vertices[i + 1];
        let z = vertices[i + 2];
        
        // Apply scaling first
        x *= scaleX;
        y *= scaleY;
        z *= scaleZ;
        
        // Apply bending
        if (Math.abs(bendAngle) > 0.001) {
            if (bendAxis === "X") {
                // Bend along X axis (curves in Y-Z plane)
                const distanceFromCenter = x - bendCenter;
                const angle = distanceFromCenter * bendAngle;
                
                // Rotate around X axis
                const cosA = Math.cos(angle);
                const sinA = Math.sin(angle);
                const newY = y * cosA - z * sinA;
                const newZ = y * sinA + z * cosA;
                y = newY;
                z = newZ;
                
                // Update normals
                if (normals && normals.length > i + 2) {
                    const nx = normals[i];
                    const ny = normals[i + 1];
                    const nz = normals[i + 2];
                    distortedNormals.push(
                        nx,
                        ny * cosA - nz * sinA,
                        ny * sinA + nz * cosA
                    );
                }
            } else if (bendAxis === "Y") {
                // Bend along Y axis (curves in X-Z plane)
                const distanceFromCenter = y - bendCenter;
                const angle = distanceFromCenter * bendAngle;
                
                const cosA = Math.cos(angle);
                const sinA = Math.sin(angle);
                const newX = x * cosA - z * sinA;
                const newZ = x * sinA + z * cosA;
                x = newX;
                z = newZ;
                
                if (normals && normals.length > i + 2) {
                    const nx = normals[i];
                    const ny = normals[i + 1];
                    const nz = normals[i + 2];
                    distortedNormals.push(
                        nx * cosA - nz * sinA,
                        ny,
                        nx * sinA + nz * cosA
                    );
                }
            } else if (bendAxis === "Z") {
                // Bend along Z axis (curves in X-Y plane)
                const distanceFromCenter = z - bendCenter;
                const angle = distanceFromCenter * bendAngle;
                
                const cosA = Math.cos(angle);
                const sinA = Math.sin(angle);
                const newX = x * cosA - y * sinA;
                const newY = x * sinA + y * cosA;
                x = newX;
                y = newY;
                
                if (normals && normals.length > i + 2) {
                    const nx = normals[i];
                    const ny = normals[i + 1];
                    const nz = normals[i + 2];
                    distortedNormals.push(
                        nx * cosA - ny * sinA,
                        nx * sinA + ny * cosA,
                        nz
                    );
                }
            }
        } else {
            // No bending, just copy normals
            if (normals && normals.length > i + 2) {
                distortedNormals.push(
                    normals[i],
                    normals[i + 1],
                    normals[i + 2]
                );
            }
        }
        
        distortedVertices.push(x, y, z);
    }
    
    outVertices.set(distortedVertices);
    if (distortedNormals.length > 0) {
        outNormals.set(distortedNormals);
    } else if (normals) {
        outNormals.set(normals);
    }
    if (uvs) {
        outUVs.set(uvs);
    }
}

// Update when inputs change
inVertices.onChange = distortVertices;
inNormals.onChange = distortVertices;
inUVs.onChange = distortVertices;
inScaleX.onChange = distortVertices;
inScaleY.onChange = distortVertices;
inScaleZ.onChange = distortVertices;
inBendAngle.onChange = distortVertices;
inBendCenter.onChange = distortVertices;
inBendAxis.onChange = distortVertices;
```

#### Using the Wall Distorter Op

**Setup:**

```
Plane (Base Wall)
GetVertices -> WallDistorter (Input Vertices)
GetNormals -> WallDistorter (Input Normals)
GetUVs -> WallDistorter (Input UVs)
WallDistorter (Distorted Vertices) -> CustomGeometry
WallDistorter (Distorted Normals) -> CustomGeometry
WallDistorter (Output UVs) -> CustomGeometry
Material -> Render
```

**Controls:**
- **Scale X/Y/Z**: Resize the wall
- **Bend Angle**: Curvature amount (in radians, use Math.PI/4 for 45°)
- **Bend Center X**: Where the bend occurs along the wall
- **Bend Axis**: Which axis to bend around

### Advanced: Animated Wall Distortion

Combine distortion with animation for dynamic effects:

```javascript
// Custom Op: AnimatedWallDistorter
// Adds time-based animation to distortion

const inVertices = op.inArray("Input Vertices");
const inNormals = op.inArray("Input Normals");
const inUVs = op.inArray("Input UVs");

// Animation parameters
const inTime = op.inFloat("Time", 0.0);
const inAnimationSpeed = op.inFloat("Animation Speed", 1.0);
const inAnimationType = op.inSwitch("Animation Type",
    ["None", "Pulse", "Wave", "Oscillate"], "None");

// Distortion parameters (same as before)
const inScaleX = op.inFloat("Scale X", 1.0);
const inScaleY = op.inFloat("Scale Y", 1.0);
const inScaleZ = op.inFloat("Scale Z", 1.0);
const inBendAngle = op.inFloat("Bend Angle", 0.0);
const inBendCenter = op.inFloat("Bend Center X", 0.0);

// Outputs
const outVertices = op.outArray("Distorted Vertices");
const outNormals = op.outArray("Distorted Normals");
const outUVs = op.outArray("Output UVs");

function getAnimatedBendAngle() {
    const baseAngle = inBendAngle.get();
    const time = inTime.get();
    const speed = inAnimationSpeed.get();
    const type = inAnimationType.get();
    
    if (type === "None") {
        return baseAngle;
    } else if (type === "Pulse") {
        // Pulse between 0 and baseAngle
        const pulse = (Math.sin(time * speed) + 1) / 2; // 0 to 1
        return baseAngle * pulse;
    } else if (type === "Wave") {
        // Wave effect
        return baseAngle * Math.sin(time * speed);
    } else if (type === "Oscillate") {
        // Oscillate around baseAngle
        return baseAngle + Math.sin(time * speed) * (baseAngle * 0.5);
    }
    
    return baseAngle;
}

function distortVertices() {
    const vertices = inVertices.get();
    const normals = inNormals.get();
    const uvs = inUVs.get();
    
    if (!vertices || vertices.length === 0) {
        outVertices.set([]);
        outNormals.set([]);
        outUVs.set([]);
        return;
    }
    
    const scaleX = inScaleX.get();
    const scaleY = inScaleY.get();
    const scaleZ = inScaleZ.get();
    const bendAngle = getAnimatedBendAngle();
    const bendCenter = inBendCenter.get();
    
    const distortedVertices = [];
    const distortedNormals = [];
    
    for (let i = 0; i < vertices.length; i += 3) {
        let x = vertices[i];
        let y = vertices[i + 1];
        let z = vertices[i + 2];
        
        // Apply scaling
        x *= scaleX;
        y *= scaleY;
        z *= scaleZ;
        
        // Apply animated bending
        if (Math.abs(bendAngle) > 0.001) {
            const distanceFromCenter = x - bendCenter;
            const angle = distanceFromCenter * bendAngle;
            
            const cosA = Math.cos(angle);
            const sinA = Math.sin(angle);
            const newY = y * cosA - z * sinA;
            const newZ = y * sinA + z * cosA;
            y = newY;
            z = newZ;
            
            // Update normals
            if (normals && normals.length > i + 2) {
                const nx = normals[i];
                const ny = normals[i + 1];
                const nz = normals[i + 2];
                distortedNormals.push(
                    nx,
                    ny * cosA - nz * sinA,
                    ny * sinA + nz * cosA
                );
            }
        } else {
            if (normals && normals.length > i + 2) {
                distortedNormals.push(
                    normals[i],
                    normals[i + 1],
                    normals[i + 2]
                );
            }
        }
        
        distortedVertices.push(x, y, z);
    }
    
    outVertices.set(distortedVertices);
    if (distortedNormals.length > 0) {
        outNormals.set(distortedNormals);
    } else if (normals) {
        outNormals.set(normals);
    }
    if (uvs) {
        outUVs.set(uvs);
    }
}

// Update on input changes
inVertices.onChange = distortVertices;
inNormals.onChange = distortVertices;
inUVs.onChange = distortVertices;
inTime.onChange = distortVertices;
inAnimationSpeed.onChange = distortVertices;
inAnimationType.onChange = distortVertices;
inScaleX.onChange = distortVertices;
inScaleY.onChange = distortVertices;
inScaleZ.onChange = distortVertices;
inBendAngle.onChange = distortVertices;
inBendCenter.onChange = distortVertices;
```

### Practical Example: Interactive Curved Wall

Complete setup for an interactive curved wall with real-time controls:

```
INTERACTIVE CURVED WALL SETUP
MainLoop
Plane (Base Wall)
Width: 10, Height: 5
Segments: 30x15 (for smooth curves)
GetVertices -> WallDistorter
GetNormals -> WallDistorter
GetUVs -> WallDistorter
Slider (Bend Angle: 0 to PI/2) -> WallDistorter
Slider (Bend Center: -5 to 5) -> WallDistorter
Slider (Scale X: 0.5 to 2.0) -> WallDistorter
Slider (Scale Y: 0.5 to 2.0) -> WallDistorter
WallDistorter -> CustomGeometry
StandardMaterial -> Render
Camera -> OrbitControls
```

### Performance Optimization

For real-time distortion, optimize your setup:

1. **Reduce Vertex Count When Possible:**
   - Use fewer segments for static walls
   - Increase segments only where distortion is visible

2. **Cache Calculations:**
   ```javascript
   let cachedVertices = null;
   let cachedBendAngle = null;
   let cachedScale = null;
   
   function distortVertices() {
       const bendAngle = inBendAngle.get();
       const scale = inScaleX.get();
       
       // Only recalculate if inputs changed
       if (cachedVertices && 
           cachedBendAngle === bendAngle && 
           cachedScale === scale) {
           outVertices.set(cachedVertices);
           return; // Use cached result
       }
       
       // Recalculate...
       // (distortedVertices should be computed above)
       cachedVertices = distortedVertices;
       cachedBendAngle = bendAngle;
       cachedScale = scale;
   }
   ```

3. **Use Instancing for Multiple Walls:**
   - Create one distorted wall
   - Use `InstancedMesh` to duplicate it
   - Much faster than distorting each wall separately

4. **Update Only When Needed:**
   ```javascript
   // Only update on frame if animation is active
   const inRender = op.inTrigger("Render");
   inRender.onTriggered = function() {
       if (inAnimationType.get() !== "None") {
           distortVertices();
       }
   };
   ```

### Advanced Techniques

#### Multi-Axis Bending

Bend along multiple axes simultaneously:

```javascript
// Bend along both X and Y axes
const bendX = distanceFromCenterX * bendAngleX;
const bendY = distanceFromCenterY * bendAngleY;

// Apply rotations in sequence
// First rotate around X, then around Y
```

#### Non-Linear Distortion

Use easing functions for smooth transitions:

```javascript
function easeInOutCubic(t) {
    return t < 0.5 
        ? 4 * t * t * t 
        : 1 - Math.pow(-2 * t + 2, 3) / 2;
}

const easedAngle = baseAngle * easeInOutCubic(progress);
```

#### Texture Coordinate Preservation

When distorting, UVs should remain unchanged for proper texturing:

```javascript
// Always preserve original UVs
outUVs.set(inUVs.get()); // Don't modify UVs during distortion
```

### Common Use Cases

1. **Architectural Visualization:**
   - Bend walls to show different room layouts
   - Scale walls to demonstrate space variations

2. **Interactive Installations:**
   - User-controlled wall distortion
   - Audio-reactive bending

3. **Animation:**
   - Morphing between straight and curved walls
   - Dynamic space transformations

4. **Game Mechanics:**
   - Procedural level generation
   - Dynamic environment changes

### Troubleshooting

**Problem: Normals look wrong after distortion**
- Solution: Recalculate normals after distortion
- Use `CalculateNormals` op or compute in JavaScript

**Problem: Texture stretches or distorts**
- Solution: Don't modify UV coordinates
- Keep original UVs from the base mesh

**Problem: Performance is slow**
- Solution: Reduce vertex count
- Cache calculations
- Only update when parameters change

**Problem: Bending looks jagged**
- Solution: Increase mesh segments
- Use smoother interpolation

## Materials

Materials define how surfaces appear when lit.

### BasicMaterial

Simple colored material, not affected by lighting.

### LambertMaterial

Matte material with diffuse lighting.

### PhongMaterial

Shiny material with specular highlights.

**Key Parameters:**

- `Diffuse Color` - Base color
- `Specular Color` - Highlight color
- `Shininess` - How sharp the highlights are

### PBRMaterial (Physically Based Rendering)

Most realistic material option.

**Key Parameters:**

- `Albedo` - Base color
- `Metalness` - How metallic (0 = plastic, 1 = metal)
- `Roughness` - Surface smoothness (0 = mirror, 1 = rough)
- `Normal Map` - Surface detail
- `Ambient Occlusion` - Crevice shadows
- `Emissive` - Self-illumination
- `Clearcoat` - Additional glossy layer (for car paint, etc.)

**PBR Workflow Tips:**
- Use real-world material values for best results
- Metalness and Roughness are inverse - metals are usually smooth (low roughness)
- Combine texture maps for realistic surfaces
- Use HDR environment maps for accurate reflections

### Material Blending

Blend between materials:

```
Material1 -> Mix -> Material2 (blend factor) -> BlendedMaterial
```

### Animated Materials

Animate material properties:

```
Time -> Sin -> Material Color (pulsing)
Time -> Material Roughness (shimmer effect)
MouseX -> Material Metalness (interactive)
```

### Material Variants

Create material variations:

```
BaseMaterial -> Multiply Color -> Variant1
BaseMaterial -> Multiply Color -> Variant2
```

### Custom Shader Materials

Use custom GLSL shaders (see Shaders chapter):

```
ShaderMaterial (custom GLSL) -> Mesh
```

### Material Instancing

Apply same material to multiple objects efficiently:

```
Material -> Apply to multiple meshes
```

## Transformations in 3D

### Transform

Same as 2D but with full 3D control:

```
Transform
+-- TranslateX, TranslateY, TranslateZ
+-- RotateX, RotateY, RotateZ
+-- ScaleX, ScaleY, ScaleZ (or uniform Scale)
```

### Matrix Operations

For advanced control, use matrix ops:
- `MatrixMultiply` - Combine transformations
- `LookAt` - Point object at target
- `Billboard` - Always face camera
- `MatrixInvert` - Reverse transformation
- `MatrixDecompose` - Extract position/rotation/scale

### Hierarchical Transforms

Create parent-child relationships:

```
Transform (parent)
Transform (child) - inherits parent's transform
Mesh
```

**Use Cases:**

- Character rigging (body -> arm -> hand)
- Vehicle systems (car -> wheel -> tire)
- Solar systems (sun -> planet -> moon)

### Constraint Systems

Constrain object movement:

**Distance Constraint:**
```
Object1 Position -> Distance -> Object2 Position (maintain distance)
```

**Look-At Constraint:**
```
Object -> LookAt -> Target (always face target)
```

**Path Constraint:**
```
Object -> Follow Path -> Constrained movement
```

### IK (Inverse Kinematics)

Control chains of objects:

```
End Effector Position -> IK Solver -> Joint Angles
Transform chain
```

### Physics-Based Transforms

Use physics for natural movement:

```
PhysicsBody -> Transform (position/rotation from physics)
```

### Transform Caching

Cache expensive transformations:

```
Transform -> Cache -> Reuse for multiple objects
```

## Rendering Techniques

### Rendering Order

Opaque objects should render before transparent ones:

```
MainLoop -> Camera
[Opaque objects]
EnableBlending
[Transparent objects]
```

### Multiple Render Passes

Create effects like glow, depth of field, or reflections:

```
MainLoop -> Camera -> RenderToTexture -> [Scene]
            TextureEffect
            RenderToScreen
```

### Fog

Add atmospheric depth:

```
MainLoop -> Camera -> Fog -> [Scene]
```

**Types:**
- Linear fog - Constant density
- Exponential fog - Density increases with distance
- Height fog - Fog based on Y position

### Screen-Space Ambient Occlusion (SSAO)

Add depth and realism:

```
MainLoop -> Camera -> RenderToTexture (depth)
SSAO Effect
Apply to scene
```

### Screen-Space Reflections (SSR)

Realistic reflections without reflection probes:

```
Scene -> RenderToTexture -> SSR Effect -> Reflections
```

### Depth of Field

Focus blur effect:

```
Camera -> DepthOfField -> Focus distance -> Blur amount
```

### Bloom

Glowing highlights:

```
Scene -> Brightness threshold -> Blur -> Add back -> Bloom
```

### Motion Blur

Blur moving objects:

```
Previous frame -> Current frame -> Blend -> Motion blur
```

### Color Grading

Post-process color adjustments:

```
Scene -> ColorCorrection
    +-- Exposure
    +-- Contrast
    +-- Saturation
    +-- Color temperature
    +-- Tint
```

### Chromatic Aberration

Color separation effect:

```
Scene -> ChromaticAberration -> Distorted colors
```

### Vignette

Darken edges:

```
Scene -> Vignette -> Darkened corners
```

### Post-Processing Chain

Combine multiple effects:

```
Scene
RenderToTexture
SSAO
Bloom
ColorGrading
ChromaticAberration
Vignette
Final Output
```

## Scene Management

### Scene Hierarchy

Organize complex scenes:

```
MainLoop -> Camera
Scene (root)
    +-- Environment
    +-- Skybox
    +-- Fog
    +-- Lighting
    +-- AmbientLight
    +-- DirectionalLight
    +-- PointLights (array)
    +-- Static Objects
    +-- [Buildings, terrain, etc.]
    +-- Dynamic Objects
    +-- [Characters, vehicles, etc.]
    +-- Effects
        +-- Particles
        +-- Post-processing
```

### Object Grouping

Group related objects:

```
Group (name: "Characters")
    +-- Character1
    +-- Character2
    +-- Character3
```

### Layer System

Use layers for organization:

```
Layer 0: Background
Layer 1: Environment
Layer 2: Characters
Layer 3: Effects
Layer 4: UI
```

### Culling and Optimization

Hide objects outside view:

```
Object Position -> FrustumCull -> Only render if visible
```

### LOD (Level of Detail) System

Use simpler models at distance:

```
Distance from camera -> If > threshold -> Use LOD model
```

## Practical Examples

### Example 1: Rotating Cube

```
MainLoop
PerspectiveCamera
DirectionalLight
Time -> RotateY input
PhongMaterial
Cube
```

### Example 2: Lit Sphere with Orbit Controls

```
MainLoop
PerspectiveCamera -> OrbitControls
AmbientLight (subtle)
PointLight
PBRMaterial (metalness: 1, roughness: 0.2)
Sphere
```

### Example 3: Loading a 3D Model

```
MainLoop
PerspectiveCamera
DirectionalLight
GLTFLoader (your model.glb)
Transform (scale/position)
```

### Example 4: Solar System

```
MainLoop
PerspectiveCamera -> OrbitControls
AmbientLight (space ambient)
DirectionalLight (sun)
[Sun] - Static sphere with emissive material
[Planet1] - Transform (orbit around sun)
    +-- Time -> RotateY (orbit)
    +-- Time -> RotateY (self-rotation)
    +-- Sphere
[Planet2] - Different orbit speed
    +-- [Moon] - Orbits planet
```

### Example 5: Procedural Terrain

```
MainLoop
PerspectiveCamera -> OrbitControls
DirectionalLight
IteratorLoop (grid: 100x100)
Position -> NoiseTexture (3D noise) -> Height
Calculate vertex (X, height, Z)
Calculate normal from neighbors
CustomGeometry
PBRMaterial (terrain textures)
```

### Example 6: Instanced Forest

```
MainLoop
PerspectiveCamera
DirectionalLight
TreeModel (loaded GLTF)
ArrayIterator (1000 positions)
Random -> Scale variation
Random -> Rotation variation
InstanceTransform
InstancedMesh
```

### Example 7: Interactive 3D Scene

```
MainLoop
PerspectiveCamera -> OrbitControls
MouseX -> Map -> Light Direction X
MouseY -> Map -> Light Direction Y
DirectionalLight
MouseClick -> Toggle -> Object visibility
[Scene objects]
```

### Example 8: Animated Character

```
MainLoop
PerspectiveCamera
DirectionalLight
CharacterModel
Timeline
    +-- Frame 0: Idle pose
    +-- Frame 30: Walk cycle start
    +-- Frame 60: Walk cycle end
    +-- [Loop]
Apply to skeleton
AnimatedMesh
```

### Example 9: Particle System

```
MainLoop
PerspectiveCamera
ArrayIterator (particles)
Particle Data
    +-- Position (update with velocity)
    +-- Velocity (update with forces)
    +-- Life (decrease over time)
    +-- Size (scale with life)
Transform (position, scale)
BasicMaterial (color from life)
Sphere (small)
```

### Example 10: Reflective Surface

```
MainLoop
PerspectiveCamera
[Scene to reflect]
RenderToTexture (reflection view)
CubemapTexture
PBRMaterial (reflection map)
Plane (mirror surface)
```

### Example 11: Volumetric Fog

```
MainLoop
PerspectiveCamera
Scene
RenderToTexture (depth)
VolumetricFog
    +-- Depth texture
    +-- Noise texture (for variation)
    +-- Light direction
Blend with scene
```

### Example 12: Dynamic Lighting Setup

```
MainLoop
PerspectiveCamera
Time -> Sin -> Sun angle
Sun angle -> Calculate direction
DirectionalLight (sun)
    +-- Color (warm -> cool based on angle)
    +-- Intensity (day -> night)
AmbientLight
    +-- Intensity (complement sun)
[Scene]
```

### Example 13: Morphing Objects

```
MainLoop
PerspectiveCamera
Time -> Sin -> Morph factor (0 to 1)
Mesh1 -> Morph -> Mesh2
Material
```

### Example 14: Physics Simulation

```
MainLoop
PerspectiveCamera
PhysicsWorld
    +-- Gravity
    +-- Colliders
PhysicsBody (rigid body)
    +-- Mass
    +-- Forces
    +-- Collisions
Transform (from physics)
Mesh
```

### Example 15: Post-Processing Pipeline

```
MainLoop
PerspectiveCamera
[Render scene]
RenderToTexture
SSAO
Bloom (extract bright areas)
Blur (bloom)
Add bloom back
ColorGrading
    +-- Exposure
    +-- Contrast
    +-- Saturation
ChromaticAberration
Vignette
Final output
```

### Example 16: Audio-Reactive 3D

```
MainLoop
PerspectiveCamera
AudioAnalyzer -> FFTArray
ArrayIterator (frequency bands)
FFT Value -> Scale Y
Transform (position from index, scale from FFT)
Cube (bar visualization)
```

### Example 17: Procedural City

```
MainLoop
PerspectiveCamera -> OrbitControls
DirectionalLight
IteratorLoop (grid: city blocks)
NoiseTexture -> Building height
Random -> Building type
Transform (position, height)
Cube (building)
PBRMaterial (building texture)
```

### Example 18: Water Surface

```
MainLoop
PerspectiveCamera
Time -> Sin -> Wave offset
Plane (subdivided)
Vertex shader (displace vertices)
WaterMaterial
    +-- Normal map (animated)
    +-- Reflection (scene)
    +-- Refraction
    +-- Foam (at edges)
```

### Example 19: Portal Effect

```
MainLoop
PerspectiveCamera
[Main scene]
PortalCamera (different view)
RenderToTexture (portal view)
Plane (portal frame)
Material (portal texture)
Stencil buffer (mask to portal shape)
```

### Example 20: Multi-Pass Rendering

```
MainLoop
PerspectiveCamera
[Pass 1: Opaque objects]
RenderToTexture
[Pass 2: Transparent objects]
Blend with Pass 1
[Pass 3: Effects]
Blend all passes
Post-processing
```

## Advanced Animation Techniques

### Skeletal Animation

Animate characters with bones:

```
Skeleton (bone hierarchy)
Animation data (keyframes)
Skin weights (vertex -> bone influence)
AnimatedMesh
```

### Morph Targets

Blend between shape variations:

```
BaseMesh -> MorphTarget1 (blend factor) -> MorphTarget2
```

**Use Cases:**

- Facial expressions
- Shape variations
- Smooth transitions

### Procedural Animation

Generate animation with code:

```
Time -> Math functions -> Transform values
Apply to objects
```

### Physics Animation

Use physics for natural movement:

```
PhysicsBody -> Forces -> Motion -> Transform
```

### Animation Blending

Smoothly transition between animations:

```
Animation1 -> Blend -> Animation2 (blend factor)
```

## Performance Optimization

### General Tips

1. **Reduce Polygon Count** - Use lower-poly models when possible
2. **Texture Atlas** - Combine textures to reduce draw calls
3. **Level of Detail (LOD)** - Use simpler models for distant objects
4. **Frustum Culling** - Built-in, but organize scenes efficiently
5. **Bake Lighting** - Pre-calculate lighting for static scenes

### Advanced Optimization

**Occlusion Culling:**
```
Object -> Check if occluded -> Skip rendering
```

**Batching:**
```
Similar objects -> Batch -> Single draw call
```

**Texture Compression:**
- Use compressed texture formats (DXT, ETC)
- Reduce texture resolution when possible
- Use mipmaps for distant objects

**Geometry Optimization:**
- Remove unnecessary vertices
- Use indexed geometry
- Optimize UV mapping

**Shader Optimization:**
- Minimize texture samples
- Use simpler shaders when possible
- Avoid branching in shaders

**Render Target Optimization:**
- Use appropriate render target sizes
- Don't render at higher resolution than display
- Use half-precision floats when possible

### Performance Monitoring

Track performance metrics:

```
PerformanceMonitor
    +-- FPS
    +-- Draw calls
    +-- Triangle count
    +-- Texture memory
    +-- Shader compilation time
```

### Adaptive Quality

Adjust quality based on performance:

```
FPS -> If < 30 -> Reduce quality
    +-- Lower LOD
    +-- Disable effects
    +-- Reduce particle count
```

## Common Patterns and Workflows

### Pattern: Object Pooling

Reuse objects instead of creating/destroying:

```
Pool of inactive objects
Activate when needed
Deactivate when done
Return to pool
```

### Pattern: Component System

Organize object behavior:

```
GameObject
    +-- Transform component
    +-- Render component
    +-- Physics component
    +-- Script component
```

### Pattern: Event System

Decouple object interactions:

```
EventEmitter
    +-- Subscribe (listener)
    +-- Emit (event)
Objects react to events
```

### Pattern: State Machine

Manage object states:

```
StateMachine
    +-- Idle state
    +-- Active state
    +-- Transition conditions
```

## Debugging 3D Scenes

### Visual Debugging

**Show Normals:**
```
Mesh -> DebugNormals -> Visualize normals
```

**Show Bounding Boxes:**
```
Mesh -> DebugBounds -> Show bounding boxes
```

**Show Wireframe:**
```
Material -> Wireframe mode -> See geometry
```

**Show Grid:**
```
GridHelper -> Visual reference
```

### Common Issues

**"Objects not visible"**
- Check camera position and direction
- Verify objects are within near/far planes
- Check material alpha values
- Verify lighting setup

**"Shadows look wrong"**
- Adjust shadow bias
- Increase shadow map resolution
- Check light shadow settings
- Verify shadow receiving objects

**"Performance is slow"**
- Reduce polygon count
- Lower texture resolutions
- Disable expensive effects
- Use LOD system
- Optimize shaders

**"Materials look incorrect"**
- Verify texture UV mapping
- Check normal map orientation
- Verify PBR material values
- Check lighting setup

## Best Practices

1. **Start Simple** - Build complexity gradually
2. **Optimize Early** - Consider performance from the start
3. **Use Instancing** - For repeated objects
4. **Organize Scenes** - Use hierarchies and groups
5. **Test on Target Hardware** - Performance varies by device
6. **Use Appropriate Formats** - GLTF for models, compressed textures
7. **Profile Regularly** - Use performance tools
8. **Document Complex Setups** - Add comments to patches
9. **Version Control** - Save iterations of complex scenes
10. **Reuse Assets** - Don't duplicate unnecessarily

## Featured Videos

<!-- Add 3D graphics videos here -->

<!-- Example:
```vid
https://youtu.be/XXXXX
Title: 3D in Cables.gl
Author: Channel Name
```
-->

## Exercises

### Beginner

1. Create a solar system with orbiting planets
2. Build a simple room with multiple light sources
3. Load a 3D model and add interactive rotation controls
4. Create a rotating cube with different materials
5. Build a simple scene with fog

### Intermediate

1. Create a procedural terrain with noise
2. Build an instanced forest with 100+ trees
3. Implement a three-point lighting setup
4. Create a water surface with animated waves
5. Build a particle system with physics
6. Create a portal effect with dual cameras
7. Implement post-processing effects (bloom, SSAO)
8. Build an audio-reactive 3D visualization
9. Create a morphing object animation
10. Implement a character with skeletal animation

### Advanced

1. Build a complete scene with LOD system
2. Create a volumetric fog effect
3. Implement screen-space reflections
4. Build a physics-based simulation
5. Create a procedural city generator
6. Implement a multi-pass rendering pipeline
7. Build an interactive 3D game scene
8. Create advanced post-processing chain
9. Implement custom shader materials
10. Build a complex scene with optimization techniques

## Project Ideas

1. **3D Product Viewer** - Interactive product showcase
2. **Architectural Visualization** - Building walkthrough
3. **Game Prototype** - Simple 3D game mechanics
4. **Data Visualization** - 3D charts and graphs
5. **Virtual Gallery** - 3D art exhibition
6. **Interactive Installation** - Museum or event display
7. **Music Visualizer** - 3D audio-reactive visuals
8. **Procedural World** - Generated landscape exploration
9. **Character Animation** - Animated character showcase
10. **Physics Sandbox** - Interactive physics playground

