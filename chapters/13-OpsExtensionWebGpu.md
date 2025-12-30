# Ops.Extension.WebGpu

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Extension.WebGpu

### ArrayToGpuBuffer
![ArrayToGpuBuffer op](images/ops/Ops_Extension_WebGpu_ArrayToGpuBuffer.svg)

**Full Name:** `Ops.Extension.WebGpu.ArrayToGpuBuffer`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.ArrayToGpuBuffer) for details*

**> Input Ports:**
- **Arr** (Array)

**< Output Ports:**
- **GPUBuffer** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.ArrayToGpuBuffer#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayToGpuBuffer"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.ArrayToGpuBuffer](https://cables.gl/op/Ops.Extension.WebGpu.ArrayToGpuBuffer)

---

### ArrayToTexture
![ArrayToTexture op](images/ops/Ops_Extension_WebGpu_ArrayToTexture.svg)

**Full Name:** `Ops.Extension.WebGpu.ArrayToTexture`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.ArrayToTexture) for details*

**> Input Ports:**
- **Update** (Trigger)
- **Array** (Array)
- **Wrap Index** (Number: Integer)
- **Width** (Number: Integer)
- **Height** (Number: Integer)

**< Output Ports:**
- **Next** (Trigger)
- **Texture** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.ArrayToTexture#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayToTexture"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.ArrayToTexture](https://cables.gl/op/Ops.Extension.WebGpu.ArrayToTexture)

---

### AttributeAsColorMaterial
![AttributeAsColorMaterial op](images/ops/Ops_Extension_WebGpu_AttributeAsColorMaterial.svg)

**Full Name:** `Ops.Extension.WebGpu.AttributeAsColorMaterial`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.AttributeAsColorMaterial) for details*

**> Input Ports:**
- **Render** (Trigger)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.AttributeAsColorMaterial#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AttributeAsColorMaterial"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.AttributeAsColorMaterial](https://cables.gl/op/Ops.Extension.WebGpu.AttributeAsColorMaterial)

---

### BasicMaterial
![BasicMaterial op](images/ops/Ops_Extension_WebGpu_BasicMaterial.svg)

**Full Name:** `Ops.Extension.WebGpu.BasicMaterial`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.BasicMaterial) for details*

**> Input Ports:**
- **Render** (Trigger)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)
- **Colorize Texture** (Number: Boolean)
- **DiffuseRepeatX** (Number)
- **DiffuseRepeatY** (Number)
- **Tex Offset X** (Number)
- **Tex Offset Y** (Number)
- **Texture** (Object:Texture)
- **Mask** (Object:Texture)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.BasicMaterial#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BasicMaterial"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.BasicMaterial](https://cables.gl/op/Ops.Extension.WebGpu.BasicMaterial)

---

### ColorTexture
![ColorTexture op](images/ops/Ops_Extension_WebGpu_ColorTexture.svg)

**Full Name:** `Ops.Extension.WebGpu.ColorTexture`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.ColorTexture) for details*

**> Input Ports:**
- **Render** (Trigger)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)

**< Output Ports:**
- **Next** (Trigger)
- **Texture_out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.ColorTexture#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorTexture"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.ColorTexture](https://cables.gl/op/Ops.Extension.WebGpu.ColorTexture)

---

### CompCompute
![CompCompute op](images/ops/Ops_Extension_WebGpu_CompCompute.svg)

**Full Name:** `Ops.Extension.WebGpu.CompCompute`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.CompCompute) for details*

**> Input Ports:**
- **Compute** (Trigger)
- **Source** (String)
- **Workgroups 1** (Number: Integer)
- **Workgroups 2** (Number: Integer)
- **Workgroups 3** (Number: Integer)
- **Force Update** (Trigger)

**< Output Ports:**
- **Next** (Trigger)
- **Code** (String)
- **Buffer** (Object)
- **Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.CompCompute#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CompCompute"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.CompCompute](https://cables.gl/op/Ops.Extension.WebGpu.CompCompute)

---

### ComputeStorageInput
![ComputeStorageInput op](images/ops/Ops_Extension_WebGpu_ComputeStorageInput.svg)

**Full Name:** `Ops.Extension.WebGpu.ComputeStorageInput`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.ComputeStorageInput) for details*

**> Input Ports:**
- **Trigger** (Trigger)
- **Name** (String)
- **Buffer** (Object)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.ComputeStorageInput#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ComputeStorageInput"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.ComputeStorageInput](https://cables.gl/op/Ops.Extension.WebGpu.ComputeStorageInput)

---

### ComputeStorageOutput
![ComputeStorageOutput op](images/ops/Ops_Extension_WebGpu_ComputeStorageOutput.svg)

**Full Name:** `Ops.Extension.WebGpu.ComputeStorageOutput`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.ComputeStorageOutput) for details*

