# Ops.Graphics.Geometry

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Graphics.Geometry

### AlignGeometry
![AlignGeometry op](images/ops/Ops_Graphics_Geometry_AlignGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.AlignGeometry`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.AlignGeometry) for details*

**> Input Ports:**
- **Geometry** (Object)
- **X Index** (Number: Integer)
- **Y Index** (Number: Integer)
- **Z Index** (Number: Integer)

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.AlignGeometry#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AlignGeometry"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.AlignGeometry](https://cables.gl/op/Ops.Graphics.Geometry.AlignGeometry)

---

### BoundingBox
![BoundingBox op](images/ops/Ops_Graphics_Geometry_BoundingBox.svg)

**Full Name:** `Ops.Graphics.Geometry.BoundingBox`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.BoundingBox) for details*

**> Input Ports:**
- **Width** (Number)
- **Height** (Number)
- **Depth** (Number)

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.BoundingBox#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BoundingBox"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.BoundingBox](https://cables.gl/op/Ops.Graphics.Geometry.BoundingBox)

---

### CalculateNormals
![CalculateNormals op](images/ops/Ops_Graphics_Geometry_CalculateNormals.svg)

**Full Name:** `Ops.Graphics.Geometry.CalculateNormals`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.CalculateNormals) for details*

**> Input Ports:**
- **Geometry** (Object)
- **Smooth** (Number: Boolean)
- **Force Z Up** (Number: Boolean)

**< Output Ports:**
- **Geometry Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.CalculateNormals#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CalculateNormals"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.CalculateNormals](https://cables.gl/op/Ops.Graphics.Geometry.CalculateNormals)

---

### DivideGeometry
![DivideGeometry op](images/ops/Ops_Graphics_Geometry_DivideGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.DivideGeometry`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.DivideGeometry) for details*

**> Input Ports:**
- **Geometry** (Object)

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.DivideGeometry#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DivideGeometry"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.DivideGeometry](https://cables.gl/op/Ops.Graphics.Geometry.DivideGeometry)

---

### FlipNormals
![FlipNormals op](images/ops/Ops_Graphics_Geometry_FlipNormals.svg)

**Full Name:** `Ops.Graphics.Geometry.FlipNormals`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.FlipNormals) for details*

**> Input Ports:**
- **Geometry** (Object)
- **Flip** (Number: Boolean)
- **Normalize** (Number: Boolean)

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.FlipNormals#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FlipNormals"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.FlipNormals](https://cables.gl/op/Ops.Graphics.Geometry.FlipNormals)

---

### FreezeMeshes
![FreezeMeshes op](images/ops/Ops_Graphics_Geometry_FreezeMeshes.svg)

**Full Name:** `Ops.Graphics.Geometry.FreezeMeshes`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.FreezeMeshes) for details*

**> Input Ports:**
- **Capture** (Trigger)

**< Output Ports:**
- **Geometry** (Object)
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.FreezeMeshes#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FreezeMeshes"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.FreezeMeshes](https://cables.gl/op/Ops.Graphics.Geometry.FreezeMeshes)

---

### GeometryAttributes
![GeometryAttributes op](images/ops/Ops_Graphics_Geometry_GeometryAttributes.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryAttributes`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.GeometryAttributes) for details*

**> Input Ports:**
- **Geometry** (Object)

**< Output Ports:**
- **Faces** (Array)
- **Vertices** (Array)
- **Normals** (Array)
- **TexCoords** (Array)
- **Vertex Colors** (Array)
- **Tangents** (Array)
- **BiTangents** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.GeometryAttributes#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryAttributes"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryAttributes](https://cables.gl/op/Ops.Graphics.Geometry.GeometryAttributes)

---

### GeometryExtrude
![GeometryExtrude op](images/ops/Ops_Graphics_Geometry_GeometryExtrude.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryExtrude`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.GeometryExtrude) for details*

**> Input Ports:**
- **Geometry** (Object:Geometry)
- **Height** (Number)
- **Smooth** (Number: Boolean)
- **Walls** (Number: Boolean)
- **Top** (Number: Boolean)
- **Bottom** (Number: Boolean)

**< Output Ports:**
- **Result Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.GeometryExtrude#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryExtrude"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryExtrude](https://cables.gl/op/Ops.Graphics.Geometry.GeometryExtrude)

---

