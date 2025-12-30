# Ops.Gl.Meshes

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.Meshes

### ComposingGridOverlay
![ComposingGridOverlay op](images/ops/Ops_Gl_Meshes_ComposingGridOverlay.svg)

**Full Name:** `Ops.Gl.Meshes.ComposingGridOverlay`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.ComposingGridOverlay) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Scale** (Number)
- **Show Center** (Number: Boolean)

**< Output Ports:**
- *Visit [Ops.Gl.Meshes.ComposingGridOverlay documentation](https://cables.gl/op/Ops.Gl.Meshes.ComposingGridOverlay) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.ComposingGridOverlay#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ComposingGridOverlay"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.ComposingGridOverlay](https://cables.gl/op/Ops.Gl.Meshes.ComposingGridOverlay)

---

### Cone
![Cone op](images/ops/Ops_Gl_Meshes_Cone.svg)

**Full Name:** `Ops.Gl.Meshes.Cone`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.Cone) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Slices** (Number)
- **Stacks** (Number)
- **Radius** (Number)
- **Height** (Number)
- **Active** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.Cone#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Cone"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Cone](https://cables.gl/op/Ops.Gl.Meshes.Cone)

---

### Corner
![Corner op](images/ops/Ops_Gl_Meshes_Corner.svg)

**Full Name:** `Ops.Gl.Meshes.Corner`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.Corner) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Width** (Number)
- **Height** (Number)
- **Thickness** (Number)
- **Draw** (Number: Boolean)
- **Pivot X Index** (Number: Integer)
- **Pivot Y Index** (Number: Integer)

**< Output Ports:**
- **Trigger** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.Corner#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Corner"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Corner](https://cables.gl/op/Ops.Gl.Meshes.Corner)

---

### Cylinder_v2
![Cylinder_v2 op](images/ops/Ops_Gl_Meshes_Cylinder_v2.svg)

**Full Name:** `Ops.Gl.Meshes.Cylinder_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.Cylinder_v2) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Render Mesh** (Number: Boolean)
- **Segments** (Number: Integer)
- **Stacks** (Number: Integer)
- **Length** (Number)
- **Outer Radius** (Number)
- **Inner Radius** (Number)
- **Flip Mapping** (Number: Boolean)
- **Caps** (Number: Boolean)
- **Flat Normals** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.Cylinder_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Cylinder_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Cylinder_v2](https://cables.gl/op/Ops.Gl.Meshes.Cylinder_v2)

---

### FloorGrid
![FloorGrid op](images/ops/Ops_Gl_Meshes_FloorGrid.svg)

**Full Name:** `Ops.Gl.Meshes.FloorGrid`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.FloorGrid) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Active** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.FloorGrid#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FloorGrid"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.FloorGrid](https://cables.gl/op/Ops.Gl.Meshes.FloorGrid)

---

### FreeFormPlane
![FreeFormPlane op](images/ops/Ops_Gl_Meshes_FreeFormPlane.svg)

**Full Name:** `Ops.Gl.Meshes.FreeFormPlane`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.FreeFormPlane) for details*

**> Input Ports:**
- **Render** (Trigger)
- **X 1** (Number)
- **Y 1** (Number)
- **Z 1** (Number)
- **X 2** (Number)
- **Y 2** (Number)
- **Z 2** (Number)
- **X 3** (Number)
- **Y 3** (Number)
- **Z 3** (Number)
- **X 4** (Number)
- **Y 4** (Number)
- **Z 4** (Number)
- **Tc X 1** (Number)
- **Tc Y 1** (Number)
- **Tc X 2** (Number)
- **Tc Y 2** (Number)
- **Tc X 3** (Number)
- **Tc Y 3** (Number)
- **Tc X 4** (Number)
- **Tc Y 4** (Number)

**< Output Ports:**
- **Trigger** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.FreeFormPlane#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FreeFormPlane"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.FreeFormPlane](https://cables.gl/op/Ops.Gl.Meshes.FreeFormPlane)

---

### FullscreenRectangle_v2
![FullscreenRectangle_v2 op](images/ops/Ops_Gl_Meshes_FullscreenRectangle_v2.svg)

**Full Name:** `Ops.Gl.Meshes.FullscreenRectangle_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.FullscreenRectangle_v2) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Flip Y** (Number: Boolean)
- **Flip X** (Number: Boolean)
- **Texture** (Object:Texture)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.FullscreenRectangle_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FullscreenRectangle_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.FullscreenRectangle_v2](https://cables.gl/op/Ops.Gl.Meshes.FullscreenRectangle_v2)

---

### GeometryToTexture_v3
![GeometryToTexture_v3 op](images/ops/Ops_Gl_Meshes_GeometryToTexture_v3.svg)

**Full Name:** `Ops.Gl.Meshes.GeometryToTexture_v3`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.GeometryToTexture_v3) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Geometry** (Object:Geometry)
- **Continously Update** (Number: Boolean)
- **Order Index** (Number: Integer)
- **Content Index** (Number: Integer)
- **New Size** (Number)
- **Tex Width** (Number: Integer)
- **Filter Index** (Number: Integer)
- **Wrap Index** (Number: Integer)
- **Pixel Format Index** (Number: Integer)
- **Color Texture** (Object:Texture)

