# Ops.Gl.ImageCompose.Math


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### ColorMapRange
![ColorMapRange op](images/ops/Ops_Gl_ImageCompose_Math_ColorMapRange.svg)

**Full Name:** `Ops.Gl.ImageCompose.Math.ColorMapRange`

Map the range of color number values to another.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Old Min** (Number)
- **Old Max** (Number)
- **New Min** (Number)
- **New Max** (Number)
- **Clamp** (Number: Boolean)
- **R** (Number: Boolean)
- **G** (Number: Boolean)
- **B** (Number: Boolean)
- **A** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/TgoiV6](https://cables.gl/edit/TgoiV6)

**Doc:** [cables.gl/op/Ops.Gl.ImageCompose.Math.ColorMapRange](https://cables.gl/op/Ops.Gl.ImageCompose.Math.ColorMapRange)

### Normalize
![Normalize op](images/ops/Ops_Gl_ImageCompose_Math_Normalize.svg)

**Full Name:** `Ops.Gl.ImageCompose.Math.Normalize`

normalize texture rgb values.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Fade** (Number)
- **Size** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/7c4jW2](https://cables.gl/edit/7c4jW2)

**Doc:** [cables.gl/op/Ops.Gl.ImageCompose.Math.Normalize](https://cables.gl/op/Ops.Gl.ImageCompose.Math.Normalize)

### RgbeToFloat32Texture
![RgbeToFloat32Texture op](images/ops/Ops_Gl_ImageCompose_Math_RgbeToFloat32Texture.svg)

**Full Name:** `Ops.Gl.ImageCompose.Math.RgbeToFloat32Texture`

Convert a RGBE texture to HDR/floating point texture.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Blend Mode Index** (Number: Integer)
- **Amount** (Number)
- **Mode Index** (Number: Integer)
- **Min** (Number)
- **Max** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/adsLpX](https://cables.gl/edit/adsLpX)

**Doc:** [cables.gl/op/Ops.Gl.ImageCompose.Math.RgbeToFloat32Texture](https://cables.gl/op/Ops.Gl.ImageCompose.Math.RgbeToFloat32Texture)

### RgbMath
![RgbMath op](images/ops/Ops_Gl_ImageCompose_Math_RgbMath.svg)

**Full Name:** `Ops.Gl.ImageCompose.Math.RgbMath`

This OP enables you to use precise values to modify the pixels in your texture. For example adjusting texture values that are modifying your geometry or array values, or even your post processing compositions.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Operation Index** (Number: Integer)
- **R Active** (Number: Boolean)
- **G Active** (Number: Boolean)
- **B Active** (Number: Boolean)
- **A Active** (Number: Boolean)
- **Texture** (Object:Texture)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)
- **Multiply Texture** (Number)
- **Mask** (Object:Texture)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/H3cEpX](https://cables.gl/edit/H3cEpX)

**Doc:** [cables.gl/op/Ops.Gl.ImageCompose.Math.RgbMath](https://cables.gl/op/Ops.Gl.ImageCompose.Math.RgbMath)

### RgbMathExpression
![RgbMathExpression op](images/ops/Ops_Gl_ImageCompose_Math_RgbMathExpression.svg)

**Full Name:** `Ops.Gl.ImageCompose.Math.RgbMathExpression`

Execute a glsl code math expression in a image compose.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Update Shader** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **W** (Number)
- **TexA** (Object:Texture)
- **TexB** (Object:Texture)
- **TexC** (Object:Texture)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)
- **Code** (String)

**Example Patch:** [cables.gl/edit/tG4xFs](https://cables.gl/edit/tG4xFs)

**Doc:** [cables.gl/op/Ops.Gl.ImageCompose.Math.RgbMathExpression](https://cables.gl/op/Ops.Gl.ImageCompose.Math.RgbMathExpression)

### RgbTransform
![RgbTransform op](images/ops/Ops_Gl_ImageCompose_Math_RgbTransform.svg)

**Full Name:** `Ops.Gl.ImageCompose.Math.RgbTransform`

transform RGB values interpreted as XYZ coordinates.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Translate** (Number: Boolean)
- **Pos X** (Number)
- **Pos Y** (Number)
- **Pos Z** (Number)
- **Scale** (Number: Boolean)
- **Scale X** (Number)
- **Scale Y** (Number)
- **Scale Z** (Number)
- **Rotate** (Number: Boolean)
- **Rotation X** (Number)
- **Rotation Y** (Number)
- **Rotation Z** (Number)
- **Mask** (Object:Texture)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/UJvMbk](https://cables.gl/edit/UJvMbk)

**Doc:** [cables.gl/op/Ops.Gl.ImageCompose.Math.RgbTransform](https://cables.gl/op/Ops.Gl.ImageCompose.Math.RgbTransform)

### Round
![Round op](images/ops/Ops_Gl_ImageCompose_Math_Round.svg)

**Full Name:** `Ops.Gl.ImageCompose.Math.Round`

Round number values of texture color channels.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Amount** (Number)
- **Multiplier** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/op/Ops.Gl.ImageCompose.Math.Round#example](https://cables.gl/op/Ops.Gl.ImageCompose.Math.Round#example)

**Doc:** [cables.gl/op/Ops.Gl.ImageCompose.Math.Round](https://cables.gl/op/Ops.Gl.ImageCompose.Math.Round)

### TexMathCompare
![TexMathCompare op](images/ops/Ops_Gl_ImageCompose_Math_TexMathCompare.svg)

**Full Name:** `Ops.Gl.ImageCompose.Math.TexMathCompare`

compare and pass through of color channel values.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Comparison Index** (Number: Integer)
- **Result Index** (Number: Integer)
- **Number** (Number)
- **R Active** (Number: Boolean)
- **G Active** (Number: Boolean)
- **B Active** (Number: Boolean)
- **A Active** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example Patch:** [cables.gl/edit/RjKQWp](https://cables.gl/edit/RjKQWp)

**Doc:** [cables.gl/op/Ops.Gl.ImageCompose.Math.TexMathCompare](https://cables.gl/op/Ops.Gl.ImageCompose.Math.TexMathCompare)