**> Input Ports:**
- **Trigger** (Trigger)
- **Name** (String)
- **Length** (Number: Integer)

**< Output Ports:**
- **Next** (Trigger)
- **Buffer** (Object)
- **Buffer Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.ComputeStorageOutput#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ComputeStorageOutput"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.ComputeStorageOutput](https://cables.gl/op/Ops.Extension.WebGpu.ComputeStorageOutput)

---

### ComputeUniform
![ComputeUniform op](images/ops/Ops_Extension_WebGpu_ComputeUniform.svg)

**Full Name:** `Ops.Extension.WebGpu.ComputeUniform`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.ComputeUniform) for details*

**> Input Ports:**
- **Trigger** (Trigger)
- **Name** (String)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **W** (Number)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.ComputeUniform#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ComputeUniform"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.ComputeUniform](https://cables.gl/op/Ops.Extension.WebGpu.ComputeUniform)

---

### DefaultTextures
![DefaultTextures op](images/ops/Ops_Extension_WebGpu_DefaultTextures.svg)

**Full Name:** `Ops.Extension.WebGpu.DefaultTextures`

**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.DefaultTextures) for details*

**> Input Ports:**
- *Visit [Ops.Extension.WebGpu.DefaultTextures documentation](https://cables.gl/op/Ops.Extension.WebGpu.DefaultTextures) for input port details*

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.DefaultTextures#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DefaultTextures"*

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.DefaultTextures](https://cables.gl/op/Ops.Extension.WebGpu.DefaultTextures)

---

### FaceCulling
![FaceCulling op](images/ops/Ops_Extension_WebGpu_FaceCulling.svg)

**Full Name:** `Ops.Extension.WebGpu.FaceCulling`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.FaceCulling) for details*

**> Input Ports:**
- **Render** (Trigger)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.FaceCulling#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FaceCulling"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.FaceCulling](https://cables.gl/op/Ops.Extension.WebGpu.FaceCulling)

---

### FrontBacksideMaterial
![FrontBacksideMaterial op](images/ops/Ops_Extension_WebGpu_FrontBacksideMaterial.svg)

**Full Name:** `Ops.Extension.WebGpu.FrontBacksideMaterial`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.FrontBacksideMaterial) for details*

**> Input Ports:**
- **Render** (Trigger)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)
- **R 2** (Number)
- **G 2** (Number)
- **B 2** (Number)
- **A 2** (Number)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.FrontBacksideMaterial#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FrontBacksideMaterial"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.FrontBacksideMaterial](https://cables.gl/op/Ops.Extension.WebGpu.FrontBacksideMaterial)

---

### FullScreenRect
![FullScreenRect op](images/ops/Ops_Extension_WebGpu_FullScreenRect.svg)

**Full Name:** `Ops.Extension.WebGpu.FullScreenRect`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.FullScreenRect) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Flip Y** (Number: Boolean)
- **Flip X** (Number: Boolean)
- **Texture** (Object:Texture)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.FullScreenRect#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FullScreenRect"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.FullScreenRect](https://cables.gl/op/Ops.Extension.WebGpu.FullScreenRect)

---

### GpuBufferToArray
![GpuBufferToArray op](images/ops/Ops_Extension_WebGpu_GpuBufferToArray.svg)

**Full Name:** `Ops.Extension.WebGpu.GpuBufferToArray`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.GpuBufferToArray) for details*

**> Input Ports:**
- **Trigger** (Trigger)
- **Pos Buffer** (Object)

**< Output Ports:**
- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.GpuBufferToArray#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GpuBufferToArray"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.GpuBufferToArray](https://cables.gl/op/Ops.Extension.WebGpu.GpuBufferToArray)

---

### MatCapMaterial
![MatCapMaterial op](images/ops/Ops_Extension_WebGpu_MatCapMaterial.svg)

**Full Name:** `Ops.Extension.WebGpu.MatCapMaterial`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.MatCapMaterial) for details*

**> Input Ports:**
- **Render** (Trigger)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)
- **Colorize Texture** (Number: Boolean)
- **DiffuseRepeatX** (Number)
- **DiffuseRepeatY** (Number)
- **Tex Offset X** (Number)
- **Tex Offset Y** (Number)
- **Matcap** (Object:Texture)
- **Diffuse** (Object:Texture)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.MatCapMaterial#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MatCapMaterial"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.MatCapMaterial](https://cables.gl/op/Ops.Extension.WebGpu.MatCapMaterial)

---

### MeshInstancer
![MeshInstancer op](images/ops/Ops_Extension_WebGpu_MeshInstancer.svg)

**Full Name:** `Ops.Extension.WebGpu.MeshInstancer`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.MeshInstancer) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Geometry** (Object:Geometry)
- **Pos Buffer** (Object)
- **Scale Buffer** (Object)
- **Num Instances** (Number: Integer)
- **Reset** (Trigger)
- **Test** (Trigger)

