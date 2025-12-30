# Ops.Gl.Meshes

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.Meshes

### ComposingGridOverlay
![ComposingGridOverlay op](images/ops/Ops_Gl_Meshes_ComposingGridOverlay.svg)

**Full Name:** `Ops.Gl.Meshes.ComposingGridOverlay`
**Description:** Rule of thirds image composition helper

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Scale** (Number): *See documentation*
- **Show Center** (Number: Boolean): *See documentation*

**< Output Ports:**
- *Visit [Ops.Gl.Meshes.ComposingGridOverlay documentation](https://cables.gl/op/Ops.Gl.Meshes.ComposingGridOverlay) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/G8mQQ2)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ComposingGridOverlay"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.ComposingGridOverlay](https://cables.gl/op/Ops.Gl.Meshes.ComposingGridOverlay)

---

### Cone
![Cone op](images/ops/Ops_Gl_Meshes_Cone.svg)

**Full Name:** `Ops.Gl.Meshes.Cone`
**Description:** number of horizontal segments

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Slices** (Number): *See documentation*
- **Stacks** (Number): *See documentation*
- **Radius** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/fGA7W6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Cone"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Cone](https://cables.gl/op/Ops.Gl.Meshes.Cone)

---

### Corner
![Corner op](images/ops/Ops_Gl_Meshes_Corner.svg)

**Full Name:** `Ops.Gl.Meshes.Corner`
**Description:** render a rectangular corner

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Thickness** (Number): *See documentation*
- **Draw** (Number: Boolean): *See documentation*
- **Pivot X Index** (Number: Integer): *See documentation*
- **Pivot Y Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/KWolQ6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Corner"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Corner](https://cables.gl/op/Ops.Gl.Meshes.Corner)

---

### Cylinder_v2
![Cylinder_v2 op](images/ops/Ops_Gl_Meshes_Cylinder_v2.svg)

**Full Name:** `Ops.Gl.Meshes.Cylinder_v2`
**Description:** draw parameterizable cylinder (aka tube,pipe,round,circle)

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Render Mesh** (Number: Boolean): *See documentation*
- **Segments** (Number: Integer): *See documentation*
- **Stacks** (Number: Integer): *See documentation*
- **Length** (Number): *See documentation*
- **Outer Radius** (Number): *See documentation*
- **Inner Radius** (Number): *See documentation*
- **Flip Mapping** (Number: Boolean): *See documentation*
- **Caps** (Number: Boolean): *See documentation*
- **Flat Normals** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/GxagQ6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Cylinder_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Cylinder_v2](https://cables.gl/op/Ops.Gl.Meshes.Cylinder_v2)

---

### FloorGrid
![FloorGrid op](images/ops/Ops_Gl_Meshes_FloorGrid.svg)

**Full Name:** `Ops.Gl.Meshes.FloorGrid`
**Description:** draw a grid on the floor

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/LiwB16)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FloorGrid"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.FloorGrid](https://cables.gl/op/Ops.Gl.Meshes.FloorGrid)

---

### FreeFormPlane
![FreeFormPlane op](images/ops/Ops_Gl_Meshes_FreeFormPlane.svg)

**Full Name:** `Ops.Gl.Meshes.FreeFormPlane`
**Description:** A freely deformable plane, rectangle, polygon

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **X 1** (Number): *See documentation*
- **Y 1** (Number): *See documentation*
- **Z 1** (Number): *See documentation*
- **X 2** (Number): *See documentation*
- **Y 2** (Number): *See documentation*
- **Z 2** (Number): *See documentation*
- **X 3** (Number): *See documentation*
- **Y 3** (Number): *See documentation*
- **Z 3** (Number): *See documentation*
- **X 4** (Number): *See documentation*
- **Y 4** (Number): *See documentation*
- **Z 4** (Number): *See documentation*
- **Tc X 1** (Number): *See documentation*
- **Tc Y 1** (Number): *See documentation*
- **Tc X 2** (Number): *See documentation*
- **Tc Y 2** (Number): *See documentation*
- **Tc X 3** (Number): *See documentation*
- **Tc Y 3** (Number): *See documentation*
- **Tc X 4** (Number): *See documentation*
- **Tc Y 4** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Q92nQ6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FreeFormPlane"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.FreeFormPlane](https://cables.gl/op/Ops.Gl.Meshes.FreeFormPlane)

---

### FullscreenRectangle_v2
![FullscreenRectangle_v2 op](images/ops/Ops_Gl_Meshes_FullscreenRectangle_v2.svg)

