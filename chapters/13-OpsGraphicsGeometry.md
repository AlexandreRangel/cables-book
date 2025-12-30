# Ops.Graphics.Geometry

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Graphics.Geometry

### AlignGeometry
![AlignGeometry op](images/ops/Ops_Graphics_Geometry_AlignGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.AlignGeometry`
**Description:** align a geometry / change its pivot / center / origin point

**> Input Ports:**
- **Geometry** (Object): *See documentation*
- **X Index** (Number: Integer): *See documentation*
- **Y Index** (Number: Integer): *See documentation*
- **Z Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/FbXQ-G)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AlignGeometry"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.AlignGeometry](https://cables.gl/op/Ops.Graphics.Geometry.AlignGeometry)

---

### BoundingBox
![BoundingBox op](images/ops/Ops_Graphics_Geometry_BoundingBox.svg)

**Full Name:** `Ops.Graphics.Geometry.BoundingBox`
**Description:** create a simple bounding box from width,height,depth

**> Input Ports:**
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Depth** (Number): *See documentation*

**< Output Ports:**
- **Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.BoundingBox#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BoundingBox"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.BoundingBox](https://cables.gl/op/Ops.Graphics.Geometry.BoundingBox)

---

### CalculateNormals
![CalculateNormals op](images/ops/Ops_Graphics_Geometry_CalculateNormals.svg)

**Full Name:** `Ops.Graphics.Geometry.CalculateNormals`
**Description:** calculate normals of a geometry

**> Input Ports:**
- **Geometry** (Object): *See documentation*
- **Smooth** (Number: Boolean): *See documentation*
- **Force Z Up** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Geometry Out** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.CalculateNormals#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CalculateNormals"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.CalculateNormals](https://cables.gl/op/Ops.Graphics.Geometry.CalculateNormals)

---

### DivideGeometry
![DivideGeometry op](images/ops/Ops_Graphics_Geometry_DivideGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.DivideGeometry`
**Description:** disconnect faces/polygons of a mesh

**> Input Ports:**
- **Geometry** (Object): *See documentation*

**< Output Ports:**
- **Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/sYIxm1)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DivideGeometry"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.DivideGeometry](https://cables.gl/op/Ops.Graphics.Geometry.DivideGeometry)

---

### FlipNormals
![FlipNormals op](images/ops/Ops_Graphics_Geometry_FlipNormals.svg)

**Full Name:** `Ops.Graphics.Geometry.FlipNormals`
**Description:** flip all normals of a geometry

**> Input Ports:**
- **Geometry** (Object): *See documentation*
- **Flip** (Number: Boolean): *See documentation*
- **Normalize** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/cTfoii)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FlipNormals"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.FlipNormals](https://cables.gl/op/Ops.Graphics.Geometry.FlipNormals)

---

### FreezeMeshes
![FreezeMeshes op](images/ops/Ops_Graphics_Geometry_FreezeMeshes.svg)

**Full Name:** `Ops.Graphics.Geometry.FreezeMeshes`
**Description:** capture all following meshes into one geometry

**> Input Ports:**
- **Capture** (Trigger): *See documentation*

**< Output Ports:**
- **Geometry** (Object): *See documentation*
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/BwxY2f)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FreezeMeshes"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.FreezeMeshes](https://cables.gl/op/Ops.Graphics.Geometry.FreezeMeshes)

---

### GeometryAttributes
![GeometryAttributes op](images/ops/Ops_Graphics_Geometry_GeometryAttributes.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryAttributes`
**Description:** Get vertices of a geometry as array3x (vertex vertices)

**> Input Ports:**
- **Geometry** (Object): *See documentation*

**< Output Ports:**
- **Faces** (Array): *See documentation*
- **Vertices** (Array): *See documentation*
- **Normals** (Array): *See documentation*
- **TexCoords** (Array): *See documentation*
- **Vertex Colors** (Array): *See documentation*
- **Tangents** (Array): *See documentation*
- **BiTangents** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/4VpJz6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryAttributes"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryAttributes](https://cables.gl/op/Ops.Graphics.Geometry.GeometryAttributes)

---

### GeometryExtrude
![GeometryExtrude op](images/ops/Ops_Graphics_Geometry_GeometryExtrude.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryExtrude`
**Description:** basic extrusion of flat geometry

**> Input Ports:**
- **Geometry** (Object:Geometry): *See documentation*
- **Height** (Number): *See documentation*
- **Smooth** (Number: Boolean): *See documentation*
- **Walls** (Number: Boolean): *See documentation*
- **Top** (Number: Boolean): *See documentation*
- **Bottom** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Result Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Cp5VS3)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryExtrude"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryExtrude](https://cables.gl/op/Ops.Graphics.Geometry.GeometryExtrude)

---

