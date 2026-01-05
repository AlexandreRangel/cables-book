# Ops.Extension.WebGpu

---

## Ops.Extension.WebGpu

### ArrayToGpuBuffer
![ArrayToGpuBuffer op](images/ops/Ops_Extension_WebGpu_ArrayToGpuBuffer.svg)

**Full Name:** `Ops.Extension.WebGpu.ArrayToGpuBuffer`

**Description:** Upload an array to the GPU as a GpuBuffer

**`\inputsymbol`{=latex} Inputs**

- **Arr** (Array)

**`\outputsymbol`{=latex} Output**

- **GPUBuffer** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/VShX3I)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.ArrayToGpuBuffer](https://cables.gl/op/Ops.Extension.WebGpu.ArrayToGpuBuffer)

### ArrayToTexture
![ArrayToTexture op](images/ops/Ops_Extension_WebGpu_ArrayToTexture.svg)

**Full Name:** `Ops.Extension.WebGpu.ArrayToTexture`

**Description:** Convert an array of numbers to a webgpu texture

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **Array** (Array)
- **Wrap Index** (Number: Integer)
- **Width** (Number: Integer)
- **Height** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Texture** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/hYt34I)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.ArrayToTexture](https://cables.gl/op/Ops.Extension.WebGpu.ArrayToTexture)

### AttributeAsColorMaterial
![AttributeAsColorMaterial op](images/ops/Ops_Extension_WebGpu_AttributeAsColorMaterial.svg)

**Full Name:** `Ops.Extension.WebGpu.AttributeAsColorMaterial`

**Description:** Render mesh attribultes as color

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/FM4hQB)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.AttributeAsColorMaterial](https://cables.gl/op/Ops.Extension.WebGpu.AttributeAsColorMaterial)

### BasicMaterial
![BasicMaterial op](images/ops/Ops_Extension_WebGpu_BasicMaterial.svg)

**Full Name:** `Ops.Extension.WebGpu.BasicMaterial`

**Description:** A simple material without shading

**`\inputsymbol`{=latex} Inputs**

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

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/J0HjQB)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.BasicMaterial](https://cables.gl/op/Ops.Extension.WebGpu.BasicMaterial)

### ColorTexture
![ColorTexture op](images/ops/Ops_Extension_WebGpu_ColorTexture.svg)

**Full Name:** `Ops.Extension.WebGpu.ColorTexture`

**Description:** A texture containing only one color

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Texture_out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/13IW3I)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.ColorTexture](https://cables.gl/op/Ops.Extension.WebGpu.ColorTexture)

### CompCompute
![CompCompute op](images/ops/Ops_Extension_WebGpu_CompCompute.svg)

**Full Name:** `Ops.Extension.WebGpu.CompCompute`

**Description:** Compose a compute shader

**`\inputsymbol`{=latex} Inputs**

- **Compute** (Trigger)
- **Source** (String)
- **Workgroups 1** (Number: Integer)
- **Workgroups 2** (Number: Integer)
- **Workgroups 3** (Number: Integer)
- **Force Update** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Code** (String)
- **Buffer** (Object)
- **Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/1ff0dH)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.CompCompute](https://cables.gl/op/Ops.Extension.WebGpu.CompCompute)

### ComputeStorageInput
![ComputeStorageInput op](images/ops/Ops_Extension_WebGpu_ComputeStorageInput.svg)

**Full Name:** `Ops.Extension.WebGpu.ComputeStorageInput`

**Description:** Compute shader GPU buffer storage input

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Name** (String)
- **Buffer** (Object)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.ComputeStorageInput#example)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.ComputeStorageInput](https://cables.gl/op/Ops.Extension.WebGpu.ComputeStorageInput)

### ComputeStorageOutput
![ComputeStorageOutput op](images/ops/Ops_Extension_WebGpu_ComputeStorageOutput.svg)

**Full Name:** `Ops.Extension.WebGpu.ComputeStorageOutput`

**Description:** Compute shader GPU buffer storage output

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Name** (String)
- **Length** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Buffer** (Object)
- **Buffer Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/1ff0dH)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.ComputeStorageOutput](https://cables.gl/op/Ops.Extension.WebGpu.ComputeStorageOutput)

### ComputeUniform
![ComputeUniform op](images/ops/Ops_Extension_WebGpu_ComputeUniform.svg)

**Full Name:** `Ops.Extension.WebGpu.ComputeUniform`

**Description:** Add a uniform input to a compute shader composition

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Name** (String)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **W** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.ComputeUniform#example)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.ComputeUniform](https://cables.gl/op/Ops.Extension.WebGpu.ComputeUniform)

### DefaultTextures
![DefaultTextures op](images/ops/Ops_Extension_WebGpu_DefaultTextures.svg)

**Full Name:** `Ops.Extension.WebGpu.DefaultTextures`

**Description:** Outputs textures

**`\inputsymbol`{=latex} Inputs**

- *Visit [Ops.Extension.WebGpu.DefaultTextures documentation](https://cables.gl/op/Ops.Extension.WebGpu.DefaultTextures) for input port details*

**`\outputsymbol`{=latex} Output**

- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/nQEVKB)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.DefaultTextures](https://cables.gl/op/Ops.Extension.WebGpu.DefaultTextures)

### FaceCulling
![FaceCulling op](images/ops/Ops_Extension_WebGpu_FaceCulling.svg)

**Full Name:** `Ops.Extension.WebGpu.FaceCulling`

**Description:** cull (do not draw) back or front facing faces/triangles

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/zKLQ3I)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.FaceCulling](https://cables.gl/op/Ops.Extension.WebGpu.FaceCulling)

### FrontBacksideMaterial
![FrontBacksideMaterial op](images/ops/Ops_Extension_WebGpu_FrontBacksideMaterial.svg)

**Full Name:** `Ops.Extension.WebGpu.FrontBacksideMaterial`

**Description:** Show direction of faces as color

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)
- **R 2** (Number)
- **G 2** (Number)
- **B 2** (Number)
- **A 2** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/1Jm1LB)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.FrontBacksideMaterial](https://cables.gl/op/Ops.Extension.WebGpu.FrontBacksideMaterial)

### FullScreenRect
![FullScreenRect op](images/ops/Ops_Extension_WebGpu_FullScreenRect.svg)

**Full Name:** `Ops.Extension.WebGpu.FullScreenRect`

**Description:** Render a rectangle that fills the whole canvas

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Flip Y** (Number: Boolean)
- **Flip X** (Number: Boolean)
- **Texture** (Object:Texture)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/PNx2LB)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.FullScreenRect](https://cables.gl/op/Ops.Extension.WebGpu.FullScreenRect)

### GpuBufferToArray
![GpuBufferToArray op](images/ops/Ops_Extension_WebGpu_GpuBufferToArray.svg)

**Full Name:** `Ops.Extension.WebGpu.GpuBufferToArray`

**Description:** Convert a GpuBuffer to a CPU Array

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Pos Buffer** (Object)

**`\outputsymbol`{=latex} Output**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/bQQYKB)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.GpuBufferToArray](https://cables.gl/op/Ops.Extension.WebGpu.GpuBufferToArray)

### MatCapMaterial
![MatCapMaterial op](images/ops/Ops_Extension_WebGpu_MatCapMaterial.svg)

**Full Name:** `Ops.Extension.WebGpu.MatCapMaterial`

**Description:** Image based material that uses a matcap environment texture

**`\inputsymbol`{=latex} Inputs**

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

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/WwXZKB)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.MatCapMaterial](https://cables.gl/op/Ops.Extension.WebGpu.MatCapMaterial)

### MeshInstancer
![MeshInstancer op](images/ops/Ops_Extension_WebGpu_MeshInstancer.svg)

**Full Name:** `Ops.Extension.WebGpu.MeshInstancer`

**Description:** Draw the same mesh many times very fast

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Geometry** (Object:Geometry)
- **Pos Buffer** (Object)
- **Scale Buffer** (Object)
- **Num Instances** (Number: Integer)
- **Reset** (Trigger)
- **Test** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Total Instances** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/bQQYKB)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.MeshInstancer](https://cables.gl/op/Ops.Extension.WebGpu.MeshInstancer)

### Pipeline
![Pipeline op](images/ops/Ops_Extension_WebGpu_Pipeline.svg)

**Full Name:** `Ops.Extension.WebGpu.Pipeline`

**Description:** show content of last used pipeline for debugging

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Force Rebuild** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Pipeline** (Object)
- **Shader Info** (Object)
- **Shader Source** (String)
- **Compile Count** (Number)
- **Shader Id** (String)
- **Defines** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.Pipeline#example)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.Pipeline](https://cables.gl/op/Ops.Extension.WebGpu.Pipeline)

### RenderToTexture
![RenderToTexture op](images/ops/Ops_Extension_WebGpu_RenderToTexture.svg)

**Full Name:** `Ops.Extension.WebGpu.RenderToTexture`

**Description:** render into a texture

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Texture Width** (Number: Integer)
- **Texture Height** (Number: Integer)
- **Clear** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Texture** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/pyXXKB)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.RenderToTexture](https://cables.gl/op/Ops.Extension.WebGpu.RenderToTexture)

### SaselHund
![SaselHund op](images/ops/Ops_Extension_WebGpu_SaselHund.svg)

**Full Name:** `Ops.Extension.WebGpu.SaselHund`

**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.WebGpu.SaselHund) for details*