**< Output Ports:**
- **Next** (Trigger)
- **Total Vertices** (Number)
- **Texture** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.GeometryToTexture_v3#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryToTexture_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.GeometryToTexture_v3](https://cables.gl/op/Ops.Gl.Meshes.GeometryToTexture_v3)

---

### Grid
![Grid op](images/ops/Ops_Gl_Meshes_Grid.svg)

**Full Name:** `Ops.Gl.Meshes.Grid`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.Grid) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Num** (Number: Integer)
- **Spacing** (Number)
- **Center** (Number: Boolean)
- **Axis Index** (Number: Integer)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.Grid#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Grid"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Grid](https://cables.gl/op/Ops.Gl.Meshes.Grid)

---

### HeightMap
![HeightMap op](images/ops/Ops_Gl_Meshes_HeightMap.svg)

**Full Name:** `Ops.Gl.Meshes.HeightMap`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.HeightMap) for details*

**> Input Ports:**
- **Render** (Trigger)
- **File** (String)
- **Extrude** (Number)
- **Width** (Number)
- **Height** (Number)
- **Rows** (Number: Integer)
- **Columns** (Number: Integer)
- **TexCoords Slice** (Number: Boolean)
- **Flat** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.HeightMap#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HeightMap"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.HeightMap](https://cables.gl/op/Ops.Gl.Meshes.HeightMap)

---

### Helix
![Helix op](images/ops/Ops_Gl_Meshes_Helix.svg)

**Full Name:** `Ops.Gl.Meshes.Helix`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.Helix) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Draw** (Number: Boolean)
- **Segments** (Number)
- **Frequency** (Number)
- **Radius** (Number)
- **Radius End** (Number)
- **Height** (Number)

**< Output Ports:**
- **Next** (Trigger)
- **Points** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.Helix#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Helix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Helix](https://cables.gl/op/Ops.Gl.Meshes.Helix)

---

### Icosahedron_v2
![Icosahedron_v2 op](images/ops/Ops_Gl_Meshes_Icosahedron_v2.svg)

