# Ops.Graphics

---

```{=latex}
\stepcounter{subsection}\setcounter{subsubsection}{0}
```
### ArrayToExr
![ArrayToExr op](images/ops/Ops_Graphics_ArrayToExr.svg)

**Full Name:** `Ops.Graphics.ArrayToExr`

**Description:** convert and download an array of numbers as an .exr image file

**`\inputsymbol`{=latex} Inputs**

- **Array** (Array)
- **Width** (Number: Integer)
- **Height** (Number: Integer)
- **ZIP Compression** (Number: Boolean)
- **Filename** (String)
- **Download** (Trigger)

**`\outputsymbol`{=latex} Output**

- *Visit [Ops.Graphics.ArrayToExr documentation](https://cables.gl/op/Ops.Graphics.ArrayToExr) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/PoAXNA)

**Docs:** [https://cables.gl/op/Ops.Graphics.ArrayToExr](https://cables.gl/op/Ops.Graphics.ArrayToExr)

### DepthTest
![DepthTest op](images/ops/Ops_Graphics_DepthTest.svg)

**Full Name:** `Ops.Graphics.DepthTest`

**Description:** change depth testing method (depthMask,depthWrite,depthFunc)

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Enable Depth Testing** (Number: Boolean)
- **Depth Test Method Index** (Number: Integer)
- **Write To Depth Buffer** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/A9PD8i)

**Docs:** [https://cables.gl/op/Ops.Graphics.DepthTest](https://cables.gl/op/Ops.Graphics.DepthTest)

### GeometryMergeSimple
![GeometryMergeSimple op](images/ops/Ops_Graphics_GeometryMergeSimple.svg)

**Full Name:** `Ops.Graphics.GeometryMergeSimple`

**Description:** merge two geometries into one

**`\inputsymbol`{=latex} Inputs**

- **Geometry** (Object)
- **Geometry 2** (Object)

**`\outputsymbol`{=latex} Output**

- **Geometry Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/4gsNve)

**Docs:** [https://cables.gl/op/Ops.Graphics.GeometryMergeSimple](https://cables.gl/op/Ops.Graphics.GeometryMergeSimple)

### GetMaterialId
![GetMaterialId op](images/ops/Ops_Graphics_GetMaterialId.svg)

**Full Name:** `Ops.Graphics.GetMaterialId`

**Description:** get the id/index of the current set material

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Material Id** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/PYpQit)

**Docs:** [https://cables.gl/op/Ops.Graphics.GetMaterialId](https://cables.gl/op/Ops.Graphics.GetMaterialId)

### GetObjectId
![GetObjectId op](images/ops/Ops_Graphics_GetObjectId.svg)

**Full Name:** `Ops.Graphics.GetObjectId`

**Description:** get the id/index of the current object/mesh

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Material Id** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.GetObjectId#example)

**Docs:** [https://cables.gl/op/Ops.Graphics.GetObjectId](https://cables.gl/op/Ops.Graphics.GetObjectId)

### OrbitControls_v3
![OrbitControls_v3 op](images/ops/Ops_Graphics_OrbitControls_v3.svg)

**Full Name:** `Ops.Graphics.OrbitControls_v3`

**Description:** rotate your object by clicking and dragging the mouse

**`\inputsymbol`{=latex} Inputs**

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

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)
- **Radius** (Number)
- **Rot X** (Number)
- **Rot Y** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Krorsh)

**Docs:** [https://cables.gl/op/Ops.Graphics.OrbitControls_v3](https://cables.gl/op/Ops.Graphics.OrbitControls_v3)

### Transform
![Transform op](images/ops/Ops_Graphics_Transform.svg)

**Full Name:** `Ops.Graphics.Transform`

**Description:** Transform objects in 3d space (rotate, translate, scale)

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **PosX** (Number)
- **PosY** (Number)
- **PosZ** (Number)
- **Scale** (Number)
- **RotX** (Number)
- **RotY** (Number)
- **RotZ** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/o741ft)

**Docs:** [https://cables.gl/op/Ops.Graphics.Transform](https://cables.gl/op/Ops.Graphics.Transform)

### TransformView
![TransformView op](images/ops/Ops_Graphics_TransformView.svg)

**Full Name:** `Ops.Graphics.TransformView`

**Description:** the most simple camera op / transform the viewmatrix

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **PosX** (Number)
- **PosY** (Number)
- **PosZ** (Number)
- **Scale** (Number)
- **RotX** (Number)
- **RotY** (Number)
- **RotZ** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/0GAv8i)

**Docs:** [https://cables.gl/op/Ops.Graphics.TransformView](https://cables.gl/op/Ops.Graphics.TransformView)


