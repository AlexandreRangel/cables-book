# Ops.Gl.CubeMap

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.CubeMap

### CubeMapFromTextures_v2
![CubeMapFromTextures_v2 op](images/ops/Ops_Gl_CubeMap_CubeMapFromTextures_v2.svg)

**Full Name:** `Ops.Gl.CubeMap.CubeMapFromTextures_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.CubeMap.CubeMapFromTextures_v2) for details*

**> Input Ports:**
- **Posx** (String)
- **Negx** (String)
- **Posy** (String)
- **Negy** (String)
- **Posz** (String)
- **Negz** (String)
- **Flip Y** (Number: Boolean)

**< Output Ports:**
- **Cubemap** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.CubeMap.CubeMapFromTextures_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CubeMapFromTextures_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.CubeMap.CubeMapFromTextures_v2](https://cables.gl/op/Ops.Gl.CubeMap.CubeMapFromTextures_v2)

---

### CubeMapMaterial_v2
![CubeMapMaterial_v2 op](images/ops/Ops_Gl_CubeMap_CubeMapMaterial_v2.svg)

**Full Name:** `Ops.Gl.CubeMap.CubeMapMaterial_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.CubeMap.CubeMapMaterial_v2) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Cubemap** (Object)
- **Use Reflection** (Number: Boolean)
- **Blur** (Number)
- **Rotation** (Number)
- **Flip X** (Number: Boolean)
- **Flip Y** (Number: Boolean)
- **Flip Z** (Number: Boolean)
- **Colorize** (Number: Boolean)
- **R** (Number)
- **G** (Number)
- **B** (Number)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.CubeMap.CubeMapMaterial_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CubeMapMaterial_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.CubeMap.CubeMapMaterial_v2](https://cables.gl/op/Ops.Gl.CubeMap.CubeMapMaterial_v2)

---

### CubemapToEquirectangularTexture_v2
![CubemapToEquirectangularTexture_v2 op](images/ops/Ops_Gl_CubeMap_CubemapToEquirectangularTexture_v2.svg)

**Full Name:** `Ops.Gl.CubeMap.CubemapToEquirectangularTexture_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.CubeMap.CubemapToEquirectangularTexture_v2) for details*

**> Input Ports:**
- **In Trigger** (Trigger)
- **Cubemap** (Object)
- **Projection Index** (Number: Integer)
- **Format Index** (Number: Integer)
- **Filter Index** (Number: Integer)
- **Width** (Number: Integer)
- **Height** (Number: Integer)

**< Output Ports:**
- **Out Trigger** (Trigger)
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.CubeMap.CubemapToEquirectangularTexture_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CubemapToEquirectangularTexture_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.CubeMap.CubemapToEquirectangularTexture_v2](https://cables.gl/op/Ops.Gl.CubeMap.CubemapToEquirectangularTexture_v2)

---

### EquirectangularTextureToCubemap
![EquirectangularTextureToCubemap op](images/ops/Ops_Gl_CubeMap_EquirectangularTextureToCubemap.svg)

**Full Name:** `Ops.Gl.CubeMap.EquirectangularTextureToCubemap`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.CubeMap.EquirectangularTextureToCubemap) for details*

**> Input Ports:**
- **Trigger In** (Trigger)
- **Equirectangular Map** (Object:Texture)
- **Cubemap Size Index** (Number: Integer)
- **Advanced** (Number: Boolean)
- **Filter Index** (Number: Integer)

**< Output Ports:**
- **Trigger Out** (Trigger)
- **Cubemap Projection** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.CubeMap.EquirectangularTextureToCubemap#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "EquirectangularTextureToCubemap"*
**Docs:** [https://cables.gl/op/Ops.Gl.CubeMap.EquirectangularTextureToCubemap](https://cables.gl/op/Ops.Gl.CubeMap.EquirectangularTextureToCubemap)

---

### RenderToCubemap_v3
![RenderToCubemap_v3 op](images/ops/Ops_Gl_CubeMap_RenderToCubemap_v3.svg)

**Full Name:** `Ops.Gl.CubeMap.RenderToCubemap_v3`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.CubeMap.RenderToCubemap_v3) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Size Index** (Number: Integer)
- **Pixel Format Index** (Number: Integer)
- **MSAA Index** (Number: Integer)

**< Output Ports:**
- **Next** (Trigger)
- **Cubemap** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.CubeMap.RenderToCubemap_v3#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RenderToCubemap_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.CubeMap.RenderToCubemap_v3](https://cables.gl/op/Ops.Gl.CubeMap.RenderToCubemap_v3)

---

### Skybox
![Skybox op](images/ops/Ops_Gl_CubeMap_Skybox.svg)

**Full Name:** `Ops.Gl.CubeMap.Skybox`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.CubeMap.Skybox) for details*

**> Input Ports:**
- **Trigger In** (Trigger)
- **Render** (Number: Boolean)
- **Skybox** (Object:Texture)
- **Rotate** (Number)
- **RGBE Format** (Number: Boolean)
- **Exposure** (Number)
- **Gamma** (Number)

**< Output Ports:**
- **Trigger Out** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.CubeMap.Skybox#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Skybox"*
**Docs:** [https://cables.gl/op/Ops.Gl.CubeMap.Skybox](https://cables.gl/op/Ops.Gl.CubeMap.Skybox)

---

