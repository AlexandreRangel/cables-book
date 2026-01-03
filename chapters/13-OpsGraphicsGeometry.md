# Ops.Graphics.Geometry

---

## Ops.Graphics.Geometry

### AlignGeometry
![AlignGeometry op](images/ops/Ops_Graphics_Geometry_AlignGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.AlignGeometry`

**Description:** align a geometry / change its pivot / center / origin point

**> Input Ports:**

- **Geometry** (Object)
- **X Index** (Number: Integer)
- **Y Index** (Number: Integer)
- **Z Index** (Number: Integer)

**< Output Ports:**

- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/FbXQ-G)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AlignGeometry"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.AlignGeometry](https://cables.gl/op/Ops.Graphics.Geometry.AlignGeometry)


### BoundingBox
![BoundingBox op](images/ops/Ops_Graphics_Geometry_BoundingBox.svg)

**Full Name:** `Ops.Graphics.Geometry.BoundingBox`

**Description:** create a simple bounding box from width,height,depth

**> Input Ports:**

- **Width** (Number)
- **Height** (Number)
- **Depth** (Number)

**< Output Ports:**

- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.BoundingBox#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BoundingBox"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.BoundingBox](https://cables.gl/op/Ops.Graphics.Geometry.BoundingBox)


### CalculateNormals
![CalculateNormals op](images/ops/Ops_Graphics_Geometry_CalculateNormals.svg)

**Full Name:** `Ops.Graphics.Geometry.CalculateNormals`

**Description:** calculate normals of a geometry

**> Input Ports:**

- **Geometry** (Object)
- **Smooth** (Number: Boolean)
- **Force Z Up** (Number: Boolean)

**< Output Ports:**

- **Geometry Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.CalculateNormals#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CalculateNormals"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.CalculateNormals](https://cables.gl/op/Ops.Graphics.Geometry.CalculateNormals)


### DivideGeometry
![DivideGeometry op](images/ops/Ops_Graphics_Geometry_DivideGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.DivideGeometry`

**Description:** disconnect faces/polygons of a mesh

**> Input Ports:**

- **Geometry** (Object)

**< Output Ports:**

- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/sYIxm1)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DivideGeometry"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.DivideGeometry](https://cables.gl/op/Ops.Graphics.Geometry.DivideGeometry)


### FlipNormals
![FlipNormals op](images/ops/Ops_Graphics_Geometry_FlipNormals.svg)

**Full Name:** `Ops.Graphics.Geometry.FlipNormals`

**Description:** flip all normals of a geometry

**> Input Ports:**

- **Geometry** (Object)
- **Flip** (Number: Boolean)
- **Normalize** (Number: Boolean)

**< Output Ports:**

- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/cTfoii)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FlipNormals"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.FlipNormals](https://cables.gl/op/Ops.Graphics.Geometry.FlipNormals)


### FreezeMeshes
![FreezeMeshes op](images/ops/Ops_Graphics_Geometry_FreezeMeshes.svg)

**Full Name:** `Ops.Graphics.Geometry.FreezeMeshes`

**Description:** capture all following meshes into one geometry

**> Input Ports:**

- **Capture** (Trigger)

**< Output Ports:**

- **Geometry** (Object)
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/BwxY2f)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FreezeMeshes"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.FreezeMeshes](https://cables.gl/op/Ops.Graphics.Geometry.FreezeMeshes)


### GeometryAttributes
![GeometryAttributes op](images/ops/Ops_Graphics_Geometry_GeometryAttributes.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryAttributes`

**Description:** Get vertices of a geometry as array3x (vertex vertices)

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

**Example Patch:** [Open in Editor](https://cables.gl/edit/4VpJz6)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryAttributes"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryAttributes](https://cables.gl/op/Ops.Graphics.Geometry.GeometryAttributes)


### GeometryExtrude
![GeometryExtrude op](images/ops/Ops_Graphics_Geometry_GeometryExtrude.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryExtrude`

**Description:** basic extrusion of flat geometry

**> Input Ports:**

- **Geometry** (Object:Geometry)
- **Height** (Number)
- **Smooth** (Number: Boolean)
- **Walls** (Number: Boolean)
- **Top** (Number: Boolean)
- **Bottom** (Number: Boolean)

**< Output Ports:**

- **Result Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Cp5VS3)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryExtrude"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryExtrude](https://cables.gl/op/Ops.Graphics.Geometry.GeometryExtrude)