**Full Name:** `Ops.Gl.Meshes.FullscreenRectangle_v2`
**Description:** Draws a rectangle using the full WebGL canvas size

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Flip Y** (Number: Boolean): *See documentation*
- **Flip X** (Number: Boolean): *See documentation*
- **Texture** (Object:Texture): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/uKkIeG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FullscreenRectangle_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.FullscreenRectangle_v2](https://cables.gl/op/Ops.Gl.Meshes.FullscreenRectangle_v2)

---

### GeometryToTexture_v3
![GeometryToTexture_v3 op](images/ops/Ops_Gl_Meshes_GeometryToTexture_v3.svg)

**Full Name:** `Ops.Gl.Meshes.GeometryToTexture_v3`
**Description:** Convert vertices of a geometry to a data texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Geometry** (Object:Geometry): *See documentation*
- **Continously Update** (Number: Boolean): *See documentation*
- **Order Index** (Number: Integer): *See documentation*
- **Content Index** (Number: Integer): *See documentation*
- **New Size** (Number): *See documentation*
- **Tex Width** (Number: Integer): *See documentation*
- **Filter Index** (Number: Integer): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Pixel Format Index** (Number: Integer): *See documentation*
- **Color Texture** (Object:Texture): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Total Vertices** (Number): *See documentation*
- **Texture** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/bhWkpX)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryToTexture_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.GeometryToTexture_v3](https://cables.gl/op/Ops.Gl.Meshes.GeometryToTexture_v3)

---

### Grid
![Grid op](images/ops/Ops_Gl_Meshes_Grid.svg)

**Full Name:** `Ops.Gl.Meshes.Grid`
**Description:** Draw a simple grid of lines

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Num** (Number: Integer): *See documentation*
- **Spacing** (Number): *See documentation*
- **Center** (Number: Boolean): *See documentation*
- **Axis Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/VxPlQ6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Grid"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Grid](https://cables.gl/op/Ops.Gl.Meshes.Grid)

---

### HeightMap
![HeightMap op](images/ops/Ops_Gl_Meshes_HeightMap.svg)

**Full Name:** `Ops.Gl.Meshes.HeightMap`
**Description:** generate a rectangular mesh where the height is defined by the luminance of an image

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **File** (String): *See documentation*
- **Extrude** (Number): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Rows** (Number: Integer): *See documentation*
- **Columns** (Number: Integer): *See documentation*
- **TexCoords Slice** (Number: Boolean): *See documentation*
- **Flat** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/bRlSDe)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HeightMap"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.HeightMap](https://cables.gl/op/Ops.Gl.Meshes.HeightMap)

---

### Helix
![Helix op](images/ops/Ops_Gl_Meshes_Helix.svg)

**Full Name:** `Ops.Gl.Meshes.Helix`
**Description:** generates a helix, spiral spline

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Draw** (Number: Boolean): *See documentation*
- **Segments** (Number): *See documentation*
- **Frequency** (Number): *See documentation*
- **Radius** (Number): *See documentation*
- **Radius End** (Number): *See documentation*
- **Height** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Points** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/CW8-I6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Helix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Helix](https://cables.gl/op/Ops.Gl.Meshes.Helix)

---

### Icosahedron_v2
![Icosahedron_v2 op](images/ops/Ops_Gl_Meshes_Icosahedron_v2.svg)

**Full Name:** `Ops.Gl.Meshes.Icosahedron_v2`
**Description:** Renders a icosahedron (polyhedron with 20 faces)

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Smooth** (Number: Boolean): *See documentation*
- **Render Mesh** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Ie6iQ6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Icosahedron_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Icosahedron_v2](https://cables.gl/op/Ops.Gl.Meshes.Icosahedron_v2)

---

### Line
![Line op](images/ops/Ops_Gl_Meshes_Line.svg)

**Full Name:** `Ops.Gl.Meshes.Line`
**Description:** Draw a line between two points

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **X 1** (Number): *See documentation*
- **Y 1** (Number): *See documentation*
- **Z 1** (Number): *See documentation*
- **X 2** (Number): *See documentation*
- **Y 2** (Number): *See documentation*
- **Z 2** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Array** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/D_eE98)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Line"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Line](https://cables.gl/op/Ops.Gl.Meshes.Line)

---

### LinesArray
![LinesArray op](images/ops/Ops_Gl_Meshes_LinesArray.svg)

