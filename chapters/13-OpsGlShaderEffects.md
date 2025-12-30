# Ops.Gl.ShaderEffects

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.ShaderEffects

### AreaDiscardPixel_v2
![AreaDiscardPixel_v2 op](images/ops/Ops_Gl_ShaderEffects_AreaDiscardPixel_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.AreaDiscardPixel_v2`
**Description:** do not draw pixels inside a defined 3d area

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Invert** (Number: Boolean): *See documentation*
- **Area Index** (Number: Integer): *See documentation*
- **Area** (Number: String): *See documentation*
- **Size** (Number): *See documentation*
- **Size X** (Number): *See documentation*
- **Size Y** (Number): *See documentation*
- **Size Z** (Number): *See documentation*
- **Repeat** (Number: Boolean): *See documentation*
- **Repeat Distance** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **WorldSpace** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/GQiw18)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AreaDiscardPixel_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.AreaDiscardPixel_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.AreaDiscardPixel_v2)

---

### AreaRotate_v2
![AreaRotate_v2 op](images/ops/Ops_Gl_ShaderEffects_AreaRotate_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.AreaRotate_v2`
**Description:** rotate vertices in an area around a center point

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Size** (Number): *See documentation*
- **Strength** (Number): *See documentation*
- **Smooth** (Number: Boolean): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/7mss1Q)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AreaRotate_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.AreaRotate_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.AreaRotate_v2)

---

### AreaScaler_v3
![AreaScaler_v3 op](images/ops/Ops_Gl_ShaderEffects_AreaScaler_v3.svg)

**Full Name:** `Ops.Gl.ShaderEffects.AreaScaler_v3`
**Description:** Scales the size of meshes within the area of influence

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Area Size** (Number): *See documentation*
- **Source Index** (Number: Integer): *See documentation*
- **Strength** (Number): *See documentation*
- **Smoothstep** (Number: Boolean): *See documentation*
- **Min Size Original** (Number: Boolean): *See documentation*
- **Clamp Size** (Number: Boolean): *See documentation*
- **Clamp Min** (Number): *See documentation*
- **Clamp Max** (Number): *See documentation*
- **Pos X** (Number): *See documentation*
- **Pos Y** (Number): *See documentation*
- **Pos Z** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/LXN7D-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AreaScaler_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.AreaScaler_v3](https://cables.gl/op/Ops.Gl.ShaderEffects.AreaScaler_v3)

---

### AreaTranslateFBMNoise
![AreaTranslateFBMNoise op](images/ops/Ops_Gl_ShaderEffects_AreaTranslateFBMNoise.svg)

**Full Name:** `Ops.Gl.ShaderEffects.AreaTranslateFBMNoise`
**Description:** Area size of noise

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Mode Index** (Number: Integer): *See documentation*
- **Size** (Number): *See documentation*
- **Strength** (Number): *See documentation*
- **Smooth** (Number: Boolean): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **Noise Scale** (Number): *See documentation*
- **Noise X** (Number): *See documentation*
- **Noise Y** (Number): *See documentation*
- **Noise Z** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/hDcUC-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AreaTranslateFBMNoise"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.AreaTranslateFBMNoise](https://cables.gl/op/Ops.Gl.ShaderEffects.AreaTranslateFBMNoise)

---

### AreaTranslateMeshes_v3
![AreaTranslateMeshes_v3 op](images/ops/Ops_Gl_ShaderEffects_AreaTranslateMeshes_v3.svg)

**Full Name:** `Ops.Gl.ShaderEffects.AreaTranslateMeshes_v3`
**Description:** Change the position of all meshes inside of the area of influence

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Size** (Number): *See documentation*
- **Strength** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **Multiply X** (Number): *See documentation*
- **Multiply Y** (Number): *See documentation*
- **Multiply Z** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/yWVQC-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AreaTranslateMeshes_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.AreaTranslateMeshes_v3](https://cables.gl/op/Ops.Gl.ShaderEffects.AreaTranslateMeshes_v3)

---

### Bend_v2
![Bend_v2 op](images/ops/Ops_Gl_ShaderEffects_Bend_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.Bend_v2`
**Description:** bend objects along an axis

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Amount** (Number): *See documentation*
- **RotX** (Number): *See documentation*
- **RotY** (Number): *See documentation*
- **RotZ** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **Offset** (Number): *See documentation*
- **Limited** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/HtcN9Z)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Bend_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.Bend_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.Bend_v2)

---

### ClampVertexPosition_v2
![ClampVertexPosition_v2 op](images/ops/Ops_Gl_ShaderEffects_ClampVertexPosition_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.ClampVertexPosition_v2`
**Description:** clamp/restrict the vertex position to min/max values per axis

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Axis Index** (Number: Integer): *See documentation*
- **Min** (Number): *See documentation*
- **Max** (Number): *See documentation*
- **Update Normals** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/RP4O73)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ClampVertexPosition_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.ClampVertexPosition_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.ClampVertexPosition_v2)