**Full Name:** `Ops.Gl.Meshes.Icosahedron_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.Icosahedron_v2) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Smooth** (Number: Boolean)
- **Render Mesh** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.Icosahedron_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Icosahedron_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Icosahedron_v2](https://cables.gl/op/Ops.Gl.Meshes.Icosahedron_v2)

---

### Line
![Line op](images/ops/Ops_Gl_Meshes_Line.svg)

**Full Name:** `Ops.Gl.Meshes.Line`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.Line) for details*

**> Input Ports:**
- **Render** (Trigger)
- **X 1** (Number)
- **Y 1** (Number)
- **Z 1** (Number)
- **X 2** (Number)
- **Y 2** (Number)
- **Z 2** (Number)

**< Output Ports:**
- **Next** (Trigger)
- **Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.Line#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Line"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Line](https://cables.gl/op/Ops.Gl.Meshes.Line)

---

### LinesArray
![LinesArray op](images/ops/Ops_Gl_Meshes_LinesArray.svg)

**Full Name:** `Ops.Gl.Meshes.LinesArray`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.LinesArray) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Width** (Number)
- **Height** (Number)
- **Logarithmic** (Number: Boolean)
- **Pivot X Index** (Number: Integer)
- **Pivot Y Index** (Number: Integer)
- **Num Columns** (Number: Integer)
- **Num Rows** (Number: Integer)
- **Axis Index** (Number: Integer)

**< Output Ports:**
- **Trigger** (Trigger)
- **Point Arrays** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.LinesArray#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LinesArray"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.LinesArray](https://cables.gl/op/Ops.Gl.Meshes.LinesArray)

---

### MeshInstancerFromTexture_v3
![MeshInstancerFromTexture_v3 op](images/ops/Ops_Gl_Meshes_MeshInstancerFromTexture_v3.svg)

**Full Name:** `Ops.Gl.Meshes.MeshInstancerFromTexture_v3`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.MeshInstancerFromTexture_v3) for details*

**> Input Ports:**
- **Exe** (Trigger)
- **Geometry** (Object:Geometry)
- **Scale** (Number)
- **Limit Instances** (Number: Boolean)
- **Num Instances** (Number: Integer)
- **Position Texture** (Object:Texture)
- **Rotation Texture** (Object:Texture)
- **Scale Texture** (Object:Texture)
- **Color Texture** (Object:Texture)
- **TexCoord Texture** (Object:Texture)
- **Ignore Alpha Less Than** (Number)
- **Multiply Pos X** (Number)
- **Multiply Pos Y** (Number)
- **Multiply Pos Z** (Number)

**< Output Ports:**
- **Trigger Out** (Trigger)
- **Num** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.MeshInstancerFromTexture_v3#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MeshInstancerFromTexture_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.MeshInstancerFromTexture_v3](https://cables.gl/op/Ops.Gl.Meshes.MeshInstancerFromTexture_v3)

---

### ParametricSurface
![ParametricSurface op](images/ops/Ops_Gl_Meshes_ParametricSurface.svg)

**Full Name:** `Ops.Gl.Meshes.ParametricSurface`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.ParametricSurface) for details*

**> Input Ports:**
- **Shapes Index** (Number: Integer)
- **Render** (Trigger)
- **U Segments** (Number: Integer)
- **V Segments** (Number: Integer)
- **Multiple Of PI - U** (Number: Boolean)
- **UMin** (Number)
- **UMax** (Number)
- **Displace U** (Number)
- **Multiple Of PI - V** (Number: Boolean)
- **VMin** (Number)
- **VMax** (Number)
- **Displace V** (Number)
- **X Function** (String)
- **Y Function** (String)
- **Z Function** (String)
- **Scale X** (Number)
- **Scale Y** (Number)
- **Scale Z** (Number)
- **Draw** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)
- **Geometry** (Object)
- **Position** (Array)
- **outputs the vertices of the surface** (as an xyz-Array)
- **Position Amount** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.ParametricSurface#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ParametricSurface"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.ParametricSurface](https://cables.gl/op/Ops.Gl.Meshes.ParametricSurface)

---

### PointCloudFromArray_v2
![PointCloudFromArray_v2 op](images/ops/Ops_Gl_Meshes_PointCloudFromArray_v2.svg)

**Full Name:** `Ops.Gl.Meshes.PointCloudFromArray_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.PointCloudFromArray_v2) for details*

**> Input Ports:**
- **Exe** (Trigger)
- **Positions** (Array)
- **Num Points** (Number: Integer)
- **Scramble Texcoords** (Number: Boolean)
- **Seed** (Number)
- **Texture Coordinates** (Array)
- **Point Sizes** (Array)
- **Vertex Colors** (Array)

**< Output Ports:**
- **Trigger Out** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.PointCloudFromArray_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointCloudFromArray_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.PointCloudFromArray_v2](https://cables.gl/op/Ops.Gl.Meshes.PointCloudFromArray_v2)

---

### PointCloudFromTexture
![PointCloudFromTexture op](images/ops/Ops_Gl_Meshes_PointCloudFromTexture.svg)

**Full Name:** `Ops.Gl.Meshes.PointCloudFromTexture`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.PointCloudFromTexture) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Num Points** (Number: Integer)
- **Texture** (Object:Texture)
- **Point Size** (Object:Texture)
- **Normalize** (Number: Boolean)
- **Remove Point At 0** (Number: Boolean)
- **Ignore Alpha 0** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)
- **Total Points** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.PointCloudFromTexture#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointCloudFromTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.PointCloudFromTexture](https://cables.gl/op/Ops.Gl.Meshes.PointCloudFromTexture)

