# Ops.Graphics.Meshes

---

## Ops.Graphics.Meshes

### CablesLogo
![CablesLogo op](images/ops/Ops_Graphics_Meshes_CablesLogo.svg)

**Full Name:** `Ops.Graphics.Meshes.CablesLogo`

**Description:** cables logo mesh/geometry

**> Input Ports:**

- **Render** (Trigger)
- **Scale** (Number)
- **Draw** (Number: Boolean)

**< Output Ports:**

- **Trigger** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/xUMq3j)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CablesLogo"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Meshes.CablesLogo](https://cables.gl/op/Ops.Graphics.Meshes.CablesLogo)


### Circle_v3
![Circle_v3 op](images/ops/Ops_Graphics_Meshes_Circle_v3.svg)

**Full Name:** `Ops.Graphics.Meshes.Circle_v3`

**Description:** Draws a circle to the canvas.

**> Input Ports:**

- **Render** (Trigger)
- **Radius** (Number)
- **InnerRadius** (Number)
- **Segments** (Number: Integer)
- **Percent** (Number)
- **Steps** (Number)
- **InvertSteps** (Number: Boolean)
- **Spline** (Number: Boolean)
- **Render Mesh** (Number: Boolean)

**< Output Ports:**

- **Trigger** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/DAAkQ6)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Circle_v3"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Meshes.Circle_v3](https://cables.gl/op/Ops.Graphics.Meshes.Circle_v3)


### Cross
![Cross op](images/ops/Ops_Graphics_Meshes_Cross.svg)

**Full Name:** `Ops.Graphics.Meshes.Cross`

**Description:** Draws a cross with controllable thickness and length.

**> Input Ports:**

- **Render** (Trigger)
- **Size** (Number)
- **Thickness** (Number)
- **Crosshair** (Number: Boolean)
- **Left** (Number: Boolean)
- **Right** (Number: Boolean)
- **Top** (Number: Boolean)
- **Bottom** (Number: Boolean)
- **Active** (Number: Boolean)

**< Output Ports:**

- **Next** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/ojTS_o)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Cross"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Meshes.Cross](https://cables.gl/op/Ops.Graphics.Meshes.Cross)


### Cube_v2
![Cube_v2 op](images/ops/Ops_Graphics_Meshes_Cube_v2.svg)

**Full Name:** `Ops.Graphics.Meshes.Cube_v2`

**Description:** Draws a cube to the canvas. Please note that without doing a rotation you will only see a rectangle.

**> Input Ports:**

- **Render** (Trigger)
- **Render Mesh** (Number: Boolean)
- **Width** (Number)
- **Length** (Number)
- **Height** (Number)
- **Center** (Number: Boolean)
- **Bias** (Number)
- **Flip X** (Number: Boolean)
- **Top** (Number: Boolean)
- **Bottom** (Number: Boolean)
- **Left** (Number: Boolean)
- **Right** (Number: Boolean)
- **Front** (Number: Boolean)
- **Back** (Number: Boolean)

**< Output Ports:**

- **Next** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/0ghhQ6)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Cube_v2"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Meshes.Cube_v2](https://cables.gl/op/Ops.Graphics.Meshes.Cube_v2)


### Rectangle_v4
![Rectangle_v4 op](images/ops/Ops_Graphics_Meshes_Rectangle_v4.svg)

**Full Name:** `Ops.Graphics.Meshes.Rectangle_v4`

**Description:** draw a rectangle (plane, square)

**> Input Ports:**

- **Trigger** (Trigger)
- **Render** (Number: Boolean)
- **Width** (Number)
- **Height** (Number)
- **Flip TexCoord X** (Number: Boolean)
- **Flip TexCoord Y** (Number: Boolean)
- **Num Columns** (Number: Integer)
- **Num Rows** (Number: Integer)

**< Output Ports:**

- **Trigger** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/M3QiQ6)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Rectangle_v4"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Meshes.Rectangle_v4](https://cables.gl/op/Ops.Graphics.Meshes.Rectangle_v4)


### Sphere_v3
![Sphere_v3 op](images/ops/Ops_Graphics_Meshes_Sphere_v3.svg)

**Full Name:** `Ops.Graphics.Meshes.Sphere_v3`

**Description:** Draw parameterizable sphere

**> Input Ports:**

- **Render** (Trigger)
- **Radius** (Number)
- **Stacks** (Number)
- **Slices** (Number)
- **Filloffset** (Number)

**< Output Ports:**

- **Trigger** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/HvxfQ6)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Sphere_v3"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Meshes.Sphere_v3](https://cables.gl/op/Ops.Graphics.Meshes.Sphere_v3)


### Star_v2
![Star_v2 op](images/ops/Ops_Graphics_Meshes_Star_v2.svg)

**Full Name:** `Ops.Graphics.Meshes.Star_v2`

**Description:** draw a star mesh (saw,gear)

**> Input Ports:**

- **Render** (Trigger)
- **Segments** (Number)
- **Radius** (Number)
- **Shape Index** (Number: Integer)
- **Length** (Number)
- **Peak Z Pos** (Number)
- **Percent** (Number)
- **Fill** (Number: Boolean)
- **Render Mesh** (Number: Boolean)

**< Output Ports:**

- **Trigger** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/eXhAY4)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Star_v2"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Meshes.Star_v2](https://cables.gl/op/Ops.Graphics.Meshes.Star_v2)


### Triangle_v2
![Triangle_v2 op](images/ops/Ops_Graphics_Meshes_Triangle_v2.svg)

**Full Name:** `Ops.Graphics.Meshes.Triangle_v2`

**Description:** Renders a triangle to the canvas.

**> Input Ports:**

- **Render** (Trigger)
- **Width** (Number)
- **Height** (Number)
- **Draw** (Number: Boolean)

**< Output Ports:**

- **Trigger** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/RnNiQ6)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Triangle_v2"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Meshes.Triangle_v2](https://cables.gl/op/Ops.Graphics.Meshes.Triangle_v2)