**< Output Ports:**
- **Next** (Trigger)
- **Total Instances** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.MeshInstancer#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MeshInstancer"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.MeshInstancer](https://cables.gl/op/Ops.Extension.WebGpu.MeshInstancer)

---

### Pipeline
![Pipeline op](images/ops/Ops_Extension_WebGpu_Pipeline.svg)

**Full Name:** `Ops.Extension.WebGpu.Pipeline`

**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.Pipeline) for details*

**> Input Ports:**
- **Trigger** (Trigger)
- **Force Rebuild** (Trigger)

**< Output Ports:**
- **Next** (Trigger)
- **Pipeline** (Object)
- **Shader Info** (Object)
- **Shader Source** (String)
- **Compile Count** (Number)
- **Shader Id** (String)
- **Defines** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.Pipeline#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Pipeline"*

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.Pipeline](https://cables.gl/op/Ops.Extension.WebGpu.Pipeline)

---

### RenderToTexture
![RenderToTexture op](images/ops/Ops_Extension_WebGpu_RenderToTexture.svg)

**Full Name:** `Ops.Extension.WebGpu.RenderToTexture`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.RenderToTexture) for details*

**> Input Ports:**
- **Trigger** (Trigger)
- **Texture Width** (Number: Integer)
- **Texture Height** (Number: Integer)
- **Clear** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)
- **Texture** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.RenderToTexture#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RenderToTexture"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.RenderToTexture](https://cables.gl/op/Ops.Extension.WebGpu.RenderToTexture)

---

### SaselHund
![SaselHund op](images/ops/Ops_Extension_WebGpu_SaselHund.svg)

**Full Name:** `Ops.Extension.WebGpu.SaselHund`

**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.SaselHund) for details*

**> Input Ports:**
- *Visit [Ops.Extension.WebGpu.SaselHund documentation](https://cables.gl/op/Ops.Extension.WebGpu.SaselHund) for input port details*

**< Output Ports:**
- *Visit [Ops.Extension.WebGpu.SaselHund documentation](https://cables.gl/op/Ops.Extension.WebGpu.SaselHund) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.SaselHund#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SaselHund"*

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.SaselHund](https://cables.gl/op/Ops.Extension.WebGpu.SaselHund)

---

### Texture
![Texture op](images/ops/Ops_Extension_WebGpu_Texture.svg)

**Full Name:** `Ops.Extension.WebGpu.Texture`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.Texture) for details*

**> Input Ports:**
- **File** (String)
- **Wrap Index** (Number: Integer)

**< Output Ports:**
- **Texture** (Object)
- **Width** (Number)
- **Height** (Number)
- **Pixelformat** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.Texture#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Texture"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.Texture](https://cables.gl/op/Ops.Extension.WebGpu.Texture)

---

### VizTexture
![VizTexture op](images/ops/Ops_Extension_WebGpu_VizTexture.svg)

**Full Name:** `Ops.Extension.WebGpu.VizTexture`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.VizTexture) for details*

**> Input Ports:**
- **Texture In** (Object:Texture)

**< Output Ports:**
- *Visit [Ops.Extension.WebGpu.VizTexture documentation](https://cables.gl/op/Ops.Extension.WebGpu.VizTexture) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.VizTexture#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "VizTexture"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.VizTexture](https://cables.gl/op/Ops.Extension.WebGpu.VizTexture)

---

### WebGpuCanvas
![WebGpuCanvas op](images/ops/Ops_Extension_WebGpu_WebGpuCanvas.svg)

**Full Name:** `Ops.Extension.WebGpu.WebGpuCanvas`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.WebGpuCanvas) for details*

**> Input Ports:**
- **Active** (Number: Boolean)
- **Catch Errors** (Number: Boolean)
- **Stop On Errors** (Number: Boolean)
- **Profile** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)
- **Next2** (Trigger)
- **Supported** (booleanNumber)
- **MS Frame** (Number)
- **Canvas** (Object)
- **Canvas Prev** (Object)
- **Profiler Data** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.WebGpuCanvas#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WebGpuCanvas"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.WebGpuCanvas](https://cables.gl/op/Ops.Extension.WebGpu.WebGpuCanvas)

---

### WebGpuInfo
![WebGpuInfo op](images/ops/Ops_Extension_WebGpu_WebGpuInfo.svg)

**Full Name:** `Ops.Extension.WebGpu.WebGpuInfo`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.WebGpuInfo) for details*

**> Input Ports:**
- **Trigger** (Trigger)

**< Output Ports:**
- **Next** (Trigger)
- **Limits** (Object)
- **Vendor** (String)
- **Architecture** (String)
- **Presentation Format** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.WebGpuInfo#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WebGpuInfo"*
**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.WebGpuInfo](https://cables.gl/op/Ops.Extension.WebGpu.WebGpuInfo)

---