---

### Polyhedron_v2
![Polyhedron_v2 op](images/ops/Ops_Gl_Meshes_Polyhedron_v2.svg)

**Full Name:** `Ops.Gl.Meshes.Polyhedron_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.Polyhedron_v2) for details*

**> Input Ports:**
- **Receipt** (String)

**< Output Ports:**
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.Polyhedron_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Polyhedron_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Polyhedron_v2](https://cables.gl/op/Ops.Gl.Meshes.Polyhedron_v2)

---

### Pyramid_v2
![Pyramid_v2 op](images/ops/Ops_Gl_Meshes_Pyramid_v2.svg)

**Full Name:** `Ops.Gl.Meshes.Pyramid_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.Pyramid_v2) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Width** (Number)
- **Length** (Number)
- **Height** (Number)
- **Smooth** (Number: Boolean)
- **Draw** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.Pyramid_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Pyramid_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Pyramid_v2](https://cables.gl/op/Ops.Gl.Meshes.Pyramid_v2)

---

### QuadWarpTexture
![QuadWarpTexture op](images/ops/Ops_Gl_Meshes_QuadWarpTexture.svg)

**Full Name:** `Ops.Gl.Meshes.QuadWarpTexture`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.QuadWarpTexture) for details*

**> Input Ports:**
- **Render** (Trigger)
- **A X** (Number)
- **A Y** (Number)
- **B X** (Number)
- **B Y** (Number)
- **C X** (Number)
- **C Y** (Number)
- **D X** (Number)
- **D Y** (Number)
- **Flip Y** (Number: Boolean)
- **Flip X** (Number: Boolean)
- **Texture** (Object)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.QuadWarpTexture#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "QuadWarpTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.QuadWarpTexture](https://cables.gl/op/Ops.Gl.Meshes.QuadWarpTexture)

---

### Rectangle9Slice
![Rectangle9Slice op](images/ops/Ops_Gl_Meshes_Rectangle9Slice.svg)

**Full Name:** `Ops.Gl.Meshes.Rectangle9Slice`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.Rectangle9Slice) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Width** (Number)
- **Height** (Number)
- **Border Width** (Number)
- **Scale X** (Number)
- **Scale Y** (Number)
- **Draw** (Number: Boolean)
- **Pivot X Index** (Number: Integer)
- **Pivot Y Index** (Number: Integer)

**< Output Ports:**
- **Trigger** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.Rectangle9Slice#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Rectangle9Slice"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Rectangle9Slice](https://cables.gl/op/Ops.Gl.Meshes.Rectangle9Slice)

---

### RectangleFrame_v2
![RectangleFrame_v2 op](images/ops/Ops_Gl_Meshes_RectangleFrame_v2.svg)

