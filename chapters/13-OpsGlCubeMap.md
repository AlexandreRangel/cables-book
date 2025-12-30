# Ops.Gl.CubeMap

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.CubeMap

### CubeMapFromTextures_v2
![CubeMapFromTextures_v2 op](images/ops/Ops_Gl_CubeMap_CubeMapFromTextures_v2.svg)

**Full Name:** `Ops.Gl.CubeMap.CubeMapFromTextures_v2`
**Description:** generate a cubemap from 6 textures

**> Input Ports:**
- **Posx** (String): *See documentation*
- **Negx** (String): *See documentation*
- **Posy** (String): *See documentation*
- **Negy** (String): *See documentation*
- **Posz** (String): *See documentation*
- **Negz** (String): *See documentation*
- **Flip Y** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Cubemap** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/-QPf26)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CubeMapFromTextures_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.CubeMap.CubeMapFromTextures_v2](https://cables.gl/op/Ops.Gl.CubeMap.CubeMapFromTextures_v2)

---

### CubeMapMaterial_v2
![CubeMapMaterial_v2 op](images/ops/Ops_Gl_CubeMap_CubeMapMaterial_v2.svg)

**Full Name:** `Ops.Gl.CubeMap.CubeMapMaterial_v2`
**Description:** use a cubemap or equirectangular texture as a material

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Cubemap** (Object): *See documentation*
- **Use Reflection** (Number: Boolean): *See documentation*
- **Blur** (Number): *See documentation*
- **Rotation** (Number): *See documentation*
- **Flip X** (Number: Boolean): *See documentation*
- **Flip Y** (Number: Boolean): *See documentation*
- **Flip Z** (Number: Boolean): *See documentation*
- **Colorize** (Number: Boolean): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/u5y0Z5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CubeMapMaterial_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.CubeMap.CubeMapMaterial_v2](https://cables.gl/op/Ops.Gl.CubeMap.CubeMapMaterial_v2)

---

### CubemapToEquirectangularTexture_v2
![CubemapToEquirectangularTexture_v2 op](images/ops/Ops_Gl_CubeMap_CubemapToEquirectangularTexture_v2.svg)

**Full Name:** `Ops.Gl.CubeMap.CubemapToEquirectangularTexture_v2`
**Description:** visualize cubemap as folded texture or equirectangular texture

**> Input Ports:**
- **In Trigger** (Trigger): *See documentation*
- **Cubemap** (Object): *See documentation*
- **Projection Index** (Number: Integer): *See documentation*
- **Format Index** (Number: Integer): *See documentation*
- **Filter Index** (Number: Integer): *See documentation*
- **Width** (Number: Integer): *See documentation*
- **Height** (Number: Integer): *See documentation*

**< Output Ports:**
- **Out Trigger** (Trigger): *See documentation*
- **Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/pNZHYa)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CubemapToEquirectangularTexture_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.CubeMap.CubemapToEquirectangularTexture_v2](https://cables.gl/op/Ops.Gl.CubeMap.CubemapToEquirectangularTexture_v2)

---

### EquirectangularTextureToCubemap
![EquirectangularTextureToCubemap op](images/ops/Ops_Gl_CubeMap_EquirectangularTextureToCubemap.svg)

**Full Name:** `Ops.Gl.CubeMap.EquirectangularTextureToCubemap`
**Description:** convert an equirectangular map to a cubemap

**> Input Ports:**
- **Trigger In** (Trigger): *See documentation*
- **Equirectangular Map** (Object:Texture): *See documentation*
- **Cubemap Size Index** (Number: Integer): *See documentation*
- **Advanced** (Number: Boolean): *See documentation*
- **Filter Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*
- **Cubemap Projection** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/O1NBYa)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "EquirectangularTextureToCubemap"*
**Docs:** [https://cables.gl/op/Ops.Gl.CubeMap.EquirectangularTextureToCubemap](https://cables.gl/op/Ops.Gl.CubeMap.EquirectangularTextureToCubemap)

---

### RenderToCubemap_v3
![RenderToCubemap_v3 op](images/ops/Ops_Gl_CubeMap_RenderToCubemap_v3.svg)

**Full Name:** `Ops.Gl.CubeMap.RenderToCubemap_v3`
**Description:** render a scene into a cubemap

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Size Index** (Number: Integer): *See documentation*
- **Pixel Format Index** (Number: Integer): *See documentation*
- **MSAA Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Cubemap** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Z3KuUQ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RenderToCubemap_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.CubeMap.RenderToCubemap_v3](https://cables.gl/op/Ops.Gl.CubeMap.RenderToCubemap_v3)

---

### Skybox
![Skybox op](images/ops/Ops_Gl_CubeMap_Skybox.svg)

**Full Name:** `Ops.Gl.CubeMap.Skybox`
**Description:** render an equirectangular map or a cubemap as scene background

**> Input Ports:**
- **Trigger In** (Trigger): *See documentation*
- **Render** (Number: Boolean): *See documentation*
- **Skybox** (Object:Texture): *See documentation*
- **Rotate** (Number): *See documentation*
- **RGBE Format** (Number: Boolean): *See documentation*
- **Exposure** (Number): *See documentation*
- **Gamma** (Number): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/40hoYa)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Skybox"*
**Docs:** [https://cables.gl/op/Ops.Gl.CubeMap.Skybox](https://cables.gl/op/Ops.Gl.CubeMap.Skybox)

---

