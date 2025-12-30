# Ops.Gl.ImageCompose.Noise

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.ImageCompose.Noise

### CellularNoise_v2
![CellularNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_CellularNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.CellularNoise_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.CellularNoise_v2) for details*

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Mask** (Object:Texture): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **Harmonics Index** (Number: Integer): *See documentation*
- **Tileable** (Number: Boolean): *See documentation*
- **Offset** (Object:Texture): *See documentation*
- **Offset Multiply** (Number): *See documentation*
- **Offset X Index** (Number: Integer): *See documentation*
- **Offset Y Index** (Number: Integer): *See documentation*
- **Offset Z Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/9DZmT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CellularNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.CellularNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.CellularNoise_v2)

---

### FBMNoise_v2
![FBMNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_FBMNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.FBMNoise_v2`
**Description:** fractional brownian motion noise

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **Anim** (Number): *See documentation*
- **ScrollX** (Number): *See documentation*
- **ScrollY** (Number): *See documentation*
- **Repeat** (Number): *See documentation*
- **Aspect** (Number): *See documentation*
- **Layer 1** (Number: Boolean): *See documentation*
- **Layer 2** (Number: Boolean): *See documentation*
- **Layer 3** (Number: Boolean): *See documentation*
- **Layer 4** (Number: Boolean): *See documentation*
- **Tileable** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/DmWmT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FBMNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.FBMNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.FBMNoise_v2)

---

### GaborNoise
![GaborNoise op](images/ops/Ops_Gl_ImageCompose_Noise_GaborNoise.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.GaborNoise`
**Description:** Render "gabor noise" into a texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Phase** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/PWDdQm)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GaborNoise"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.GaborNoise](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.GaborNoise)

---

### GlitchNoise_v2
![GlitchNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_GlitchNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.GlitchNoise_v2`
**Description:** Creates a black and white glitched texture to use for displacement

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Amount** (Number): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Seed** (Number): *See documentation*
- **Frequency** (Number): *See documentation*
- **Strength** (Number): *See documentation*
- **Block Size Small X** (Number): *See documentation*
- **Block Size Small Y** (Number): *See documentation*
- **Block Size Large X** (Number): *See documentation*
- **Block Size Large Y** (Number): *See documentation*
- **Scroll X** (Number): *See documentation*
- **Scroll Y** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/cknm0r)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GlitchNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.GlitchNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.GlitchNoise_v2)

---

### HexagonNoise_v2
![HexagonNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_HexagonNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.HexagonNoise_v2`
**Description:** Creates a hexagonal noise

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Loop** (Number: Boolean): *See documentation*
- **RGB** (Number: Boolean): *See documentation*
- **Minimum Value** (Number): *See documentation*
- **Maximum Value** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **Orientation** (Number: Boolean): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **Seed** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/plbB53)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HexagonNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.HexagonNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.HexagonNoise_v2)

---

### LayerNoise_v3
![LayerNoise_v3 op](images/ops/Ops_Gl_ImageCompose_Noise_LayerNoise_v3.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.LayerNoise_v3`
**Description:** Multilayer perlin noise variation

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Mode Index** (Number: Integer): *See documentation*
- **RGBA** (Number: Boolean): *See documentation*
- **Scale** (Number): *See documentation*
- **Layers** (Number: Integer): *See documentation*
- **Factor** (Number): *See documentation*
- **Exponent** (Number): *See documentation*
- **ScrollX** (Number): *See documentation*
- **ScrollY** (Number): *See documentation*
- **ScrollZ** (Number): *See documentation*
- **Tileable** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/NSYy0t)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LayerNoise_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.LayerNoise_v3](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.LayerNoise_v3)

---

### Noise_v2
![Noise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_Noise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.Noise_v2`
**Description:** White noise pixel effect

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Threshold** (Number): *See documentation*
- **Animated** (Number: Boolean): *See documentation*
- **RGB** (Number: Boolean): *See documentation*
- **Normalize** (Number: Boolean): *See documentation*
- **Multiply** (Object:Texture): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/PdHmT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Noise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.Noise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.Noise_v2)

---