**Full Name:** `Ops.Gl.Meshes.RectangleFrame_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.RectangleFrame_v2) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Width** (Number)
- **Height** (Number)
- **Thickness** (Number)
- **Draw Top** (Number: Boolean)
- **Draw Bottom** (Number: Boolean)
- **Draw Left** (Number: Boolean)
- **Draw Right** (Number: Boolean)
- **Active** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.RectangleFrame_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RectangleFrame_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.RectangleFrame_v2](https://cables.gl/op/Ops.Gl.Meshes.RectangleFrame_v2)

---

### RectangleRounded_v2
![RectangleRounded_v2 op](images/ops/Ops_Gl_Meshes_RectangleRounded_v2.svg)

**Full Name:** `Ops.Gl.Meshes.RectangleRounded_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.RectangleRounded_v2) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Segments** (Number: Integer)
- **Width** (Number)
- **Height** (Number)
- **Border Radius** (Number)
- **Top Left** (Number: Boolean)
- **Top Right** (Number: Boolean)
- **Bottom Left** (Number: Boolean)
- **Bottom Right** (Number: Boolean)
- **Draw** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.RectangleRounded_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RectangleRounded_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.RectangleRounded_v2](https://cables.gl/op/Ops.Gl.Meshes.RectangleRounded_v2)

---

### SimpleSpline_v2
![SimpleSpline_v2 op](images/ops/Ops_Gl_Meshes_SimpleSpline_v2.svg)

**Full Name:** `Ops.Gl.Meshes.SimpleSpline_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.SimpleSpline_v2) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Points** (Array)
- **Num Points** (Number: Integer)
- **Line Strip** (Number: Boolean)
- **TexCoords Array** (Array)
- **Vertex Colors** (Array)

**< Output Ports:**
- **Geometry** (Object)
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.SimpleSpline_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SimpleSpline_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.SimpleSpline_v2](https://cables.gl/op/Ops.Gl.Meshes.SimpleSpline_v2)

---

### SimpleWireframe
![SimpleWireframe op](images/ops/Ops_Gl_Meshes_SimpleWireframe.svg)

**Full Name:** `Ops.Gl.Meshes.SimpleWireframe`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.SimpleWireframe) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Geometry** (Object:Geometry)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.SimpleWireframe#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SimpleWireframe"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.SimpleWireframe](https://cables.gl/op/Ops.Gl.Meshes.SimpleWireframe)

---

### SplineMesh_v2
![SplineMesh_v2 op](images/ops/Ops_Gl_Meshes_SplineMesh_v2.svg)

**Full Name:** `Ops.Gl.Meshes.SplineMesh_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.SplineMesh_v2) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Points** (Array)
- **Tesselate Edges** (Number: Boolean)
- **Render Mesh** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.SplineMesh_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SplineMesh_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.SplineMesh_v2](https://cables.gl/op/Ops.Gl.Meshes.SplineMesh_v2)

---

### SplineMeshMaterial_v2
![SplineMeshMaterial_v2 op](images/ops/Ops_Gl_Meshes_SplineMeshMaterial_v2.svg)

**Full Name:** `Ops.Gl.Meshes.SplineMeshMaterial_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.SplineMeshMaterial_v2) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Width** (Number)
- **Width Perspective** (Number: Boolean)
- **Texture** (Object:Texture)
- **Texture Mask** (Object:Texture)
- **Mapping Index** (Number: Integer)
- **Mapping** (String)
- **Colorize Texture** (Number: Boolean)
- **Offset** (Number)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)

**< Output Ports:**
- **Trigger** (Trigger)
- **Shader** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.SplineMeshMaterial_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SplineMeshMaterial_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.SplineMeshMaterial_v2](https://cables.gl/op/Ops.Gl.Meshes.SplineMeshMaterial_v2)

---

### TextMesh_v2
![TextMesh_v2 op](images/ops/Ops_Gl_Meshes_TextMesh_v2.svg)

**Full Name:** `Ops.Gl.Meshes.TextMesh_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.TextMesh_v2) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Text** (String)
- **Scale Text** (Number)
- **Line Scale** (Number)
- **Font** (String)
- **Align Index** (Number: Integer)
- **Vertical Align Index** (Number: Integer)
- **Line Height** (Number)
- **Letter Spacing** (Number)
- **Texture Color** (Object:Texture)
- **Texture Mask** (Object:Texture)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)

**< Output Ports:**
- **Next** (Trigger)
- **Total Lines** (Number)
- **Width** (Number)
- **Font Available** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.TextMesh_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextMesh_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.TextMesh_v2](https://cables.gl/op/Ops.Gl.Meshes.TextMesh_v2)

---

### Torus_v3
![Torus_v3 op](images/ops/Ops_Gl_Meshes_Torus_v3.svg)

**Full Name:** `Ops.Gl.Meshes.Torus_v3`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.Torus_v3) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Sides** (Number)
- **Rings** (Number)
- **InnerRadius** (Number)
- **OuterRadius** (Number)
- **Render Mesh** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.Torus_v3#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Torus_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.Torus_v3](https://cables.gl/op/Ops.Gl.Meshes.Torus_v3)

---

### TriangleSphere
![TriangleSphere op](images/ops/Ops_Gl_Meshes_TriangleSphere.svg)

**Full Name:** `Ops.Gl.Meshes.TriangleSphere`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Meshes.TriangleSphere) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Iterations** (Number)
- **Flat** (Number: Boolean)
- **Draw** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Meshes.TriangleSphere#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriangleSphere"*
**Docs:** [https://cables.gl/op/Ops.Gl.Meshes.TriangleSphere](https://cables.gl/op/Ops.Gl.Meshes.TriangleSphere)

---