**`\inputsymbol`{=latex} Inputs**

- *Visit [Ops.Extension.WebGpu.SaselHund documentation](https://cables.gl/op/Ops.Extension.WebGpu.SaselHund) for input port details*

**`\outputsymbol`{=latex} Output**

- *Visit [Ops.Extension.WebGpu.SaselHund documentation](https://cables.gl/op/Ops.Extension.WebGpu.SaselHund) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.WebGpu.SaselHund#example)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.SaselHund](https://cables.gl/op/Ops.Extension.WebGpu.SaselHund)

### Texture
![Texture op](images/ops/Ops_Extension_WebGpu_Texture.svg)

**Full Name:** `Ops.Extension.WebGpu.Texture`

**Description:** Load an image file as a texture

**`\inputsymbol`{=latex} Inputs**

- **File** (String)
- **Wrap Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Texture** (Object)
- **Width** (Number)
- **Height** (Number)
- **Pixelformat** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/08iWKB)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.Texture](https://cables.gl/op/Ops.Extension.WebGpu.Texture)

### VizTexture
![VizTexture op](images/ops/Ops_Extension_WebGpu_VizTexture.svg)

**Full Name:** `Ops.Extension.WebGpu.VizTexture`

**Description:** Vizualize a webgpu texture on the patchfield

**`\inputsymbol`{=latex} Inputs**

- **Texture In** (Object:Texture)

**`\outputsymbol`{=latex} Output**

- *Visit [Ops.Extension.WebGpu.VizTexture documentation](https://cables.gl/op/Ops.Extension.WebGpu.VizTexture) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/tk5uLB)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.VizTexture](https://cables.gl/op/Ops.Extension.WebGpu.VizTexture)

### WebGpuCanvas
![WebGpuCanvas op](images/ops/Ops_Extension_WebGpu_WebGpuCanvas.svg)

**Full Name:** `Ops.Extension.WebGpu.WebGpuCanvas`

**Description:** Create a canvas for WebGPU

**`\inputsymbol`{=latex} Inputs**

- **Active** (Number: Boolean)
- **Catch Errors** (Number: Boolean)
- **Stop On Errors** (Number: Boolean)
- **Profile** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Next2** (Trigger)
- **Supported** (booleanNumber)
- **MS Frame** (Number)
- **Canvas** (Object)
- **Canvas Prev** (Object)
- **Profiler Data** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/ALyYKB)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.WebGpuCanvas](https://cables.gl/op/Ops.Extension.WebGpu.WebGpuCanvas)

### WebGpuInfo
![WebGpuInfo op](images/ops/Ops_Extension_WebGpu_WebGpuInfo.svg)

**Full Name:** `Ops.Extension.WebGpu.WebGpuInfo`

**Description:** Output information about WebGPU adapter and implementation

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Limits** (Object)
- **Vendor** (String)
- **Architecture** (String)
- **Presentation Format** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/UTES3I)

**Docs:** [https://cables.gl/op/Ops.Extension.WebGpu.WebGpuInfo](https://cables.gl/op/Ops.Extension.WebGpu.WebGpuInfo)