**Full Name:** `Ops.Gl.Meshes.LinesArray`
**Description:** an array of lines

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Logarithmic** (Number: Boolean): *See documentation*
- **Pivot X Index** (Number: Integer): *See documentation*
- **Pivot Y Index** (Number: Integer): *See documentation*
- **Num Columns** (Number: Integer): *See documentation*
- **Num Rows** (Number: Integer): *See documentation*
- **Axis Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Point Arrays** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/oXke6r)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LinesArray"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.LinesArray](https://cables.gl/op/Ops.Gl.Meshes.LinesArray)

---

### MeshInstancerFromTexture_v3
![MeshInstancerFromTexture_v3 op](images/ops/Ops_Gl_Meshes_MeshInstancerFromTexture_v3.svg)

**Full Name:** `Ops.Gl.Meshes.MeshInstancerFromTexture_v3`
**Description:** Draw the same mesh multiple times on the GPU

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Geometry** (Object:Geometry): *See documentation*
- **Scale** (Number): *See documentation*
- **Limit Instances** (Number: Boolean): *See documentation*
- **Num Instances** (Number: Integer): *See documentation*
- **Position Texture** (Object:Texture): *See documentation*
- **Rotation Texture** (Object:Texture): *See documentation*
- **Scale Texture** (Object:Texture): *See documentation*
- **Color Texture** (Object:Texture): *See documentation*
- **TexCoord Texture** (Object:Texture): *See documentation*
- **Ignore Alpha Less Than** (Number): *See documentation*
- **Multiply Pos X** (Number): *See documentation*
- **Multiply Pos Y** (Number): *See documentation*
- **Multiply Pos Z** (Number): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*
- **Num** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/H3cEpX)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MeshInstancerFromTexture_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.MeshInstancerFromTexture_v3](https://cables.gl/op/Ops.Gl.Meshes.MeshInstancerFromTexture_v3)

---

### ParametricSurface
![ParametricSurface op](images/ops/Ops_Gl_Meshes_ParametricSurface.svg)

**Full Name:** `Ops.Gl.Meshes.ParametricSurface`
**Description:** Creates a 3d mesh from a 2d area expressions

**> Input Ports:**
- **Shapes Index** (Number: Integer): *See documentation*
- **Render** (Trigger): *See documentation*
- **U Segments** (Number: Integer): *See documentation*
- **V Segments** (Number: Integer): *See documentation*
- **Multiple Of PI - U** (Number: Boolean): *See documentation*
- **UMin** (Number): *See documentation*
- **UMax** (Number): *See documentation*
- **Displace U** (Number): *See documentation*
- **Multiple Of PI - V** (Number: Boolean): *See documentation*
- **VMin** (Number): *See documentation*
- **VMax** (Number): *See documentation*
- **Displace V** (Number): *See documentation*
- **X Function** (String): *See documentation*
- **Y Function** (String): *See documentation*
- **Z Function** (String): *See documentation*
- **Scale X** (Number): *See documentation*
- **Scale Y** (Number): *See documentation*
- **Scale Z** (Number): *See documentation*
- **Draw** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*
- **Position** (Array): *See documentation*
- **outputs the vertices of the surface** (as an xyz-Array): *See documentation*
- **Position Amount** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/TnUBsL)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ParametricSurface"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.ParametricSurface](https://cables.gl/op/Ops.Gl.Meshes.ParametricSurface)

---

### PointCloudFromArray_v2
![PointCloudFromArray_v2 op](images/ops/Ops_Gl_Meshes_PointCloudFromArray_v2.svg)

