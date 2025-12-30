# Ops.Array.PointArray

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Array.PointArray

### Array3AreaRemove
![Array3AreaRemove op](images/ops/Ops_Array_PointArray_Array3AreaRemove.svg)

**Full Name:** `Ops.Array.PointArray.Array3AreaRemove`
**Description:** Remove points from an array3 with different shapes

**> Input Ports:**
- **In Trigger** (Trigger): *See documentation*
- **In Array** (Array): *See documentation*
- **Mode Index** (Number: Integer): *See documentation*
- **Size** (Number): *See documentation*
- **Invert** (Number: Boolean): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**< Output Ports:**
- **Out Trigger** (Trigger): *See documentation*
- **Out Array** (Array): *See documentation*
- **Array Length** (Number): *See documentation*
- **Out X** (Number): *See documentation*
- **Out Y** (Number): *See documentation*
- **Out Z** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/sfikWi)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3AreaRemove"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.Array3AreaRemove](https://cables.gl/op/Ops.Array.PointArray.Array3AreaRemove)

---

### Array3PointEditor
![Array3PointEditor op](images/ops/Ops_Array_PointArray_Array3PointEditor.svg)

**Full Name:** `Ops.Array.PointArray.Array3PointEditor`
**Description:** Visually edit positions in an array of point coordinates

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Total Points** (Number: Integer): *See documentation*
- **Edit** (Number: Boolean): *See documentation*
- **Index** (Number: Integer): *See documentation*
- **Copy From Index** (Number: Integer): *See documentation*
- **Copy Coordinates** (Trigger): *See documentation*
- **Reset** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Coordinates** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/2Bhet7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3PointEditor"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.Array3PointEditor](https://cables.gl/op/Ops.Array.PointArray.Array3PointEditor)

---

### Array3RepeatTransform
![Array3RepeatTransform op](images/ops/Ops_Array_PointArray_Array3RepeatTransform.svg)

**Full Name:** `Ops.Array.PointArray.Array3RepeatTransform`
**Description:** Repeat an array by transforming it x times

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **Array** (Array): *See documentation*
- **Times** (Number: Integer): *See documentation*
- **Translate X** (Number): *See documentation*
- **Translate Y** (Number): *See documentation*
- **Translate Z** (Number): *See documentation*
- **Scale X** (Number): *See documentation*
- **Scale Y** (Number): *See documentation*
- **Scale Z** (Number): *See documentation*
- **Rotation X** (Number): *See documentation*
- **Rotation Y** (Number): *See documentation*
- **Rotation Z** (Number): *See documentation*
- **Position Array** (Array): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Result** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/9nSWVj)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3RepeatTransform"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.Array3RepeatTransform](https://cables.gl/op/Ops.Array.PointArray.Array3RepeatTransform)

---

### Array3VectorDistance
![Array3VectorDistance op](images/ops/Ops_Array_PointArray_Array3VectorDistance.svg)

**Full Name:** `Ops.Array.PointArray.Array3VectorDistance`
**Description:** Return the distance between 2 points from an array

**> Input Ports:**
- **Array In 1** (Array): *See documentation*
- **Array In 2** (Array): *See documentation*

**< Output Ports:**
- **Array Out** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Tbb8xN)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3VectorDistance"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.Array3VectorDistance](https://cables.gl/op/Ops.Array.PointArray.Array3VectorDistance)

---

### ArraySpray
![ArraySpray op](images/ops/Ops_Array_PointArray_ArraySpray.svg)

**Full Name:** `Ops.Array.PointArray.ArraySpray`
**Description:** Particle spray simulation

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Time** (Number): *See documentation*
- **Num** (Number): *See documentation*
- **Size X** (Number): *See documentation*
- **Size Y** (Number): *See documentation*
- **Size Z** (Number): *See documentation*
- **Movement X** (Number): *See documentation*
- **Movement Y** (Number): *See documentation*
- **Movement Z** (Number): *See documentation*
- **Center X** (Number: Boolean): *See documentation*
- **Center Y** (Number: Boolean): *See documentation*
- **Center Z** (Number: Boolean): *See documentation*
- **Reset** (Trigger): *See documentation*
- **Lifetime** (Number): *See documentation*
- **Lifetime Minimum** (Number): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*
- **Positions** (Array): *See documentation*
- **Lifetime** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/hY5lAw)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArraySpray"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.ArraySpray](https://cables.gl/op/Ops.Array.PointArray.ArraySpray)

---

### CircularPoints_v2
![CircularPoints_v2 op](images/ops/Ops_Array_PointArray_CircularPoints_v2.svg)

**Full Name:** `Ops.Array.PointArray.CircularPoints_v2`
**Description:** Create arrays for circular shapes, helix, circle, etc.