### GeometryFromArrays
![GeometryFromArrays op](images/ops/Ops_Graphics_Geometry_GeometryFromArrays.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryFromArrays`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.GeometryFromArrays) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Vertices** (Array)
- **Faces** (Array)
- **Texture Coords** (Array)
- **Normals** (Array)

**< Output Ports:**
- **Next** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.GeometryFromArrays#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryFromArrays"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryFromArrays](https://cables.gl/op/Ops.Graphics.Geometry.GeometryFromArrays)

---

### GeometryInfo
![GeometryInfo op](images/ops/Ops_Graphics_Geometry_GeometryInfo.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryInfo`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.GeometryInfo) for details*

**> Input Ports:**
- **Geometry** (Object:Geometry)

**< Output Ports:**
- **Indexed** (Number)
- **Faces** (Number)
- **Indices** (Number)
- **Vertices** (Number)
- **Normals** (Number)
- **TexCoords** (Number)
- **Tangents** (Number)
- **BiTangents** (Number)
- **VertexColors** (Number)
- **Other Attributes** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.GeometryInfo#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryInfo"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryInfo](https://cables.gl/op/Ops.Graphics.Geometry.GeometryInfo)

---

### GeometryMerge
![GeometryMerge op](images/ops/Ops_Graphics_Geometry_GeometryMerge.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryMerge`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.GeometryMerge) for details*

**> Input Ports:**
- **Geometry** (Object)
- **Geometry 2** (Object)
- **Merge** (Trigger)
- **Reset** (Trigger)

**< Output Ports:**
- **Geometry Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.GeometryMerge#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryMerge"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryMerge](https://cables.gl/op/Ops.Graphics.Geometry.GeometryMerge)

---

### GeometryToObj
![GeometryToObj op](images/ops/Ops_Graphics_Geometry_GeometryToObj.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryToObj`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.GeometryToObj) for details*

**> Input Ports:**
- **Geometry** (Object:Geometry)

**< Output Ports:**
- **Obj** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.GeometryToObj#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryToObj"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryToObj](https://cables.gl/op/Ops.Graphics.Geometry.GeometryToObj)

---

### GeometryToWireframeArray3
![GeometryToWireframeArray3 op](images/ops/Ops_Graphics_Geometry_GeometryToWireframeArray3.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryToWireframeArray3`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.GeometryToWireframeArray3) for details*

**> Input Ports:**
- **Geometry** (Object)

**< Output Ports:**
- **Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.GeometryToWireframeArray3#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryToWireframeArray3"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryToWireframeArray3](https://cables.gl/op/Ops.Graphics.Geometry.GeometryToWireframeArray3)

---

### GeometryUnIndex
![GeometryUnIndex op](images/ops/Ops_Graphics_Geometry_GeometryUnIndex.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryUnIndex`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.GeometryUnIndex) for details*

**> Input Ports:**
- **Geometry** (Object:Geometry)

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.GeometryUnIndex#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryUnIndex"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryUnIndex](https://cables.gl/op/Ops.Graphics.Geometry.GeometryUnIndex)

---

### ObjGeometry
![ObjGeometry op](images/ops/Ops_Graphics_Geometry_ObjGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.ObjGeometry`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.ObjGeometry) for details*

**> Input Ports:**
- **Obj** (String)

**< Output Ports:**
- **Geometry** (Object)
- **Status** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.ObjGeometry#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjGeometry"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.ObjGeometry](https://cables.gl/op/Ops.Graphics.Geometry.ObjGeometry)

---

### RandomizeTriangles
![RandomizeTriangles op](images/ops/Ops_Graphics_Geometry_RandomizeTriangles.svg)

**Full Name:** `Ops.Graphics.Geometry.RandomizeTriangles`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.RandomizeTriangles) for details*

**> Input Ports:**
- **Geometry** (Object)
- **Seed** (Number)

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.RandomizeTriangles#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RandomizeTriangles"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.RandomizeTriangles](https://cables.gl/op/Ops.Graphics.Geometry.RandomizeTriangles)

---

### ReverseVertices
![ReverseVertices op](images/ops/Ops_Graphics_Geometry_ReverseVertices.svg)

**Full Name:** `Ops.Graphics.Geometry.ReverseVertices`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.ReverseVertices) for details*

**> Input Ports:**
- **Geometry** (Object)
- **Flip** (Number: Boolean)

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.ReverseVertices#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ReverseVertices"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.ReverseVertices](https://cables.gl/op/Ops.Graphics.Geometry.ReverseVertices)

---

### ScaleGeometry
![ScaleGeometry op](images/ops/Ops_Graphics_Geometry_ScaleGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.ScaleGeometry`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.ScaleGeometry) for details*

