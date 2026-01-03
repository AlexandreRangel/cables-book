# Ops.Gl.Shader

---

## Ops.Gl.Shader

### AttributeAsColorMaterial
![AttributeAsColorMaterial op](images/ops/Ops_Gl_Shader_AttributeAsColorMaterial.svg)

**Full Name:** `Ops.Gl.Shader.AttributeAsColorMaterial`

**Description:** render mesh normals as colors

**> Input Ports:**

- **Render** (Trigger)
- **Absolute** (Number: Boolean)
- **World Space** (Number: Boolean)

**< Output Ports:**

- **Trigger** (Trigger)
- **Shader** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/bZEZGc)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AttributeAsColorMaterial"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.AttributeAsColorMaterial](https://cables.gl/op/Ops.Gl.Shader.AttributeAsColorMaterial)


### BasicMaterial_v3
![BasicMaterial_v3 op](images/ops/Ops_Gl_Shader_BasicMaterial_v3.svg)

**Full Name:** `Ops.Gl.Shader.BasicMaterial_v3`

**Description:** A material without shading

**> Input Ports:**

- **Render** (Trigger)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)
- **Texture** (Object:Texture)
- **ColorizeTexture** (Number: Boolean)
- **Vertex Colors** (Number: Boolean)
- **TextureOpacity** (Object:Texture)
- **Opacity TexCoords Transform** (Number: Boolean)
- **Discard Transparent Pixels** (Number: Boolean)
- **DiffuseRepeatX** (Number)
- **DiffuseRepeatY** (Number)
- **Tex Offset X** (Number)
- **Tex Offset Y** (Number)
- **Crop TexCoords** (Number: Boolean)
- **Billboard** (Number: Boolean)

**< Output Ports:**

- **Trigger** (Trigger)
- **Shader** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/SKCL88)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BasicMaterial_v3"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.BasicMaterial_v3](https://cables.gl/op/Ops.Gl.Shader.BasicMaterial_v3)


### ChromaKeyMaterial
![ChromaKeyMaterial op](images/ops/Ops_Gl_Shader_ChromaKeyMaterial.svg)

**Full Name:** `Ops.Gl.Shader.ChromaKeyMaterial`

**Description:** display texture and replace a color with transparency

**> Input Ports:**

- **Render** (Trigger)
- **Texture** (Object)
- **Mode Index** (Number: Integer)
- **WeightMul** (Number)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **White** (Number)
- **DiffuseRepeatX** (Number)
- **DiffuseRepeatY** (Number)
- **Tex Offset X** (Number)
- **Tex Offset Y** (Number)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/aDqoTq)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ChromaKeyMaterial"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.ChromaKeyMaterial](https://cables.gl/op/Ops.Gl.Shader.ChromaKeyMaterial)


### CustomShader_v2
![CustomShader_v2 op](images/ops/Ops_Gl_Shader_CustomShader_v2.svg)

**Full Name:** `Ops.Gl.Shader.CustomShader_v2`

**Description:** Write your own custom shader

**> Input Ports:**

- **Render** (Trigger)
- **Fragment Code** (String)
- **Vertex Code** (String)
- **Use As Material** (Number: Boolean)
- **W** (Number)
- **H** (Number)
- **GPosition** (Object)
- **GNormal** (Object)
- **TexNoise** (Object)
- **Samples** (Array)
- **Projection** (Array)

**< Output Ports:**

- **Trigger** (Trigger)
- **Shader** (Object)
- **Has Errors** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/vWyGud)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CustomShader_v2"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.CustomShader_v2](https://cables.gl/op/Ops.Gl.Shader.CustomShader_v2)


### ErrorMaterial
![ErrorMaterial op](images/ops/Ops_Gl_Shader_ErrorMaterial.svg)

**Full Name:** `Ops.Gl.Shader.ErrorMaterial`

**Description:** draw meshes using the cables error material shader

**> Input Ports:**

- **Render** (Trigger)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Shader.ErrorMaterial#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ErrorMaterial"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.ErrorMaterial](https://cables.gl/op/Ops.Gl.Shader.ErrorMaterial)