### GeometryFromArrays
![GeometryFromArrays op](images/ops/Ops_Graphics_Geometry_GeometryFromArrays.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryFromArrays`

**Description:** Create a geometry from array data

**> Input Ports:**

- **Render** (Trigger)
- **Vertices** (Array)
- **Faces** (Array)
- **Texture Coords** (Array)
- **Normals** (Array)

**< Output Ports:**

- **Next** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/isWvii)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryFromArrays"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryFromArrays](https://cables.gl/op/Ops.Graphics.Geometry.GeometryFromArrays)


### GeometryInfo
![GeometryInfo op](images/ops/Ops_Graphics_Geometry_GeometryInfo.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryInfo`

**Description:** information about a geometry

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


### GeometryMerge
![GeometryMerge op](images/ops/Ops_Graphics_Geometry_GeometryMerge.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryMerge`

**Description:** merge two geometries to one

**> Input Ports:**

- **Geometry** (Object)
- **Geometry 2** (Object)
- **Merge** (Trigger)
- **Reset** (Trigger)

**< Output Ports:**

- **Geometry Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/3rCDz6)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryMerge"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryMerge](https://cables.gl/op/Ops.Graphics.Geometry.GeometryMerge)


### GeometryToObj
![GeometryToObj op](images/ops/Ops_Graphics_Geometry_GeometryToObj.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryToObj`

**Description:** Generate an .obj file as string from a geometry

**> Input Ports:**

- **Geometry** (Object:Geometry)

**< Output Ports:**

- **Obj** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/BwxY2f)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryToObj"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryToObj](https://cables.gl/op/Ops.Graphics.Geometry.GeometryToObj)


### GeometryToWireframeArray3
![GeometryToWireframeArray3 op](images/ops/Ops_Graphics_Geometry_GeometryToWireframeArray3.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryToWireframeArray3`

**Description:** generate an array of lines from a mesh to render a wireframe

**> Input Ports:**

- **Geometry** (Object)

**< Output Ports:**

- **Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/r--xve)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryToWireframeArray3"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryToWireframeArray3](https://cables.gl/op/Ops.Graphics.Geometry.GeometryToWireframeArray3)


### GeometryUnIndex
![GeometryUnIndex op](images/ops/Ops_Graphics_Geometry_GeometryUnIndex.svg)

**Full Name:** `Ops.Graphics.Geometry.GeometryUnIndex`

**Description:** convert geometry to only flat triangles without reusing vertices positions

**> Input Ports:**

- **Geometry** (Object:Geometry)

**< Output Ports:**

- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.GeometryUnIndex#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryUnIndex"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.GeometryUnIndex](https://cables.gl/op/Ops.Graphics.Geometry.GeometryUnIndex)


### ObjGeometry
![ObjGeometry op](images/ops/Ops_Graphics_Geometry_ObjGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.ObjGeometry`

**Description:** parse an obj string to a geometry object

**> Input Ports:**

- **Obj** (String)

**< Output Ports:**

- **Geometry** (Object)
- **Status** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/JeA8ck)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjGeometry"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.ObjGeometry](https://cables.gl/op/Ops.Graphics.Geometry.ObjGeometry)


### RandomizeTriangles
![RandomizeTriangles op](images/ops/Ops_Graphics_Geometry_RandomizeTriangles.svg)

**Full Name:** `Ops.Graphics.Geometry.RandomizeTriangles`

**Description:** randomize order of triangles in a geometry

**> Input Ports:**

- **Geometry** (Object)
- **Seed** (Number)

**< Output Ports:**

- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/gLrrJV)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RandomizeTriangles"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.RandomizeTriangles](https://cables.gl/op/Ops.Graphics.Geometry.RandomizeTriangles)


### ReverseVertices
![ReverseVertices op](images/ops/Ops_Graphics_Geometry_ReverseVertices.svg)

**Full Name:** `Ops.Graphics.Geometry.ReverseVertices`

**Description:** Reverses the order of vertices in a geometry, back facing triangles become front facing ones

**> Input Ports:**

- **Geometry** (Object)
- **Flip** (Number: Boolean)

**< Output Ports:**

- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/u9N6v4)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ReverseVertices"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.ReverseVertices](https://cables.gl/op/Ops.Graphics.Geometry.ReverseVertices)


### ScaleGeometry
![ScaleGeometry op](images/ops/Ops_Graphics_Geometry_ScaleGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.ScaleGeometry`

**Description:** uniform scaling of geometry vertices

**> Input Ports:**

- **Geometry** (Object)
- **Scale** (Number)

**< Output Ports:**

- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.ScaleGeometry#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScaleGeometry"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.ScaleGeometry](https://cables.gl/op/Ops.Graphics.Geometry.ScaleGeometry)


### SortGeometryAxis
![SortGeometryAxis op](images/ops/Ops_Graphics_Geometry_SortGeometryAxis.svg)

**Full Name:** `Ops.Graphics.Geometry.SortGeometryAxis`

**Description:** sort geometry triangles by position

**> Input Ports:**

- **Geometry** (Object)
- **Sort Index** (Number: Integer)
- **Reverse** (Number: Boolean)

**< Output Ports:**

- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Geometry.SortGeometryAxis#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SortGeometryAxis"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.SortGeometryAxis](https://cables.gl/op/Ops.Graphics.Geometry.SortGeometryAxis)


### SvgPathToGeometry_v2
![SvgPathToGeometry_v2 op](images/ops/Ops_Graphics_Geometry_SvgPathToGeometry_v2.svg)

**Full Name:** `Ops.Graphics.Geometry.SvgPathToGeometry_v2`

**Description:** Generate a SVG path string of a string using an opentype font

**> Input Ports:**

- **SVG Path** (String)
- **Bezier Stepsize** (Number)
- **Rescale** (Number)

**< Output Ports:**

- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Cp5VS3)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SvgPathToGeometry_v2"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.SvgPathToGeometry_v2](https://cables.gl/op/Ops.Graphics.Geometry.SvgPathToGeometry_v2)


### TesselateGeometry
![TesselateGeometry op](images/ops/Ops_Graphics_Geometry_TesselateGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.TesselateGeometry`

**Description:** create new triangles in a mesh (subdivide)

**> Input Ports:**

- **Geometry** (Object)
- **Iterations** (Number: Integer)

**< Output Ports:**

- **Result** (Object)
- **Num Vertices** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/gLrrJV)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TesselateGeometry"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.TesselateGeometry](https://cables.gl/op/Ops.Graphics.Geometry.TesselateGeometry)


### TransformGeometry
![TransformGeometry op](images/ops/Ops_Graphics_Geometry_TransformGeometry.svg)

**Full Name:** `Ops.Graphics.Geometry.TransformGeometry`

**Description:** transform vertices of geometry

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

**Example Patch:** [Open in Editor](https://cables.gl/edit/aoBFz6)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TransformGeometry"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.TransformGeometry](https://cables.gl/op/Ops.Graphics.Geometry.TransformGeometry)


### TriangleArrayToGeometry_v2
![TriangleArrayToGeometry_v2 op](images/ops/Ops_Graphics_Geometry_TriangleArrayToGeometry_v2.svg)

**Full Name:** `Ops.Graphics.Geometry.TriangleArrayToGeometry_v2`

**Description:** Draws multiple triangles using coordinates from an array

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

**Example Patch:** [Open in Editor](https://cables.gl/edit/0fnxrc)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriangleArrayToGeometry_v2"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.TriangleArrayToGeometry_v2](https://cables.gl/op/Ops.Graphics.Geometry.TriangleArrayToGeometry_v2)


### Triangulate2dPath
![Triangulate2dPath op](images/ops/Ops_Graphics_Geometry_Triangulate2dPath.svg)

**Full Name:** `Ops.Graphics.Geometry.Triangulate2dPath`

**Description:** Triangulate a 2d path to a flat and filled 3d geometry

**> Input Ports:**

- **Update** (Trigger)
- **Combine Index** (Number: Integer)
- **Path 2** (Array)
- **Path 3** (Array)

**< Output Ports:**

- **Next** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/LzTAeT)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Triangulate2dPath"*

**Docs:** [https://cables.gl/op/Ops.Graphics.Geometry.Triangulate2dPath](https://cables.gl/op/Ops.Graphics.Geometry.Triangulate2dPath)