**Full Name:** `Ops.Gl.Meshes.PointCloudFromArray_v2`
**Description:** visualize an array of coordinates as points

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Positions** (Array): *See documentation*
- **Num Points** (Number: Integer): *See documentation*
- **Scramble Texcoords** (Number: Boolean): *See documentation*
- **Seed** (Number): *See documentation*
- **Texture Coordinates** (Array): *See documentation*
- **Point Sizes** (Array): *See documentation*
- **Vertex Colors** (Array): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/v8G4Wz)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointCloudFromArray_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.PointCloudFromArray_v2](https://cables.gl/op/Ops.Gl.Meshes.PointCloudFromArray_v2)

---

### PointCloudFromTexture
![PointCloudFromTexture op](images/ops/Ops_Gl_Meshes_PointCloudFromTexture.svg)

**Full Name:** `Ops.Gl.Meshes.PointCloudFromTexture`
**Description:** Visualize a RGB texture as XYZ coordinates as points

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Num Points** (Number: Integer): *See documentation*
- **Texture** (Object:Texture): *See documentation*
- **Point Size** (Object:Texture): *See documentation*
- **Normalize** (Number: Boolean): *See documentation*
- **Remove Point At 0** (Number: Boolean): *See documentation*
- **Ignore Alpha 0** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Total Points** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/bhWkpX)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointCloudFromTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.PointCloudFromTexture](https://cables.gl/op/Ops.Gl.Meshes.PointCloudFromTexture)

---

### Polyhedron_v2
![Polyhedron_v2 op](images/ops/Ops_Gl_Meshes_Polyhedron_v2.svg)

**Full Name:** `Ops.Gl.Meshes.Polyhedron_v2`
**Description:** Generate polyhedron meshes

**> Input Ports:**
- **Receipt** (String): *See documentation*

**< Output Ports:**
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/VRG6Q6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Polyhedron_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Polyhedron_v2](https://cables.gl/op/Ops.Gl.Meshes.Polyhedron_v2)

---

### Pyramid_v2
![Pyramid_v2 op](images/ops/Ops_Gl_Meshes_Pyramid_v2.svg)

**Full Name:** `Ops.Gl.Meshes.Pyramid_v2`
**Description:** render a pyramid mesh

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Width** (Number): *See documentation*
- **Length** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Smooth** (Number: Boolean): *See documentation*
- **Draw** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Y09mQ6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Pyramid_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Pyramid_v2](https://cables.gl/op/Ops.Gl.Meshes.Pyramid_v2)

---

### QuadWarpTexture
![QuadWarpTexture op](images/ops/Ops_Gl_Meshes_QuadWarpTexture.svg)

**Full Name:** `Ops.Gl.Meshes.QuadWarpTexture`
**Description:** Warp a texture mapped quad (projection mapping)

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **A X** (Number): *See documentation*
- **A Y** (Number): *See documentation*
- **B X** (Number): *See documentation*
- **B Y** (Number): *See documentation*
- **C X** (Number): *See documentation*
- **C Y** (Number): *See documentation*
- **D X** (Number): *See documentation*
- **D Y** (Number): *See documentation*
- **Flip Y** (Number: Boolean): *See documentation*
- **Flip X** (Number: Boolean): *See documentation*
- **Texture** (Object): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/T2A7zp)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "QuadWarpTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.QuadWarpTexture](https://cables.gl/op/Ops.Gl.Meshes.QuadWarpTexture)

---

### Rectangle9Slice
![Rectangle9Slice op](images/ops/Ops_Gl_Meshes_Rectangle9Slice.svg)

**Full Name:** `Ops.Gl.Meshes.Rectangle9Slice`
**Description:** nine slice image format texture mapped rectangle

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Border Width** (Number): *See documentation*
- **Scale X** (Number): *See documentation*
- **Scale Y** (Number): *See documentation*
- **Draw** (Number: Boolean): *See documentation*
- **Pivot X Index** (Number: Integer): *See documentation*
- **Pivot Y Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/WkQpIG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Rectangle9Slice"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Rectangle9Slice](https://cables.gl/op/Ops.Gl.Meshes.Rectangle9Slice)

---

### RectangleFrame_v2
![RectangleFrame_v2 op](images/ops/Ops_Gl_Meshes_RectangleFrame_v2.svg)

**Full Name:** `Ops.Gl.Meshes.RectangleFrame_v2`
**Description:** Draws a rectangle frame

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Thickness** (Number): *See documentation*
- **Draw Top** (Number: Boolean): *See documentation*
- **Draw Bottom** (Number: Boolean): *See documentation*
- **Draw Left** (Number: Boolean): *See documentation*
- **Draw Right** (Number: Boolean): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/HLViQ6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RectangleFrame_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.RectangleFrame_v2](https://cables.gl/op/Ops.Gl.Meshes.RectangleFrame_v2)

---

### RectangleRounded_v2
![RectangleRounded_v2 op](images/ops/Ops_Gl_Meshes_RectangleRounded_v2.svg)

**Full Name:** `Ops.Gl.Meshes.RectangleRounded_v2`
**Description:** Draws a rectangle with rounded corners

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Segments** (Number: Integer): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Border Radius** (Number): *See documentation*
- **Top Left** (Number: Boolean): *See documentation*
- **Top Right** (Number: Boolean): *See documentation*
- **Bottom Left** (Number: Boolean): *See documentation*
- **Bottom Right** (Number: Boolean): *See documentation*
- **Draw** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/1la6mJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RectangleRounded_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.RectangleRounded_v2](https://cables.gl/op/Ops.Gl.Meshes.RectangleRounded_v2)

---

### SimpleSpline_v2
![SimpleSpline_v2 op](images/ops/Ops_Gl_Meshes_SimpleSpline_v2.svg)

**Full Name:** `Ops.Gl.Meshes.SimpleSpline_v2`
**Description:** Draws a simple spline only one pixel wide

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Points** (Array): *See documentation*
- **Num Points** (Number: Integer): *See documentation*
- **Line Strip** (Number: Boolean): *See documentation*
- **TexCoords Array** (Array): *See documentation*
- **Vertex Colors** (Array): *See documentation*

**< Output Ports:**
- **Geometry** (Object): *See documentation*
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/qRD7W6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SimpleSpline_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.SimpleSpline_v2](https://cables.gl/op/Ops.Gl.Meshes.SimpleSpline_v2)

---

### SimpleWireframe
![SimpleWireframe op](images/ops/Ops_Gl_Meshes_SimpleWireframe.svg)

**Full Name:** `Ops.Gl.Meshes.SimpleWireframe`
**Description:** Simple Wireframe Line Renderer

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Geometry** (Object:Geometry): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/gt0cay)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SimpleWireframe"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.SimpleWireframe](https://cables.gl/op/Ops.Gl.Meshes.SimpleWireframe)

