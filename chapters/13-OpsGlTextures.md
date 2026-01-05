# Ops.Gl.Textures

---

```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### Base64ToTexture
![Base64ToTexture op](images/ops/Ops_Gl_Textures_Base64ToTexture.svg)

**Full Name:** `Ops.Gl.Textures.Base64ToTexture`

**Description:** Converts a base-64 image string into a texture

**`\inputsymbol`{=latex} Inputs**

- **Wrap Index** (Number: Integer)
- **Pre Multiplied Alpha** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Texture** (Object)
- **Has Error** (booleanNumber)
- **Loading** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/dNuMWr)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.Base64ToTexture](https://cables.gl/op/Ops.Gl.Textures.Base64ToTexture)

### ColorTexture
![ColorTexture op](images/ops/Ops_Gl_Textures_ColorTexture.svg)

**Full Name:** `Ops.Gl.Textures.ColorTexture`

**Description:** Simple texture filled with one color

**`\inputsymbol`{=latex} Inputs**

- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)

**`\outputsymbol`{=latex} Output**

- **Texture_out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/QuT1X2)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.ColorTexture](https://cables.gl/op/Ops.Gl.Textures.ColorTexture)

### CombineTextures
![CombineTextures op](images/ops/Ops_Gl_Textures_CombineTextures.svg)

**Full Name:** `Ops.Gl.Textures.CombineTextures`

**Description:** combine multiple textures into one by copying colorchannels

**`\inputsymbol`{=latex} Inputs**

- **Execute** (Trigger)
- **Filter Index** (Number: Integer)
- **Wrap Index** (Number: Integer)
- **Pixel Format Index** (Number: Integer)
- **Size Index** (Number: Integer)
- **R** (Object:Texture)
- **R Source Index** (Number: Integer)
- **R Value Index** (Number: Integer)
- **R Default** (Number)
- **G** (Object:Texture)
- **G Source Index** (Number: Integer)
- **G Value Index** (Number: Integer)
- **G Default** (Number)
- **B** (Object:Texture)
- **B Source Index** (Number: Integer)
- **B Value Index** (Number: Integer)
- **B Default** (Number)
- **A** (Object:Texture)
- **A Source Index** (Number: Integer)
- **A Value Index** (Number: Integer)
- **A Default** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Texture** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/yZJ2WW)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.CombineTextures](https://cables.gl/op/Ops.Gl.Textures.CombineTextures)

### CopyTexture_v3
![CopyTexture_v3 op](images/ops/Ops_Gl_Textures_CopyTexture_v3.svg)

**Full Name:** `Ops.Gl.Textures.CopyTexture_v3`

**Description:** copy a texture and optionally resize it

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Texture** (Object:Texture)
- **Alpha Mask** (Object:Texture)
- **Use Original Size** (Number: Boolean)
- **Width** (Number: Integer)
- **Height** (Number: Integer)
- **Pixel Format Index** (Number: Integer)
- **Wrap Index** (Number: Integer)
- **Invert A** (Number: Boolean)
- **Flip X** (Number: Boolean)
- **Flip Y** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)
- **Texture_out** (Object)
- **Aspect Ratio** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/G2_my7)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.CopyTexture_v3](https://cables.gl/op/Ops.Gl.Textures.CopyTexture_v3)

### EmptyTexture
![EmptyTexture op](images/ops/Ops_Gl_Textures_EmptyTexture.svg)

**Full Name:** `Ops.Gl.Textures.EmptyTexture`

**Description:** A very simple empty transparent texture with an opacity of 0

**`\inputsymbol`{=latex} Inputs**

- **Width** (Number)
- **Height** (Number)

**`\outputsymbol`{=latex} Output**

- **Texture** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/QuT1X2)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.EmptyTexture](https://cables.gl/op/Ops.Gl.Textures.EmptyTexture)

### ExrTexture
![ExrTexture op](images/ops/Ops_Gl_Textures_ExrTexture.svg)

**Full Name:** `Ops.Gl.Textures.ExrTexture`

**Description:** load .exr floating point texture files

**`\inputsymbol`{=latex} Inputs**

- **EXR File** (String)
- **Remove Alpha** (Number: Boolean)
- **Flip** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Texture** (Object)
- **Width** (Number)
- **Height** (Number)
- **Channels** (String)
- **Loading** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/zHxXMW)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.ExrTexture](https://cables.gl/op/Ops.Gl.Textures.ExrTexture)

### GraphTexture
![GraphTexture op](images/ops/Ops_Gl_Textures_GraphTexture.svg)

**Full Name:** `Ops.Gl.Textures.GraphTexture`

**Description:** draw a graph of a value into a texture

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Value** (Number)
- **Index** (Number: Integer)
- **Reset** (Trigger)
- **Color Random Seed** (Number)
- **Texture Width** (Number: Integer)
- **Texture Height** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Texture** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/eqfKTx)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.GraphTexture](https://cables.gl/op/Ops.Gl.Textures.GraphTexture)

### Histogram
![Histogram op](images/ops/Ops_Gl_Textures_Histogram.svg)

**Full Name:** `Ops.Gl.Textures.Histogram`

**Description:** graphical representation of distribution of color in a texture

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Texture** (Object:Texture)

**`\outputsymbol`{=latex} Output**

- **Histogram Texture** (Object)
- **Histogram Data** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Z315nc)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.Histogram](https://cables.gl/op/Ops.Gl.Textures.Histogram)

### MontageTextures_v2
![MontageTextures_v2 op](images/ops/Ops_Gl_Textures_MontageTextures_v2.svg)

**Full Name:** `Ops.Gl.Textures.MontageTextures_v2`

**Description:** combine multiple textures into one by copying colorchannels

**`\inputsymbol`{=latex} Inputs**

- **Execute** (Trigger)
- **Flip Order** (Number: Boolean)
- **Width** (Number: Integer)
- **Height** (Number: Integer)
- **Wrap Index** (Number: Integer)
- **Pixel Format Index** (Number: Integer)
- **Texture 0** (Object:Texture)
- **Texture 1** (Object:Texture)
- **Texture 2** (Object:Texture)
- **Texture 3** (Object:Texture)
- **Texture 4** (Object:Texture)
- **Texture 5** (Object:Texture)
- **Texture 6** (Object:Texture)
- **Texture 7** (Object:Texture)
- **Texture 8** (Object:Texture)
- **Texture 9** (Object:Texture)
- **Texture 10** (Object:Texture)
- **Texture 11** (Object:Texture)
- **Texture 12** (Object:Texture)
- **Texture 13** (Object:Texture)
- **Texture 14** (Object:Texture)
- **Texture 15** (Object:Texture)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Texture** (Object)
- **Columns** (Number)
- **Rows** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/pM45O8)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.MontageTextures_v2](https://cables.gl/op/Ops.Gl.Textures.MontageTextures_v2)

### NoiseTexture
![NoiseTexture op](images/ops/Ops_Gl_Textures_NoiseTexture.svg)

**Full Name:** `Ops.Gl.Textures.NoiseTexture`

**Description:** Simple noisetexture

**`\inputsymbol`{=latex} Inputs**

- **Width** (Number: Integer)
- **Height** (Number: Integer)
- **Wrap Index** (Number: Integer)
- **Color** (Number: Boolean)
- **Pixel Format Index** (Number: Integer)
- **Integer** (Number: Boolean)
- **Seed** (Number)
- **Channel R** (Number: Boolean)
- **Min R** (Number)
- **Max R** (Number)
- **Channel G** (Number: Boolean)
- **Min G** (Number)
- **Max G** (Number)
- **Channel B** (Number: Boolean)
- **Min B** (Number)
- **Max B** (Number)
- **Channel A** (Number: Boolean)
- **Min A** (Number)
- **Max A** (Number)

**`\outputsymbol`{=latex} Output**

- **Texture** (Object)
- **Total Pixel** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Lv4hay)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.NoiseTexture](https://cables.gl/op/Ops.Gl.Textures.NoiseTexture)

### PaletteTexture
![PaletteTexture op](images/ops/Ops_Gl_Textures_PaletteTexture.svg)

**Full Name:** `Ops.Gl.Textures.PaletteTexture`

**Description:** Create a RGB color palette using an array

**`\inputsymbol`{=latex} Inputs**

- **Palette Array** (Array)
- **Smooth** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Color Array** (Array)
- **Texture** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/tdRoSP)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.PaletteTexture](https://cables.gl/op/Ops.Gl.Textures.PaletteTexture)

### SequenceTextures
![SequenceTextures op](images/ops/Ops_Gl_Textures_SequenceTextures.svg)

**Full Name:** `Ops.Gl.Textures.SequenceTextures`

**Description:** control order and flow of objects

**`\inputsymbol`{=latex} Inputs**

- **Texture 0** (Object:Texture)
- **Texture 1** (Object:Texture)
- **Texture 2** (Object:Texture)
- **Texture 3** (Object:Texture)
- **Texture 4** (Object:Texture)
- **Texture 5** (Object:Texture)
- **Texture 6** (Object:Texture)
- **Texture 7** (Object:Texture)
- **Texture 8** (Object:Texture)
- **Texture 9** (Object:Texture)
- **Texture 10** (Object:Texture)
- **Texture 11** (Object:Texture)
- **Texture 12** (Object:Texture)
- **Texture 13** (Object:Texture)
- **Texture 14** (Object:Texture)
- **Texture 15** (Object:Texture)

**`\outputsymbol`{=latex} Output**

- **Output 0** (Object)
- **Output 1** (Object)
- **Output 2** (Object)
- **Output 3** (Object)
- **Output 4** (Object)
- **Output 5** (Object)
- **Output 6** (Object)
- **Output 7** (Object)
- **Output 8** (Object)
- **Output 9** (Object)
- **Output 10** (Object)
- **Output 11** (Object)
- **Output 12** (Object)
- **Output 13** (Object)
- **Output 14** (Object)
- **Output 15** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Textures.SequenceTextures#example)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.SequenceTextures](https://cables.gl/op/Ops.Gl.Textures.SequenceTextures)

### SSAO
![SSAO op](images/ops/Ops_Gl_Textures_SSAO.svg)

**Full Name:** `Ops.Gl.Textures.SSAO`

**Description:** screen space ambient occlusion from depth texture

**`\inputsymbol`{=latex} Inputs**

- **Execute** (Trigger)
- **Depth Texture** (Object:Texture)
- **Radius** (Number)
- **Max Dist** (Number)
- **Begin** (Number)
- **End** (Number)
- **Strength** (Number)
- **Base** (Number)
- **Filter Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **SSAO** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/qt0JiG)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.SSAO](https://cables.gl/op/Ops.Gl.Textures.SSAO)

### SwitchTextureMultiPort_v2
![SwitchTextureMultiPort_v2 op](images/ops/Ops_Gl_Textures_SwitchTextureMultiPort_v2.svg)

**Full Name:** `Ops.Gl.Textures.SwitchTextureMultiPort_v2`

**Description:** Switch between multiple textures

**`\inputsymbol`{=latex} Inputs**

- **Index** (Number: Integer)
- **Textures_0** (Object)
- **Add Port** (Object)

**`\outputsymbol`{=latex} Output**

- **Texture** (Object)
- **Num Textures** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/pDGOrh)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.SwitchTextureMultiPort_v2](https://cables.gl/op/Ops.Gl.Textures.SwitchTextureMultiPort_v2)

### SwitchTextures_v2
![SwitchTextures_v2 op](images/ops/Ops_Gl_Textures_SwitchTextures_v2.svg)

**Full Name:** `Ops.Gl.Textures.SwitchTextures_v2`

**Description:** Switch between different textures

**`\inputsymbol`{=latex} Inputs**

- **Exec** (Trigger)
- **Num** (Number: Integer)
- **Default Texture Transparent** (Number: Boolean)
- **Texture0** (Object:Texture)
- **Texture1** (Object:Texture)
- **Texture2** (Object:Texture)
- **Texture3** (Object:Texture)
- **Texture4** (Object:Texture)
- **Texture5** (Object:Texture)
- **Texture6** (Object:Texture)
- **Texture7** (Object:Texture)
- **Texture8** (Object:Texture)
- **Texture9** (Object:Texture)
- **Texture10** (Object:Texture)
- **Texture11** (Object:Texture)
- **Texture12** (Object:Texture)
- **Texture13** (Object:Texture)
- **Texture14** (Object:Texture)
- **Texture15** (Object:Texture)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Texture** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/gsXwVJ)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.SwitchTextures_v2](https://cables.gl/op/Ops.Gl.Textures.SwitchTextures_v2)

### TextTexture_v6
![TextTexture_v6 op](images/ops/Ops_Gl_Textures_TextTexture_v6.svg)

**Full Name:** `Ops.Gl.Textures.TextTexture_v6`

**Description:** Generates a texture of Text using one of the font ops

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Text** (String)
- **Draw Mesh** (Number: Boolean)
- **Scale Mesh** (Number)
- **Width** (Number: Integer)
- **Height** (Number: Integer)
- **Auto Height** (Number: Boolean)
- **Auto Line Breaks** (Number: Boolean)
- **Font** (String)
- **Weight** (String)
- **FontSize** (Number)
- **Letter Spacing** (Number)
- **Line Height Add** (Number)
- **Padding Y Top** (Number: Integer)
- **Padding Y Bottom** (Number: Integer)
- **Padding X** (Number: Integer)
- **Wrap Index** (Number: Integer)
- **Reuse Texture** (Number: Boolean)
- **Show Debug** (Number: Boolean)
- **Redraw On Font Load** (Number: Boolean)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **Opacity** (Number)
- **Background R** (Number)
- **Background G** (Number)
- **Background B** (Number)
- **Background A** (Number)
- **Force Redraw** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Ratio** (Number)
- **Texture** (Object)
- **Canvas** (Object)
- **Aspect** (Number)
- **Num Lines** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/RZsPWU)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.TextTexture_v6](https://cables.gl/op/Ops.Gl.Textures.TextTexture_v6)

### TextureArrayInfo
![TextureArrayInfo op](images/ops/Ops_Gl_Textures_TextureArrayInfo.svg)

**Full Name:** `Ops.Gl.Textures.TextureArrayInfo`

**Description:** Information about Textures in an array

**`\inputsymbol`{=latex} Inputs**

- **Texture Array** (Array)

**`\outputsymbol`{=latex} Output**

- **Names** (Array)
- **Widths** (Array)
- **Heights** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/vS5fjz)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.TextureArrayInfo](https://cables.gl/op/Ops.Gl.Textures.TextureArrayInfo)

### TextureInfo_v2
![TextureInfo_v2 op](images/ops/Ops_Gl_Textures_TextureInfo_v2.svg)

**Full Name:** `Ops.Gl.Textures.TextureInfo_v2`

**Description:** Outputs information about the connected texture

**`\inputsymbol`{=latex} Inputs**

- **Texture** (Object:Texture)

**`\outputsymbol`{=latex} Output**

- **Name** (String)
- **PixelFormat** (String)
- **Width** (Number)
- **Height** (Number)
- **Ratio** (Number)
- **Filter** (Number)
- **Wrap** (Number)
- **Flipped** (booleanNumber)
- **HDR** (booleanNumber)
- **Is Empty Default Texture** (booleanNumber)
- **Is Default Texture** (booleanNumber)
- **Is Cubemap** (booleanNumber)
- **Id** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/y0A18i)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.TextureInfo_v2](https://cables.gl/op/Ops.Gl.Textures.TextureInfo_v2)

### TextureSVG_v2
![TextureSVG_v2 op](images/ops/Ops_Gl_Textures_TextureSVG_v2.svg)

**Full Name:** `Ops.Gl.Textures.TextureSVG_v2`

**Description:** Load a SVG image and convert to a texture of pixels

**`\inputsymbol`{=latex} Inputs**

- **File** (String)
- **Texture Width** (Number: Integer)
- **Texture Height** (Number: Integer)
- **Wrap Index** (Number: Integer)
- **Filter Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Texture** (Object)
- **Loaded** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/oqCKY6)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.TextureSVG_v2](https://cables.gl/op/Ops.Gl.Textures.TextureSVG_v2)

### TextureToBase64_v5
![TextureToBase64_v5 op](images/ops/Ops_Gl_Textures_TextureToBase64_v5.svg)

**Full Name:** `Ops.Gl.Textures.TextureToBase64_v5`

**Description:** Converts a texture into a base-64 image string

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Texture** (Object:Texture)
- **Quality** (Number)
- **Output DataUrl** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Binary Size** (Number)
- **Base64 String** (String)
- **Loading** (booleanNumber)
- **Finished** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/dNuMWr)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.TextureToBase64_v5](https://cables.gl/op/Ops.Gl.Textures.TextureToBase64_v5)

### TextureToCoordinateGrid
![TextureToCoordinateGrid op](images/ops/Ops_Gl_Textures_TextureToCoordinateGrid.svg)

**Full Name:** `Ops.Gl.Textures.TextureToCoordinateGrid`

**Description:** convert a texture to a 3d coordinate grid storing coordinates in texture RGB channels

**`\inputsymbol`{=latex} Inputs**

- **Execute** (Trigger)
- **Texture** (Object:Texture)
- **Aspect** (Number)
- **Threshold** (Number)
- **Repeats** (Number: Integer)
- **Repeats Spacing** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **HDR Texture** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/nMBUVW)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.TextureToCoordinateGrid](https://cables.gl/op/Ops.Gl.Textures.TextureToCoordinateGrid)

### VideoTexture_v3
![VideoTexture_v3 op](images/ops/Ops_Gl_Textures_VideoTexture_v3.svg)

**Full Name:** `Ops.Gl.Textures.VideoTexture_v3`

**Description:** Play a video file and use it as a texture

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **File** (String)
- **Play** (Number: Boolean)
- **Loop** (Number: Boolean)
- **Volume** (Number)
- **Mute** (Number: Boolean)
- **Update FPS** (Number)
- **Wrap Index** (Number: Integer)
- **Flip** (Number: Boolean)
- **Speed** (Number)
- **Set Time** (Number)
- **Rewind** (Trigger)
- **Preload** (Number: Boolean)
- **Show Interaction Needed Button** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Texture** (Object)
- **Duration** (Number)
- **Progress** (Number)
- **Interaction Needed** (booleanNumber)
- **CurrentTime** (Number)
- **Loading** (booleanNumber)
- **Playing** (booleanNumber)
- **Can Play Through** (booleanNumber)
- **Width** (Number)
- **Height** (Number)
- **Aspect Ratio** (Number)
- **Has Error** (booleanNumber)
- **Auto FPS** (booleanNumber)
- **Error Message** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/RQCm0m)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.VideoTexture_v3](https://cables.gl/op/Ops.Gl.Textures.VideoTexture_v3)

### WebcamTexture_v3
![WebcamTexture_v3 op](images/ops/Ops_Gl_Textures_WebcamTexture_v3.svg)

**Full Name:** `Ops.Gl.Textures.WebcamTexture_v3`

**Description:** Use your webcam camera as a texture

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Active** (Number: Boolean)
- **Generate Texture** (Number: Boolean)
- **Webcam Input Index** (Number: Integer)
- **Requested Width** (Number: Integer)
- **Requested Height** (Number: Integer)
- **Flip X** (Number: Boolean)
- **Flip Y** (Number: Boolean)
- **Show HTML Element** (Number: Boolean)
- **CSS** (String)
- **Element Flip X** (Number: Boolean)
- **Element Flip Y** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Texture** (Object)
- **Ratio** (Number)
- **Available** (booleanNumber)
- **Size Width** (Number)
- **Size Height** (Number)
- **Error** (String)
- **HTML Element** (Object)
- **Available Devices** (Array)
- **Active Device** (String)
- **Texture Updated** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/iwaEwm)

**Docs:** [https://cables.gl/op/Ops.Gl.Textures.WebcamTexture_v3](https://cables.gl/op/Ops.Gl.Textures.WebcamTexture_v3)