**> Input Ports:**
- **Geometry** (Object)
- **Scale** (Number)

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.ScaleGeometry#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScaleGeometry"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.ScaleGeometry](https://cables.gl/op/Ops.Graphics.Geometry.ScaleGeometry)

---

### SortGeometryAxis
![SortGeometryAxis op](images/ops/Ops_Graphics_Geometry_SortGeometryAxis.svg)

**Full Name:** `Ops.Graphics.Geometry.SortGeometryAxis`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.SortGeometryAxis) for details*

**> Input Ports:**
- **Geometry** (Object)
- **Sort Index** (Number: Integer)
- **Reverse** (Number: Boolean)

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.SortGeometryAxis#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SortGeometryAxis"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.SortGeometryAxis](https://cables.gl/op/Ops.Graphics.Geometry.SortGeometryAxis)

---

### SvgPathToGeometry_v2
![SvgPathToGeometry_v2 op](images/ops/Ops_Graphics_Geometry_SvgPathToGeometry_v2.svg)

**Full Name:** `Ops.Graphics.Geometry.SvgPathToGeometry_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.SvgPathToGeometry_v2) for details*

**> Input Ports:**
- **SVG Path** (String)
- **Bezier Stepsize** (Number)
- **Rescale** (Number)

**< Output Ports:**
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.SvgPathToGeometry_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SvgPathToGeometry_v2"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.SvgPathToGeometry_v2](https://cables.gl/op/Ops.Graphics.Geometry.SvgPathToGeometry_v2)

---

### TesselateGeometry
![TesselateGeometry op](images/ops/Ops_Graphics_Geometry_TesselateGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.TesselateGeometry`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.TesselateGeometry) for details*

**> Input Ports:**
- **Geometry** (Object)
- **Iterations** (Number: Integer)

**< Output Ports:**
- **Result** (Object)
- **Num Vertices** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.TesselateGeometry#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TesselateGeometry"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.TesselateGeometry](https://cables.gl/op/Ops.Graphics.Geometry.TesselateGeometry)

---

### TransformGeometry
![TransformGeometry op](images/ops/Ops_Graphics_Geometry_TransformGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.TransformGeometry`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.TransformGeometry) for details*

**> Input Ports:**
- **Geometry** (Object)
- **Translate X** (Number)
- **Translate Y** (Number)
- **Translate Z** (Number)
- **Scale X** (Number)
- **Scale Y** (Number)
- **Scale Z** (Number)
- **Rotation X** (Number)
- **Rotation Y** (Number)
- **Rotation Z** (Number)

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.TransformGeometry#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TransformGeometry"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.TransformGeometry](https://cables.gl/op/Ops.Graphics.Geometry.TransformGeometry)

---

### TriangleArrayToGeometry_v2
![TriangleArrayToGeometry_v2 op](images/ops/Ops_Graphics_Geometry_TriangleArrayToGeometry_v2.svg)

**Full Name:** `Ops.Graphics.Geometry.TriangleArrayToGeometry_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.TriangleArrayToGeometry_v2) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Points** (Array)
- **Vertex Colors** (Array)
- **TexCoords** (Array)
- **Flat** (Number: Boolean)
- **Render Mesh** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.TriangleArrayToGeometry_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriangleArrayToGeometry_v2"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.TriangleArrayToGeometry_v2](https://cables.gl/op/Ops.Graphics.Geometry.TriangleArrayToGeometry_v2)

---

### Triangulate2dPath
![Triangulate2dPath op](images/ops/Ops_Graphics_Geometry_Triangulate2dPath.svg)

**Full Name:** `Ops.Graphics.Geometry.Triangulate2dPath`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Geometry.Triangulate2dPath) for details*

**> Input Ports:**
- **Update** (Trigger)
- **Combine Index** (Number: Integer)
- **Path 2** (Array)
- **Path 3** (Array)

**< Output Ports:**
- **Next** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.Triangulate2dPath#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Triangulate2dPath"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.Triangulate2dPath](https://cables.gl/op/Ops.Graphics.Geometry.Triangulate2dPath)

---