---

### SplineMesh_v2
![SplineMesh_v2 op](images/ops/Ops_Gl_Meshes_SplineMesh_v2.svg)

**Full Name:** `Ops.Gl.Meshes.SplineMesh_v2`
**Description:** draw splines/lines

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Points** (Array): *See documentation*
- **Tesselate Edges** (Number: Boolean): *See documentation*
- **Render Mesh** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/3l5Uu-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SplineMesh_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.SplineMesh_v2](https://cables.gl/op/Ops.Gl.Meshes.SplineMesh_v2)

---

### SplineMeshMaterial_v2
![SplineMeshMaterial_v2 op](images/ops/Ops_Gl_Meshes_SplineMeshMaterial_v2.svg)

**Full Name:** `Ops.Gl.Meshes.SplineMeshMaterial_v2`
**Description:** material for splinemesh

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Width** (Number): *See documentation*
- **Width Perspective** (Number: Boolean): *See documentation*
- **Texture** (Object:Texture): *See documentation*
- **Texture Mask** (Object:Texture): *See documentation*
- **Mapping Index** (Number: Integer): *See documentation*
- **Mapping** (String): *See documentation*
- **Colorize Texture** (Number: Boolean): *See documentation*
- **Offset** (Number): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Shader** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/tnUJta)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SplineMeshMaterial_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.SplineMeshMaterial_v2](https://cables.gl/op/Ops.Gl.Meshes.SplineMeshMaterial_v2)

---

### TextMesh_v2
![TextMesh_v2 op](images/ops/Ops_Gl_Meshes_TextMesh_v2.svg)

**Full Name:** `Ops.Gl.Meshes.TextMesh_v2`
**Description:** Draws text in 3d space using one of the font ops

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Text** (String): *See documentation*
- **Scale Text** (Number): *See documentation*
- **Line Scale** (Number): *See documentation*
- **Font** (String): *See documentation*
- **Align Index** (Number: Integer): *See documentation*
- **Vertical Align Index** (Number: Integer): *See documentation*
- **Line Height** (Number): *See documentation*
- **Letter Spacing** (Number): *See documentation*
- **Texture Color** (Object:Texture): *See documentation*
- **Texture Mask** (Object:Texture): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Total Lines** (Number): *See documentation*
- **Width** (Number): *See documentation*
- **Font Available** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/LzDnH-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextMesh_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.TextMesh_v2](https://cables.gl/op/Ops.Gl.Meshes.TextMesh_v2)

---

### Torus_v3
![Torus_v3 op](images/ops/Ops_Gl_Meshes_Torus_v3.svg)

**Full Name:** `Ops.Gl.Meshes.Torus_v3`
**Description:** Draw a torus (doughnut, donut, ring mesh)

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Sides** (Number): *See documentation*
- **Rings** (Number): *See documentation*
- **InnerRadius** (Number): *See documentation*
- **OuterRadius** (Number): *See documentation*
- **Render Mesh** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ECMhQ6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Torus_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Torus_v3](https://cables.gl/op/Ops.Gl.Meshes.Torus_v3)

---

### TriangleSphere
![TriangleSphere op](images/ops/Ops_Gl_Meshes_TriangleSphere.svg)

**Full Name:** `Ops.Gl.Meshes.TriangleSphere`
**Description:** A sphere mesh with uniform distributed vertices

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Iterations** (Number): *See documentation*
- **Flat** (Number: Boolean): *See documentation*
- **Draw** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/T43V0D)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriangleSphere"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.TriangleSphere](https://cables.gl/op/Ops.Gl.Meshes.TriangleSphere)

---

