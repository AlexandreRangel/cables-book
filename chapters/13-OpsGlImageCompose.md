# Ops.Gl.ImageCompose

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.ImageCompose

### Alpha
![Alpha op](images/ops/Ops_Gl_ImageCompose_Alpha.svg)

**Full Name:** `Ops.Gl.ImageCompose.Alpha`
**Description:** Modify current alpha/opacity

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Amount** (Number): *See documentation*
- **Clamp** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/y6f1ei)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Alpha"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Alpha](https://cables.gl/op/Ops.Gl.ImageCompose.Alpha)

---

### AlphaMask_v2
![AlphaMask_v2 op](images/ops/Ops_Gl_ImageCompose_AlphaMask_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.AlphaMask_v2`
**Description:** Set alphachannel of current imagecompose via a texture mask

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Amount** (Number): *See documentation*
- **Invert** (Number: Boolean): *See documentation*
- **Image** (Object:Texture): *See documentation*
- **Method Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.ImageCompose.AlphaMask_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AlphaMask_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.AlphaMask_v2](https://cables.gl/op/Ops.Gl.ImageCompose.AlphaMask_v2)

---

### BarrelDistortion_v3
![BarrelDistortion_v3 op](images/ops/Ops_Gl_ImageCompose_BarrelDistortion_v3.svg)

**Full Name:** `Ops.Gl.ImageCompose.BarrelDistortion_v3`
**Description:** Simulate fisheye effect

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Intensity** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/qIOrS-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BarrelDistortion_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.BarrelDistortion_v3](https://cables.gl/op/Ops.Gl.ImageCompose.BarrelDistortion_v3)

---

### Blur
![Blur op](images/ops/Ops_Gl_ImageCompose_Blur.svg)

**Full Name:** `Ops.Gl.ImageCompose.Blur`
**Description:** Blur the pixels of an image

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Amount** (Number): *See documentation*
- **Direction Index** (Number: Integer): *See documentation*
- **Direction** (String): *See documentation*
- **Fast** (Number: Boolean): *See documentation*
- **Mask** (Object:Texture): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/1T9f7g)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Blur"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Blur](https://cables.gl/op/Ops.Gl.ImageCompose.Blur)

---

### Border_v2
![Border_v2 op](images/ops/Ops_Gl_ImageCompose_Border_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Border_v2`
**Description:** Draws a Border (rectangular frame) around the current ImageCompose

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Width** (Number): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Smooth** (Number: Boolean): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **Side A** (Number): *See documentation*
- **Side B** (Number): *See documentation*
- **Side C** (Number): *See documentation*
- **Side D** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ctPnT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Border_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Border_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Border_v2)

---

### BrightnessContrast
![BrightnessContrast op](images/ops/Ops_Gl_ImageCompose_BrightnessContrast.svg)

**Full Name:** `Ops.Gl.ImageCompose.BrightnessContrast`
**Description:** adjust image brightness and contrast

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Contrast** (Number): *See documentation*
- **Brightness** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/8p4mT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BrightnessContrast"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.BrightnessContrast](https://cables.gl/op/Ops.Gl.ImageCompose.BrightnessContrast)

---

### BulgePinch
![BulgePinch op](images/ops/Ops_Gl_ImageCompose_BulgePinch.svg)

**Full Name:** `Ops.Gl.ImageCompose.BulgePinch`
**Description:** bulge and pinch an image (deform,stretch,distort)

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Radius** (Number): *See documentation*
- **Strength** (Number): *See documentation*
- **Center X** (Number): *See documentation*
- **Center Y** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/2lC9W6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BulgePinch"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.BulgePinch](https://cables.gl/op/Ops.Gl.ImageCompose.BulgePinch)

---