**> Input Ports:**
- **Radius** (Number): *See documentation*
- **Round Segments** (Number): *See documentation*
- **Rounds** (Number): *See documentation*
- **Radius Add Round** (Number): *See documentation*
- **Radius Add Point** (Number): *See documentation*
- **Offset** (Number): *See documentation*
- **Point Offset XY** (Number): *See documentation*
- **Point Offset Z** (Number): *See documentation*
- **Offset Rotation** (Number): *See documentation*
- **Loop** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Points** (Array): *See documentation*
- **Rotation** (Array): *See documentation*
- **Total Points** (Number): *See documentation*
- **Array Lengths** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/V34dYh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CircularPoints_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.CircularPoints_v2](https://cables.gl/op/Ops.Array.PointArray.CircularPoints_v2)

---

### FillPointArrayDuplicates
![FillPointArrayDuplicates op](images/ops/Ops_Array_PointArray_FillPointArrayDuplicates.svg)

**Full Name:** `Ops.Array.PointArray.FillPointArrayDuplicates`
**Description:** Fill an XYZ array with existing duplicate points until it reaches the length

**> Input Ports:**
- **Array** (Array): *See documentation*
- **Num Elements** (Number: Integer): *See documentation*
- **Calculate** (Trigger): *See documentation*

**< Output Ports:**
- **Result** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.FillPointArrayDuplicates#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FillPointArrayDuplicates"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.FillPointArrayDuplicates](https://cables.gl/op/Ops.Array.PointArray.FillPointArrayDuplicates)

---

### PointsCube
![PointsCube op](images/ops/Ops_Array_PointArray_PointsCube.svg)

**Full Name:** `Ops.Array.PointArray.PointsCube`
**Description:** Generate a 3d point field with controllable amount of xyz points (was PointsField3d)

**> Input Ports:**
- **Num X** (Number: Integer): *See documentation*
- **Num Y** (Number: Integer): *See documentation*
- **Num Z** (Number: Integer): *See documentation*
- **Mul** (Number): *See documentation*
- **Center** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Array Out** (Array): *See documentation*
- **Total Points** (Number): *See documentation*
- **Array Length** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/_SC2JB)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointsCube"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.PointsCube](https://cables.gl/op/Ops.Array.PointArray.PointsCube)

---

### PointsHexagonGrid
![PointsHexagonGrid op](images/ops/Ops_Array_PointArray_PointsHexagonGrid.svg)

**Full Name:** `Ops.Array.PointArray.PointsHexagonGrid`
**Description:** Generate coordinates for a hexagon grid, outputs array3x

**> Input Ports:**
- **Rows** (Number: Integer): *See documentation*
- **Colums** (Number: Integer): *See documentation*
- **Hex Facing Index** (Number: Integer): *See documentation*
- **Hex Facing** (String): *See documentation*
- **Flip Corners** (Number: Boolean): *See documentation*
- **Tile X Offset** (Number): *See documentation*
- **Tile Y Offset** (Number): *See documentation*
- **Multiplier** (Number): *See documentation*

**< Output Ports:**
- **Array Out** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/GLLdrn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointsHexagonGrid"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.PointsHexagonGrid](https://cables.gl/op/Ops.Array.PointArray.PointsHexagonGrid)

---

### PointsPlane_v2
![PointsPlane_v2 op](images/ops/Ops_Array_PointArray_PointsPlane_v2.svg)

**Full Name:** `Ops.Array.PointArray.PointsPlane_v2`
**Description:** Generate coordinates for a rectangular field / grid of points