### FrontBacksideMaterial
![FrontBacksideMaterial op](images/ops/Ops_Gl_Shader_FrontBacksideMaterial.svg)

**Full Name:** `Ops.Gl.Shader.FrontBacksideMaterial`

**Description:** visualize which faces are facing the camera

**> Input Ports:**

- **Render** (Trigger)

**< Output Ports:**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Lm6p9r)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FrontBacksideMaterial"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.FrontBacksideMaterial](https://cables.gl/op/Ops.Gl.Shader.FrontBacksideMaterial)


### GetShader
![GetShader op](images/ops/Ops_Gl_Shader_GetShader.svg)

**Full Name:** `Ops.Gl.Shader.GetShader`

**Description:** get current set shader

**> Input Ports:**

- **Update** (Trigger)

**< Output Ports:**

- **Next** (Trigger)
- **Shader** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/BweOVl)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetShader"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.GetShader](https://cables.gl/op/Ops.Gl.Shader.GetShader)


### MatCapMaterial_v3
![MatCapMaterial_v3 op](images/ops/Ops_Gl_Shader_MatCapMaterial_v3.svg)

**Full Name:** `Ops.Gl.Shader.MatCapMaterial_v3`

**Description:** Easy to use image based lighting Material

**> Input Ports:**

- **Render** (Trigger)
- **MatCap** (Object:Texture)
- **Diffuse** (Object:Texture)
- **Normal** (Object:Texture)
- **Specular Mask** (Object:Texture)
- **Specular MatCap** (Object:Texture)
- **AO Texture** (Object:Texture)
- **Opacity Texture** (Object:Texture)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **Opacity** (Number)
- **AO Intensity** (Number)
- **Normal Map Intensity** (Number)
- **Repeat X** (Number)
- **Repeat Y** (Number)
- **Offset X** (Number)
- **Offset Y** (Number)
- **Double Sided** (Number: Boolean)
- **Screen Space Normals** (Number: Boolean)
- **check to use screen space normals** (flat shading)
- **Calc Normal Tangents** (Number: Boolean)
- **Opacity TexCoords Transform** (Number: Boolean)
- **Discard Transparent Pixels** (Number: Boolean)

**< Output Ports:**

- **Next** (Trigger)
- **Shader** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/gWkghi)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MatCapMaterial_v3"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.MatCapMaterial_v3](https://cables.gl/op/Ops.Gl.Shader.MatCapMaterial_v3)


### MinifyGlsl
![MinifyGlsl op](images/ops/Ops_Gl_Shader_MinifyGlsl.svg)

**Full Name:** `Ops.Gl.Shader.MinifyGlsl`

**Description:** Minify GLSL shader source code

**> Input Ports:**

- **Shader Source** (String)

**< Output Ports:**

- **Minified Shader Source** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/t5H1Qc)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MinifyGlsl"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.MinifyGlsl](https://cables.gl/op/Ops.Gl.Shader.MinifyGlsl)


### PointMaterial_v6
![PointMaterial_v6 op](images/ops/Ops_Gl_Shader_PointMaterial_v6.svg)

**Full Name:** `Ops.Gl.Shader.PointMaterial_v6`

**Description:** Draw all vertices as points / circles

**> Input Ports:**

- **Render** (Trigger)
- **PointSize** (Number)
- **Size In Pixels** (Number: Boolean)
- **Random Size** (Number)
- **Round** (Number: Boolean)
- **Round Antialias** (Number: Boolean)
- **Scale By Distance** (Number: Boolean)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)
- **Vertex Colors** (Number: Boolean)
- **Texture** (Object:Texture)
- **Colorize Texture** (Number: Boolean)
- **Texture Mask** (Object:Texture)
- **Texture Colorize** (Object:Texture)
- **Colorize Randomize** (Number: Boolean)
- **Texture Opacity** (Object:Texture)
- **Texture Point Size** (Object:Texture)
- **Texture Point Size Mul** (Number)
- **Flip Texture** (Number: Boolean)
- **Atlas Cross Fade** (Number: Boolean)
- **Atlas Repeat X** (Number)
- **Atlas Lookup** (Object:Texture)
- **Rotate Texture** (Object:Texture)
- **Min Point Size** (Number)

