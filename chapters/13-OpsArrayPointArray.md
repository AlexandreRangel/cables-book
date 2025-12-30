# Ops.Array.PointArray

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Array.PointArray

### Array3AreaRemove
![Array3AreaRemove op](images/ops/Ops_Array_PointArray_Array3AreaRemove.svg)

**Full Name:** `Ops.Array.PointArray.Array3AreaRemove`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.Array3AreaRemove) for details*

**> Input Ports:**
- **In Trigger** (Trigger)
- **In Array** (Array)
- **Mode Index** (Number: Integer)
- **Size** (Number)
- **Invert** (Number: Boolean)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**< Output Ports:**
- **Out Trigger** (Trigger)
- **Out Array** (Array)
- **Array Length** (Number)
- **Out X** (Number)
- **Out Y** (Number)
- **Out Z** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.Array3AreaRemove#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3AreaRemove"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.Array3AreaRemove](https://cables.gl/op/Ops.Array.PointArray.Array3AreaRemove)

---

### Array3PointEditor
![Array3PointEditor op](images/ops/Ops_Array_PointArray_Array3PointEditor.svg)

**Full Name:** `Ops.Array.PointArray.Array3PointEditor`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.Array3PointEditor) for details*

**> Input Ports:**
- **Execute** (Trigger)
- **Total Points** (Number: Integer)
- **Edit** (Number: Boolean)
- **Index** (Number: Integer)
- **Copy From Index** (Number: Integer)
- **Copy Coordinates** (Trigger)
- **Reset** (Trigger)

**< Output Ports:**
- **Next** (Trigger)
- **Coordinates** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.Array3PointEditor#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3PointEditor"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.Array3PointEditor](https://cables.gl/op/Ops.Array.PointArray.Array3PointEditor)

---

### Array3RepeatTransform
![Array3RepeatTransform op](images/ops/Ops_Array_PointArray_Array3RepeatTransform.svg)

**Full Name:** `Ops.Array.PointArray.Array3RepeatTransform`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.Array3RepeatTransform) for details*

**> Input Ports:**
- **Trigger** (Trigger)
- **Array** (Array)
- **Times** (Number: Integer)
- **Translate X** (Number)
- **Translate Y** (Number)
- **Translate Z** (Number)
- **Scale X** (Number)
- **Scale Y** (Number)
- **Scale Z** (Number)
- **Rotation X** (Number)
- **Rotation Y** (Number)
- **Rotation Z** (Number)
- **Position Array** (Array)

**< Output Ports:**
- **Next** (Trigger)
- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.Array3RepeatTransform#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3RepeatTransform"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.Array3RepeatTransform](https://cables.gl/op/Ops.Array.PointArray.Array3RepeatTransform)

---

### Array3VectorDistance
![Array3VectorDistance op](images/ops/Ops_Array_PointArray_Array3VectorDistance.svg)

**Full Name:** `Ops.Array.PointArray.Array3VectorDistance`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.Array3VectorDistance) for details*

**> Input Ports:**
- **Array In 1** (Array)
- **Array In 2** (Array)

**< Output Ports:**
- **Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.Array3VectorDistance#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3VectorDistance"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.Array3VectorDistance](https://cables.gl/op/Ops.Array.PointArray.Array3VectorDistance)

---

### ArraySpray
![ArraySpray op](images/ops/Ops_Array_PointArray_ArraySpray.svg)

**Full Name:** `Ops.Array.PointArray.ArraySpray`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.ArraySpray) for details*

**> Input Ports:**
- **Exe** (Trigger)
- **Time** (Number)
- **Num** (Number)
- **Size X** (Number)
- **Size Y** (Number)
- **Size Z** (Number)
- **Movement X** (Number)
- **Movement Y** (Number)
- **Movement Z** (Number)
- **Center X** (Number: Boolean)
- **Center Y** (Number: Boolean)
- **Center Z** (Number: Boolean)
- **Reset** (Trigger)
- **Lifetime** (Number)
- **Lifetime Minimum** (Number)

**< Output Ports:**
- **Trigger Out** (Trigger)
- **Positions** (Array)
- **Lifetime** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.ArraySpray#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArraySpray"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.ArraySpray](https://cables.gl/op/Ops.Array.PointArray.ArraySpray)

---

### CircularPoints_v2
![CircularPoints_v2 op](images/ops/Ops_Array_PointArray_CircularPoints_v2.svg)

