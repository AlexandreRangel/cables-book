# Ops.Gl.Shader

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.Shader

### AttributeAsColorMaterial
![AttributeAsColorMaterial op](images/ops/Ops_Gl_Shader_AttributeAsColorMaterial.svg)

**Full Name:** `Ops.Gl.Shader.AttributeAsColorMaterial`
**Description:** render mesh normals as colors

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Absolute** (Number: Boolean): *See documentation*
- **World Space** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Shader** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/bZEZGc)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AttributeAsColorMaterial"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.AttributeAsColorMaterial](https://cables.gl/op/Ops.Gl.Shader.AttributeAsColorMaterial)

---

### BasicMaterial_v3
![BasicMaterial_v3 op](images/ops/Ops_Gl_Shader_BasicMaterial_v3.svg)

**Full Name:** `Ops.Gl.Shader.BasicMaterial_v3`
**Description:** A material without shading

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*
- **Texture** (Object:Texture): *See documentation*
- **ColorizeTexture** (Number: Boolean): *See documentation*
- **Vertex Colors** (Number: Boolean): *See documentation*
- **TextureOpacity** (Object:Texture): *See documentation*
- **Opacity TexCoords Transform** (Number: Boolean): *See documentation*
- **Discard Transparent Pixels** (Number: Boolean): *See documentation*
- **DiffuseRepeatX** (Number): *See documentation*
- **DiffuseRepeatY** (Number): *See documentation*
- **Tex Offset X** (Number): *See documentation*
- **Tex Offset Y** (Number): *See documentation*
- **Crop TexCoords** (Number: Boolean): *See documentation*
- **Billboard** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Shader** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/SKCL88)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BasicMaterial_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.BasicMaterial_v3](https://cables.gl/op/Ops.Gl.Shader.BasicMaterial_v3)

---

### ChromaKeyMaterial
![ChromaKeyMaterial op](images/ops/Ops_Gl_Shader_ChromaKeyMaterial.svg)

**Full Name:** `Ops.Gl.Shader.ChromaKeyMaterial`
**Description:** display texture and replace a color with transparency

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Texture** (Object): *See documentation*
- **Mode Index** (Number: Integer): *See documentation*
- **WeightMul** (Number): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **White** (Number): *See documentation*
- **DiffuseRepeatX** (Number): *See documentation*
- **DiffuseRepeatY** (Number): *See documentation*
- **Tex Offset X** (Number): *See documentation*
- **Tex Offset Y** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/aDqoTq)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ChromaKeyMaterial"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.ChromaKeyMaterial](https://cables.gl/op/Ops.Gl.Shader.ChromaKeyMaterial)

---

### CustomShader_v2
![CustomShader_v2 op](images/ops/Ops_Gl_Shader_CustomShader_v2.svg)

**Full Name:** `Ops.Gl.Shader.CustomShader_v2`
**Description:** Write your own custom shader

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Fragment Code** (String): *See documentation*
- **Vertex Code** (String): *See documentation*
- **Use As Material** (Number: Boolean): *See documentation*
- **W** (Number): *See documentation*
- **H** (Number): *See documentation*
- **GPosition** (Object): *See documentation*
- **GNormal** (Object): *See documentation*
- **TexNoise** (Object): *See documentation*
- **Samples** (Array): *See documentation*
- **Projection** (Array): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Shader** (Object): *See documentation*
- **Has Errors** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/vWyGud)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CustomShader_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.CustomShader_v2](https://cables.gl/op/Ops.Gl.Shader.CustomShader_v2)

---

### ErrorMaterial
![ErrorMaterial op](images/ops/Ops_Gl_Shader_ErrorMaterial.svg)

**Full Name:** `Ops.Gl.Shader.ErrorMaterial`
**Description:** draw meshes using the cables error material shader

**> Input Ports:**
- **Render** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Shader.ErrorMaterial#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ErrorMaterial"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.ErrorMaterial](https://cables.gl/op/Ops.Gl.Shader.ErrorMaterial)

---

### FrontBacksideMaterial
![FrontBacksideMaterial op](images/ops/Ops_Gl_Shader_FrontBacksideMaterial.svg)

**Full Name:** `Ops.Gl.Shader.FrontBacksideMaterial`
**Description:** visualize which faces are facing the camera

**> Input Ports:**
- **Render** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Lm6p9r)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FrontBacksideMaterial"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.FrontBacksideMaterial](https://cables.gl/op/Ops.Gl.Shader.FrontBacksideMaterial)