### CheckerBoard_v2
![CheckerBoard_v2 op](images/ops/Ops_Gl_ImageCompose_CheckerBoard_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.CheckerBoard_v2`
**Description:** Draw a checkerboard pattern

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Square** (Number: Boolean): *See documentation*
- **Num X** (Number): *See documentation*
- **Num Y** (Number): *See documentation*
- **Rotate** (Number): *See documentation*
- **Centered** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/J4KL_4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CheckerBoard_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.CheckerBoard_v2](https://cables.gl/op/Ops.Gl.ImageCompose.CheckerBoard_v2)

---

### ChromaticAberration_v2
![ChromaticAberration_v2 op](images/ops/Ops_Gl_ImageCompose_ChromaticAberration_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.ChromaticAberration_v2`
**Description:** simulating lens effect by shifting rgb channels

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Pixel** (Number): *See documentation*
- **Lens Distort** (Number): *See documentation*
- **Smooth** (Number: Boolean): *See documentation*
- **Mask** (Object:Texture): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/X0WkT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ChromaticAberration_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.ChromaticAberration_v2](https://cables.gl/op/Ops.Gl.ImageCompose.ChromaticAberration_v2)

---

### CircleTexture_v4
![CircleTexture_v4 op](images/ops/Ops_Gl_ImageCompose_CircleTexture_v4.svg)

**Full Name:** `Ops.Gl.ImageCompose.CircleTexture_v4`
**Description:** Draw 2d circle into texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Amount** (Number): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Size** (Number): *See documentation*
- **Inner** (Number): *See documentation*
- **Stretch X** (Number): *See documentation*
- **Stretch Y** (Number): *See documentation*
- **Pos X** (Number): *See documentation*
- **Pos Y** (Number): *See documentation*
- **FallOff Index** (Number: Integer): *See documentation*
- **Fade Out** (Number): *See documentation*
- **Warn Overflow** (Number: Boolean): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/asslT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CircleTexture_v4"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.CircleTexture_v4](https://cables.gl/op/Ops.Gl.ImageCompose.CircleTexture_v4)

---

### ClampTexture_v2
![ClampTexture_v2 op](images/ops/Ops_Gl_ImageCompose_ClampTexture_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.ClampTexture_v2`
**Description:** Clamps a texture to min and max values - Also has remap modes

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Mode Index** (Number: Integer): *See documentation*
- **R** (Number: Boolean): *See documentation*
- **R Min** (Number): *See documentation*
- **R Max** (Number): *See documentation*
- **G** (Number: Boolean): *See documentation*
- **G Min** (Number): *See documentation*
- **G Max** (Number): *See documentation*
- **B** (Number: Boolean): *See documentation*
- **B Min** (Number): *See documentation*
- **B Max** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/eYNP7-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ClampTexture_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.ClampTexture_v2](https://cables.gl/op/Ops.Gl.ImageCompose.ClampTexture_v2)

---

### Clarity
![Clarity op](images/ops/Ops_Gl_ImageCompose_Clarity.svg)

**Full Name:** `Ops.Gl.ImageCompose.Clarity`
**Description:** Increase contrast in midtones

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Amount** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.ImageCompose.Clarity#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Clarity"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Clarity](https://cables.gl/op/Ops.Gl.ImageCompose.Clarity)

---

### Color_v2
![Color_v2 op](images/ops/Ops_Gl_ImageCompose_Color_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Color_v2`
**Description:** fill image using a color (overlay)

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Mask** (Object:Texture): *See documentation*
- **Mask Invert** (Number: Boolean): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/AnqmT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Color_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Color_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Color_v2)

---

### ColorBalance_v2
![ColorBalance_v2 op](images/ops/Ops_Gl_ImageCompose_ColorBalance_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.ColorBalance_v2`
**Description:** change intensity of r,g,b channels

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Tone Index** (Number: Integer): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/FGVncy)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorBalance_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.ColorBalance_v2](https://cables.gl/op/Ops.Gl.ImageCompose.ColorBalance_v2)

---

### ColorChannel_v2
![ColorChannel_v2 op](images/ops/Ops_Gl_ImageCompose_ColorChannel_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.ColorChannel_v2`
**Description:** enable disable RGB color channels

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **ChannelR** (Number: Boolean): *See documentation*
- **ChannelG** (Number: Boolean): *See documentation*
- **ChannelB** (Number: Boolean): *See documentation*
- **ChannelA** (Number: Boolean): *See documentation*
- **Mono** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.ImageCompose.ColorChannel_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorChannel_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.ColorChannel_v2](https://cables.gl/op/Ops.Gl.ImageCompose.ColorChannel_v2)

---

### ColorMap_v2
![ColorMap_v2 op](images/ops/Ops_Gl_ImageCompose_ColorMap_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.ColorMap_v2`
**Description:** colorize a black and white image using a gradient texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Gradient** (Object:Texture): *See documentation*
- **Method Index** (Number: Integer): *See documentation*
- **Min** (Number): *See documentation*
- **Max** (Number): *See documentation*
- **Position** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/E7Dou7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorMap_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.ColorMap_v2](https://cables.gl/op/Ops.Gl.ImageCompose.ColorMap_v2)

---

### Denoise
![Denoise op](images/ops/Ops_Gl_ImageCompose_Denoise.svg)

**Full Name:** `Ops.Gl.ImageCompose.Denoise`
**Description:** Denoise texture effect - used to smooth out noisy images

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Exponent** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/4vWud8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Denoise"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Denoise](https://cables.gl/op/Ops.Gl.ImageCompose.Denoise)

---

### DepthTexture_v2
![DepthTexture_v2 op](images/ops/Ops_Gl_ImageCompose_DepthTexture_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.DepthTexture_v2`
**Description:** draw the content of a depth texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Image** (Object:Texture): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Farplane** (Number): *See documentation*
- **Nearplane** (Number): *See documentation*
- **Invert** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/tmLbW6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DepthTexture_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.DepthTexture_v2](https://cables.gl/op/Ops.Gl.ImageCompose.DepthTexture_v2)

---

### DepthTextureFocus_v2
![DepthTextureFocus_v2 op](images/ops/Ops_Gl_ImageCompose_DepthTextureFocus_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.DepthTextureFocus_v2`
**Description:** draws a gradient from white to black back to white over distance of the scene

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Depth Texture** (Object): *See documentation*
- **Focus** (Number): *See documentation*
- **focus distance** (in world space): *See documentation*
- **Width** (Number): *See documentation*
- **width of the focus** (in world space): *See documentation*
- **Invert** (Number: Boolean): *See documentation*
- **Nearplane** (Number): *See documentation*
- **Farplane** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/6Z8zJm)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DepthTextureFocus_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.DepthTextureFocus_v2](https://cables.gl/op/Ops.Gl.ImageCompose.DepthTextureFocus_v2)

---

### Desaturate
![Desaturate op](images/ops/Ops_Gl_ImageCompose_Desaturate.svg)

**Full Name:** `Ops.Gl.ImageCompose.Desaturate`
**Description:** Remove colors from image / greyscale

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Amount** (Number): *See documentation*
- **Mask** (Object): *See documentation*
- **Invert Mask** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/g1kmT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Desaturate"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Desaturate](https://cables.gl/op/Ops.Gl.ImageCompose.Desaturate)

---

### Dither_v2
![Dither_v2 op](images/ops/Ops_Gl_ImageCompose_Dither_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Dither_v2`
**Description:** convert color to black and white patterns

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Threshold** (Number): *See documentation*
- **Strength** (Number): *See documentation*
- **Mask** (Object:Texture): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/eECnT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Dither_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Dither_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Dither_v2)

---

### DrawImage_v3
![DrawImage_v3 op](images/ops/Ops_Gl_ImageCompose_DrawImage_v3.svg)

**Full Name:** `Ops.Gl.ImageCompose.DrawImage_v3`
**Description:** Draws an image into a composition

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **BlendMode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Image** (Object:Texture): *See documentation*
- **Premultiplied** (Number: Boolean): *See documentation*
- **Alpha Mask** (Number: Boolean): *See documentation*
- **RemoveAlphaSrc** (Number: Boolean): *See documentation*
- **Mask** (Object:Texture): *See documentation*
- **Mask Src Index** (Number: Integer): *See documentation*
- **Invert Alpha Channel** (Number: Boolean): *See documentation*
- **Aspect Ratio** (Number: Boolean): *See documentation*
- **Stretch Axis Index** (Number: Integer): *See documentation*
- **Position** (Number): *See documentation*
- **Crop** (Number: Boolean): *See documentation*
- **Flip X** (Number: Boolean): *See documentation*
- **Flip Y** (Number: Boolean): *See documentation*
- **Transform** (Number: Boolean): *See documentation*
- **Scale X** (Number): *See documentation*
- **Scale Y** (Number): *See documentation*
- **Position X** (Number): *See documentation*
- **Position Y** (Number): *See documentation*
- **Rotation** (Number): *See documentation*
- **Clip Repeat** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/k6ttde)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DrawImage_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.DrawImage_v3](https://cables.gl/op/Ops.Gl.ImageCompose.DrawImage_v3)

---

### EdgeDetection_v4
![EdgeDetection_v4 op](images/ops/Ops_Gl_ImageCompose_EdgeDetection_v4.svg)

**Full Name:** `Ops.Gl.ImageCompose.EdgeDetection_v4`
**Description:** Draw only the edges of an image

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Strength** (Number): *See documentation*
- **Width** (Number): *See documentation*
- **Mul Color** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dK8td8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "EdgeDetection_v4"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.EdgeDetection_v4](https://cables.gl/op/Ops.Gl.ImageCompose.EdgeDetection_v4)

---

### Emboss
![Emboss op](images/ops/Ops_Gl_ImageCompose_Emboss.svg)

**Full Name:** `Ops.Gl.ImageCompose.Emboss`
**Description:** Emboss / bevel effect

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Strength** (Number): *See documentation*
- **Clear** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/xsRcay)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Emboss"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Emboss](https://cables.gl/op/Ops.Gl.ImageCompose.Emboss)

---

### FastBlur_v2
![FastBlur_v2 op](images/ops/Ops_Gl_ImageCompose_FastBlur_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.FastBlur_v2`
**Description:** Blurs a texture - simple and fast

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Passes** (Number: Integer): *See documentation*
- **Clamp** (Number: Boolean): *See documentation*
- **Direction Index** (Number: Integer): *See documentation*
- **Mask** (Object:Texture): *See documentation*
- **Mask Invert** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/wl2T7i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FastBlur_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.FastBlur_v2](https://cables.gl/op/Ops.Gl.ImageCompose.FastBlur_v2)

---

### Flip
![Flip op](images/ops/Ops_Gl_ImageCompose_Flip.svg)

**Full Name:** `Ops.Gl.ImageCompose.Flip`
**Description:** flip the image on x or y axis

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **X** (Number: Boolean): *See documentation*
- **Y** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/179Jjr)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Flip"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Flip](https://cables.gl/op/Ops.Gl.ImageCompose.Flip)

---

### Float32ToRgbeTexture
![Float32ToRgbeTexture op](images/ops/Ops_Gl_ImageCompose_Float32ToRgbeTexture.svg)

**Full Name:** `Ops.Gl.ImageCompose.Float32ToRgbeTexture`
**Description:** Convert a Float32 bit/HDR texture to RGBE format (only positive numbers)

**> Input Ports:**
- **Render** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dXLhW2)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Float32ToRgbeTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Float32ToRgbeTexture](https://cables.gl/op/Ops.Gl.ImageCompose.Float32ToRgbeTexture)

---

### Fog_v4
![Fog_v4 op](images/ops/Ops_Gl_ImageCompose_Fog_v4.svg)

**Full Name:** `Ops.Gl.ImageCompose.Fog_v4`
**Description:** add post processing fog (nebula) to a scene

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **BlendMode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Depth Texture** (Object:Texture): *See documentation*
- **Gradient Texture** (Object:Texture): *See documentation*
- **Background Texture** (Object:Texture): *See documentation*
- **Fog Start** (Number): *See documentation*
- **Fog End** (Number): *See documentation*
- **Fog Density** (Number): *See documentation*
- **Ignore Infinity** (Number: Boolean): *See documentation*
- **Nearplane** (Number): *See documentation*
- **Farplane** (Number): *See documentation*
- **Fog R** (Number): *See documentation*
- **Fog G** (Number): *See documentation*
- **Fog B** (Number): *See documentation*
- **Fog A** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/I6pZnO)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Fog_v4"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Fog_v4](https://cables.gl/op/Ops.Gl.ImageCompose.Fog_v4)

---

### FXAA
![FXAA op](images/ops/Ops_Gl_ImageCompose_FXAA.svg)

**Full Name:** `Ops.Gl.ImageCompose.FXAA`
**Description:** post processing antialiasing

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Span Index** (Number: Integer): *See documentation*
- **ReduceMin** (Number): *See documentation*
- **ReduceMul** (Number): *See documentation*
- **Use Viewport Size** (Number: Boolean): *See documentation*
- **Width** (Number: Integer): *See documentation*
- **Height** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/c5uYnO)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FXAA"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.FXAA](https://cables.gl/op/Ops.Gl.ImageCompose.FXAA)

---

### GammaCorrection_v2
![GammaCorrection_v2 op](images/ops/Ops_Gl_ImageCompose_GammaCorrection_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.GammaCorrection_v2`
**Description:** Allows for Gamma correction of a texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Multiply Texture** (Number): *See documentation*
- **Gamma Correction** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/WugPbx)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GammaCorrection_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.GammaCorrection_v2](https://cables.gl/op/Ops.Gl.ImageCompose.GammaCorrection_v2)

---

### Gradient_v2
![Gradient_v2 op](images/ops/Ops_Gl_ImageCompose_Gradient_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Gradient_v2`
**Description:** Draws a simple gradient between three colors

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Width** (Number): *See documentation*
- **Type Index** (Number: Integer): *See documentation*
- **Pos** (Number): *See documentation*
- **Smoothstep** (Number: Boolean): *See documentation*
- **SRGB** (Number: Boolean): *See documentation*
- **Color Space Index** (Number: Integer): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **R2** (Number): *See documentation*
- **G2** (Number): *See documentation*
- **B2** (Number): *See documentation*
- **R3** (Number): *See documentation*
- **G3** (Number): *See documentation*
- **B3** (Number): *See documentation*
- **Randomize** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dlSpQ6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Gradient_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Gradient_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Gradient_v2)

---

### GridTexture_v2
![GridTexture_v2 op](images/ops/Ops_Gl_ImageCompose_GridTexture_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.GridTexture_v2`
**Description:** Creates a grid texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Line Thickness X** (Number): *See documentation*
- **Line Thickness Y** (Number): *See documentation*
- **Cells X** (Number): *See documentation*
- **Cells Y** (Number): *See documentation*
- **Rotate** (Number): *See documentation*
- **Offset X** (Number): *See documentation*
- **Offset Y** (Number): *See documentation*
- **Invert Color** (Number: Boolean): *See documentation*
- **Line Red** (Number): *See documentation*
- **Line Green** (Number): *See documentation*
- **Line Blue** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/pG_qUH)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GridTexture_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.GridTexture_v2](https://cables.gl/op/Ops.Gl.ImageCompose.GridTexture_v2)

---

### GrowPixels_v2
![GrowPixels_v2 op](images/ops/Ops_Gl_ImageCompose_GrowPixels_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.GrowPixels_v2`
**Description:** Make one pixel lines thicker via postprocessing

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Strength** (Number): *See documentation*
- **Iterations** (Number: Integer): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/3WSXCU)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GrowPixels_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.GrowPixels_v2](https://cables.gl/op/Ops.Gl.ImageCompose.GrowPixels_v2)

---

### Hue
![Hue op](images/ops/Ops_Gl_ImageCompose_Hue.svg)

**Full Name:** `Ops.Gl.ImageCompose.Hue`
**Description:** Adjust Hue of current ImageCompose

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Hue** (Number): *See documentation*
- **Mask** (Object:Texture): *See documentation*
- **Offset** (Object:Texture): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/kubmT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Hue"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Hue](https://cables.gl/op/Ops.Gl.ImageCompose.Hue)

---

### ImageCompose_v4
![ImageCompose_v4 op](images/ops/Ops_Gl_ImageCompose_ImageCompose_v4.svg)

**Full Name:** `Ops.Gl.ImageCompose.ImageCompose_v4`
**Description:** Compose Images and effects as layers to generate new Images

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Base Texture** (Object:Texture): *See documentation*
- **UV Texture** (Object:Texture): *See documentation*
- **Width** (Number: Integer): *See documentation*
- **Height** (Number: Integer): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Pixel Format Index** (Number: Integer): *See documentation*
- **Clear** (Number: Boolean): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Texture_out** (Object): *See documentation*
- **Aspect Ratio** (Number): *See documentation*
- **Texture Width** (Number): *See documentation*
- **Texture Height** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dNv2r1)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ImageCompose_v4"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.ImageCompose_v4](https://cables.gl/op/Ops.Gl.ImageCompose.ImageCompose_v4)

---

### ImageComposeAspectRatio
![ImageComposeAspectRatio op](images/ops/Ops_Gl_ImageCompose_ImageComposeAspectRatio.svg)

**Full Name:** `Ops.Gl.ImageCompose.ImageComposeAspectRatio`
**Description:** Adjust aspect ratio of an image compose branch

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Aspect** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/iwX7v4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ImageComposeAspectRatio"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.ImageComposeAspectRatio](https://cables.gl/op/Ops.Gl.ImageCompose.ImageComposeAspectRatio)

---

### ImageComposeSnapshot
![ImageComposeSnapshot op](images/ops/Ops_Gl_ImageCompose_ImageComposeSnapshot.svg)

**Full Name:** `Ops.Gl.ImageCompose.ImageComposeSnapshot`
**Description:** capture the current state of an imageCompose branch by copying the texture

**> Input Ports:**
- **Update** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Texture** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Dc1a-W)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ImageComposeSnapshot"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.ImageComposeSnapshot](https://cables.gl/op/Ops.Gl.ImageCompose.ImageComposeSnapshot)

---

### Interlace
![Interlace op](images/ops/Ops_Gl_ImageCompose_Interlace.svg)

**Full Name:** `Ops.Gl.ImageCompose.Interlace`
**Description:** Tv scanlines effect

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Amount** (Number): *See documentation*
- **Lumi Scale** (Number): *See documentation*
- **X Or Y** (Number: Boolean): *See documentation*
- **Line Size** (Number): *See documentation*
- **Displacement** (Number): *See documentation*
- **Add** (Number): *See documentation*
- **Scroll** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/MCpnT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Interlace"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Interlace](https://cables.gl/op/Ops.Gl.ImageCompose.Interlace)

---

### Invert_v2
![Invert_v2 op](images/ops/Ops_Gl_ImageCompose_Invert_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Invert_v2`
**Description:** Invert image colors

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Mask Invert** (Number: Boolean): *See documentation*
- **Mask** (Object:Texture): *See documentation*
- **Invert R** (Number: Boolean): *See documentation*
- **Invert G** (Number: Boolean): *See documentation*
- **Invert B** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Ld3nT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Invert_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Invert_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Invert_v2)

---

### Kaleidoscope_v2
![Kaleidoscope_v2 op](images/ops/Ops_Gl_ImageCompose_Kaleidoscope_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Kaleidoscope_v2`
**Description:** Kaleidoscope effect

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Sides** (Number): *See documentation*
- **Angle** (Number): *See documentation*
- **Slide X** (Number): *See documentation*
- **Slide Y** (Number): *See documentation*
- **Center X** (Number): *See documentation*
- **Center Y** (Number): *See documentation*
- **Aspect Ratio** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/n4DaW6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Kaleidoscope_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Kaleidoscope_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Kaleidoscope_v2)

---

### LensDirt_v2
![LensDirt_v2 op](images/ops/Ops_Gl_ImageCompose_LensDirt_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.LensDirt_v2`
**Description:** Creates a lens dirt like texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Offset X** (Number): *See documentation*
- **Offset Y** (Number): *See documentation*
- **Zoom** (Number): *See documentation*
- **Iterations** (Number: Integer): *See documentation*
- **Seed** (Number: Integer): *See documentation*
- **Spot Edge** (Number): *See documentation*
- **Gamma** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/vwgWMX)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LensDirt_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.LensDirt_v2](https://cables.gl/op/Ops.Gl.ImageCompose.LensDirt_v2)

---

### LensScratches_v2
![LensScratches_v2 op](images/ops/Ops_Gl_ImageCompose_LensScratches_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.LensScratches_v2`
**Description:** Creates a procedural texture simulating scratches on a lens

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Offset X** (Number): *See documentation*
- **Offset Y** (Number): *See documentation*
- **Wavyness** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **Layers** (Number: Integer): *See documentation*
- **AA Iterations** (Number): *See documentation*
- **Frequency** (Number): *See documentation*
- **Frequency Step Size** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ucr5NX)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LensScratches_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.LensScratches_v2](https://cables.gl/op/Ops.Gl.ImageCompose.LensScratches_v2)

---

### Levels_v2
![Levels_v2 op](images/ops/Ops_Gl_ImageCompose_Levels_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Levels_v2`
**Description:** adjust levels to correct the tonal range of an image

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **In Min** (Number): *See documentation*
- **Midpoint** (Number): *See documentation*
- **In Max** (Number): *See documentation*
- **Out Min** (Number): *See documentation*
- **Out Max** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/F8M9W6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Levels_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Levels_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Levels_v2)

---

### LumaKey_v3
![LumaKey_v3 op](images/ops/Ops_Gl_ImageCompose_LumaKey_v3.svg)

**Full Name:** `Ops.Gl.ImageCompose.LumaKey_v3`
**Description:** Remove darkest or brightest parts of the image

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Invert** (Number: Boolean): *See documentation*
- **Black White** (Number: Boolean): *See documentation*
- **Remove Alpha** (Number: Boolean): *See documentation*
- **Remap** (Number: Boolean): *See documentation*
- **Threshold Low** (Number): *See documentation*
- **Threshold High** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ukO5qe)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LumaKey_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.LumaKey_v3](https://cables.gl/op/Ops.Gl.ImageCompose.LumaKey_v3)

---

### LUTMap
![LUTMap op](images/ops/Ops_Gl_ImageCompose_LUTMap.svg)

**Full Name:** `Ops.Gl.ImageCompose.LUTMap`
**Description:** apply color filter/effects by using a lookup texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **LUT Image** (Object:Texture): *See documentation*
- **Amount** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/2_nZX7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LUTMap"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.LUTMap](https://cables.gl/op/Ops.Gl.ImageCompose.LUTMap)

---

### Mirror
![Mirror op](images/ops/Ops_Gl_ImageCompose_Mirror.svg)

**Full Name:** `Ops.Gl.ImageCompose.Mirror`
**Description:** mirroring image effect

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Axis Index** (Number: Integer): *See documentation*
- **Width** (Number): *See documentation*
- **Offset** (Number): *See documentation*
- **Flip** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/MVFoT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Mirror"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Mirror](https://cables.gl/op/Ops.Gl.ImageCompose.Mirror)

---

### Mix
![Mix op](images/ops/Ops_Gl_ImageCompose_Mix.svg)

**Full Name:** `Ops.Gl.ImageCompose.Mix`
**Description:** simple mix/fade of two input images

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Texture 1** (Object:Texture): *See documentation*
- **Fade** (Number): *See documentation*
- **Texture 2** (Object:Texture): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/CDaQK2)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Mix"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Mix](https://cables.gl/op/Ops.Gl.ImageCompose.Mix)