### GeometryFromArrays
![GeometryFromArrays op](images/ops/Ops_Graphics_Geometry_GeometryFromArrays.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryFromArrays`
**Description:** Create a geometry from array data

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Vertices** (Array): *See documentation*
- **Faces** (Array): *See documentation*
- **Texture Coords** (Array): *See documentation*
- **Normals** (Array): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/isWvii)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryFromArrays"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryFromArrays](https://cables.gl/op/Ops.Graphics.Geometry.GeometryFromArrays)

---

### GeometryInfo
![GeometryInfo op](images/ops/Ops_Graphics_Geometry_GeometryInfo.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryInfo`
**Description:** information about a geometry

**> Input Ports:**
- **Geometry** (Object:Geometry): *See documentation*

**< Output Ports:**
- **Indexed** (Number): *See documentation*
- **Faces** (Number): *See documentation*
- **Indices** (Number): *See documentation*
- **Vertices** (Number): *See documentation*
- **Normals** (Number): *See documentation*
- **TexCoords** (Number): *See documentation*
- **Tangents** (Number): *See documentation*
- **BiTangents** (Number): *See documentation*
- **VertexColors** (Number): *See documentation*
- **Other Attributes** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.GeometryInfo#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryInfo"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryInfo](https://cables.gl/op/Ops.Graphics.Geometry.GeometryInfo)

---

### GeometryMerge
![GeometryMerge op](images/ops/Ops_Graphics_Geometry_GeometryMerge.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryMerge`
**Description:** merge two geometries to one

**> Input Ports:**
- **Geometry** (Object): *See documentation*
- **Geometry 2** (Object): *See documentation*
- **Merge** (Trigger): *See documentation*
- **Reset** (Trigger): *See documentation*

**< Output Ports:**
- **Geometry Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/3rCDz6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryMerge"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryMerge](https://cables.gl/op/Ops.Graphics.Geometry.GeometryMerge)

---

### GeometryToObj
![GeometryToObj op](images/ops/Ops_Graphics_Geometry_GeometryToObj.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryToObj`
**Description:** Generate an .obj file as string from a geometry

**> Input Ports:**
- **Geometry** (Object:Geometry): *See documentation*

**< Output Ports:**
- **Obj** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/BwxY2f)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryToObj"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryToObj](https://cables.gl/op/Ops.Graphics.Geometry.GeometryToObj)

---

### GeometryToWireframeArray3
![GeometryToWireframeArray3 op](images/ops/Ops_Graphics_Geometry_GeometryToWireframeArray3.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryToWireframeArray3`
**Description:** generate an array of lines from a mesh to render a wireframe

**> Input Ports:**
- **Geometry** (Object): *See documentation*

**< Output Ports:**
- **Array** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/r--xve)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryToWireframeArray3"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryToWireframeArray3](https://cables.gl/op/Ops.Graphics.Geometry.GeometryToWireframeArray3)

---

### GeometryUnIndex
![GeometryUnIndex op](images/ops/Ops_Graphics_Geometry_GeometryUnIndex.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryUnIndex`
**Description:** convert geometry to only flat triangles without reusing vertices positions

**> Input Ports:**
- **Geometry** (Object:Geometry): *See documentation*

**< Output Ports:**
- **Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.GeometryUnIndex#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryUnIndex"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryUnIndex](https://cables.gl/op/Ops.Graphics.Geometry.GeometryUnIndex)

---

### ObjGeometry
![ObjGeometry op](images/ops/Ops_Graphics_Geometry_ObjGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.ObjGeometry`
**Description:** parse an obj string to a geometry object

**> Input Ports:**
- **Obj** (String): *See documentation*

**< Output Ports:**
- **Geometry** (Object): *See documentation*
- **Status** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/JeA8ck)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjGeometry"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.ObjGeometry](https://cables.gl/op/Ops.Graphics.Geometry.ObjGeometry)

---

### RandomizeTriangles
![RandomizeTriangles op](images/ops/Ops_Graphics_Geometry_RandomizeTriangles.svg)

**Full Name:** `Ops.Graphics.Geometry.RandomizeTriangles`
**Description:** randomize order of triangles in a geometry

**> Input Ports:**
- **Geometry** (Object): *See documentation*
- **Seed** (Number): *See documentation*

**< Output Ports:**
- **Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/gLrrJV)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RandomizeTriangles"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.RandomizeTriangles](https://cables.gl/op/Ops.Graphics.Geometry.RandomizeTriangles)

---

### ReverseVertices
![ReverseVertices op](images/ops/Ops_Graphics_Geometry_ReverseVertices.svg)

**Full Name:** `Ops.Graphics.Geometry.ReverseVertices`
**Description:** Reverses the order of vertices in a geometry, back facing triangles become front facing ones

**> Input Ports:**
- **Geometry** (Object): *See documentation*
- **Flip** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/u9N6v4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ReverseVertices"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.ReverseVertices](https://cables.gl/op/Ops.Graphics.Geometry.ReverseVertices)

---

### ScaleGeometry
![ScaleGeometry op](images/ops/Ops_Graphics_Geometry_ScaleGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.ScaleGeometry`
**Description:** uniform scaling of geometry vertices

**> Input Ports:**
- **Geometry** (Object): *See documentation*
- **Scale** (Number): *See documentation*

**< Output Ports:**
- **Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.ScaleGeometry#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScaleGeometry"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.ScaleGeometry](https://cables.gl/op/Ops.Graphics.Geometry.ScaleGeometry)

---

### SortGeometryAxis
![SortGeometryAxis op](images/ops/Ops_Graphics_Geometry_SortGeometryAxis.svg)

**Full Name:** `Ops.Graphics.Geometry.SortGeometryAxis`
**Description:** sort geometry triangles by position

**> Input Ports:**
- **Geometry** (Object): *See documentation*
- **Sort Index** (Number: Integer): *See documentation*
- **Reverse** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.SortGeometryAxis#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SortGeometryAxis"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.SortGeometryAxis](https://cables.gl/op/Ops.Graphics.Geometry.SortGeometryAxis)

---

### SvgPathToGeometry_v2
![SvgPathToGeometry_v2 op](images/ops/Ops_Graphics_Geometry_SvgPathToGeometry_v2.svg)

**Full Name:** `Ops.Graphics.Geometry.SvgPathToGeometry_v2`
**Description:** Generate a SVG path string of a string using an opentype font

**> Input Ports:**
- **SVG Path** (String): *See documentation*
- **Bezier Stepsize** (Number): *See documentation*
- **Rescale** (Number): *See documentation*

**< Output Ports:**
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Cp5VS3)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SvgPathToGeometry_v2"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.SvgPathToGeometry_v2](https://cables.gl/op/Ops.Graphics.Geometry.SvgPathToGeometry_v2)

---

### TesselateGeometry
![TesselateGeometry op](images/ops/Ops_Graphics_Geometry_TesselateGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.TesselateGeometry`
**Description:** create new triangles in a mesh (subdivide)

**> Input Ports:**
- **Geometry** (Object): *See documentation*
- **Iterations** (Number: Integer): *See documentation*

**< Output Ports:**
- **Result** (Object): *See documentation*
- **Num Vertices** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/gLrrJV)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TesselateGeometry"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.TesselateGeometry](https://cables.gl/op/Ops.Graphics.Geometry.TesselateGeometry)

---

### TransformGeometry
![TransformGeometry op](images/ops/Ops_Graphics_Geometry_TransformGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.TransformGeometry`
**Description:** transform vertices of geometry

**> Input Ports:**
- **Geometry** (Object): *See documentation*
- **Translate X** (Number): *See documentation*
- **Translate Y** (Number): *See documentation*
- **Translate Z** (Number): *See documentation*
- **Scale X** (Number): *See documentation*
- **Scale Y** (Number): *See documentation*
- **Scale Z** (Number): *See documentation*
- **Rotation X** (Number): *See documentation*
- **Rotation Y** (Number): *See documentation*
- **Rotation Z** (Number): *See documentation*

**< Output Ports:**
- **Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/aoBFz6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TransformGeometry"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.TransformGeometry](https://cables.gl/op/Ops.Graphics.Geometry.TransformGeometry)

---

### TriangleArrayToGeometry_v2
![TriangleArrayToGeometry_v2 op](images/ops/Ops_Graphics_Geometry_TriangleArrayToGeometry_v2.svg)

**Full Name:** `Ops.Graphics.Geometry.TriangleArrayToGeometry_v2`
**Description:** Draws multiple triangles using coordinates from an array

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Points** (Array): *See documentation*
- **Vertex Colors** (Array): *See documentation*
- **TexCoords** (Array): *See documentation*
- **Flat** (Number: Boolean): *See documentation*
- **Render Mesh** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/0fnxrc)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriangleArrayToGeometry_v2"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.TriangleArrayToGeometry_v2](https://cables.gl/op/Ops.Graphics.Geometry.TriangleArrayToGeometry_v2)

---

### Triangulate2dPath
![Triangulate2dPath op](images/ops/Ops_Graphics_Geometry_Triangulate2dPath.svg)

**Full Name:** `Ops.Graphics.Geometry.Triangulate2dPath`
**Description:** Triangulate a 2d path to a flat and filled 3d geometry

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Combine Index** (Number: Integer): *See documentation*
- **Path 2** (Array): *See documentation*
- **Path 3** (Array): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/LzTAeT)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Triangulate2dPath"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.Triangulate2dPath](https://cables.gl/op/Ops.Graphics.Geometry.Triangulate2dPath)

---

