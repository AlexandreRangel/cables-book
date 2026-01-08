# Ops.Gl.ShaderEffects


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### AreaDiscardPixel_v2
![AreaDiscardPixel_v2 op](images/ops/Ops_Gl_ShaderEffects_AreaDiscardPixel_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.AreaDiscardPixel_v2`

do not draw pixels inside a defined 3d area.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Invert** (Number: Boolean)
- **Area Index** (Number: Integer)
- **Area** (Number: String)
- **Size** (Number)
- **Size X** (Number)
- **Size Y** (Number)
- **Size Z** (Number)
- **Repeat** (Number: Boolean)
- **Repeat Distance** (Number)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **WorldSpace** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/GQiw18](https://cables.gl/edit/GQiw18)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.AreaDiscardPixel_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.AreaDiscardPixel_v2)

### AreaRotate_v2
![AreaRotate_v2 op](images/ops/Ops_Gl_ShaderEffects_AreaRotate_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.AreaRotate_v2`

rotate vertices in an area around a center point.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Size** (Number)
- **Strength** (Number)
- **Smooth** (Number: Boolean)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/7mss1Q](https://cables.gl/edit/7mss1Q)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.AreaRotate_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.AreaRotate_v2)

### AreaScaler_v3
![AreaScaler_v3 op](images/ops/Ops_Gl_ShaderEffects_AreaScaler_v3.svg)

**Full Name:** `Ops.Gl.ShaderEffects.AreaScaler_v3`

Scales the size of meshes within the area of influence.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Area Size** (Number)
- **Source Index** (Number: Integer)
- **Strength** (Number)
- **Smoothstep** (Number: Boolean)
- **Min Size Original** (Number: Boolean)
- **Clamp Size** (Number: Boolean)
- **Clamp Min** (Number)
- **Clamp Max** (Number)
- **Pos X** (Number)
- **Pos Y** (Number)
- **Pos Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/LXN7D-](https://cables.gl/edit/LXN7D-)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.AreaScaler_v3](https://cables.gl/op/Ops.Gl.ShaderEffects.AreaScaler_v3)

### AreaTranslateFBMNoise
![AreaTranslateFBMNoise op](images/ops/Ops_Gl_ShaderEffects_AreaTranslateFBMNoise.svg)

**Full Name:** `Ops.Gl.ShaderEffects.AreaTranslateFBMNoise`

Area size of noise.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Mode Index** (Number: Integer)
- **Size** (Number)
- **Strength** (Number)
- **Smooth** (Number: Boolean)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Noise Scale** (Number)
- **Noise X** (Number)
- **Noise Y** (Number)
- **Noise Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/hDcUC-](https://cables.gl/edit/hDcUC-)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.AreaTranslateFBMNoise](https://cables.gl/op/Ops.Gl.ShaderEffects.AreaTranslateFBMNoise)

### AreaTranslateMeshes_v3
![AreaTranslateMeshes_v3 op](images/ops/Ops_Gl_ShaderEffects_AreaTranslateMeshes_v3.svg)

**Full Name:** `Ops.Gl.ShaderEffects.AreaTranslateMeshes_v3`

Change the position of all meshes inside of the area of influence.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Size** (Number)
- **Strength** (Number)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Multiply X** (Number)
- **Multiply Y** (Number)
- **Multiply Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/yWVQC-](https://cables.gl/edit/yWVQC-)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.AreaTranslateMeshes_v3](https://cables.gl/op/Ops.Gl.ShaderEffects.AreaTranslateMeshes_v3)

### Bend_v2
![Bend_v2 op](images/ops/Ops_Gl_ShaderEffects_Bend_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.Bend_v2`

bend objects along an axis.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Amount** (Number)
- **RotX** (Number)
- **RotY** (Number)
- **RotZ** (Number)
- **Scale** (Number)
- **Offset** (Number)
- **Limited** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/HtcN9Z](https://cables.gl/edit/HtcN9Z)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.Bend_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.Bend_v2)

### ClampVertexPosition_v2
![ClampVertexPosition_v2 op](images/ops/Ops_Gl_ShaderEffects_ClampVertexPosition_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.ClampVertexPosition_v2`

clamp/restrict the vertex position to min/max values per axis.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Axis Index** (Number: Integer)
- **Min** (Number)
- **Max** (Number)
- **Update Normals** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/RP4O73](https://cables.gl/edit/RP4O73)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.ClampVertexPosition_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.ClampVertexPosition_v2)

### ColorArea_v5
![ColorArea_v5 op](images/ops/Ops_Gl_ShaderEffects_ColorArea_v5.svg)

**Full Name:** `Ops.Gl.ShaderEffects.ColorArea_v5`

Colorize all meshes around current position.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Area Index** (Number: Integer)
- **Size** (Number)
- **Roundness** (Number)
- **Amount** (Number)
- **Falloff** (Number)
- **Invert** (Number: Boolean)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Change Size** (Number: Boolean)
- **Size X** (Number)
- **Size Y** (Number)
- **Size Z** (Number)
- **Texture** (Object:Texture)
- **Priority** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/0Ti2gT](https://cables.gl/edit/0Ti2gT)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.ColorArea_v5](https://cables.gl/op/Ops.Gl.ShaderEffects.ColorArea_v5)

### DeformArea
![DeformArea op](images/ops/Ops_Gl_ShaderEffects_DeformArea.svg)

**Full Name:** `Ops.Gl.ShaderEffects.DeformArea`

deform a spherical area of a mesh.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Size** (Number)
- **Strength** (Number)
- **Smooth** (Number: Boolean)
- **WorldSpace** (Number: Boolean)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/CQ0wmo](https://cables.gl/edit/CQ0wmo)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.DeformArea](https://cables.gl/op/Ops.Gl.ShaderEffects.DeformArea)

### DiscardMaterialAlpha
![DiscardMaterialAlpha op](images/ops/Ops_Gl_ShaderEffects_DiscardMaterialAlpha.svg)

**Full Name:** `Ops.Gl.ShaderEffects.DiscardMaterialAlpha`

discard transparent pixels in material textures.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Method Index** (Number: Integer)
- **Threshold** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/3r_lf6](https://cables.gl/edit/3r_lf6)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.DiscardMaterialAlpha](https://cables.gl/op/Ops.Gl.ShaderEffects.DiscardMaterialAlpha)

### ExplodeDividedMesh_v2
![ExplodeDividedMesh_v2 op](images/ops/Ops_Gl_ShaderEffects_ExplodeDividedMesh_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.ExplodeDividedMesh_v2`

explode a (divided) mesh in the direction of faces normals.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Distance** (Number)
- **Size** (Number)
- **Absolute** (Number: Boolean)
- **Add X** (Number)
- **Add Y** (Number)
- **Add Z** (Number)
- **Mul X** (Number)
- **Mul Y** (Number)
- **Mul Z** (Number)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/sYIxm1](https://cables.gl/edit/sYIxm1)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.ExplodeDividedMesh_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.ExplodeDividedMesh_v2)

### FogEffect
![FogEffect op](images/ops/Ops_Gl_ShaderEffects_FogEffect.svg)

**Full Name:** `Ops.Gl.ShaderEffects.FogEffect`

Fog as a shadereffect applied to a material.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Mode Index** (Number: Integer)
- **Start** (Number)
- **End** (Number)
- **Amount** (Number)
- **R** (Number)
- **G** (Number)
- **B** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/3L3of6](https://cables.gl/edit/3L3of6)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.FogEffect](https://cables.gl/op/Ops.Gl.ShaderEffects.FogEffect)

### FresnelGlow
![FresnelGlow op](images/ops/Ops_Gl_ShaderEffects_FresnelGlow.svg)

**Full Name:** `Ops.Gl.ShaderEffects.FresnelGlow`

add fresnel glow to any material.

**`\inputsymbol`{=latex} Inputs**

- **Trigger In** (Trigger)
- **Active** (Number: Boolean)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **Fresnel Intensity** (Number)
- **Fresnel Exponent** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger Out** (Trigger)

**Example Patch:** [cables.gl/edit/e02kYa](https://cables.gl/edit/e02kYa)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.FresnelGlow](https://cables.gl/op/Ops.Gl.ShaderEffects.FresnelGlow)

### InstancedDisplacementMap_v2
![InstancedDisplacementMap_v2 op](images/ops/Ops_Gl_ShaderEffects_InstancedDisplacementMap_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.InstancedDisplacementMap_v2`

displace positions of instanced meshes using a texture.

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Texture** (Object:Texture)
- **Source Index** (Number: Integer)
- **Mode Index** (Number: Integer)
- **Strength** (Number)
- **Min** (Number)
- **Scale** (Number)
- **Clamp** (Number: Boolean)
- **Colorize** (Number: Boolean)
- **Debug Bounds** (Number: Boolean)
- **Normalize** (Number: Boolean)
- **Offset X** (Number)
- **Offset Y** (Number)
- **Abs** (Number: Boolean)
- **Channel Index** (Number: Integer)
- **X** (Number: Boolean)
- **Y** (Number: Boolean)
- **Z** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/yQJfFj](https://cables.gl/edit/yQJfFj)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.InstancedDisplacementMap_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.InstancedDisplacementMap_v2)

### InstancedPerlinPosition_v2
![InstancedPerlinPosition_v2 op](images/ops/Ops_Gl_ShaderEffects_InstancedPerlinPosition_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.InstancedPerlinPosition_v2`

displace position of instanced object by perlin noise value.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Strength** (Number)
- **Scroll X** (Number)
- **Scroll Y** (Number)
- **Scroll Z** (Number)
- **Scale** (Number)
- **Method Index** (Number: Integer)
- **Method** (String)
- **Mul X** (Number)
- **Mul Y** (Number)
- **Mul Z** (Number)
- **Min Scale** (Number)
- **WorldSpace** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/33bSY7](https://cables.gl/edit/33bSY7)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.InstancedPerlinPosition_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.InstancedPerlinPosition_v2)

### InstancedTextureColorize
![InstancedTextureColorize op](images/ops/Ops_Gl_ShaderEffects_InstancedTextureColorize.svg)

**Full Name:** `Ops.Gl.ShaderEffects.InstancedTextureColorize`

colorize instanced meshes using a texture.

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Texture** (Object:Texture)
- **Strength** (Number)
- **Scale** (Number)
- **Clamp** (Number: Boolean)
- **Debug Bounds** (Number: Boolean)
- **Offset X** (Number)
- **Offset Y** (Number)
- **Method Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/yQJfFj](https://cables.gl/edit/yQJfFj)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.InstancedTextureColorize](https://cables.gl/op/Ops.Gl.ShaderEffects.InstancedTextureColorize)

### LimitMeshByTexCoord
![LimitMeshByTexCoord op](images/ops/Ops_Gl_ShaderEffects_LimitMeshByTexCoord.svg)

**Full Name:** `Ops.Gl.ShaderEffects.LimitMeshByTexCoord`

discard pixel if texture coordinate is below threshold.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Axis Index** (Number: Integer)
- **Treshhold** (Number)
- **Sine Animation** (Number: Boolean)
- **Time** (Number)
- **Sine Source Index** (Number: Integer)
- **Frequency** (Number)
- **Amplitude** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/pHfgJ5](https://cables.gl/edit/pHfgJ5)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.LimitMeshByTexCoord](https://cables.gl/op/Ops.Gl.ShaderEffects.LimitMeshByTexCoord)

### MeshPixelNoise_v2
![MeshPixelNoise_v2 op](images/ops/Ops_Gl_ShaderEffects_MeshPixelNoise_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.MeshPixelNoise_v2`

3d space noise for mesh materials.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Scale** (Number)
- **Amount** (Number)
- **Blendmode Index** (Number: Integer)
- **Blendmode** (String)
- **WorldSpace** (Number: Boolean)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/V7rjQ6](https://cables.gl/edit/V7rjQ6)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.MeshPixelNoise_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.MeshPixelNoise_v2)

### ModuloVertexPosition
![ModuloVertexPosition op](images/ops/Ops_Gl_ShaderEffects_ModuloVertexPosition.svg)

**Full Name:** `Ops.Gl.ShaderEffects.ModuloVertexPosition`

vertex shader modulo operation on vertex position.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Axis Index** (Number: Integer)
- **Modulo** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/lMCl_8](https://cables.gl/edit/lMCl_8)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.ModuloVertexPosition](https://cables.gl/op/Ops.Gl.ShaderEffects.ModuloVertexPosition)

### PerlinAreaDeform_v4
![PerlinAreaDeform_v4 op](images/ops/Ops_Gl_ShaderEffects_PerlinAreaDeform_v4.svg)

**Full Name:** `Ops.Gl.ShaderEffects.PerlinAreaDeform_v4`

Displace vertices using perlin noise animation.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Scale** (Number)
- **Size** (Number)
- **Strength** (Number)
- **Calc Normals** (Number: Boolean)
- **Flip Normals** (Number: Boolean)
- **Falloff** (Number)
- **Output Index** (Number: Integer)
- **Source Index** (Number: Integer)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Scroll X** (Number)
- **Scroll Y** (Number)
- **Scroll Z** (Number)
- **WorldSpace** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/8RexP8](https://cables.gl/edit/8RexP8)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.PerlinAreaDeform_v4](https://cables.gl/op/Ops.Gl.ShaderEffects.PerlinAreaDeform_v4)

### ScaleByNormal_v2
![ScaleByNormal_v2 op](images/ops/Ops_Gl_ShaderEffects_ScaleByNormal_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.ScaleByNormal_v2`

Scale vertices of an object in the direction of face normals.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Strength** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/Ft2xm1](https://cables.gl/edit/Ft2xm1)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.ScaleByNormal_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.ScaleByNormal_v2)

### Shadow_v3
![Shadow_v3 op](images/ops/Ops_Gl_ShaderEffects_Shadow_v3.svg)

**Full Name:** `Ops.Gl.ShaderEffects.Shadow_v3`

add shadow capabilities to any material.

**`\inputsymbol`{=latex} Inputs**

- **Trigger In** (Trigger)
- **Cast Shadow** (Number: Boolean)
- **Receive Shadow** (Number: Boolean)
- **Sample Distribution** (Number: Integer)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **Discard Transparent** (Number: Boolean)
- **Opacity Threshold** (Number)
- **Opacity Texture** (Object:Texture)
- **Cull Backfacing** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Trigger Out** (Trigger)

**Example Patch:** [cables.gl/edit/auVl18](https://cables.gl/edit/auVl18)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.Shadow_v3](https://cables.gl/op/Ops.Gl.ShaderEffects.Shadow_v3)

### SplineDeform_v2
![SplineDeform_v2 op](images/ops/Ops_Gl_ShaderEffects_SplineDeform_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.SplineDeform_v2`

Deform a mesh along a spline.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Size** (Number)
- **Offset** (Number)
- **Points** (Array)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/F-UNZ4](https://cables.gl/edit/F-UNZ4)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.SplineDeform_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.SplineDeform_v2)

### TextureProjection_v2
![TextureProjection_v2 op](images/ops/Ops_Gl_ShaderEffects_TextureProjection_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.TextureProjection_v2`

texture projection on meshes.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Texture** (Object:Texture)
- **BlendMode Index** (Number: Integer)
- **Amount** (Number)
- **Scale** (Number)
- **Use Texture Alpha** (Number: Boolean)
- **Pos X** (Number)
- **Pos Y** (Number)
- **Rot X** (Number)
- **Rot Y** (Number)
- **Rot Z** (Number)
- **Mapping Index** (Number: Integer)
- **Discard** (Number: Boolean)
- **WorldSpace** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/fJHt0e](https://cables.gl/edit/fJHt0e)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.TextureProjection_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.TextureProjection_v2)

### TransformTextureCoordinates
![TransformTextureCoordinates op](images/ops/Ops_Gl_ShaderEffects_TransformTextureCoordinates.svg)

**Full Name:** `Ops.Gl.ShaderEffects.TransformTextureCoordinates`

Transform and repeat texture coordinates of a mesh via vertex shader.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Translate X** (Number)
- **Translate Y** (Number)
- **Repeat X** (Number)
- **Repeat Y** (Number)
- **Flip X** (Number: Boolean)
- **Flip Y** (Number: Boolean)
- **Rotation** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/YzNrx8](https://cables.gl/edit/YzNrx8)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.TransformTextureCoordinates](https://cables.gl/op/Ops.Gl.ShaderEffects.TransformTextureCoordinates)

### TransformVertex
![TransformVertex op](images/ops/Ops_Gl_ShaderEffects_TransformVertex.svg)

**Full Name:** `Ops.Gl.ShaderEffects.TransformVertex`

transform vertices of a mesh via vertex shader.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Translate X** (Number)
- **Translate Y** (Number)
- **Translate Z** (Number)
- **Scale X** (Number)
- **Scale Y** (Number)
- **Scale Z** (Number)
- **Rotation X** (Number)
- **Rotation Y** (Number)
- **Rotation Z** (Number)
- **Transform Normals** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/u1iOhI](https://cables.gl/edit/u1iOhI)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.TransformVertex](https://cables.gl/op/Ops.Gl.ShaderEffects.TransformVertex)

### Twist_v3
![Twist_v3 op](images/ops/Ops_Gl_ShaderEffects_Twist_v3.svg)

**Full Name:** `Ops.Gl.ShaderEffects.Twist_v3`

twist a mesh around an axis.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Degree** (Number)
- **Height** (Number)
- **Axis Index** (Number: Integer)
- **Axis** (Number: String)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/VYPlJ5](https://cables.gl/edit/VYPlJ5)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.Twist_v3](https://cables.gl/op/Ops.Gl.ShaderEffects.Twist_v3)

### UseVertexColor
![UseVertexColor op](images/ops/Ops_Gl_ShaderEffects_UseVertexColor.svg)

**Full Name:** `Ops.Gl.ShaderEffects.UseVertexColor`

Use vertex color as basecolor/diffuse color.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/ep1Umu](https://cables.gl/edit/ep1Umu)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.UseVertexColor](https://cables.gl/op/Ops.Gl.ShaderEffects.UseVertexColor)

### VertexArea
![VertexArea op](images/ops/Ops_Gl_ShaderEffects_VertexArea.svg)

**Full Name:** `Ops.Gl.ShaderEffects.VertexArea`

transform an area of a mesh.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Area Index** (Number: Integer)
- **Visualize Area** (Number: Boolean)
- **WorldSpace** (Number: Boolean)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Radius** (Number)
- **Area Size X** (Number)
- **Area Size Y** (Number)
- **Area Size Z** (Number)
- **Translate X** (Number)
- **Translate Y** (Number)
- **Translate Z** (Number)
- **Scale X** (Number)
- **Scale Y** (Number)
- **Scale Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/op/Ops.Gl.ShaderEffects.VertexArea#example](https://cables.gl/op/Ops.Gl.ShaderEffects.VertexArea#example)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.VertexArea](https://cables.gl/op/Ops.Gl.ShaderEffects.VertexArea)

### VertexColorAsAlpha
![VertexColorAsAlpha op](images/ops/Ops_Gl_ShaderEffects_VertexColorAsAlpha.svg)

**Full Name:** `Ops.Gl.ShaderEffects.VertexColorAsAlpha`

Use mesh vertexcolor as Alpha/Opacity.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Input Index** (Number: Integer)
- **Invert** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/ChcFXk](https://cables.gl/edit/ChcFXk)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.VertexColorAsAlpha](https://cables.gl/op/Ops.Gl.ShaderEffects.VertexColorAsAlpha)

### VertexDisplacementMap_v5
![VertexDisplacementMap_v5 op](images/ops/Ops_Gl_ShaderEffects_VertexDisplacementMap_v5.svg)

**Full Name:** `Ops.Gl.ShaderEffects.VertexDisplacementMap_v5`

Displace the vertices of a mesh with the pixels brightness values from a texture.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Extrude** (Number)
- **Texture** (Object:Texture)
- **Offset X** (Number)
- **Offset Y** (Number)
- **Scale** (Number)
- **Calc Normals** (Number: Boolean)
- **Discard Zero Values** (Number: Boolean)
- **Colorize** (Number: Boolean)
- **Colorize Min** (Number)
- **Colorize Max** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/aSWlLu](https://cables.gl/edit/aSWlLu)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.VertexDisplacementMap_v5](https://cables.gl/op/Ops.Gl.ShaderEffects.VertexDisplacementMap_v5)

### VertexNumberLimit_v2
![VertexNumberLimit_v2 op](images/ops/Ops_Gl_ShaderEffects_VertexNumberLimit_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.VertexNumberLimit_v2`

only draw the first X vertices of a mesh.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Min** (Number: Integer)
- **Max** (Number: Integer)
- **Invert** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/gLrrJV](https://cables.gl/edit/gLrrJV)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.VertexNumberLimit_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.VertexNumberLimit_v2)

### VertexPositionFromTexture_v2
![VertexPositionFromTexture_v2 op](images/ops/Ops_Gl_ShaderEffects_VertexPositionFromTexture_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.VertexPositionFromTexture_v2`

set vertex positions of a mesh from a texture.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Texture** (Object:Texture)
- **Mode Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/LDfZgL](https://cables.gl/edit/LDfZgL)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.VertexPositionFromTexture_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.VertexPositionFromTexture_v2)

### VertexWobble_v2
![VertexWobble_v2 op](images/ops/Ops_Gl_ShaderEffects_VertexWobble_v2.svg)

**Full Name:** `Ops.Gl.ShaderEffects.VertexWobble_v2`

sine wave vertex displacement.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Source Index** (Number: Integer)
- **Amount** (Number)
- **Time** (Number)
- **Scale** (Number)
- **AxisX** (Number: Boolean)
- **AxisY** (Number: Boolean)
- **AxisZ** (Number: Boolean)
- **Area Index** (Number: Integer)
- **Size** (Number)
- **Falloff** (Number)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **WorldSpace** (Number: Boolean)
- **Invert** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/0PxhuO](https://cables.gl/edit/0PxhuO)

**Doc:** [cables.gl/op/Ops.Gl.ShaderEffects.VertexWobble_v2](https://cables.gl/op/Ops.Gl.ShaderEffects.VertexWobble_v2)