---

### MultiDrawImage
![MultiDrawImage op](images/ops/Ops_Gl_ImageCompose_MultiDrawImage.svg)

**Full Name:** `Ops.Gl.ImageCompose.MultiDrawImage`
**Description:** draw multiple images at once

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Mask Invert** (Number: Boolean): *See documentation*
- **Texture 1** (Object:Texture): *See documentation*
- **Blendmode 1 Index** (Number: Integer): *See documentation*
- **Mask 1** (Object:Texture): *See documentation*
- **Mask Source 1 Index** (Number: Integer): *See documentation*
- **Opacity 1 Index** (Number: Integer): *See documentation*
- **Amount 1** (Number): *See documentation*
- **Texture 2** (Object:Texture): *See documentation*
- **Blendmode 2 Index** (Number: Integer): *See documentation*
- **Mask 2** (Object:Texture): *See documentation*
- **Mask Source 2 Index** (Number: Integer): *See documentation*
- **Opacity 2 Index** (Number: Integer): *See documentation*
- **Amount 2** (Number): *See documentation*
- **Texture 3** (Object:Texture): *See documentation*
- **Blendmode 3 Index** (Number: Integer): *See documentation*
- **Mask 3** (Object:Texture): *See documentation*
- **Mask Source 3 Index** (Number: Integer): *See documentation*
- **Opacity 3 Index** (Number: Integer): *See documentation*
- **Amount 3** (Number): *See documentation*
- **Texture 4** (Object:Texture): *See documentation*
- **Blendmode 4 Index** (Number: Integer): *See documentation*
- **Mask 4** (Object:Texture): *See documentation*
- **Mask Source 4 Index** (Number: Integer): *See documentation*
- **Opacity 4 Index** (Number: Integer): *See documentation*
- **Amount 4** (Number): *See documentation*
- **Texture 5** (Object:Texture): *See documentation*
- **Blendmode 5 Index** (Number: Integer): *See documentation*
- **Mask 5** (Object:Texture): *See documentation*
- **Mask Source 5 Index** (Number: Integer): *See documentation*
- **Opacity 5 Index** (Number: Integer): *See documentation*
- **Amount 5** (Number): *See documentation*
- **Texture 6** (Object:Texture): *See documentation*
- **Blendmode 6 Index** (Number: Integer): *See documentation*
- **Mask 6** (Object:Texture): *See documentation*
- **Mask Source 6 Index** (Number: Integer): *See documentation*
- **Opacity 6 Index** (Number: Integer): *See documentation*
- **Amount 6** (Number): *See documentation*
- **Texture 7** (Object:Texture): *See documentation*
- **Blendmode 7 Index** (Number: Integer): *See documentation*
- **Mask 7** (Object:Texture): *See documentation*
- **Mask Source 7 Index** (Number: Integer): *See documentation*
- **Opacity 7 Index** (Number: Integer): *See documentation*
- **Amount 7** (Number): *See documentation*
- **Texture 8** (Object:Texture): *See documentation*
- **Blendmode 8 Index** (Number: Integer): *See documentation*
- **Mask 8** (Object:Texture): *See documentation*
- **Mask Source 8 Index** (Number: Integer): *See documentation*
- **Opacity 8 Index** (Number: Integer): *See documentation*
- **Amount 8** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dr8EeE)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MultiDrawImage"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.MultiDrawImage](https://cables.gl/op/Ops.Gl.ImageCompose.MultiDrawImage)