### PerlinNoise_v2
![PerlinNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_PerlinNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.PerlinNoise_v2`
**Description:** Draw perlin noise into an image

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Mask** (Object:Texture): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Color Index** (Number: Integer): *See documentation*
- **Scale** (Number): *See documentation*
- **Multiply** (Number): *See documentation*
- **Harmonics Index** (Number: Integer): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **Offset** (Object:Texture): *See documentation*
- **Offset Multiply** (Number): *See documentation*
- **Offset X Index** (Number: Integer): *See documentation*
- **Offset Y Index** (Number: Integer): *See documentation*
- **Offset Z Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/zfzmT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PerlinNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.PerlinNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.PerlinNoise_v2)

---

### PixelNoise_v3
![PixelNoise_v3 op](images/ops/Ops_Gl_ImageCompose_Noise_PixelNoise_v3.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.PixelNoise_v3`
**Description:** Amount of blend mode to apply

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Loop** (Number: Boolean): *See documentation*
- **RGB** (Number: Boolean): *See documentation*
- **Minimum Value** (Number): *See documentation*
- **Maximum Value** (Number): *See documentation*
- **Num X** (Number): *See documentation*
- **Num Y** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **Seed** (Number): *See documentation*
- **Centered** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/pdjoOb)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PixelNoise_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.PixelNoise_v3](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.PixelNoise_v3)

---

### PolkaDotNoise_v2
![PolkaDotNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_PolkaDotNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.PolkaDotNoise_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.PolkaDotNoise_v2) for details*

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Square Look** (Number: Boolean): *See documentation*
- **Threshold** (Number): *See documentation*
- **Radius Low** (Number): *See documentation*
- **Radius High** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/pKNTub)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PolkaDotNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.PolkaDotNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.PolkaDotNoise_v2)

---

### Shardnoise
![Shardnoise op](images/ops/Ops_Gl_ImageCompose_Noise_Shardnoise.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.Shardnoise`
**Description:** Render "shard noise" into a texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Sharpness** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **Round** (Number: Boolean): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/GSZtvs)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Shardnoise"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.Shardnoise](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.Shardnoise)

---

### SimplexNoise_v2
![SimplexNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_SimplexNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.SimplexNoise_v2`
**Description:** simplex noise generator

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Mask** (Object:Texture): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Smoothness** (Number): *See documentation*
- **Harmonics Index** (Number: Integer): *See documentation*
- **Scale** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Time** (Number): *See documentation*
- **Offset** (Object:Texture): *See documentation*
- **Offset Multiply** (Number): *See documentation*
- **Offset X Index** (Number: Integer): *See documentation*
- **Offset Y Index** (Number: Integer): *See documentation*
- **Offset Z Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/c3vmUf)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SimplexNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.SimplexNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.SimplexNoise_v2)

---

### TriangleNoise_v2
![TriangleNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_TriangleNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.TriangleNoise_v2`
**Description:** noise made from triangles

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Scale** (Number): *See documentation*
- **Angle** (Number): *See documentation*
- **Add** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/wvkJyC)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriangleNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.TriangleNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.TriangleNoise_v2)

---

### ValueNoise_v2
![ValueNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_ValueNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.ValueNoise_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.ValueNoise_v2) for details*

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/SgTmT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ValueNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.ValueNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.ValueNoise_v2)

---

### Voronoise_v2
![Voronoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_Voronoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.Voronoise_v2`
**Description:** Voronoi Noise function

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Time** (Number): *See documentation*
- **Movement** (Number): *See documentation*
- **Num** (Number): *See documentation*
- **Seed** (Number): *See documentation*
- **Fill Index** (Number: Integer): *See documentation*
- **Draw Isolines** (Number: Boolean): *See documentation*
- **Draw Distance** (Number: Boolean): *See documentation*
- **Draw Center** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/3zb6Us)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Voronoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.Voronoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.Voronoise_v2)

---

### WorleyNoise_v2
![WorleyNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_WorleyNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.WorleyNoise_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.WorleyNoise_v2) for details*

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **Harmonics Index** (Number: Integer): *See documentation*
- **Invert** (Number: Boolean): *See documentation*
- **RangeA** (Number): *See documentation*
- **RangeB** (Number): *See documentation*
- **Tileable** (Number: Boolean): *See documentation*
- **Amount Map** (Object:Texture): *See documentation*
- **Source Strength Map Index** (Number: Integer): *See documentation*
- **Invert Strength Map** (Number: Boolean): *See documentation*
- **Offset** (Object:Texture): *See documentation*
- **Offset Multiply** (Number): *See documentation*
- **Offset X Index** (Number: Integer): *See documentation*
- **Offset Y Index** (Number: Integer): *See documentation*
- **Offset Z Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/sivDJd)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WorleyNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.WorleyNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.WorleyNoise_v2)

---