---

### ColorArea_v5
![ColorArea_v5 op](images/ops/Ops_Gl_ShaderEffects_ColorArea_v5.svg)

**Full Name:** `Ops.Gl.ShaderEffects.ColorArea_v5`
**Description:** Colorize all meshes around current position

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Area Index** (Number: Integer): *See documentation*
- **Size** (Number): *See documentation*
- **Roundness** (Number): *See documentation*
- **Amount** (Number): *See documentation*
- **Falloff** (Number): *See documentation*
- **Invert** (Number: Boolean): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **Change Size** (Number: Boolean): *See documentation*
- **Size X** (Number): *See documentation*
- **Size Y** (Number): *See documentation*
- **Size Z** (Number): *See documentation*
- **Texture** (Object:Texture): *See documentation*
- **Priority** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/0Ti2gT)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorArea_v5"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.ColorArea_v5](https://cables.gl/op/Ops.Gl.ShaderEffects.ColorArea_v5)

---

### DeformArea
![DeformArea op](images/ops/Ops_Gl_ShaderEffects_DeformArea.svg)

**Full Name:** `Ops.Gl.ShaderEffects.DeformArea`
**Description:** deform a spherical area of a mesh

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Size** (Number): *See documentation*
- **Strength** (Number): *See documentation*
- **Smooth** (Number: Boolean): *See documentation*
- **WorldSpace** (Number: Boolean): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/CQ0wmo)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DeformArea"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.DeformArea](https://cables.gl/op/Ops.Gl.ShaderEffects.DeformArea)

---

### DiscardMaterialAlpha
![DiscardMaterialAlpha op](images/ops/Ops_Gl_ShaderEffects_DiscardMaterialAlpha.svg)

**Full Name:** `Ops.Gl.ShaderEffects.DiscardMaterialAlpha`
**Description:** discard transparent pixels in material textures

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Method Index** (Number: Integer): *See documentation*
- **Threshold** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/3r_lf6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DiscardMaterialAlpha"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.DiscardMaterialAlpha](https://cables.gl/op/Ops.Gl.ShaderEffects.DiscardMaterialAlpha)

---