---

### GetShader
![GetShader op](images/ops/Ops_Gl_Shader_GetShader.svg)

**Full Name:** `Ops.Gl.Shader.GetShader`
**Description:** get current set shader

**> Input Ports:**
- **Update** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Shader** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/BweOVl)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetShader"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.GetShader](https://cables.gl/op/Ops.Gl.Shader.GetShader)

---

### MatCapMaterial_v3
![MatCapMaterial_v3 op](images/ops/Ops_Gl_Shader_MatCapMaterial_v3.svg)

**Full Name:** `Ops.Gl.Shader.MatCapMaterial_v3`
**Description:** Easy to use image based lighting Material

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **MatCap** (Object:Texture): *See documentation*
- **Diffuse** (Object:Texture): *See documentation*
- **Normal** (Object:Texture): *See documentation*
- **Specular Mask** (Object:Texture): *See documentation*
- **Specular MatCap** (Object:Texture): *See documentation*
- **AO Texture** (Object:Texture): *See documentation*
- **Opacity Texture** (Object:Texture): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **Opacity** (Number): *See documentation*
- **AO Intensity** (Number): *See documentation*
- **Normal Map Intensity** (Number): *See documentation*
- **Repeat X** (Number): *See documentation*
- **Repeat Y** (Number): *See documentation*
- **Offset X** (Number): *See documentation*
- **Offset Y** (Number): *See documentation*
- **Double Sided** (Number: Boolean): *See documentation*
- **Screen Space Normals** (Number: Boolean): *See documentation*
- **check to use screen space normals** (flat shading): *See documentation*
- **Calc Normal Tangents** (Number: Boolean): *See documentation*
- **Opacity TexCoords Transform** (Number: Boolean): *See documentation*
- **Discard Transparent Pixels** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Shader** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/gWkghi)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MatCapMaterial_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.MatCapMaterial_v3](https://cables.gl/op/Ops.Gl.Shader.MatCapMaterial_v3)

---

### MinifyGlsl
![MinifyGlsl op](images/ops/Ops_Gl_Shader_MinifyGlsl.svg)

**Full Name:** `Ops.Gl.Shader.MinifyGlsl`
**Description:** Minify GLSL shader source code

**> Input Ports:**
- **Shader Source** (String): *See documentation*

**< Output Ports:**
- **Minified Shader Source** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/t5H1Qc)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MinifyGlsl"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.MinifyGlsl](https://cables.gl/op/Ops.Gl.Shader.MinifyGlsl)

---

### PointMaterial_v6
![PointMaterial_v6 op](images/ops/Ops_Gl_Shader_PointMaterial_v6.svg)

**Full Name:** `Ops.Gl.Shader.PointMaterial_v6`
**Description:** Draw all vertices as points / circles

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **PointSize** (Number): *See documentation*
- **Size In Pixels** (Number: Boolean): *See documentation*
- **Random Size** (Number): *See documentation*
- **Round** (Number: Boolean): *See documentation*
- **Round Antialias** (Number: Boolean): *See documentation*
- **Scale By Distance** (Number: Boolean): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*
- **Vertex Colors** (Number: Boolean): *See documentation*
- **Texture** (Object:Texture): *See documentation*
- **Colorize Texture** (Number: Boolean): *See documentation*
- **Texture Mask** (Object:Texture): *See documentation*
- **Texture Colorize** (Object:Texture): *See documentation*
- **Colorize Randomize** (Number: Boolean): *See documentation*
- **Texture Opacity** (Object:Texture): *See documentation*
- **Texture Point Size** (Object:Texture): *See documentation*
- **Texture Point Size Mul** (Number): *See documentation*
- **Flip Texture** (Number: Boolean): *See documentation*
- **Atlas Cross Fade** (Number: Boolean): *See documentation*
- **Atlas Repeat X** (Number): *See documentation*
- **Atlas Lookup** (Object:Texture): *See documentation*
- **Rotate Texture** (Object:Texture): *See documentation*
- **Min Point Size** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Shader** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/O9yRO6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointMaterial_v6"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.PointMaterial_v6](https://cables.gl/op/Ops.Gl.Shader.PointMaterial_v6)

