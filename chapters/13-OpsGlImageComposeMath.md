# Ops.Gl.ImageCompose.Math

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.ImageCompose.Math

### ColorMapRange
![ColorMapRange op](images/ops/Ops_Gl_ImageCompose_Math_ColorMapRange.svg)

**Full Name:** `Ops.Gl.ImageCompose.Math.ColorMapRange`
**Description:** Map the range of color number values to another

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Old Min** (Number): *See documentation*
- **Old Max** (Number): *See documentation*
- **New Min** (Number): *See documentation*
- **New Max** (Number): *See documentation*
- **Clamp** (Number: Boolean): *See documentation*
- **R** (Number: Boolean): *See documentation*
- **G** (Number: Boolean): *See documentation*
- **B** (Number: Boolean): *See documentation*
- **A** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/TgoiV6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorMapRange"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Math.ColorMapRange](https://cables.gl/op/Ops.Gl.ImageCompose.Math.ColorMapRange)

---

### Normalize
![Normalize op](images/ops/Ops_Gl_ImageCompose_Math_Normalize.svg)

**Full Name:** `Ops.Gl.ImageCompose.Math.Normalize`
**Description:** normalize texture rgb values

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Fade** (Number): *See documentation*
- **Size** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/7c4jW2)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Normalize"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Math.Normalize](https://cables.gl/op/Ops.Gl.ImageCompose.Math.Normalize)

---

### RgbeToFloat32Texture
![RgbeToFloat32Texture op](images/ops/Ops_Gl_ImageCompose_Math_RgbeToFloat32Texture.svg)

**Full Name:** `Ops.Gl.ImageCompose.Math.RgbeToFloat32Texture`
**Description:** Convert a RGBE texture to HDR/floating point texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Mode Index** (Number: Integer): *See documentation*
- **Min** (Number): *See documentation*
- **Max** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/adsLpX)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RgbeToFloat32Texture"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Math.RgbeToFloat32Texture](https://cables.gl/op/Ops.Gl.ImageCompose.Math.RgbeToFloat32Texture)

---

### RgbMath
![RgbMath op](images/ops/Ops_Gl_ImageCompose_Math_RgbMath.svg)

**Full Name:** `Ops.Gl.ImageCompose.Math.RgbMath`
**Description:** This OP enables you to use precise values to modify the pixels in your texture. For example adjusting texture values that are modifying your geometry or array values, or even your post processing compositions.

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Operation Index** (Number: Integer): *See documentation*
- **R Active** (Number: Boolean): *See documentation*
- **G Active** (Number: Boolean): *See documentation*
- **B Active** (Number: Boolean): *See documentation*
- **A Active** (Number: Boolean): *See documentation*
- **Texture** (Object:Texture): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*
- **Multiply Texture** (Number): *See documentation*
- **Mask** (Object:Texture): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/H3cEpX)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RgbMath"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Math.RgbMath](https://cables.gl/op/Ops.Gl.ImageCompose.Math.RgbMath)

---

### RgbMathExpression
![RgbMathExpression op](images/ops/Ops_Gl_ImageCompose_Math_RgbMathExpression.svg)

**Full Name:** `Ops.Gl.ImageCompose.Math.RgbMathExpression`
**Description:** Execute a glsl code math expression in a image compose

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Update Shader** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **W** (Number): *See documentation*
- **TexA** (Object:Texture): *See documentation*
- **TexB** (Object:Texture): *See documentation*
- **TexC** (Object:Texture): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Code** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/tG4xFs)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RgbMathExpression"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Math.RgbMathExpression](https://cables.gl/op/Ops.Gl.ImageCompose.Math.RgbMathExpression)

---

### RgbTransform
![RgbTransform op](images/ops/Ops_Gl_ImageCompose_Math_RgbTransform.svg)

**Full Name:** `Ops.Gl.ImageCompose.Math.RgbTransform`
**Description:** transform RGB values interpreted as XYZ coordinates

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Translate** (Number: Boolean): *See documentation*
- **Pos X** (Number): *See documentation*
- **Pos Y** (Number): *See documentation*
- **Pos Z** (Number): *See documentation*
- **Scale** (Number: Boolean): *See documentation*
- **Scale X** (Number): *See documentation*
- **Scale Y** (Number): *See documentation*
- **Scale Z** (Number): *See documentation*
- **Rotate** (Number: Boolean): *See documentation*
- **Rotation X** (Number): *See documentation*
- **Rotation Y** (Number): *See documentation*
- **Rotation Z** (Number): *See documentation*
- **Mask** (Object:Texture): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/UJvMbk)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RgbTransform"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Math.RgbTransform](https://cables.gl/op/Ops.Gl.ImageCompose.Math.RgbTransform)

---

### Round
![Round op](images/ops/Ops_Gl_ImageCompose_Math_Round.svg)

**Full Name:** `Ops.Gl.ImageCompose.Math.Round`
**Description:** Round number values of texture color channels

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Amount** (Number): *See documentation*
- **Multiplier** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.ImageCompose.Math.Round#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Round"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Math.Round](https://cables.gl/op/Ops.Gl.ImageCompose.Math.Round)

---

### TexMathCompare
![TexMathCompare op](images/ops/Ops_Gl_ImageCompose_Math_TexMathCompare.svg)

**Full Name:** `Ops.Gl.ImageCompose.Math.TexMathCompare`
**Description:** compare and pass through of color channel values

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Comparison Index** (Number: Integer): *See documentation*
- **Result Index** (Number: Integer): *See documentation*
- **Number** (Number): *See documentation*
- **R Active** (Number: Boolean): *See documentation*
- **G Active** (Number: Boolean): *See documentation*
- **B Active** (Number: Boolean): *See documentation*
- **A Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/RjKQWp)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TexMathCompare"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Math.TexMathCompare](https://cables.gl/op/Ops.Gl.ImageCompose.Math.TexMathCompare)

---