**Full Name:** `Ops.Array.PointArray.CircularPoints_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.CircularPoints_v2) for details*

**> Input Ports:**
- **Radius** (Number)
- **Round Segments** (Number)
- **Rounds** (Number)
- **Radius Add Round** (Number)
- **Radius Add Point** (Number)
- **Offset** (Number)
- **Point Offset XY** (Number)
- **Point Offset Z** (Number)
- **Offset Rotation** (Number)
- **Loop** (Number: Boolean)

**< Output Ports:**
- **Points** (Array)
- **Rotation** (Array)
- **Total Points** (Number)
- **Array Lengths** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.CircularPoints_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CircularPoints_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.CircularPoints_v2](https://cables.gl/op/Ops.Array.PointArray.CircularPoints_v2)

---

### FillPointArrayDuplicates
![FillPointArrayDuplicates op](images/ops/Ops_Array_PointArray_FillPointArrayDuplicates.svg)

**Full Name:** `Ops.Array.PointArray.FillPointArrayDuplicates`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.FillPointArrayDuplicates) for details*

**> Input Ports:**
- **Array** (Array)
- **Num Elements** (Number: Integer)
- **Calculate** (Trigger)

**< Output Ports:**
- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.FillPointArrayDuplicates#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FillPointArrayDuplicates"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.FillPointArrayDuplicates](https://cables.gl/op/Ops.Array.PointArray.FillPointArrayDuplicates)

---

### PointsCube
![PointsCube op](images/ops/Ops_Array_PointArray_PointsCube.svg)

**Full Name:** `Ops.Array.PointArray.PointsCube`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.PointsCube) for details*

**> Input Ports:**
- **Num X** (Number: Integer)
- **Num Y** (Number: Integer)
- **Num Z** (Number: Integer)
- **Mul** (Number)
- **Center** (Number: Boolean)

**< Output Ports:**
- **Array Out** (Array)
- **Total Points** (Number)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.PointsCube#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointsCube"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.PointsCube](https://cables.gl/op/Ops.Array.PointArray.PointsCube)

---

### PointsHexagonGrid
![PointsHexagonGrid op](images/ops/Ops_Array_PointArray_PointsHexagonGrid.svg)

**Full Name:** `Ops.Array.PointArray.PointsHexagonGrid`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.PointsHexagonGrid) for details*

**> Input Ports:**
- **Rows** (Number: Integer)
- **Colums** (Number: Integer)
- **Hex Facing Index** (Number: Integer)
- **Hex Facing** (String)
- **Flip Corners** (Number: Boolean)
- **Tile X Offset** (Number)
- **Tile Y Offset** (Number)
- **Multiplier** (Number)

**< Output Ports:**
- **Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.PointsHexagonGrid#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointsHexagonGrid"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.PointsHexagonGrid](https://cables.gl/op/Ops.Array.PointArray.PointsHexagonGrid)

---

### PointsPlane_v2
![PointsPlane_v2 op](images/ops/Ops_Array_PointArray_PointsPlane_v2.svg)

**Full Name:** `Ops.Array.PointArray.PointsPlane_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.PointsPlane_v2) for details*

**> Input Ports:**
- **Rows** (Number: Integer)
- **Columns** (Number: Integer)
- **Width** (Number)
- **Height** (Number)
- **Row Offset** (Number)
- **Center** (Number: Boolean)

**< Output Ports:**
- **Result** (Array)
- **Total Points** (Number)
- **Array Length** (Number)
- **Row Numbers** (Array)
- **Column Numbers** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.PointsPlane_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointsPlane_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.PointsPlane_v2](https://cables.gl/op/Ops.Array.PointArray.PointsPlane_v2)

---

### PointsRectangle_v2
![PointsRectangle_v2 op](images/ops/Ops_Array_PointArray_PointsRectangle_v2.svg)

**Full Name:** `Ops.Array.PointArray.PointsRectangle_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.PointsRectangle_v2) for details*

**> Input Ports:**
- **Line Strip** (Number: Boolean)
- **Segments** (Number: Integer)
- **Width** (Number)
- **Height** (Number)
- **Border Radius** (Number)
- **Loop** (Number: Boolean)
- **Top Left** (Number: Boolean)
- **Top Right** (Number: Boolean)
- **Bottom Left** (Number: Boolean)
- **Bottom Right** (Number: Boolean)

**< Output Ports:**
- **Points** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.PointsRectangle_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointsRectangle_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.PointsRectangle_v2](https://cables.gl/op/Ops.Array.PointArray.PointsRectangle_v2)

---

### PointsRectangleRounded_v2
![PointsRectangleRounded_v2 op](images/ops/Ops_Array_PointArray_PointsRectangleRounded_v2.svg)

**Full Name:** `Ops.Array.PointArray.PointsRectangleRounded_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.PointsRectangleRounded_v2) for details*

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
- **Points** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.PointsRectangleRounded_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointsRectangleRounded_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.PointsRectangleRounded_v2](https://cables.gl/op/Ops.Array.PointArray.PointsRectangleRounded_v2)

---

### PointsSphereRandom
![PointsSphereRandom op](images/ops/Ops_Array_PointArray_PointsSphereRandom.svg)

**Full Name:** `Ops.Array.PointArray.PointsSphereRandom`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.PointsSphereRandom) for details*