### ExplodeDividedMesh_v2
![ExplodeDividedMesh_v2 op](images/ops/Ops_Gl_ShaderEffects_ExplodeDividedMesh_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.ExplodeDividedMesh_v2`
**Description:** explode a (divided) mesh in the direction of faces normals

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Distance** (Number): *See documentation*
- **Size** (Number): *See documentation*
- **Absolute** (Number: Boolean): *See documentation*
- **Add X** (Number): *See documentation*
- **Add Y** (Number): *See documentation*
- **Add Z** (Number): *See documentation*
- **Mul X** (Number): *See documentation*
- **Mul Y** (Number): *See documentation*
- **Mul Z** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/sYIxm1)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ExplodeDividedMesh_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.ExplodeDividedMesh_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.ExplodeDividedMesh_v2)

---

### FogEffect
![FogEffect op](images/ops/Ops_Gl_ShaderEffects_FogEffect.svg)

**Full Name:** `Ops.Gl.ShaderEffects.FogEffect`
**Description:** Fog as a shadereffect applied to a material

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Mode Index** (Number: Integer): *See documentation*
- **Start** (Number): *See documentation*
- **End** (Number): *See documentation*
- **Amount** (Number): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/3L3of6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FogEffect"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.FogEffect](https://cables.gl/op/Ops.Gl.ShaderEffects.FogEffect)

---

### FresnelGlow
![FresnelGlow op](images/ops/Ops_Gl_ShaderEffects_FresnelGlow.svg)

**Full Name:** `Ops.Gl.ShaderEffects.FresnelGlow`
**Description:** add fresnel glow to any material

**> Input Ports:**
- **Trigger In** (Trigger): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **Fresnel Intensity** (Number): *See documentation*
- **Fresnel Exponent** (Number): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/e02kYa)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FresnelGlow"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.FresnelGlow](https://cables.gl/op/Ops.Gl.ShaderEffects.FresnelGlow)

---

### InstancedDisplacementMap_v2
![InstancedDisplacementMap_v2 op](images/ops/Ops_Gl_ShaderEffects_InstancedDisplacementMap_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.InstancedDisplacementMap_v2`
**Description:** displace positions of instanced meshes using a texture

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **Texture** (Object:Texture): *See documentation*
- **Source Index** (Number: Integer): *See documentation*
- **Mode Index** (Number: Integer): *See documentation*
- **Strength** (Number): *See documentation*
- **Min** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **Clamp** (Number: Boolean): *See documentation*
- **Colorize** (Number: Boolean): *See documentation*
- **Debug Bounds** (Number: Boolean): *See documentation*
- **Normalize** (Number: Boolean): *See documentation*
- **Offset X** (Number): *See documentation*
- **Offset Y** (Number): *See documentation*
- **Abs** (Number: Boolean): *See documentation*
- **Channel Index** (Number: Integer): *See documentation*
- **X** (Number: Boolean): *See documentation*
- **Y** (Number: Boolean): *See documentation*
- **Z** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/yQJfFj)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InstancedDisplacementMap_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.InstancedDisplacementMap_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.InstancedDisplacementMap_v2)

---

### InstancedPerlinPosition_v2
![InstancedPerlinPosition_v2 op](images/ops/Ops_Gl_ShaderEffects_InstancedPerlinPosition_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.InstancedPerlinPosition_v2`
**Description:** displace position of instanced object by perlin noise value

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Strength** (Number): *See documentation*
- **Scroll X** (Number): *See documentation*
- **Scroll Y** (Number): *See documentation*
- **Scroll Z** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **Method Index** (Number: Integer): *See documentation*
- **Method** (String): *See documentation*
- **Mul X** (Number): *See documentation*
- **Mul Y** (Number): *See documentation*
- **Mul Z** (Number): *See documentation*
- **Min Scale** (Number): *See documentation*
- **WorldSpace** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/33bSY7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InstancedPerlinPosition_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.InstancedPerlinPosition_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.InstancedPerlinPosition_v2)

---

### InstancedTextureColorize
![InstancedTextureColorize op](images/ops/Ops_Gl_ShaderEffects_InstancedTextureColorize.svg)

**Full Name:** `Ops.Gl.ShaderEffects.InstancedTextureColorize`
**Description:** colorize instanced meshes using a texture

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **Texture** (Object:Texture): *See documentation*
- **Strength** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **Clamp** (Number: Boolean): *See documentation*
- **Debug Bounds** (Number: Boolean): *See documentation*
- **Offset X** (Number): *See documentation*
- **Offset Y** (Number): *See documentation*
- **Method Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/yQJfFj)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InstancedTextureColorize"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.InstancedTextureColorize](https://cables.gl/op/Ops.Gl.ShaderEffects.InstancedTextureColorize)

---

### LimitMeshByTexCoord
![LimitMeshByTexCoord op](images/ops/Ops_Gl_ShaderEffects_LimitMeshByTexCoord.svg)

**Full Name:** `Ops.Gl.ShaderEffects.LimitMeshByTexCoord`
**Description:** discard pixel if texture coordinate is below threshold

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Axis Index** (Number: Integer): *See documentation*
- **Treshhold** (Number): *See documentation*
- **Sine Animation** (Number: Boolean): *See documentation*
- **Time** (Number): *See documentation*
- **Sine Source Index** (Number: Integer): *See documentation*
- **Frequency** (Number): *See documentation*
- **Amplitude** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/pHfgJ5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LimitMeshByTexCoord"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.LimitMeshByTexCoord](https://cables.gl/op/Ops.Gl.ShaderEffects.LimitMeshByTexCoord)

---

### MeshPixelNoise_v2
![MeshPixelNoise_v2 op](images/ops/Ops_Gl_ShaderEffects_MeshPixelNoise_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.MeshPixelNoise_v2`
**Description:** 3d space noise for mesh materials

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Scale** (Number): *See documentation*
- **Amount** (Number): *See documentation*
- **Blendmode Index** (Number: Integer): *See documentation*
- **Blendmode** (String): *See documentation*
- **WorldSpace** (Number: Boolean): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/V7rjQ6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MeshPixelNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.MeshPixelNoise_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.MeshPixelNoise_v2)