---

### OnePassBlur
![OnePassBlur op](images/ops/Ops_Gl_ImageCompose_OnePassBlur.svg)

**Full Name:** `Ops.Gl.ImageCompose.OnePassBlur`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.ImageCompose.OnePassBlur) for details*

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Radius** (Number): *See documentation*
- **Mask** (Object:Texture): *See documentation*
- **Mask Invert** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/xHp9eG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "OnePassBlur"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.OnePassBlur](https://cables.gl/op/Ops.Gl.ImageCompose.OnePassBlur)

---

### PatternLookup
![PatternLookup op](images/ops/Ops_Gl_ImageCompose_PatternLookup.svg)

**Full Name:** `Ops.Gl.ImageCompose.PatternLookup`
**Description:** map a pattern to value levels of your texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Multiplier** (Object): *See documentation*
- **Blend Mode** (Number: String): *See documentation*
- **Amount** (Number): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/lj31ZO)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PatternLookup"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.PatternLookup](https://cables.gl/op/Ops.Gl.ImageCompose.PatternLookup)

---

### Pixelate_v2
![Pixelate_v2 op](images/ops/Ops_Gl_ImageCompose_Pixelate_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Pixelate_v2`
**Description:** Pixelate an image

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Multiplier** (Object:Texture): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/1w_9W6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Pixelate_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Pixelate_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Pixelate_v2)

---

### PixelColor
![PixelColor op](images/ops/Ops_Gl_ImageCompose_PixelColor.svg)

**Full Name:** `Ops.Gl.ImageCompose.PixelColor`
**Description:** fill image with one color picked at a position

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Source Texture** (Object:Texture): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Pos X** (Number): *See documentation*
- **Pos Y** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/qbiIbk)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PixelColor"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.PixelColor](https://cables.gl/op/Ops.Gl.ImageCompose.PixelColor)

---

### PixelDifference
![PixelDifference op](images/ops/Ops_Gl_ImageCompose_PixelDifference.svg)

**Full Name:** `Ops.Gl.ImageCompose.PixelDifference`
**Description:** visualize the difference of neighbouring pixels (slope)

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Strength** (Number): *See documentation*
- **Step** (Number): *See documentation*
- **Red Index** (Number: Integer): *See documentation*
- **Red Flip** (Number: Boolean): *See documentation*
- **Green Index** (Number: Integer): *See documentation*
- **Green Flip** (Number: Boolean): *See documentation*
- **Blue Index** (Number: Integer): *See documentation*
- **Blue Flip** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/LEMBZ4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PixelDifference"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.PixelDifference](https://cables.gl/op/Ops.Gl.ImageCompose.PixelDifference)

---

### PixelDisplacement_v4
![PixelDisplacement_v4 op](images/ops/Ops_Gl_ImageCompose_PixelDisplacement_v4.svg)

**Full Name:** `Ops.Gl.ImageCompose.PixelDisplacement_v4`
**Description:** Changes color lookup for every pixel using a displacement map

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **DisplaceTex** (Object:Texture): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Amount X** (Number): *See documentation*
- **Amount Y** (Number): *See documentation*
- **Input Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Qxb9W6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PixelDisplacement_v4"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.PixelDisplacement_v4](https://cables.gl/op/Ops.Gl.ImageCompose.PixelDisplacement_v4)

---

### Plasma_v2
![Plasma_v2 op](images/ops/Ops_Gl_ImageCompose_Plasma_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Plasma_v2`
**Description:** Renders a plasma effect

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Aspect** (Number: Boolean): *See documentation*
- **Mul** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Time** (Number): *See documentation*
- **Greyscale** (Number: Boolean): *See documentation*
- **Offset** (Object:Texture): *See documentation*
- **Offset Multiply** (Number): *See documentation*
- **Offset X Index** (Number: Integer): *See documentation*
- **Offset Y Index** (Number: Integer): *See documentation*
- **Offset Time Index** (Number: Integer): *See documentation*
- **Mask** (Object:Texture): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dD6aW6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Plasma_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Plasma_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Plasma_v2)

