# Ops.Color

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Color

### ColorArraySort
![ColorArraySort op](images/ops/Ops_Color_ColorArraySort.svg)

**Full Name:** `Ops.Color.ColorArraySort`
**Description:** Sort an array of colors by saturation/lightness etc.

**> Input Ports:**

- **Colors** (Array)

**< Output Ports:**

- **New Colors** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/zKfluu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorArraySort"*
**Docs:** [https://cables.gl/op/Ops.Color.ColorArraySort](https://cables.gl/op/Ops.Color.ColorArraySort)

---

### ColorPalettes
![ColorPalettes op](images/ops/Ops_Color_ColorPalettes.svg)

**Full Name:** `Ops.Color.ColorPalettes`
**Description:** Contains a collection of nice color palettes output to texture or array via index

**> Input Ports:**

- **Index** (Number: Integer)
- **Smooth** (Number: Boolean)

**< Output Ports:**

- **Texture** (Object)
- **Color Array** (Array)
- **The color array containing 5 colors** (15 values in total, 3 values per color – r, g and b)

**Example Patch:** [Open in Editor](https://cables.gl/edit/xRvD98)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorPalettes"*
**Docs:** [https://cables.gl/op/Ops.Color.ColorPalettes](https://cables.gl/op/Ops.Color.ColorPalettes)

---

### ColorValue
![ColorValue op](images/ops/Ops_Color_ColorValue.svg)

**Full Name:** `Ops.Color.ColorValue`
**Description:** Use a color value on multiple places

**> Input Ports:**

- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)

**< Output Ports:**

- **Outr** (Number)
- **Outg** (Number)
- **Outb** (Number)
- **Outa** (Number)
- **Hex** (Number)
- **Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/19KZet)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorValue"*
**Docs:** [https://cables.gl/op/Ops.Color.ColorValue](https://cables.gl/op/Ops.Color.ColorValue)

---

### EyeDropper
![EyeDropper op](images/ops/Ops_Color_EyeDropper.svg)

**Full Name:** `Ops.Color.EyeDropper`
**Description:** Native color picker

**> Input Ports:**

- **Open** (Trigger)

**< Output Ports:**

- **Hex** (String)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **Supported** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/kYsAkv)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "EyeDropper"*
**Docs:** [https://cables.gl/op/Ops.Color.EyeDropper](https://cables.gl/op/Ops.Color.EyeDropper)

---

### Gradient
![Gradient op](images/ops/Ops_Color_Gradient.svg)

**Full Name:** `Ops.Color.Gradient`
**Description:** gradient editor,outputs an objects with gradient information

**> Input Ports:**

- **Gradient** (Number)
- **Randomize Colors** (Trigger)

**< Output Ports:**

- **Gradient Object** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/QB7br5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Gradient"*
**Docs:** [https://cables.gl/op/Ops.Color.Gradient](https://cables.gl/op/Ops.Color.Gradient)

---

### GradientColorArray
![GradientColorArray op](images/ops/Ops_Color_GradientColorArray.svg)

**Full Name:** `Ops.Color.GradientColorArray`
**Description:** texture containing a colour gradient that can be altered with an editor

**> Input Ports:**

- **Gradient** (Number)
- **Direction Index** (Number: Integer)
- **Smoothstep** (Number: Boolean)
- **Step** (Number: Boolean)
- **Flip** (Number: Boolean)
- **SRGB** (Number: Boolean)
- **Oklab** (Number: Boolean)
- **Size** (Number: Integer)
- **Dither** (Number)
- **Gradient Array** (Array)
- **Randomize Colors** (Trigger)

**< Output Ports:**

- **Color Array** (Array)
- **Width** (Number)
- **Height** (Number)
- **Colors** (Array)
- **Colors Pos** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/xAdV8x)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GradientColorArray"*
**Docs:** [https://cables.gl/op/Ops.Color.GradientColorArray](https://cables.gl/op/Ops.Color.GradientColorArray)

---

### HexToRGB_v2
![HexToRGB_v2 op](images/ops/Ops_Color_HexToRGB_v2.svg)

**Full Name:** `Ops.Color.HexToRGB_v2`
**Description:** Converts a hex color like `#ff0000` to number values

**> Input Ports:**

- **Hex** (String)
- **Bytes** (Number: Boolean)

**< Output Ports:**

- **R** (Number)
- **G** (Number)
- **B** (Number)
- **RGB Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/IBX1ft)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HexToRGB_v2"*
**Docs:** [https://cables.gl/op/Ops.Color.HexToRGB_v2](https://cables.gl/op/Ops.Color.HexToRGB_v2)

---

### HSLtoRGB
![HSLtoRGB op](images/ops/Ops_Color_HSLtoRGB.svg)

**Full Name:** `Ops.Color.HSLtoRGB`
**Description:** Convert HSL to RGB

**> Input Ports:**

- **Hue** (Number)
- **Saturation** (Number)
- **Lightness** (Number)

**< Output Ports:**

- **R** (Number)
- **G** (Number)
- **B** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/3fOpvs)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HSLtoRGB"*
**Docs:** [https://cables.gl/op/Ops.Color.HSLtoRGB](https://cables.gl/op/Ops.Color.HSLtoRGB)

---

### LuminanceContrast
![LuminanceContrast op](images/ops/Ops_Color_LuminanceContrast.svg)

**Full Name:** `Ops.Color.LuminanceContrast`
**Description:** Calculate the luminance contrast between two colors

**> Input Ports:**

- **R 1** (Number)
- **G 1** (Number)
- **B 1** (Number)
- **R 2** (Number)
- **G 2** (Number)
- **B 2** (Number)

**< Output Ports:**

- **Contrast** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/lFzrvs)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LuminanceContrast"*
**Docs:** [https://cables.gl/op/Ops.Color.LuminanceContrast](https://cables.gl/op/Ops.Color.LuminanceContrast)

---

### RGBLuminance
![RGBLuminance op](images/ops/Ops_Color_RGBLuminance.svg)

**Full Name:** `Ops.Color.RGBLuminance`
**Description:** Calculate the luminance of a RGB color

**> Input Ports:**

- **R** (Number)
- **G** (Number)
- **B** (Number)

**< Output Ports:**

- **Luminance** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Du0rvs)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RGBLuminance"*
**Docs:** [https://cables.gl/op/Ops.Color.RGBLuminance](https://cables.gl/op/Ops.Color.RGBLuminance)

---

### RGBToCMYK
![RGBToCMYK op](images/ops/Ops_Color_RGBToCMYK.svg)

**Full Name:** `Ops.Color.RGBToCMYK`
**Description:** Output the CMYK value of a RGB color

**> Input Ports:**

- **R** (Number)
- **G** (Number)
- **B** (Number)

**< Output Ports:**

- **C** (Number)
- **M** (Number)
- **Y** (Number)
- **K** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Du0rvs)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RGBToCMYK"*
**Docs:** [https://cables.gl/op/Ops.Color.RGBToCMYK](https://cables.gl/op/Ops.Color.RGBToCMYK)

---

### RgbToHex
![RgbToHex op](images/ops/Ops_Color_RgbToHex.svg)

**Full Name:** `Ops.Color.RgbToHex`
**Description:** convert RGB float values to HEX color String

**> Input Ports:**

- **R** (Number)
- **G** (Number)
- **B** (Number)

**< Output Ports:**

- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Up7r8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RgbToHex"*
**Docs:** [https://cables.gl/op/Ops.Color.RgbToHex](https://cables.gl/op/Ops.Color.RgbToHex)

---

### RGBtoHSB
![RGBtoHSB op](images/ops/Ops_Color_RGBtoHSB.svg)

**Full Name:** `Ops.Color.RGBtoHSB`
**Description:** convert RGB color to HSB Hue, Saturation, Brightness

**> Input Ports:**

- **R** (Number)
- **G** (Number)
- **B** (Number)

**< Output Ports:**

- **Hue** (Number)
- **Saturation** (Number)
- **Brightness** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Up7r8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RGBtoHSB"*
**Docs:** [https://cables.gl/op/Ops.Color.RGBtoHSB](https://cables.gl/op/Ops.Color.RGBtoHSB)

---

### RGBtoHSL
![RGBtoHSL op](images/ops/Ops_Color_RGBtoHSL.svg)

**Full Name:** `Ops.Color.RGBtoHSL`
**Description:** Convert RGB color to HSL values

**> Input Ports:**

- **R** (Number)
- **G** (Number)
- **B** (Number)

**< Output Ports:**

- **Hue** (Number)
- **Saturation** (Number)
- **Lightness** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Du0rvs)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RGBtoHSL"*
**Docs:** [https://cables.gl/op/Ops.Color.RGBtoHSL](https://cables.gl/op/Ops.Color.RGBtoHSL)

---