---

### ModuloVertexPosition
![ModuloVertexPosition op](images/ops/Ops_Gl_ShaderEffects_ModuloVertexPosition.svg)

**Full Name:** `Ops.Gl.ShaderEffects.ModuloVertexPosition`
**Description:** vertex shader modulo operation on vertex position

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Axis Index** (Number: Integer): *See documentation*
- **Modulo** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/lMCl_8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ModuloVertexPosition"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.ModuloVertexPosition](https://cables.gl/op/Ops.Gl.ShaderEffects.ModuloVertexPosition)

---

### PerlinAreaDeform_v4
![PerlinAreaDeform_v4 op](images/ops/Ops_Gl_ShaderEffects_PerlinAreaDeform_v4.svg)

**Full Name:** `Ops.Gl.ShaderEffects.PerlinAreaDeform_v4`
**Description:** Displace vertices using perlin noise animation

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Scale** (Number): *See documentation*
- **Size** (Number): *See documentation*
- **Strength** (Number): *See documentation*
- **Calc Normals** (Number: Boolean): *See documentation*
- **Flip Normals** (Number: Boolean): *See documentation*
- **Falloff** (Number): *See documentation*
- **Output Index** (Number: Integer): *See documentation*
- **Source Index** (Number: Integer): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **Scroll X** (Number): *See documentation*
- **Scroll Y** (Number): *See documentation*
- **Scroll Z** (Number): *See documentation*
- **WorldSpace** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/8RexP8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PerlinAreaDeform_v4"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.PerlinAreaDeform_v4](https://cables.gl/op/Ops.Gl.ShaderEffects.PerlinAreaDeform_v4)

---

### ScaleByNormal_v2
![ScaleByNormal_v2 op](images/ops/Ops_Gl_ShaderEffects_ScaleByNormal_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.ScaleByNormal_v2`
**Description:** Scale vertices of an object in the direction of face normals

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Strength** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Ft2xm1)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScaleByNormal_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.ScaleByNormal_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.ScaleByNormal_v2)

---

### Shadow_v3
![Shadow_v3 op](images/ops/Ops_Gl_ShaderEffects_Shadow_v3.svg)

**Full Name:** `Ops.Gl.ShaderEffects.Shadow_v3`
**Description:** add shadow capabilities to any material

**> Input Ports:**
- **Trigger In** (Trigger): *See documentation*
- **Cast Shadow** (Number: Boolean): *See documentation*
- **Receive Shadow** (Number: Boolean): *See documentation*
- **Sample Distribution** (Number: Integer): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **Discard Transparent** (Number: Boolean): *See documentation*
- **Opacity Threshold** (Number): *See documentation*
- **Opacity Texture** (Object:Texture): *See documentation*
- **Cull Backfacing** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/auVl18)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Shadow_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.Shadow_v3](https://cables.gl/op/Ops.Gl.ShaderEffects.Shadow_v3)

---

### SplineDeform_v2
![SplineDeform_v2 op](images/ops/Ops_Gl_ShaderEffects_SplineDeform_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.SplineDeform_v2`
**Description:** Deform a mesh along a spline

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Size** (Number): *See documentation*
- **Offset** (Number): *See documentation*
- **Points** (Array): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/F-UNZ4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SplineDeform_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.SplineDeform_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.SplineDeform_v2)