**> Input Ports:**
- **Amount Of Points** (Number: Integer)
- **Sphere Size** (Number)
- **Random Seed** (Number)
- **Random Distance From Sphere** (Number)
- **Distribution Index** (Number: Integer)

**< Output Ports:**
- **Array Out** (Array)
- **Total Points** (Number)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.PointsSphereRandom#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointsSphereRandom"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.PointsSphereRandom](https://cables.gl/op/Ops.Array.PointArray.PointsSphereRandom)

---

### RedistributeSplinePoints
![RedistributeSplinePoints op](images/ops/Ops_Array_PointArray_RedistributeSplinePoints.svg)

**Full Name:** `Ops.Array.PointArray.RedistributeSplinePoints`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.RedistributeSplinePoints) for details*

**> Input Ports:**
- **Array3x** (Array)
- **Num Points** (Number: Integer)
- **Calculate** (Trigger)
- **Normalized** (Number: Boolean)

**< Output Ports:**
- **Result** (Array)
- **Spline Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.RedistributeSplinePoints#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RedistributeSplinePoints"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.RedistributeSplinePoints](https://cables.gl/op/Ops.Array.PointArray.RedistributeSplinePoints)

---

### SortArray3ByDistance
![SortArray3ByDistance op](images/ops/Ops_Array_PointArray_SortArray3ByDistance.svg)

**Full Name:** `Ops.Array.PointArray.SortArray3ByDistance`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.SortArray3ByDistance) for details*

**> Input Ports:**
- **Array** (Array)

**< Output Ports:**
- **Result** (Array)
- **Result Index** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.SortArray3ByDistance#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SortArray3ByDistance"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.SortArray3ByDistance](https://cables.gl/op/Ops.Array.PointArray.SortArray3ByDistance)

---

### SplinePositionAtDistanceArray3
![SplinePositionAtDistanceArray3 op](images/ops/Ops_Array_PointArray_SplinePositionAtDistanceArray3.svg)

**Full Name:** `Ops.Array.PointArray.SplinePositionAtDistanceArray3`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.SplinePositionAtDistanceArray3) for details*

**> Input Ports:**
- **Calculate** (Trigger)
- **Array3x** (Array)
- **Distance** (Number)
- **Normalized** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Spline Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.SplinePositionAtDistanceArray3#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SplinePositionAtDistanceArray3"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.SplinePositionAtDistanceArray3](https://cables.gl/op/Ops.Array.PointArray.SplinePositionAtDistanceArray3)

---

### SubdivideArray3_v2
![SubdivideArray3_v2 op](images/ops/Ops_Array_PointArray_SubdivideArray3_v2.svg)

**Full Name:** `Ops.Array.PointArray.SubdivideArray3_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.SubdivideArray3_v2) for details*

**> Input Ports:**
- **Points** (Array)
- **Num Subdivs** (Number: Integer)
- **Smooth** (Number: Boolean)
- **Loop** (Number: Boolean)

**< Output Ports:**
- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.SubdivideArray3_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SubdivideArray3_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.SubdivideArray3_v2](https://cables.gl/op/Ops.Array.PointArray.SubdivideArray3_v2)

---

### TransformArray3
![TransformArray3 op](images/ops/Ops_Array_PointArray_TransformArray3.svg)

**Full Name:** `Ops.Array.PointArray.TransformArray3`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.PointArray.TransformArray3) for details*

**> Input Ports:**
- **Transform** (Trigger)
- **Array** (Array)
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
- **Next** (Trigger)
- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.PointArray.TransformArray3#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TransformArray3"*
**Docs:** [https://cables.gl/op/Ops.Array.PointArray.TransformArray3](https://cables.gl/op/Ops.Array.PointArray.TransformArray3)

---