---

### PolarCoords
![PolarCoords op](images/ops/Ops_Gl_ImageCompose_PolarCoords.svg)

**Full Name:** `Ops.Gl.ImageCompose.PolarCoords`
**Description:** display texture using polar/radial coordinate system

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Radius Inner** (Number): *See documentation*
- **Radius Outer** (Number): *See documentation*
- **Crop** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/cM2nB2)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PolarCoords"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.PolarCoords](https://cables.gl/op/Ops.Gl.ImageCompose.PolarCoords)

---

### Posterize_v2
![Posterize_v2 op](images/ops/Ops_Gl_ImageCompose_Posterize_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Posterize_v2`
**Description:** reduce number of colors

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Levels** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/_MMoT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Posterize_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Posterize_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Posterize_v2)

---

### PseudoLensFlares
![PseudoLensFlares op](images/ops/Ops_Gl_ImageCompose_PseudoLensFlares.svg)

**Full Name:** `Ops.Gl.ImageCompose.PseudoLensFlares`
**Description:** simulate lens flare effect

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Ghosts** (Number): *See documentation*
- **Num Ghosts** (Number: Integer): *See documentation*
- **Dispersal** (Number): *See documentation*
- **Halo** (Number): *See documentation*
- **Halo Width** (Number): *See documentation*
- **Color Lookup** (Object): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/P8heur)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PseudoLensFlares"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.PseudoLensFlares](https://cables.gl/op/Ops.Gl.ImageCompose.PseudoLensFlares)

---

### RandomNumberTexture
![RandomNumberTexture op](images/ops/Ops_Gl_ImageCompose_RandomNumberTexture.svg)

**Full Name:** `Ops.Gl.ImageCompose.RandomNumberTexture`
**Description:** Set random numbers into an imagecompose

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Seed** (Number): *See documentation*
- **Min R** (Number): *See documentation*
- **Max R** (Number): *See documentation*
- **Min G** (Number): *See documentation*
- **Max G** (Number): *See documentation*
- **Min B** (Number): *See documentation*
- **Max B** (Number): *See documentation*
- **Min A** (Number): *See documentation*
- **Max A** (Number): *See documentation*
- **Multiply** (Object:Texture): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/j_I1TG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RandomNumberTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.RandomNumberTexture](https://cables.gl/op/Ops.Gl.ImageCompose.RandomNumberTexture)

---

### RectangleTexture_v5
![RectangleTexture_v5 op](images/ops/Ops_Gl_ImageCompose_RectangleTexture_v5.svg)

**Full Name:** `Ops.Gl.ImageCompose.RectangleTexture_v5`
**Description:** draws a 2d rectangle into a texture.

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Amount** (Number): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Center** (Number: Boolean): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Inner** (Number): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Rotate** (Number): *See documentation*
- **Roundness** (Number): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*
- **Map Texture** (Object:Texture): *See documentation*
- **Start X** (Number): *See documentation*
- **Start Y** (Number): *See documentation*
- **Map Width** (Number): *See documentation*
- **Map Height** (Number): *See documentation*
- **Mask** (Object:Texture): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/IPPT7i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RectangleTexture_v5"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.RectangleTexture_v5](https://cables.gl/op/Ops.Gl.ImageCompose.RectangleTexture_v5)

---

### RemoveAlpha
![RemoveAlpha op](images/ops/Ops_Gl_ImageCompose_RemoveAlpha.svg)

**Full Name:** `Ops.Gl.ImageCompose.RemoveAlpha`
**Description:** Remove alpha information from image

**> Input Ports:**
- **Render** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.ImageCompose.RemoveAlpha#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RemoveAlpha"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.RemoveAlpha](https://cables.gl/op/Ops.Gl.ImageCompose.RemoveAlpha)

---

### RepeatTexture_v2
![RepeatTexture_v2 op](images/ops/Ops_Gl_ImageCompose_RepeatTexture_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.RepeatTexture_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.ImageCompose.RepeatTexture_v2) for details*

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Clear** (Number: Boolean): *See documentation*
- **Multiply** (Object:Texture): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/S6JnT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RepeatTexture_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.RepeatTexture_v2](https://cables.gl/op/Ops.Gl.ImageCompose.RepeatTexture_v2)

---

### RgbMultiply
![RgbMultiply op](images/ops/Ops_Gl_ImageCompose_RgbMultiply.svg)

**Full Name:** `Ops.Gl.ImageCompose.RgbMultiply`
**Description:** multiply image colors by color channel

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/3l_8W6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RgbMultiply"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.RgbMultiply](https://cables.gl/op/Ops.Gl.ImageCompose.RgbMultiply)

---

### RGBOffset_v2
![RGBOffset_v2 op](images/ops/Ops_Gl_ImageCompose_RGBOffset_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.RGBOffset_v2`
**Description:** Offsets the xy components of an RGB texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Red Offset X** (Number): *See documentation*
- **Red Offset Y** (Number): *See documentation*
- **Red Amount** (Number): *See documentation*
- **amount of red** (fade, hide, show): *See documentation*
- **Green Offset X** (Number): *See documentation*
- **Green Offset Y** (Number): *See documentation*
- **Green Amount** (Number): *See documentation*
- **amount of green** (fade, hide, show): *See documentation*
- **Blue Offset X** (Number): *See documentation*
- **Blue Offset Y** (Number): *See documentation*
- **Blue Amount** (Number): *See documentation*
- **amount of blue** (fade, hide, show): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/pzC9rn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RGBOffset_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.RGBOffset_v2](https://cables.gl/op/Ops.Gl.ImageCompose.RGBOffset_v2)

---

### RgbToHsvTexture
![RgbToHsvTexture op](images/ops/Ops_Gl_ImageCompose_RgbToHsvTexture.svg)

**Full Name:** `Ops.Gl.ImageCompose.RgbToHsvTexture`
**Description:** Convert a RGB Texture to Hue/Saturation/Lightness values as RGB colors

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Output RGB Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/V7z4v4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RgbToHsvTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.RgbToHsvTexture](https://cables.gl/op/Ops.Gl.ImageCompose.RgbToHsvTexture)

---

### RotateTexture_v2
![RotateTexture_v2 op](images/ops/Ops_Gl_ImageCompose_RotateTexture_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.RotateTexture_v2`
**Description:** Rotates a texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Multiplier** (Object:Texture): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Rotate** (Number): *See documentation*
- **Crop** (Number: Boolean): *See documentation*
- **Clear** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/flURFr)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RotateTexture_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.RotateTexture_v2](https://cables.gl/op/Ops.Gl.ImageCompose.RotateTexture_v2)

---

### RoundCorners
![RoundCorners op](images/ops/Ops_Gl_ImageCompose_RoundCorners.svg)

**Full Name:** `Ops.Gl.ImageCompose.RoundCorners`
**Description:** Draw round corners around image (border)

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Radius** (Number): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/iYLmJ5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RoundCorners"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.RoundCorners](https://cables.gl/op/Ops.Gl.ImageCompose.RoundCorners)

---

### ScaleTexture_v3
![ScaleTexture_v3 op](images/ops/Ops_Gl_ImageCompose_ScaleTexture_v3.svg)

**Full Name:** `Ops.Gl.ImageCompose.ScaleTexture_v3`
**Description:** Scales a texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Multiplier** (Object:Texture): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Scale X** (Number): *See documentation*
- **Scale Y** (Number): *See documentation*
- **Offset X** (Number): *See documentation*
- **Offset Y** (Number): *See documentation*
- **Center X** (Number): *See documentation*
- **Center Y** (Number): *See documentation*
- **Clear** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/kj_Zbx)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScaleTexture_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.ScaleTexture_v3](https://cables.gl/op/Ops.Gl.ImageCompose.ScaleTexture_v3)

---

### ScrollTexture
![ScrollTexture op](images/ops/Ops_Gl_ImageCompose_ScrollTexture.svg)

**Full Name:** `Ops.Gl.ImageCompose.ScrollTexture`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.ImageCompose.ScrollTexture) for details*

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **AmountX** (Number): *See documentation*
- **AmountY** (Number): *See documentation*
- **Mask** (Object:Texture): *See documentation*
- **Repeat** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/DutaW6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScrollTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.ScrollTexture](https://cables.gl/op/Ops.Gl.ImageCompose.ScrollTexture)

---

### Shapes2d_v2
![Shapes2d_v2 op](images/ops/Ops_Gl_ImageCompose_Shapes2d_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Shapes2d_v2`
**Description:** Generates different 2d shapes to use as a texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Shape Index** (Number: Integer): *See documentation*
- **Mirror X** (Number: Boolean): *See documentation*
- **Mirror Y** (Number: Boolean): *See documentation*
- **Offset X** (Number): *See documentation*
- **Offset Y** (Number): *See documentation*
- **FillShape** (Number: Boolean): *See documentation*
- **Line Thickness** (Number): *See documentation*
- **Invert Color** (Number: Boolean): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Rotate** (Number): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/XBGbPO)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Shapes2d_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Shapes2d_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Shapes2d_v2)