**< Output Ports:**

- **Trigger** (Trigger)
- **Shader** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/O9yRO6)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointMaterial_v6"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.PointMaterial_v6](https://cables.gl/op/Ops.Gl.Shader.PointMaterial_v6)


### PositionAsColorMaterial
![PositionAsColorMaterial op](images/ops/Ops_Gl_Shader_PositionAsColorMaterial.svg)

**Full Name:** `Ops.Gl.Shader.PositionAsColorMaterial`

**Description:** draw meshes using XYZ position coordinates as RGB color

**> Input Ports:**

- **Render** (Trigger)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/qbiIbk)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PositionAsColorMaterial"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.PositionAsColorMaterial](https://cables.gl/op/Ops.Gl.Shader.PositionAsColorMaterial)


### SetShader
![SetShader op](images/ops/Ops_Gl_Shader_SetShader.svg)

**Full Name:** `Ops.Gl.Shader.SetShader`

**Description:** Reuse another shader at different points in the patch.

**> Input Ports:**

- **Render** (Trigger)
- **Shader** (Object)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/BweOVl)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SetShader"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.SetShader](https://cables.gl/op/Ops.Gl.Shader.SetShader)


### SetUniformFloat_v2
![SetUniformFloat_v2 op](images/ops/Ops_Gl_Shader_SetUniformFloat_v2.svg)

**Full Name:** `Ops.Gl.Shader.SetUniformFloat_v2`

**Description:** set a uniform value of the current shader

**> Input Ports:**

- **Render** (Trigger)
- **Uniform Index** (Number: Integer)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **W** (Number)

**< Output Ports:**

- **Next** (Trigger)
- **Type** (String)
- **Found** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/5W7X2f)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SetUniformFloat_v2"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.SetUniformFloat_v2](https://cables.gl/op/Ops.Gl.Shader.SetUniformFloat_v2)


### SetUniformTexture_v2
![SetUniformTexture_v2 op](images/ops/Ops_Gl_Shader_SetUniformTexture_v2.svg)

**Full Name:** `Ops.Gl.Shader.SetUniformTexture_v2`

**Description:** set a uniform value of the current shader

**> Input Ports:**

- **Render** (Trigger)
- **Uniform Index** (Number: Integer)
- **Texture** (Object:Texture)

**< Output Ports:**

- **Next** (Trigger)
- **Found** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/5W7X2f)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SetUniformTexture_v2"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.SetUniformTexture_v2](https://cables.gl/op/Ops.Gl.Shader.SetUniformTexture_v2)


### ShaderDefine
![ShaderDefine op](images/ops/Ops_Gl_Shader_ShaderDefine.svg)

**Full Name:** `Ops.Gl.Shader.ShaderDefine`

**Description:** Set shader defines

**> Input Ports:**

- **Shader** (Object)
- **Name** (String)
- **Value** (String)
- **Active** (Number: Boolean)
- **Public** (4): 1

**< Output Ports:**

