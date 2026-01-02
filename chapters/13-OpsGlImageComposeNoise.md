# Ops.Gl.ImageCompose.Noise

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.ImageCompose.Noise

### CellularNoise_v2
![CellularNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_CellularNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.CellularNoise_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.CellularNoise_v2) for details*

**> Input Ports:**

- **Render** (Trigger)
- **Mask** (Object:Texture)
- **Blend Mode Index** (Number: Integer)
- **Alpha Mask Index** (Number: Integer)
- **Amount** (Number)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Scale** (Number)
- **Harmonics Index** (Number: Integer)
- **Tileable** (Number: Boolean)
- **Offset** (Object:Texture)
- **Offset Multiply** (Number)
- **Offset X Index** (Number: Integer)
- **Offset Y Index** (Number: Integer)
- **Offset Z Index** (Number: Integer)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/9DZmT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CellularNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.CellularNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.CellularNoise_v2)

---

### FBMNoise_v2
![FBMNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_FBMNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.FBMNoise_v2`
**Description:** fractional brownian motion noise

**> Input Ports:**

- **Render** (Trigger)
- **Blend Mode Index** (Number: Integer)
- **Amount** (Number)
- **Alpha Mask Index** (Number: Integer)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **Scale** (Number)
- **Anim** (Number)
- **ScrollX** (Number)
- **ScrollY** (Number)
- **Repeat** (Number)
- **Aspect** (Number)
- **Layer 1** (Number: Boolean)
- **Layer 2** (Number: Boolean)
- **Layer 3** (Number: Boolean)
- **Layer 4** (Number: Boolean)
- **Tileable** (Number: Boolean)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/DmWmT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FBMNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.FBMNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.FBMNoise_v2)

---

### GaborNoise
![GaborNoise op](images/ops/Ops_Gl_ImageCompose_Noise_GaborNoise.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.GaborNoise`
**Description:** Render "gabor noise" into a texture

**> Input Ports:**

- **Render** (Trigger)
- **Blend Mode Index** (Number: Integer)
- **Amount** (Number)
- **Phase** (Number)
- **Scale** (Number)
- **X** (Number)
- **Y** (Number)

**< Output Ports:**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/PWDdQm)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GaborNoise"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.GaborNoise](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.GaborNoise)

---

### GlitchNoise_v2
![GlitchNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_GlitchNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.GlitchNoise_v2`
**Description:** Creates a black and white glitched texture to use for displacement

**> Input Ports:**

- **Render** (Trigger)
- **Amount** (Number)
- **Blend Mode Index** (Number: Integer)
- **Alpha Mask Index** (Number: Integer)
- **Seed** (Number)
- **Frequency** (Number)
- **Strength** (Number)
- **Block Size Small X** (Number)
- **Block Size Small Y** (Number)
- **Block Size Large X** (Number)
- **Block Size Large Y** (Number)
- **Scroll X** (Number)
- **Scroll Y** (Number)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/cknm0r)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GlitchNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.GlitchNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.GlitchNoise_v2)

---

### HexagonNoise_v2
![HexagonNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_HexagonNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.HexagonNoise_v2`
**Description:** Creates a hexagonal noise

**> Input Ports:**

- **Render** (Trigger)
- **Blend Mode Index** (Number: Integer)
- **Amount** (Number)
- **Alpha Mask Index** (Number: Integer)
- **Loop** (Number: Boolean)
- **RGB** (Number: Boolean)
- **Minimum Value** (Number)
- **Maximum Value** (Number)
- **Scale** (Number)
- **Orientation** (Number: Boolean)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Seed** (Number)

**< Output Ports:**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/plbB53)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HexagonNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.HexagonNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.HexagonNoise_v2)

---

### LayerNoise_v3
![LayerNoise_v3 op](images/ops/Ops_Gl_ImageCompose_Noise_LayerNoise_v3.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.LayerNoise_v3`
**Description:** Multilayer perlin noise variation

**> Input Ports:**

- **Render** (Trigger)
- **Blend Mode Index** (Number: Integer)
- **Amount** (Number)
- **Alpha Mask Index** (Number: Integer)
- **Mode Index** (Number: Integer)
- **RGBA** (Number: Boolean)
- **Scale** (Number)
- **Layers** (Number: Integer)
- **Factor** (Number)
- **Exponent** (Number)
- **ScrollX** (Number)
- **ScrollY** (Number)
- **ScrollZ** (Number)
- **Tileable** (Number: Boolean)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/NSYy0t)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LayerNoise_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.LayerNoise_v3](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.LayerNoise_v3)

---

### Noise_v2
![Noise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_Noise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.Noise_v2`
**Description:** White noise pixel effect

**> Input Ports:**

- **Render** (Trigger)
- **Blend Mode Index** (Number: Integer)
- **Amount** (Number)
- **Threshold** (Number)
- **Animated** (Number: Boolean)
- **RGB** (Number: Boolean)
- **Normalize** (Number: Boolean)
- **Multiply** (Object:Texture)

**< Output Ports:**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/PdHmT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Noise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.Noise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.Noise_v2)

---

