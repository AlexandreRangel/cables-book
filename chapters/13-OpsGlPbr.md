# Ops.Gl.Pbr

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.Pbr

### PbrEnvironmentLight
![PbrEnvironmentLight op](images/ops/Ops_Gl_Pbr_PbrEnvironmentLight.svg)

**Full Name:** `Ops.Gl.Pbr.PbrEnvironmentLight`
**Description:** PBR image based lighting setup

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Intensity** (Number): *See documentation*
- **RGBE Environment Map** (Object:Texture): *See documentation*
- **Size Irradiance Map Index** (Number: Integer): *See documentation*
- **Size Pre-Filtered Environment Index** (Number: Integer): *See documentation*
- **Size IBL LUT Index** (Number: Integer): *See documentation*
- **Force 8bit IBL** (Number: Boolean): *See documentation*
- **Rotation** (Number): *See documentation*
- **Use Parallax Correction** (Number: Boolean): *See documentation*
- **Center X** (Number): *See documentation*
- **Center Y** (Number): *See documentation*
- **Center Z** (Number): *See documentation*
- **Box Min X** (Number): *See documentation*
- **Box Min Y** (Number): *See documentation*
- **Box Min Z** (Number): *See documentation*
- **Box Max X** (Number): *See documentation*
- **Box Max Y** (Number): *See documentation*
- **Box Max Z** (Number): *See documentation*

**< Output Ports:**
- **Render** (Trigger): *See documentation*
- **Intensity** (Number): *See documentation*
- **RGBE Environment Map** (Object:Texture): *See documentation*
- **Size Irradiance Map Index** (Number: Integer): *See documentation*
- **Size Pre-Filtered Environment Index** (Number: Integer): *See documentation*
- **Size IBL LUT Index** (Number: Integer): *See documentation*
- **Force 8bit IBL** (Number: Boolean): *See documentation*
- **Rotation** (Number): *See documentation*
- **Use Parallax Correction** (Number: Boolean): *See documentation*
- **Center X** (Number): *See documentation*
- **Center Y** (Number): *See documentation*
- **Center Z** (Number): *See documentation*
- **Box Min X** (Number): *See documentation*
- **Box Min Y** (Number): *See documentation*
- **Box Min Z** (Number): *See documentation*
- **Box Max X** (Number): *See documentation*
- **Box Max Y** (Number): *See documentation*
- **Box Max Z** (Number): *See documentation*
- **Next** (Trigger): *See documentation*
- **IBL LUT** (Object): *See documentation*
- **for PBR Material** (not required): *See documentation*
- **Number Of Pre-Filtered Mip Levels** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/9z9kFK)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PbrEnvironmentLight"*
**Docs:** [https://cables.gl/op/Ops.Gl.Pbr.PbrEnvironmentLight](https://cables.gl/op/Ops.Gl.Pbr.PbrEnvironmentLight)

---

### PbrMaterial
![PbrMaterial op](images/ops/Ops_Gl_Pbr_PbrMaterial.svg)

**Full Name:** `Ops.Gl.Pbr.PbrMaterial`
**Description:** PBR/Physical Based Rendering Material for realistic materials

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*
- **Roughness** (Number): *See documentation*
- **Metalness** (Number): *See documentation*
- **Use Clear Coat** (Number: Boolean): *See documentation*
- **Clear Coat Intensity** (Number): *See documentation*
- **Clear Coat Roughness** (Number): *See documentation*
- **Use Normal Map For Clear Coat** (Number: Boolean): *See documentation*
- **Clear Coat Normal Map** (Object:Texture): *See documentation*
- **Use Thin Film** (Number: Boolean): *See documentation*
- **Thin Film Intensity** (Number): *See documentation*
- **Thin Film IOR** (Number): *See documentation*
- **Thickness Tex Min** (Number): *See documentation*
- **Thickness Tex Max** (Number): *See documentation*
- **Exposure** (Number): *See documentation*
- **Emission Intensity** (Number): *See documentation*
- **Disable Geometric Roughness** (Number: Boolean): *See documentation*
- **Use Roughness From Normal Map** (Number: Boolean): *See documentation*
- **Use Vertex Colours** (Number: Boolean): *See documentation*
- **Height Intensity** (Number): *See documentation*
- **Faster Heightmapping** (Number: Boolean): *See documentation*
- **Double Sided** (Number: Boolean): *See documentation*
- **IBL LUT** (Object:Texture): *See documentation*
- **Diffuse Irradiance** (Object:Texture): *See documentation*
- **Pre-Filtered Envmap** (Object:Texture): *See documentation*
- **Num Mip Levels** (Number: Integer): *See documentation*
- **Albedo** (Object:Texture): *See documentation*
- **AORM** (Object:Texture): *See documentation*
- **Normal Map** (Object:Texture): *See documentation*
- **Emission** (Object:Texture): *See documentation*
- **Height** (Object:Texture): *See documentation*
- **Lightmap** (Object:Texture): *See documentation*
- **Thin Film** (Object:Texture): *See documentation*
- **Diffuse Intensity** (Number): *See documentation*
- **Specular Intensity** (Number): *See documentation*
- **Lightmap Is RGBE** (Number: Boolean): *See documentation*
- **Lightmap Intensity** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Shader** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/9z9kFK)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PbrMaterial"*
**Docs:** [https://cables.gl/op/Ops.Gl.Pbr.PbrMaterial](https://cables.gl/op/Ops.Gl.Pbr.PbrMaterial)

---