---

### TextureProjection_v2
![TextureProjection_v2 op](images/ops/Ops_Gl_ShaderEffects_TextureProjection_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.TextureProjection_v2`
**Description:** texture projection on meshes

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Texture** (Object:Texture): *See documentation*
- **BlendMode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **Use Texture Alpha** (Number: Boolean): *See documentation*
- **Pos X** (Number): *See documentation*
- **Pos Y** (Number): *See documentation*
- **Rot X** (Number): *See documentation*
- **Rot Y** (Number): *See documentation*
- **Rot Z** (Number): *See documentation*
- **Mapping Index** (Number: Integer): *See documentation*
- **Discard** (Number: Boolean): *See documentation*
- **WorldSpace** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/fJHt0e)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureProjection_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.TextureProjection_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.TextureProjection_v2)

---

### TransformTextureCoordinates
![TransformTextureCoordinates op](images/ops/Ops_Gl_ShaderEffects_TransformTextureCoordinates.svg)

**Full Name:** `Ops.Gl.ShaderEffects.TransformTextureCoordinates`
**Description:** Transform and repeat texture coordinates of a mesh via vertex shader

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Translate X** (Number): *See documentation*
- **Translate Y** (Number): *See documentation*
- **Repeat X** (Number): *See documentation*
- **Repeat Y** (Number): *See documentation*
- **Flip X** (Number: Boolean): *See documentation*
- **Flip Y** (Number: Boolean): *See documentation*
- **Rotation** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/YzNrx8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TransformTextureCoordinates"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.TransformTextureCoordinates](https://cables.gl/op/Ops.Gl.ShaderEffects.TransformTextureCoordinates)

---

### TransformVertex
![TransformVertex op](images/ops/Ops_Gl_ShaderEffects_TransformVertex.svg)

**Full Name:** `Ops.Gl.ShaderEffects.TransformVertex`
**Description:** transform vertices of a mesh via vertex shader

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Translate X** (Number): *See documentation*
- **Translate Y** (Number): *See documentation*
- **Translate Z** (Number): *See documentation*
- **Scale X** (Number): *See documentation*
- **Scale Y** (Number): *See documentation*
- **Scale Z** (Number): *See documentation*
- **Rotation X** (Number): *See documentation*
- **Rotation Y** (Number): *See documentation*
- **Rotation Z** (Number): *See documentation*
- **Transform Normals** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/u1iOhI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TransformVertex"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.TransformVertex](https://cables.gl/op/Ops.Gl.ShaderEffects.TransformVertex)

---

### Twist_v3
![Twist_v3 op](images/ops/Ops_Gl_ShaderEffects_Twist_v3.svg)

**Full Name:** `Ops.Gl.ShaderEffects.Twist_v3`
**Description:** twist a mesh around an axis

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Degree** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Axis Index** (Number: Integer): *See documentation*
- **Axis** (Number: String): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/VYPlJ5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Twist_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.Twist_v3](https://cables.gl/op/Ops.Gl.ShaderEffects.Twist_v3)

---

### UseVertexColor
![UseVertexColor op](images/ops/Ops_Gl_ShaderEffects_UseVertexColor.svg)

**Full Name:** `Ops.Gl.ShaderEffects.UseVertexColor`
**Description:** Use vertex color as basecolor/diffuse color

**> Input Ports:**
- **Render** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ep1Umu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "UseVertexColor"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.UseVertexColor](https://cables.gl/op/Ops.Gl.ShaderEffects.UseVertexColor)

---

### VertexArea
![VertexArea op](images/ops/Ops_Gl_ShaderEffects_VertexArea.svg)

**Full Name:** `Ops.Gl.ShaderEffects.VertexArea`
**Description:** transform an area of a mesh

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Area Index** (Number: Integer): *See documentation*
- **Visualize Area** (Number: Boolean): *See documentation*
- **WorldSpace** (Number: Boolean): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **Radius** (Number): *See documentation*
- **Area Size X** (Number): *See documentation*
- **Area Size Y** (Number): *See documentation*
- **Area Size Z** (Number): *See documentation*
- **Translate X** (Number): *See documentation*
- **Translate Y** (Number): *See documentation*
- **Translate Z** (Number): *See documentation*
- **Scale X** (Number): *See documentation*
- **Scale Y** (Number): *See documentation*
- **Scale Z** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.ShaderEffects.VertexArea#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "VertexArea"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.VertexArea](https://cables.gl/op/Ops.Gl.ShaderEffects.VertexArea)

---

### VertexColorAsAlpha
![VertexColorAsAlpha op](images/ops/Ops_Gl_ShaderEffects_VertexColorAsAlpha.svg)

**Full Name:** `Ops.Gl.ShaderEffects.VertexColorAsAlpha`
**Description:** Use mesh vertexcolor as Alpha/Opacity

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Input Index** (Number: Integer): *See documentation*
- **Invert** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ChcFXk)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "VertexColorAsAlpha"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.VertexColorAsAlpha](https://cables.gl/op/Ops.Gl.ShaderEffects.VertexColorAsAlpha)

---

### VertexDisplacementMap_v5
![VertexDisplacementMap_v5 op](images/ops/Ops_Gl_ShaderEffects_VertexDisplacementMap_v5.svg)

**Full Name:** `Ops.Gl.ShaderEffects.VertexDisplacementMap_v5`
**Description:** Displace the vertices of a mesh with the pixels brightness values from a texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Extrude** (Number): *See documentation*
- **Texture** (Object:Texture): *See documentation*
- **Offset X** (Number): *See documentation*
- **Offset Y** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **Calc Normals** (Number: Boolean): *See documentation*
- **Discard Zero Values** (Number: Boolean): *See documentation*
- **Colorize** (Number: Boolean): *See documentation*
- **Colorize Min** (Number): *See documentation*
- **Colorize Max** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/aSWlLu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "VertexDisplacementMap_v5"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.VertexDisplacementMap_v5](https://cables.gl/op/Ops.Gl.ShaderEffects.VertexDisplacementMap_v5)

---

### VertexNumberLimit_v2
![VertexNumberLimit_v2 op](images/ops/Ops_Gl_ShaderEffects_VertexNumberLimit_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.VertexNumberLimit_v2`
**Description:** only draw the first X vertices of a mesh

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Min** (Number: Integer): *See documentation*
- **Max** (Number: Integer): *See documentation*
- **Invert** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/gLrrJV)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "VertexNumberLimit_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.VertexNumberLimit_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.VertexNumberLimit_v2)

---

### VertexPositionFromTexture_v2
![VertexPositionFromTexture_v2 op](images/ops/Ops_Gl_ShaderEffects_VertexPositionFromTexture_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.VertexPositionFromTexture_v2`
**Description:** set vertex positions of a mesh from a texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Texture** (Object:Texture): *See documentation*
- **Mode Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/LDfZgL)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "VertexPositionFromTexture_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.VertexPositionFromTexture_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.VertexPositionFromTexture_v2)

---

### VertexWobble_v2
![VertexWobble_v2 op](images/ops/Ops_Gl_ShaderEffects_VertexWobble_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.VertexWobble_v2`
**Description:** sine wave vertex displacement

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Source Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Time** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **AxisX** (Number: Boolean): *See documentation*
- **AxisY** (Number: Boolean): *See documentation*
- **AxisZ** (Number: Boolean): *See documentation*
- **Area Index** (Number: Integer): *See documentation*
- **Size** (Number): *See documentation*
- **Falloff** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **WorldSpace** (Number: Boolean): *See documentation*
- **Invert** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/0PxhuO)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "VertexWobble_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShaderEffects.VertexWobble_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.VertexWobble_v2)

---

