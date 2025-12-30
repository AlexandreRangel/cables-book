# Ops.Graphics

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Graphics

### ArrayToExr
![ArrayToExr op](images/ops/Ops_Graphics_ArrayToExr.svg)

**Full Name:** `Ops.Graphics.ArrayToExr`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.ArrayToExr) for details*

**> Input Ports:**
- **Array** (Array)
- **Width** (Number: Integer)
- **Height** (Number: Integer)
- **ZIP Compression** (Number: Boolean)
- **Filename** (String)
- **Download** (Trigger)

**< Output Ports:**
- *Visit [Ops.Graphics.ArrayToExr documentation](https://cables.gl/op/Ops.Graphics.ArrayToExr) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.ArrayToExr#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayToExr"*
**Docs:** [https://cables.gl/op/Ops.Graphics.ArrayToExr](https://cables.gl/op/Ops.Graphics.ArrayToExr)

---

### DepthTest
![DepthTest op](images/ops/Ops_Graphics_DepthTest.svg)

**Full Name:** `Ops.Graphics.DepthTest`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.DepthTest) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Enable Depth Testing** (Number: Boolean)
- **Depth Test Method Index** (Number: Integer)
- **Write To Depth Buffer** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.DepthTest#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DepthTest"*
**Docs:** [https://cables.gl/op/Ops.Graphics.DepthTest](https://cables.gl/op/Ops.Graphics.DepthTest)

---

### GeometryMergeSimple
![GeometryMergeSimple op](images/ops/Ops_Graphics_GeometryMergeSimple.svg)

**Full Name:** `Ops.Graphics.GeometryMergeSimple`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.GeometryMergeSimple) for details*

**> Input Ports:**
- **Geometry** (Object)
- **Geometry 2** (Object)

**< Output Ports:**
- **Geometry Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.GeometryMergeSimple#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryMergeSimple"*
**Docs:** [https://cables.gl/op/Ops.Graphics.GeometryMergeSimple](https://cables.gl/op/Ops.Graphics.GeometryMergeSimple)

---

### GetMaterialId
![GetMaterialId op](images/ops/Ops_Graphics_GetMaterialId.svg)

**Full Name:** `Ops.Graphics.GetMaterialId`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.GetMaterialId) for details*

**> Input Ports:**
- **Update** (Trigger)

**< Output Ports:**
- **Next** (Trigger)
- **Material Id** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.GetMaterialId#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetMaterialId"*
**Docs:** [https://cables.gl/op/Ops.Graphics.GetMaterialId](https://cables.gl/op/Ops.Graphics.GetMaterialId)

---

### GetObjectId
![GetObjectId op](images/ops/Ops_Graphics_GetObjectId.svg)

**Full Name:** `Ops.Graphics.GetObjectId`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.GetObjectId) for details*

**> Input Ports:**
- **Update** (Trigger)

**< Output Ports:**
- **Next** (Trigger)
- **Material Id** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.GetObjectId#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetObjectId"*
**Docs:** [https://cables.gl/op/Ops.Graphics.GetObjectId](https://cables.gl/op/Ops.Graphics.GetObjectId)

---

### OrbitControls_v3
![OrbitControls_v3 op](images/ops/Ops_Graphics_OrbitControls_v3.svg)

**Full Name:** `Ops.Graphics.OrbitControls_v3`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.OrbitControls_v3) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Min Distance** (Number)
- **Max Distance** (Number)
- **Min Rot Y** (Number)
- **Max Rot Y** (Number)
- **Initial Radius** (Number)
- **Initial Axis Y** (Number)
- **Initial Axis X** (Number)
- **Smoothness** (Number)
- **Speed X** (Number)
- **Speed Y** (Number)
- **Active** (Number: Boolean)
- **Allow Panning** (Number: Boolean)
- **Allow Zooming** (Number: Boolean)
- **Allow Rotation** (Number: Boolean)
- **Restricted** (Number: Boolean)
- **Identity** (Number: Boolean)
- **Reset** (Trigger)

**< Output Ports:**
- **Trigger** (Trigger)
- **Radius** (Number)
- **Rot X** (Number)
- **Rot Y** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.OrbitControls_v3#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "OrbitControls_v3"*
**Docs:** [https://cables.gl/op/Ops.Graphics.OrbitControls_v3](https://cables.gl/op/Ops.Graphics.OrbitControls_v3)

---

### Transform
![Transform op](images/ops/Ops_Graphics_Transform.svg)

**Full Name:** `Ops.Graphics.Transform`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Transform) for details*

**> Input Ports:**
- **Render** (Trigger)
- **PosX** (Number)
- **PosY** (Number)
- **PosZ** (Number)
- **Scale** (Number)
- **RotX** (Number)
- **RotY** (Number)
- **RotZ** (Number)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Transform#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Transform"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Transform](https://cables.gl/op/Ops.Graphics.Transform)

---

### TransformView
![TransformView op](images/ops/Ops_Graphics_TransformView.svg)

**Full Name:** `Ops.Graphics.TransformView`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.TransformView) for details*

**> Input Ports:**
- **Render** (Trigger)
- **PosX** (Number)
- **PosY** (Number)
- **PosZ** (Number)
- **Scale** (Number)
- **RotX** (Number)
- **RotY** (Number)
- **RotZ** (Number)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.TransformView#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TransformView"*
**Docs:** [https://cables.gl/op/Ops.Graphics.TransformView](https://cables.gl/op/Ops.Graphics.TransformView)

---