**> Input Ports:**
- **Rows** (Number: Integer): *See documentation*
- **Columns** (Number: Integer): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Row Offset** (Number): *See documentation*
- **Center** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Result** (Array): *See documentation*
- **Total Points** (Number): *See documentation*
- **Array Length** (Number): *See documentation*
- **Row Numbers** (Array): *See documentation*
- **Column Numbers** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/icchV5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointsPlane_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.PointsPlane_v2](https://cables.gl/op/Ops.Array.PointArray.PointsPlane_v2)

---

### PointsRectangle_v2
![PointsRectangle_v2 op](images/ops/Ops_Array_PointArray_PointsRectangle_v2.svg)

**Full Name:** `Ops.Array.PointArray.PointsRectangle_v2`
**Description:** Generate an array of XYZ coordinates of an rectangle

**> Input Ports:**
- **Line Strip** (Number: Boolean): *See documentation*
- **Segments** (Number: Integer): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Border Radius** (Number): *See documentation*
- **Loop** (Number: Boolean): *See documentation*
- **Top Left** (Number: Boolean): *See documentation*
- **Top Right** (Number: Boolean): *See documentation*
- **Bottom Left** (Number: Boolean): *See documentation*
- **Bottom Right** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Points** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/l1KQN8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointsRectangle_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.PointsRectangle_v2](https://cables.gl/op/Ops.Array.PointArray.PointsRectangle_v2)

---

### PointsRectangleRounded_v2
![PointsRectangleRounded_v2 op](images/ops/Ops_Array_PointArray_PointsRectangleRounded_v2.svg)

**Full Name:** `Ops.Array.PointArray.PointsRectangleRounded_v2`
**Description:** Generate an array of points of a rectangle with rounded corners

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
- **Points** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/A7nLgQ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointsRectangleRounded_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.PointsRectangleRounded_v2](https://cables.gl/op/Ops.Array.PointArray.PointsRectangleRounded_v2)

---

### PointsSphereRandom
![PointsSphereRandom op](images/ops/Ops_Array_PointArray_PointsSphereRandom.svg)

**Full Name:** `Ops.Array.PointArray.PointsSphereRandom`
**Description:** Generate a point field mapped to the surface of a sphere

**> Input Ports:**
- **Amount Of Points** (Number: Integer): *See documentation*
- **Sphere Size** (Number): *See documentation*
- **Random Seed** (Number): *See documentation*
- **Random Distance From Sphere** (Number): *See documentation*
- **Distribution Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Array Out** (Array): *See documentation*
- **Total Points** (Number): *See documentation*
- **Array Length** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/yBeQUy)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointsSphereRandom"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.PointsSphereRandom](https://cables.gl/op/Ops.Array.PointArray.PointsSphereRandom)

---

### RedistributeSplinePoints
![RedistributeSplinePoints op](images/ops/Ops_Array_PointArray_RedistributeSplinePoints.svg)

**Full Name:** `Ops.Array.PointArray.RedistributeSplinePoints`
**Description:** Recalculate a spline / change number of points of a spline

**> Input Ports:**
- **Array3x** (Array): *See documentation*
- **Num Points** (Number: Integer): *See documentation*
- **Calculate** (Trigger): *See documentation*
- **Normalized** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Result** (Array): *See documentation*
- **Spline Length** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.RedistributeSplinePoints#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RedistributeSplinePoints"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.RedistributeSplinePoints](https://cables.gl/op/Ops.Array.PointArray.RedistributeSplinePoints)

---

### SortArray3ByDistance
![SortArray3ByDistance op](images/ops/Ops_Array_PointArray_SortArray3ByDistance.svg)

**Full Name:** `Ops.Array.PointArray.SortArray3ByDistance`
**Description:** Sort an array3, by the distance of each point to the previous point

**> Input Ports:**
- **Array** (Array): *See documentation*

**< Output Ports:**
- **Result** (Array): *See documentation*
- **Result Index** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/7C6DlJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SortArray3ByDistance"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.SortArray3ByDistance](https://cables.gl/op/Ops.Array.PointArray.SortArray3ByDistance)

---

### SplinePositionAtDistanceArray3
![SplinePositionAtDistanceArray3 op](images/ops/Ops_Array_PointArray_SplinePositionAtDistanceArray3.svg)

**Full Name:** `Ops.Array.PointArray.SplinePositionAtDistanceArray3`
**Description:** Get position in array3/spline at distance from start

**> Input Ports:**
- **Calculate** (Trigger): *See documentation*
- **Array3x** (Array): *See documentation*
- **Distance** (Number): *See documentation*
- **Normalized** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **Spline Length** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/6XhHR7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SplinePositionAtDistanceArray3"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.SplinePositionAtDistanceArray3](https://cables.gl/op/Ops.Array.PointArray.SplinePositionAtDistanceArray3)

---

### SubdivideArray3_v2
![SubdivideArray3_v2 op](images/ops/Ops_Array_PointArray_SubdivideArray3_v2.svg)

**Full Name:** `Ops.Array.PointArray.SubdivideArray3_v2`
**Description:** For subdividing splines, smoothing lines using cubic bezier interpolation

**> Input Ports:**
- **Points** (Array): *See documentation*
- **Num Subdivs** (Number: Integer): *See documentation*
- **Smooth** (Number: Boolean): *See documentation*
- **Loop** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Result** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/uywtvc)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SubdivideArray3_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.SubdivideArray3_v2](https://cables.gl/op/Ops.Array.PointArray.SubdivideArray3_v2)

---

### TransformArray3
![TransformArray3 op](images/ops/Ops_Array_PointArray_TransformArray3.svg)

**Full Name:** `Ops.Array.PointArray.TransformArray3`
**Description:** Transform (translate, rotate, scale) positions in an array3x

**> Input Ports:**
- **Transform** (Trigger): *See documentation*
- **Array** (Array): *See documentation*
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
- **Next** (Trigger): *See documentation*
- **Result** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/NenSet)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TransformArray3"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.TransformArray3](https://cables.gl/op/Ops.Array.PointArray.TransformArray3)

---