---

### PositionAsColorMaterial
![PositionAsColorMaterial op](images/ops/Ops_Gl_Shader_PositionAsColorMaterial.svg)

**Full Name:** `Ops.Gl.Shader.PositionAsColorMaterial`
**Description:** draw meshes using XYZ position coordinates as RGB color

**> Input Ports:**
- **Render** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/qbiIbk)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PositionAsColorMaterial"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.PositionAsColorMaterial](https://cables.gl/op/Ops.Gl.Shader.PositionAsColorMaterial)

---

### SetShader
![SetShader op](images/ops/Ops_Gl_Shader_SetShader.svg)

**Full Name:** `Ops.Gl.Shader.SetShader`
**Description:** Reuse another shader at different points in the patch.

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Shader** (Object): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/BweOVl)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SetShader"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.SetShader](https://cables.gl/op/Ops.Gl.Shader.SetShader)

---

### SetUniformFloat_v2
![SetUniformFloat_v2 op](images/ops/Ops_Gl_Shader_SetUniformFloat_v2.svg)

**Full Name:** `Ops.Gl.Shader.SetUniformFloat_v2`
**Description:** set a uniform value of the current shader

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Uniform Index** (Number: Integer): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **W** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Type** (String): *See documentation*
- **Found** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/5W7X2f)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SetUniformFloat_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.SetUniformFloat_v2](https://cables.gl/op/Ops.Gl.Shader.SetUniformFloat_v2)

---

### SetUniformTexture_v2
![SetUniformTexture_v2 op](images/ops/Ops_Gl_Shader_SetUniformTexture_v2.svg)

**Full Name:** `Ops.Gl.Shader.SetUniformTexture_v2`
**Description:** set a uniform value of the current shader

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Uniform Index** (Number: Integer): *See documentation*
- **Texture** (Object:Texture): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Found** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/5W7X2f)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SetUniformTexture_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.SetUniformTexture_v2](https://cables.gl/op/Ops.Gl.Shader.SetUniformTexture_v2)

---

### ShaderDefine
![ShaderDefine op](images/ops/Ops_Gl_Shader_ShaderDefine.svg)

**Full Name:** `Ops.Gl.Shader.ShaderDefine`
**Description:** Set shader defines

**> Input Ports:**
- **Shader** (Object): *See documentation*
- **Name** (String): *See documentation*
- **Value** (String): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Public** (4): 1

**< Output Ports:**
- *Visit [Ops.Gl.Shader.ShaderDefine documentation](https://cables.gl/op/Ops.Gl.Shader.ShaderDefine) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Shader.ShaderDefine#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ShaderDefine"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.ShaderDefine](https://cables.gl/op/Ops.Gl.Shader.ShaderDefine)

---

### ShaderInfo
![ShaderInfo op](images/ops/Ops_Gl_Shader_ShaderInfo.svg)

**Full Name:** `Ops.Gl.Shader.ShaderInfo`
**Description:** view current shader source code

**> Input Ports:**
- **Exec** (Trigger): *See documentation*
- **Show Fragment** (Trigger): *See documentation*
- **Show Vertex** (Trigger): *See documentation*
- **Show Modules** (Trigger): *See documentation*
- **Show Uniforms** (Trigger): *See documentation*
- **State Info** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Source Frag** (String): *See documentation*
- **Source Vert** (String): *See documentation*
- **Name** (String): *See documentation*
- **Id** (String): *See documentation*
- **NeedsBarycentric** (booleanNumber): *See documentation*
- **Num Uniforms** (Number): *See documentation*
- **Num Attributes** (Number): *See documentation*
- **Arributes Names** (Array): *See documentation*
- **Num Defines** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Shader.ShaderInfo#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ShaderInfo"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.ShaderInfo](https://cables.gl/op/Ops.Gl.Shader.ShaderInfo)

---

### ShaderInfoUniforms_v2
![ShaderInfoUniforms_v2 op](images/ops/Ops_Gl_Shader_ShaderInfoUniforms_v2.svg)

**Full Name:** `Ops.Gl.Shader.ShaderInfoUniforms_v2`
**Description:** read back all uniforms values of the current bound shader

**> Input Ports:**
- **Exec** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Uniforms** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Shader.ShaderInfoUniforms_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ShaderInfoUniforms_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.ShaderInfoUniforms_v2](https://cables.gl/op/Ops.Gl.Shader.ShaderInfoUniforms_v2)

---

### ShaderToTexture_v2
![ShaderToTexture_v2 op](images/ops/Ops_Gl_Shader_ShaderToTexture_v2.svg)

**Full Name:** `Ops.Gl.Shader.ShaderToTexture_v2`
**Description:** render a shader into a texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Shader** (Object:Shader): *See documentation*
- **Width** (Number: Integer): *See documentation*
- **Height** (Number: Integer): *See documentation*
- **Filter Index** (Number: Integer): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Pixel Format Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Texture** (Object): *See documentation*
- **Texture 2** (Object): *See documentation*
- **Texture 3** (Object): *See documentation*
- **Texture 4** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/vWyGud)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ShaderToTexture_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.ShaderToTexture_v2](https://cables.gl/op/Ops.Gl.Shader.ShaderToTexture_v2)

---

### VertexColorMaterial
![VertexColorMaterial op](images/ops/Ops_Gl_Shader_VertexColorMaterial.svg)

**Full Name:** `Ops.Gl.Shader.VertexColorMaterial`
**Description:** Draw a mesh, showing only its vertex colors

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Opacity** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/6MsLhR)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "VertexColorMaterial"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.VertexColorMaterial](https://cables.gl/op/Ops.Gl.Shader.VertexColorMaterial)

---

### VertexNumberMaterial
![VertexNumberMaterial op](images/ops/Ops_Gl_Shader_VertexNumberMaterial.svg)

**Full Name:** `Ops.Gl.Shader.VertexNumberMaterial`
**Description:** visually debug vertices of your 3D geometry

**> Input Ports:**
- **Render** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/x2PmHf)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "VertexNumberMaterial"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.VertexNumberMaterial](https://cables.gl/op/Ops.Gl.Shader.VertexNumberMaterial)

---

### WireframeMaterial_v2
![WireframeMaterial_v2 op](images/ops/Ops_Gl_Shader_WireframeMaterial_v2.svg)

**Full Name:** `Ops.Gl.Shader.WireframeMaterial_v2`
**Description:** Renders following meshes as wireframes

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Enable Depth Testing** (Number: Boolean): *See documentation*
- **Width** (Number): *See documentation*
- **AntiAlias** (Number): *See documentation*
- **Diffuse R** (Number): *See documentation*
- **Diffuse G** (Number): *See documentation*
- **Diffuse B** (Number): *See documentation*
- **Diffuse A** (Number): *See documentation*
- **Fill** (Number: Boolean): *See documentation*
- **Fill R** (Number): *See documentation*
- **Fill G** (Number): *See documentation*
- **Fill B** (Number): *See documentation*
- **Fill A** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/bRlSDe)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WireframeMaterial_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Shader.WireframeMaterial_v2](https://cables.gl/op/Ops.Gl.Shader.WireframeMaterial_v2)

---

