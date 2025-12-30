# Ops.Gl.Phong

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.Phong

### AmbientLight_v4
![AmbientLight_v4 op](images/ops/Ops_Gl_Phong_AmbientLight_v4.svg)

**Full Name:** `Ops.Gl.Phong.AmbientLight_v4`
**Description:** ambient light for phong material shading

**> Input Ports:**
- **Trigger In** (Trigger): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **Intensity** (Number): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/g3ioXU)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AmbientLight_v4"*
**Docs:** [https://cables.gl/op/Ops.Gl.Phong.AmbientLight_v4](https://cables.gl/op/Ops.Gl.Phong.AmbientLight_v4)

---

### DirectionalLight_v5
![DirectionalLight_v5 op](images/ops/Ops_Gl_Phong_DirectionalLight_v5.svg)

**Full Name:** `Ops.Gl.Phong.DirectionalLight_v5`
**Description:** Directional light for phong shading

**> Input Ports:**
- **Trigger In** (Trigger): *See documentation*
- **Cast Light** (Number: Boolean): *See documentation*
- **Intensity** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **Specular R** (Number): *See documentation*
- **Specular G** (Number): *See documentation*
- **Specular B** (Number): *See documentation*
- **Cast Shadow** (Number: Boolean): *See documentation*
- **Rendering Active** (Number: Boolean): *See documentation*
- **Map Size Index** (Number: Integer): *See documentation*
- **Map Size** (String): *See documentation*
- **Shadow Strength** (Number): *See documentation*
- **LR-BottomTop** (Number): *See documentation*
- **Near** (Number): *See documentation*
- **Far** (Number): *See documentation*
- **Bias** (Number): *See documentation*
- **Polygon Offset** (Number: Integer): *See documentation*
- **Normal Offset** (Number): *See documentation*
- **Blur Amount** (Number): *See documentation*
- **Enable Advanced** (Number: Boolean): *See documentation*
- **MSAA Index** (Number: Integer): *See documentation*
- **MSAA** (String): *See documentation*
- **Texture Filter Index** (Number: Integer): *See documentation*
- **Texture Filter** (String): *See documentation*
- **Anisotropic Index** (Number: Integer): *See documentation*
- **Anisotropic** (String): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*
- **Shadow Map** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/nEWpXU)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DirectionalLight_v5"*
**Docs:** [https://cables.gl/op/Ops.Gl.Phong.DirectionalLight_v5](https://cables.gl/op/Ops.Gl.Phong.DirectionalLight_v5)

---

### LambertMaterial_v2
![LambertMaterial_v2 op](images/ops/Ops_Gl_Phong_LambertMaterial_v2.svg)

**Full Name:** `Ops.Gl.Phong.LambertMaterial_v2`
**Description:** a simple shaded material

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Diffuse R** (Number): *See documentation*
- **Diffuse G** (Number): *See documentation*
- **Diffuse B** (Number): *See documentation*
- **Diffuse A** (Number): *See documentation*
- **Diffuse Texture** (Object:Texture): *See documentation*
- **Colorize Texture** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Shader** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/PAvm26)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LambertMaterial_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Phong.LambertMaterial_v2](https://cables.gl/op/Ops.Gl.Phong.LambertMaterial_v2)

---

### PhongMaterial_v6
![PhongMaterial_v6 op](images/ops/Ops_Gl_Phong_PhongMaterial_v6.svg)

**Full Name:** `Ops.Gl.Phong.PhongMaterial_v6`
**Description:** A shaded material for lighting objects

**> Input Ports:**
- **Trigger In** (Trigger): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*
- **Albedo** (Number): *See documentation*
- **Roughness** (Number): *See documentation*
- **Fresnel Intensity** (Number): *See documentation*
- **Fresnel Width** (Number): *See documentation*
- **Fresnel Exponent** (Number): *See documentation*
- **Fresnel R** (Number): *See documentation*
- **Fresnel G** (Number): *See documentation*
- **Fresnel B** (Number): *See documentation*
- **Emissive Active** (Number: Boolean): *See documentation*
- **Color Intensity** (Number): *See documentation*
- **Emissive R** (Number): *See documentation*
- **Emissive G** (Number): *See documentation*
- **Emissive B** (Number): *See documentation*
- **Shininess** (Number): *See documentation*
- **Specular Amount** (Number): *See documentation*
- **Diffuse Texture** (Object:Texture): *See documentation*
- **Specular Texture** (Object:Texture): *See documentation*
- **Normal Map** (Object:Texture): *See documentation*
- **AO Texture** (Object:Texture): *See documentation*
- **Emissive Texture** (Object:Texture): *See documentation*
- **Emissive Mask** (Object:Texture): *See documentation*
- **Opacity Texture** (Object:Texture): *See documentation*
- **Environment Map** (Object:Texture): *See documentation*
- **Env Map Mask** (Object:Texture): *See documentation*
- **Diffuse Repeat X** (Number): *See documentation*
- **Diffuse Repeat Y** (Number): *See documentation*
- **Texture Offset X** (Number): *See documentation*
- **texture pixel offset on the C axis** (applied to all textures): *See documentation*
- **Texture Offset Y** (Number): *See documentation*
- **texture pixel offset on the Y axis** (applied to all textures): *See documentation*
- **Specular Intensity** (Number): *See documentation*
- **Normal Map Intensity** (Number): *See documentation*
- **AO Intensity** (Number): *See documentation*
- **Emissive Intensity** (Number): *See documentation*
- **Emissive Mask Intensity** (Number): *See documentation*
- **Env Map Intensity** (Number): *See documentation*
- **Env Mask Intensity** (Number): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*
- **Shader** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/L3HqYa)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PhongMaterial_v6"*
**Docs:** [https://cables.gl/op/Ops.Gl.Phong.PhongMaterial_v6](https://cables.gl/op/Ops.Gl.Phong.PhongMaterial_v6)

---

### PointLight_v5
![PointLight_v5 op](images/ops/Ops_Gl_Phong_PointLight_v5.svg)

**Full Name:** `Ops.Gl.Phong.PointLight_v5`
**Description:** Point light for phong shading

**> Input Ports:**
- **Trigger In** (Trigger): *See documentation*
- **Cast Light** (Number: Boolean): *See documentation*
- **Intensity** (Number): *See documentation*
- **Radius** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **Specular R** (Number): *See documentation*
- **Specular G** (Number): *See documentation*
- **Specular B** (Number): *See documentation*
- **Falloff** (Number): *See documentation*
- **Cast Shadow** (Number: Boolean): *See documentation*
- **Rendering Active** (Number: Boolean): *See documentation*
- **Shadow Strength** (Number): *See documentation*
- **Near** (Number): *See documentation*
- **Far** (Number): *See documentation*
- **Bias** (Number): *See documentation*
- **Polygon Offset** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*
- **Cubemap** (Object): *See documentation*
- **World Position X** (Number): *See documentation*
- **World Position Y** (Number): *See documentation*
- **World Position Z** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/MybtXU)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointLight_v5"*
**Docs:** [https://cables.gl/op/Ops.Gl.Phong.PointLight_v5](https://cables.gl/op/Ops.Gl.Phong.PointLight_v5)

---

### ResetLights
![ResetLights op](images/ops/Ops_Gl_Phong_ResetLights.svg)

**Full Name:** `Ops.Gl.Phong.ResetLights`
**Description:** reset lights for everything triggered after

**> Input Ports:**
- **Trigger In** (Trigger): *See documentation*
- **Reset Lights** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/eU7obI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ResetLights"*
**Docs:** [https://cables.gl/op/Ops.Gl.Phong.ResetLights](https://cables.gl/op/Ops.Gl.Phong.ResetLights)

---

### SpotLight_v5
![SpotLight_v5 op](images/ops/Ops_Gl_Phong_SpotLight_v5.svg)

**Full Name:** `Ops.Gl.Phong.SpotLight_v5`
**Description:** spot light that emits a cone of light

**> Input Ports:**
- **Trigger In** (Trigger): *See documentation*
- **Cast Light** (Number: Boolean): *See documentation*
- **Intensity** (Number): *See documentation*
- **Radius** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **Point At X** (Number): *See documentation*
- **Point At Y** (Number): *See documentation*
- **Point At Z** (Number): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **Specular R** (Number): *See documentation*
- **Specular G** (Number): *See documentation*
- **Specular B** (Number): *See documentation*
- **Cone Angle** (Number): *See documentation*
- **Inner Cone Angle** (Number): *See documentation*
- **Spot Exponent** (Number): *See documentation*
- **Falloff** (Number): *See documentation*
- **Cast Shadow** (Number: Boolean): *See documentation*
- **Rendering Active** (Number: Boolean): *See documentation*
- **Shadow Strength** (Number): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*
- **Shadow Map** (Object): *See documentation*
- **World Position X** (Number): *See documentation*
- **World Position Y** (Number): *See documentation*
- **World Position Z** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/D5evXU)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SpotLight_v5"*
**Docs:** [https://cables.gl/op/Ops.Gl.Phong.SpotLight_v5](https://cables.gl/op/Ops.Gl.Phong.SpotLight_v5)

---