---

### Sharpen
![Sharpen op](images/ops/Ops_Gl_ImageCompose_Sharpen.svg)

**Full Name:** `Ops.Gl.ImageCompose.Sharpen`
**Description:** Adjust image sharpness

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Amount** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Q6uJjr)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Sharpen"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Sharpen](https://cables.gl/op/Ops.Gl.ImageCompose.Sharpen)

---

### SkewStretchImage_v2
![SkewStretchImage_v2 op](images/ops/Ops_Gl_ImageCompose_SkewStretchImage_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.SkewStretchImage_v2`
**Description:** skew / stretch an image by rendering scaled sides

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Clamp** (Number: Boolean): *See documentation*
- **Stretch Top** (Number): *See documentation*
- **Stretch Bottom** (Number): *See documentation*
- **Stretch Left** (Number): *See documentation*
- **Stretch Right** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/M2UA7k)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SkewStretchImage_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.SkewStretchImage_v2](https://cables.gl/op/Ops.Gl.ImageCompose.SkewStretchImage_v2)

---

### Stripes_v4
![Stripes_v4 op](images/ops/Ops_Gl_ImageCompose_Stripes_v4.svg)

**Full Name:** `Ops.Gl.ImageCompose.Stripes_v4`
**Description:** Create a texture of stripes /lines

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Num** (Number): *See documentation*
- **Width** (Number): *See documentation*
- **Rotate** (Number): *See documentation*
- **Offset** (Number): *See documentation*
- **Gradients** (Number: Boolean): *See documentation*
- **Circular** (Number: Boolean): *See documentation*
- **Invert** (Number: Boolean): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dYhlT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Stripes_v4"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Stripes_v4](https://cables.gl/op/Ops.Gl.ImageCompose.Stripes_v4)

---

### TexMathModulo
![TexMathModulo op](images/ops/Ops_Gl_ImageCompose_TexMathModulo.svg)

**Full Name:** `Ops.Gl.ImageCompose.TexMathModulo`
**Description:** modulo pixel color values

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Mask Invert** (Number: Boolean): *See documentation*
- **Mask** (Object:Texture): *See documentation*
- **Amount** (Number): *See documentation*
- **Modulo** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/FOpoxm)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TexMathModulo"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.TexMathModulo](https://cables.gl/op/Ops.Gl.ImageCompose.TexMathModulo)

---

### TextureDifference
![TextureDifference op](images/ops/Ops_Gl_ImageCompose_TextureDifference.svg)

**Full Name:** `Ops.Gl.ImageCompose.TextureDifference`
**Description:** render the difference of two textures

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Texture 1** (Object:Texture): *See documentation*
- **Texture 2** (Object:Texture): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/zCDlTi)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureDifference"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.TextureDifference](https://cables.gl/op/Ops.Gl.ImageCompose.TextureDifference)

---

### ToNormalMap_v2
![ToNormalMap_v2 op](images/ops/Ops_Gl_ImageCompose_ToNormalMap_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.ToNormalMap_v2`
**Description:** Convert a black and white map to a normal map

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Strength** (Number): *See documentation*
- **Step Multiplier** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/L62oT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ToNormalMap_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.ToNormalMap_v2](https://cables.gl/op/Ops.Gl.ImageCompose.ToNormalMap_v2)

---

### Twirl_v4
![Twirl_v4 op](images/ops/Ops_Gl_ImageCompose_Twirl_v4.svg)

**Full Name:** `Ops.Gl.ImageCompose.Twirl_v4`
**Description:** Creates a twirl/swirl/spiral effect in a texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Twist Amount** (Number): *See documentation*
- **Radius** (Number): *See documentation*
- **Center X** (Number): *See documentation*
- **Center Y** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/2_pmJ5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Twirl_v4"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Twirl_v4](https://cables.gl/op/Ops.Gl.ImageCompose.Twirl_v4)

---

### Vibrance
![Vibrance op](images/ops/Ops_Gl_ImageCompose_Vibrance.svg)

**Full Name:** `Ops.Gl.ImageCompose.Vibrance`
**Description:** adjust vibrance/saturation

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Amount** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/52iaW6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Vibrance"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Vibrance](https://cables.gl/op/Ops.Gl.ImageCompose.Vibrance)

---

### Vignette_v3
![Vignette_v3 op](images/ops/Ops_Gl_ImageCompose_Vignette_v3.svg)

**Full Name:** `Ops.Gl.ImageCompose.Vignette_v3`
**Description:** Simulating an old camera effect of fading away the edges of the image

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Strength** (Number): *See documentation*
- **Radius** (Number): *See documentation*
- **Sharp** (Number): *See documentation*
- **Aspect** (Number): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **Alpha** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/WDPlT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Vignette_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Vignette_v3](https://cables.gl/op/Ops.Gl.ImageCompose.Vignette_v3)

---

### Waveform_v3
![Waveform_v3 op](images/ops/Ops_Gl_ImageCompose_Waveform_v3.svg)

**Full Name:** `Ops.Gl.ImageCompose.Waveform_v3`
**Description:** Generates 4 different waveform textures. Sine, sawtooth,Triangle, Square.

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Waveform Index** (Number: Integer): *See documentation*
- **Amplitude** (Number): *See documentation*
- **Frequency** (Number): *See documentation*
- **Line Width** (Number): *See documentation*
- **Line Glow** (Number): *See documentation*
- **Invert Color** (Number: Boolean): *See documentation*
- **Solid Fill** (Number: Boolean): *See documentation*
- **Offset X** (Number): *See documentation*
- **Offset Y** (Number): *See documentation*
- **Rotate** (Number): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/9aF_26)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Waveform_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Waveform_v3](https://cables.gl/op/Ops.Gl.ImageCompose.Waveform_v3)

---

### WaveformGradient_v4
![WaveformGradient_v4 op](images/ops/Ops_Gl_ImageCompose_WaveformGradient_v4.svg)

**Full Name:** `Ops.Gl.ImageCompose.WaveformGradient_v4`
**Description:** Generate different texture waveforms. Sine, sawtooth and triangle.

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blend Mode Index** (Number: Integer): *See documentation*
- **Alpha Mask Index** (Number: Integer): *See documentation*
- **Amount** (Number): *See documentation*
- **Mode Index** (Number: Integer): *See documentation*
- **Frequency** (Number): *See documentation*
- **Pow Factor** (Number): *See documentation*
- **Offset** (Number): *See documentation*
- **Rotate** (Number): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Hfw7yu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WaveformGradient_v4"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.WaveformGradient_v4](https://cables.gl/op/Ops.Gl.ImageCompose.WaveformGradient_v4)

---

### Wobble_v2
![Wobble_v2 op](images/ops/Ops_Gl_ImageCompose_Wobble_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.Wobble_v2`
**Description:** waving wobble motion effect

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Time** (Number): *See documentation*
- **SpeedX** (Number): *See documentation*
- **SpeedY** (Number): *See documentation*
- **RepeatX** (Number): *See documentation*
- **RepeatY** (Number): *See documentation*
- **Multiply** (Number): *See documentation*
- **Amount Map** (Object:Texture): *See documentation*
- **Source Amount Map Index** (Number: Integer): *See documentation*
- **Invert Amount Map** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/wpgXXG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Wobble_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.Wobble_v2](https://cables.gl/op/Ops.Gl.ImageCompose.Wobble_v2)

---

### ZoomBlur_v2
![ZoomBlur_v2 op](images/ops/Ops_Gl_ImageCompose_ZoomBlur_v2.svg)

**Full Name:** `Ops.Gl.ImageCompose.ZoomBlur_v2`
**Description:** Directional blur effect

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Strength** (Number): *See documentation*
- **Samples** (Number: Integer): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Strength Map** (Object:Texture): *See documentation*
- **Source Strength Map Index** (Number: Integer): *See documentation*
- **Invert Strength Map** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/qjtoT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ZoomBlur_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageCompose.ZoomBlur_v2](https://cables.gl/op/Ops.Gl.ImageCompose.ZoomBlur_v2)

---