### PerlinNoise_v2
![PerlinNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_PerlinNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.PerlinNoise_v2`
**Description:** Draw perlin noise into an image

**> Input Ports:**

- **Render** (Trigger)
- **Mask** (Object:Texture)
- **Blend Mode Index** (Number: Integer)
- **Alpha Mask Index** (Number: Integer)
- **Amount** (Number)
- **Color Index** (Number: Integer)
- **Scale** (Number)
- **Multiply** (Number)
- **Harmonics Index** (Number: Integer)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Offset** (Object:Texture)
- **Offset Multiply** (Number)
- **Offset X Index** (Number: Integer)
- **Offset Y Index** (Number: Integer)
- **Offset Z Index** (Number: Integer)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/zfzmT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PerlinNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.PerlinNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.PerlinNoise_v2)

---

### PixelNoise_v3
![PixelNoise_v3 op](images/ops/Ops_Gl_ImageCompose_Noise_PixelNoise_v3.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.PixelNoise_v3`
**Description:** Amount of blend mode to apply

**> Input Ports:**

- **Render** (Trigger)
- **Blend Mode Index** (Number: Integer)
- **Alpha Mask Index** (Number: Integer)
- **Amount** (Number)
- **Loop** (Number: Boolean)
- **RGB** (Number: Boolean)
- **Minimum Value** (Number)
- **Maximum Value** (Number)
- **Num X** (Number)
- **Num Y** (Number)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Seed** (Number)
- **Centered** (Number: Boolean)

**< Output Ports:**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/pdjoOb)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PixelNoise_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.PixelNoise_v3](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.PixelNoise_v3)

---

### PolkaDotNoise_v2
![PolkaDotNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_PolkaDotNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.PolkaDotNoise_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.PolkaDotNoise_v2) for details*

**> Input Ports:**

- **Render** (Trigger)
- **Blend Mode Index** (Number: Integer)
- **Amount** (Number)
- **Alpha Mask Index** (Number: Integer)
- **Square Look** (Number: Boolean)
- **Threshold** (Number)
- **Radius Low** (Number)
- **Radius High** (Number)
- **Scale** (Number)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**< Output Ports:**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/pKNTub)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PolkaDotNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.PolkaDotNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.PolkaDotNoise_v2)

---

### Shardnoise
![Shardnoise op](images/ops/Ops_Gl_ImageCompose_Noise_Shardnoise.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.Shardnoise`
**Description:** Render "shard noise" into a texture

**> Input Ports:**

- **Render** (Trigger)
- **Blend Mode Index** (Number: Integer)
- **Amount** (Number)
- **Sharpness** (Number)
- **Scale** (Number)
- **Round** (Number: Boolean)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**< Output Ports:**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/GSZtvs)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Shardnoise"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.Shardnoise](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.Shardnoise)

---

### SimplexNoise_v2
![SimplexNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_SimplexNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.SimplexNoise_v2`
**Description:** simplex noise generator

**> Input Ports:**

- **Render** (Trigger)
- **Mask** (Object:Texture)
- **Blend Mode Index** (Number: Integer)
- **Amount** (Number)
- **Alpha Mask Index** (Number: Integer)
- **Smoothness** (Number)
- **Harmonics Index** (Number: Integer)
- **Scale** (Number)
- **X** (Number)
- **Y** (Number)
- **Time** (Number)
- **Offset** (Object:Texture)
- **Offset Multiply** (Number)
- **Offset X Index** (Number: Integer)
- **Offset Y Index** (Number: Integer)
- **Offset Z Index** (Number: Integer)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/c3vmUf)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SimplexNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.SimplexNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.SimplexNoise_v2)

---

### TriangleNoise_v2
![TriangleNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_TriangleNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.TriangleNoise_v2`
**Description:** noise made from triangles

**> Input Ports:**

- **Render** (Trigger)
- **Blend Mode Index** (Number: Integer)
- **Amount** (Number)
- **Alpha Mask Index** (Number: Integer)
- **Scale** (Number)
- **Angle** (Number)
- **Add** (Number)

**< Output Ports:**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/wvkJyC)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriangleNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.TriangleNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.TriangleNoise_v2)

---

### ValueNoise_v2
![ValueNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_ValueNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.ValueNoise_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.ValueNoise_v2) for details*

**> Input Ports:**

- **Render** (Trigger)
- **Blend Mode Index** (Number: Integer)
- **Amount** (Number)
- **Scale** (Number)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/SgTmT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ValueNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.ValueNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.ValueNoise_v2)

---

### Voronoise_v2
![Voronoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_Voronoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.Voronoise_v2`
**Description:** Voronoi Noise function

**> Input Ports:**

- **Render** (Trigger)
- **Blend Mode Index** (Number: Integer)
- **Amount** (Number)
- **Alpha Mask Index** (Number: Integer)
- **Time** (Number)
- **Movement** (Number)
- **Num** (Number)
- **Seed** (Number)
- **Fill Index** (Number: Integer)
- **Draw Isolines** (Number: Boolean)
- **Draw Distance** (Number: Boolean)
- **Draw Center** (Number)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/3zb6Us)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Voronoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.Voronoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.Voronoise_v2)

---

### WorleyNoise_v2
![WorleyNoise_v2 op](images/ops/Ops_Gl_ImageCompose_Noise_WorleyNoise_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Noise.WorleyNoise_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.WorleyNoise_v2) for details*

**> Input Ports:**

- **Render** (Trigger)
- **Blend Mode Index** (Number: Integer)
- **Alpha Mask Index** (Number: Integer)
- **Amount** (Number)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Scale** (Number)
- **Harmonics Index** (Number: Integer)
- **Invert** (Number: Boolean)
- **RangeA** (Number)
- **RangeB** (Number)
- **Tileable** (Number: Boolean)
- **Amount Map** (Object:Texture)
- **Source Strength Map Index** (Number: Integer)
- **Invert Strength Map** (Number: Boolean)
- **Offset** (Object:Texture)
- **Offset Multiply** (Number)
- **Offset X Index** (Number: Integer)
- **Offset Y Index** (Number: Integer)
- **Offset Z Index** (Number: Integer)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/sivDJd)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WorleyNoise_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Noise.WorleyNoise_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Noise.WorleyNoise_v2)

---

