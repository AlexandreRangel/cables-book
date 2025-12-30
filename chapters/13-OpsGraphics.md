# Ops.Graphics

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Graphics

### ArrayToExr
![ArrayToExr op](images/ops/Ops_Graphics_ArrayToExr.svg)

**Full Name:** `Ops.Graphics.ArrayToExr`
**Description:** convert and download an array of numbers as an .exr image file

**> Input Ports:**
- **Array** (Array): *See documentation*
- **Width** (Number: Integer): *See documentation*
- **Height** (Number: Integer): *See documentation*
- **ZIP Compression** (Number: Boolean): *See documentation*
- **Filename** (String): *See documentation*
- **Download** (Trigger): *See documentation*

**< Output Ports:**
- *Visit [Ops.Graphics.ArrayToExr documentation](https://cables.gl/op/Ops.Graphics.ArrayToExr) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/PoAXNA)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayToExr"*
**Docs:** [https://cables.gl/op/Ops.Graphics.ArrayToExr](https://cables.gl/op/Ops.Graphics.ArrayToExr)

---

### DepthTest
![DepthTest op](images/ops/Ops_Graphics_DepthTest.svg)

**Full Name:** `Ops.Graphics.DepthTest`
**Description:** change depth testing method (depthMask,depthWrite,depthFunc)

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Enable Depth Testing** (Number: Boolean): *See documentation*
- **Depth Test Method Index** (Number: Integer): *See documentation*
- **Write To Depth Buffer** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/A9PD8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DepthTest"*
**Docs:** [https://cables.gl/op/Ops.Graphics.DepthTest](https://cables.gl/op/Ops.Graphics.DepthTest)

---

### GeometryMergeSimple
![GeometryMergeSimple op](images/ops/Ops_Graphics_GeometryMergeSimple.svg)

**Full Name:** `Ops.Graphics.GeometryMergeSimple`
**Description:** merge two geometries into one

**> Input Ports:**
- **Geometry** (Object): *See documentation*
- **Geometry 2** (Object): *See documentation*

**< Output Ports:**
- **Geometry Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/4gsNve)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryMergeSimple"*
**Docs:** [https://cables.gl/op/Ops.Graphics.GeometryMergeSimple](https://cables.gl/op/Ops.Graphics.GeometryMergeSimple)

---

### GetMaterialId
![GetMaterialId op](images/ops/Ops_Graphics_GetMaterialId.svg)

**Full Name:** `Ops.Graphics.GetMaterialId`
**Description:** get the id/index of the current set material

**> Input Ports:**
- **Update** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Material Id** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/PYpQit)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetMaterialId"*
**Docs:** [https://cables.gl/op/Ops.Graphics.GetMaterialId](https://cables.gl/op/Ops.Graphics.GetMaterialId)

---

### GetObjectId
![GetObjectId op](images/ops/Ops_Graphics_GetObjectId.svg)

**Full Name:** `Ops.Graphics.GetObjectId`
**Description:** get the id/index of the current object/mesh

**> Input Ports:**
- **Update** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Material Id** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.GetObjectId#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetObjectId"*
**Docs:** [https://cables.gl/op/Ops.Graphics.GetObjectId](https://cables.gl/op/Ops.Graphics.GetObjectId)

---

### OrbitControls_v3
![OrbitControls_v3 op](images/ops/Ops_Graphics_OrbitControls_v3.svg)

**Full Name:** `Ops.Graphics.OrbitControls_v3`
**Description:** rotate your object by clicking and dragging the mouse

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Min Distance** (Number): *See documentation*
- **Max Distance** (Number): *See documentation*
- **Min Rot Y** (Number): *See documentation*
- **Max Rot Y** (Number): *See documentation*
- **Initial Radius** (Number): *See documentation*
- **Initial Axis Y** (Number): *See documentation*
- **Initial Axis X** (Number): *See documentation*
- **Smoothness** (Number): *See documentation*
- **Speed X** (Number): *See documentation*
- **Speed Y** (Number): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Allow Panning** (Number: Boolean): *See documentation*
- **Allow Zooming** (Number: Boolean): *See documentation*
- **Allow Rotation** (Number: Boolean): *See documentation*
- **Restricted** (Number: Boolean): *See documentation*
- **Identity** (Number: Boolean): *See documentation*
- **Reset** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Radius** (Number): *See documentation*
- **Rot X** (Number): *See documentation*
- **Rot Y** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Krorsh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "OrbitControls_v3"*
**Docs:** [https://cables.gl/op/Ops.Graphics.OrbitControls_v3](https://cables.gl/op/Ops.Graphics.OrbitControls_v3)

---

### Transform
![Transform op](images/ops/Ops_Graphics_Transform.svg)

**Full Name:** `Ops.Graphics.Transform`
**Description:** Transform objects in 3d space (rotate, translate, scale)

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **PosX** (Number): *See documentation*
- **PosY** (Number): *See documentation*
- **PosZ** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **RotX** (Number): *See documentation*
- **RotY** (Number): *See documentation*
- **RotZ** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/o741ft)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Transform"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Transform](https://cables.gl/op/Ops.Graphics.Transform)

---

### TransformView
![TransformView op](images/ops/Ops_Graphics_TransformView.svg)

**Full Name:** `Ops.Graphics.TransformView`
**Description:** the most simple camera op / transform the viewmatrix

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **PosX** (Number): *See documentation*
- **PosY** (Number): *See documentation*
- **PosZ** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **RotX** (Number): *See documentation*
- **RotY** (Number): *See documentation*
- **RotZ** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/0GAv8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TransformView"*
**Docs:** [https://cables.gl/op/Ops.Graphics.TransformView](https://cables.gl/op/Ops.Graphics.TransformView)

---