- *Visit [Ops.Gl.Shader.ShaderDefine documentation](https://cables.gl/op/Ops.Gl.Shader.ShaderDefine) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Shader.ShaderDefine#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ShaderDefine"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.ShaderDefine](https://cables.gl/op/Ops.Gl.Shader.ShaderDefine)


### ShaderInfo
![ShaderInfo op](images/ops/Ops_Gl_Shader_ShaderInfo.svg)

**Full Name:** `Ops.Gl.Shader.ShaderInfo`

**Description:** view current shader source code

**> Input Ports:**

- **Exec** (Trigger)
- **Show Fragment** (Trigger)
- **Show Vertex** (Trigger)
- **Show Modules** (Trigger)
- **Show Uniforms** (Trigger)
- **State Info** (Trigger)

**< Output Ports:**

- **Next** (Trigger)
- **Source Frag** (String)
- **Source Vert** (String)
- **Name** (String)
- **Id** (String)
- **NeedsBarycentric** (booleanNumber)
- **Num Uniforms** (Number)
- **Num Attributes** (Number)
- **Arributes Names** (Array)
- **Num Defines** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Shader.ShaderInfo#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ShaderInfo"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.ShaderInfo](https://cables.gl/op/Ops.Gl.Shader.ShaderInfo)


### ShaderInfoUniforms_v2
![ShaderInfoUniforms_v2 op](images/ops/Ops_Gl_Shader_ShaderInfoUniforms_v2.svg)

**Full Name:** `Ops.Gl.Shader.ShaderInfoUniforms_v2`

**Description:** read back all uniforms values of the current bound shader

**> Input Ports:**

- **Exec** (Trigger)

**< Output Ports:**

- **Next** (Trigger)
- **Uniforms** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Shader.ShaderInfoUniforms_v2#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ShaderInfoUniforms_v2"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.ShaderInfoUniforms_v2](https://cables.gl/op/Ops.Gl.Shader.ShaderInfoUniforms_v2)


### ShaderToTexture_v2
![ShaderToTexture_v2 op](images/ops/Ops_Gl_Shader_ShaderToTexture_v2.svg)

**Full Name:** `Ops.Gl.Shader.ShaderToTexture_v2`

**Description:** render a shader into a texture

**> Input Ports:**

- **Render** (Trigger)
- **Shader** (Object:Shader)
- **Width** (Number: Integer)
- **Height** (Number: Integer)
- **Filter Index** (Number: Integer)
- **Wrap Index** (Number: Integer)
- **Pixel Format Index** (Number: Integer)

**< Output Ports:**

- **Next** (Trigger)
- **Texture** (Object)
- **Texture 2** (Object)
- **Texture 3** (Object)
- **Texture 4** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/vWyGud)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ShaderToTexture_v2"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.ShaderToTexture_v2](https://cables.gl/op/Ops.Gl.Shader.ShaderToTexture_v2)


### VertexColorMaterial
![VertexColorMaterial op](images/ops/Ops_Gl_Shader_VertexColorMaterial.svg)

**Full Name:** `Ops.Gl.Shader.VertexColorMaterial`

**Description:** Draw a mesh, showing only its vertex colors

**> Input Ports:**

- **Render** (Trigger)
- **Opacity** (Number)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/6MsLhR)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "VertexColorMaterial"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.VertexColorMaterial](https://cables.gl/op/Ops.Gl.Shader.VertexColorMaterial)


### VertexNumberMaterial
![VertexNumberMaterial op](images/ops/Ops_Gl_Shader_VertexNumberMaterial.svg)

**Full Name:** `Ops.Gl.Shader.VertexNumberMaterial`

**Description:** visually debug vertices of your 3D geometry

**> Input Ports:**

- **Render** (Trigger)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/x2PmHf)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "VertexNumberMaterial"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.VertexNumberMaterial](https://cables.gl/op/Ops.Gl.Shader.VertexNumberMaterial)


### WireframeMaterial_v2
![WireframeMaterial_v2 op](images/ops/Ops_Gl_Shader_WireframeMaterial_v2.svg)

**Full Name:** `Ops.Gl.Shader.WireframeMaterial_v2`

**Description:** Renders following meshes as wireframes

**> Input Ports:**

- **Render** (Trigger)
- **Enable Depth Testing** (Number: Boolean)
- **Width** (Number)
- **AntiAlias** (Number)
- **Diffuse R** (Number)
- **Diffuse G** (Number)
- **Diffuse B** (Number)
- **Diffuse A** (Number)
- **Fill** (Number: Boolean)
- **Fill R** (Number)
- **Fill G** (Number)
- **Fill B** (Number)
- **Fill A** (Number)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/bRlSDe)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WireframeMaterial_v2"*

**Docs:** [https://cables.gl/op/Ops.Gl.Shader.WireframeMaterial_v2](https://cables.gl/op/Ops.Gl.Shader.WireframeMaterial_v2)


