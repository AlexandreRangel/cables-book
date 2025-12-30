# Ops.Gl.Textures

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.Textures

### Base64ToTexture
![Base64ToTexture op](images/ops/Ops_Gl_Textures_Base64ToTexture.svg)

**Full Name:** `Ops.Gl.Textures.Base64ToTexture`
**Description:** Converts a base-64 image string into a texture

**> Input Ports:**
- **Wrap Index** (Number: Integer): *See documentation*
- **Pre Multiplied Alpha** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Texture** (Object): *See documentation*
- **Has Error** (booleanNumber): *See documentation*
- **Loading** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dNuMWr)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Base64ToTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.Base64ToTexture](https://cables.gl/op/Ops.Gl.Textures.Base64ToTexture)

---

### ColorTexture
![ColorTexture op](images/ops/Ops_Gl_Textures_ColorTexture.svg)

**Full Name:** `Ops.Gl.Textures.ColorTexture`
**Description:** Simple texture filled with one color

**> Input Ports:**
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*

**< Output Ports:**
- **Texture_out** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/QuT1X2)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.ColorTexture](https://cables.gl/op/Ops.Gl.Textures.ColorTexture)

---

### CombineTextures
![CombineTextures op](images/ops/Ops_Gl_Textures_CombineTextures.svg)

**Full Name:** `Ops.Gl.Textures.CombineTextures`
**Description:** combine multiple textures into one by copying colorchannels

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Filter Index** (Number: Integer): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Pixel Format Index** (Number: Integer): *See documentation*
- **Size Index** (Number: Integer): *See documentation*
- **R** (Object:Texture): *See documentation*
- **R Source Index** (Number: Integer): *See documentation*
- **R Value Index** (Number: Integer): *See documentation*
- **R Default** (Number): *See documentation*
- **G** (Object:Texture): *See documentation*
- **G Source Index** (Number: Integer): *See documentation*
- **G Value Index** (Number: Integer): *See documentation*
- **G Default** (Number): *See documentation*
- **B** (Object:Texture): *See documentation*
- **B Source Index** (Number: Integer): *See documentation*
- **B Value Index** (Number: Integer): *See documentation*
- **B Default** (Number): *See documentation*
- **A** (Object:Texture): *See documentation*
- **A Source Index** (Number: Integer): *See documentation*
- **A Value Index** (Number: Integer): *See documentation*
- **A Default** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Texture** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/yZJ2WW)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CombineTextures"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.CombineTextures](https://cables.gl/op/Ops.Gl.Textures.CombineTextures)

---

### CopyTexture_v3
![CopyTexture_v3 op](images/ops/Ops_Gl_Textures_CopyTexture_v3.svg)

**Full Name:** `Ops.Gl.Textures.CopyTexture_v3`
**Description:** copy a texture and optionally resize it

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Texture** (Object:Texture): *See documentation*
- **Alpha Mask** (Object:Texture): *See documentation*
- **Use Original Size** (Number: Boolean): *See documentation*
- **Width** (Number: Integer): *See documentation*
- **Height** (Number: Integer): *See documentation*
- **Pixel Format Index** (Number: Integer): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Invert A** (Number: Boolean): *See documentation*
- **Flip X** (Number: Boolean): *See documentation*
- **Flip Y** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Texture_out** (Object): *See documentation*
- **Aspect Ratio** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/G2_my7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CopyTexture_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.CopyTexture_v3](https://cables.gl/op/Ops.Gl.Textures.CopyTexture_v3)

---

### EmptyTexture
![EmptyTexture op](images/ops/Ops_Gl_Textures_EmptyTexture.svg)

**Full Name:** `Ops.Gl.Textures.EmptyTexture`
**Description:** A very simple empty transparent texture with an opacity of 0

**> Input Ports:**
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*

**< Output Ports:**
- **Texture** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/QuT1X2)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "EmptyTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.EmptyTexture](https://cables.gl/op/Ops.Gl.Textures.EmptyTexture)

---

### ExrTexture
![ExrTexture op](images/ops/Ops_Gl_Textures_ExrTexture.svg)

**Full Name:** `Ops.Gl.Textures.ExrTexture`
**Description:** load .exr floating point texture files

**> Input Ports:**
- **EXR File** (String): *See documentation*
- **Remove Alpha** (Number: Boolean): *See documentation*
- **Flip** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Texture** (Object): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Channels** (String): *See documentation*
- **Loading** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/zHxXMW)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ExrTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.ExrTexture](https://cables.gl/op/Ops.Gl.Textures.ExrTexture)

---

### GraphTexture
![GraphTexture op](images/ops/Ops_Gl_Textures_GraphTexture.svg)

**Full Name:** `Ops.Gl.Textures.GraphTexture`
**Description:** draw a graph of a value into a texture

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **Value** (Number): *See documentation*
- **Index** (Number: Integer): *See documentation*
- **Reset** (Trigger): *See documentation*
- **Color Random Seed** (Number): *See documentation*
- **Texture Width** (Number: Integer): *See documentation*
- **Texture Height** (Number: Integer): *See documentation*

**< Output Ports:**
- **Texture** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/eqfKTx)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GraphTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.GraphTexture](https://cables.gl/op/Ops.Gl.Textures.GraphTexture)

---

### Histogram
![Histogram op](images/ops/Ops_Gl_Textures_Histogram.svg)

**Full Name:** `Ops.Gl.Textures.Histogram`
**Description:** graphical representation of distribution of color in a texture

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **Texture** (Object:Texture): *See documentation*

**< Output Ports:**
- **Histogram Texture** (Object): *See documentation*
- **Histogram Data** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Z315nc)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Histogram"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.Histogram](https://cables.gl/op/Ops.Gl.Textures.Histogram)

---

### MontageTextures_v2
![MontageTextures_v2 op](images/ops/Ops_Gl_Textures_MontageTextures_v2.svg)

**Full Name:** `Ops.Gl.Textures.MontageTextures_v2`
**Description:** combine multiple textures into one by copying colorchannels

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Flip Order** (Number: Boolean): *See documentation*
- **Width** (Number: Integer): *See documentation*
- **Height** (Number: Integer): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Pixel Format Index** (Number: Integer): *See documentation*
- **Texture 0** (Object:Texture): *See documentation*
- **Texture 1** (Object:Texture): *See documentation*
- **Texture 2** (Object:Texture): *See documentation*
- **Texture 3** (Object:Texture): *See documentation*
- **Texture 4** (Object:Texture): *See documentation*
- **Texture 5** (Object:Texture): *See documentation*
- **Texture 6** (Object:Texture): *See documentation*
- **Texture 7** (Object:Texture): *See documentation*
- **Texture 8** (Object:Texture): *See documentation*
- **Texture 9** (Object:Texture): *See documentation*
- **Texture 10** (Object:Texture): *See documentation*
- **Texture 11** (Object:Texture): *See documentation*
- **Texture 12** (Object:Texture): *See documentation*
- **Texture 13** (Object:Texture): *See documentation*
- **Texture 14** (Object:Texture): *See documentation*
- **Texture 15** (Object:Texture): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Texture** (Object): *See documentation*
- **Columns** (Number): *See documentation*
- **Rows** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/pM45O8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MontageTextures_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.MontageTextures_v2](https://cables.gl/op/Ops.Gl.Textures.MontageTextures_v2)

---

### NoiseTexture
![NoiseTexture op](images/ops/Ops_Gl_Textures_NoiseTexture.svg)

**Full Name:** `Ops.Gl.Textures.NoiseTexture`
**Description:** Simple noisetexture

**> Input Ports:**
- **Width** (Number: Integer): *See documentation*
- **Height** (Number: Integer): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Color** (Number: Boolean): *See documentation*
- **Pixel Format Index** (Number: Integer): *See documentation*
- **Integer** (Number: Boolean): *See documentation*
- **Seed** (Number): *See documentation*
- **Channel R** (Number: Boolean): *See documentation*
- **Min R** (Number): *See documentation*
- **Max R** (Number): *See documentation*
- **Channel G** (Number: Boolean): *See documentation*
- **Min G** (Number): *See documentation*
- **Max G** (Number): *See documentation*
- **Channel B** (Number: Boolean): *See documentation*
- **Min B** (Number): *See documentation*
- **Max B** (Number): *See documentation*
- **Channel A** (Number: Boolean): *See documentation*
- **Min A** (Number): *See documentation*
- **Max A** (Number): *See documentation*

**< Output Ports:**
- **Texture** (Object): *See documentation*
- **Total Pixel** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Lv4hay)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "NoiseTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.NoiseTexture](https://cables.gl/op/Ops.Gl.Textures.NoiseTexture)

---

### PaletteTexture
![PaletteTexture op](images/ops/Ops_Gl_Textures_PaletteTexture.svg)

**Full Name:** `Ops.Gl.Textures.PaletteTexture`
**Description:** Create a RGB color palette using an array

**> Input Ports:**
- **Palette Array** (Array): *See documentation*
- **Smooth** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Color Array** (Array): *See documentation*
- **Texture** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/tdRoSP)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PaletteTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.PaletteTexture](https://cables.gl/op/Ops.Gl.Textures.PaletteTexture)

---

### SequenceTextures
![SequenceTextures op](images/ops/Ops_Gl_Textures_SequenceTextures.svg)

**Full Name:** `Ops.Gl.Textures.SequenceTextures`
**Description:** control order and flow of objects

**> Input Ports:**
- **Texture 0** (Object:Texture): *See documentation*
- **Texture 1** (Object:Texture): *See documentation*
- **Texture 2** (Object:Texture): *See documentation*
- **Texture 3** (Object:Texture): *See documentation*
- **Texture 4** (Object:Texture): *See documentation*
- **Texture 5** (Object:Texture): *See documentation*
- **Texture 6** (Object:Texture): *See documentation*
- **Texture 7** (Object:Texture): *See documentation*
- **Texture 8** (Object:Texture): *See documentation*
- **Texture 9** (Object:Texture): *See documentation*
- **Texture 10** (Object:Texture): *See documentation*
- **Texture 11** (Object:Texture): *See documentation*
- **Texture 12** (Object:Texture): *See documentation*
- **Texture 13** (Object:Texture): *See documentation*
- **Texture 14** (Object:Texture): *See documentation*
- **Texture 15** (Object:Texture): *See documentation*

**< Output Ports:**
- **Output 0** (Object): *See documentation*
- **Output 1** (Object): *See documentation*
- **Output 2** (Object): *See documentation*
- **Output 3** (Object): *See documentation*
- **Output 4** (Object): *See documentation*
- **Output 5** (Object): *See documentation*
- **Output 6** (Object): *See documentation*
- **Output 7** (Object): *See documentation*
- **Output 8** (Object): *See documentation*
- **Output 9** (Object): *See documentation*
- **Output 10** (Object): *See documentation*
- **Output 11** (Object): *See documentation*
- **Output 12** (Object): *See documentation*
- **Output 13** (Object): *See documentation*
- **Output 14** (Object): *See documentation*
- **Output 15** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Textures.SequenceTextures#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SequenceTextures"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.SequenceTextures](https://cables.gl/op/Ops.Gl.Textures.SequenceTextures)

---

### SSAO
![SSAO op](images/ops/Ops_Gl_Textures_SSAO.svg)

**Full Name:** `Ops.Gl.Textures.SSAO`
**Description:** screen space ambient occlusion from depth texture

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Depth Texture** (Object:Texture): *See documentation*
- **Radius** (Number): *See documentation*
- **Max Dist** (Number): *See documentation*
- **Begin** (Number): *See documentation*
- **End** (Number): *See documentation*
- **Strength** (Number): *See documentation*
- **Base** (Number): *See documentation*
- **Filter Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **SSAO** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/qt0JiG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SSAO"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.SSAO](https://cables.gl/op/Ops.Gl.Textures.SSAO)

---

### SwitchTextureMultiPort_v2
![SwitchTextureMultiPort_v2 op](images/ops/Ops_Gl_Textures_SwitchTextureMultiPort_v2.svg)

**Full Name:** `Ops.Gl.Textures.SwitchTextureMultiPort_v2`
**Description:** Switch between multiple textures

**> Input Ports:**
- **Index** (Number: Integer): *See documentation*
- **Textures_0** (Object): *See documentation*
- **Add Port** (Object): *See documentation*

**< Output Ports:**
- **Texture** (Object): *See documentation*
- **Num Textures** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/pDGOrh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SwitchTextureMultiPort_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.SwitchTextureMultiPort_v2](https://cables.gl/op/Ops.Gl.Textures.SwitchTextureMultiPort_v2)

---

### SwitchTextures_v2
![SwitchTextures_v2 op](images/ops/Ops_Gl_Textures_SwitchTextures_v2.svg)

**Full Name:** `Ops.Gl.Textures.SwitchTextures_v2`
**Description:** Switch between different textures

**> Input Ports:**
- **Exec** (Trigger): *See documentation*
- **Num** (Number: Integer): *See documentation*
- **Default Texture Transparent** (Number: Boolean): *See documentation*
- **Texture0** (Object:Texture): *See documentation*
- **Texture1** (Object:Texture): *See documentation*
- **Texture2** (Object:Texture): *See documentation*
- **Texture3** (Object:Texture): *See documentation*
- **Texture4** (Object:Texture): *See documentation*
- **Texture5** (Object:Texture): *See documentation*
- **Texture6** (Object:Texture): *See documentation*
- **Texture7** (Object:Texture): *See documentation*
- **Texture8** (Object:Texture): *See documentation*
- **Texture9** (Object:Texture): *See documentation*
- **Texture10** (Object:Texture): *See documentation*
- **Texture11** (Object:Texture): *See documentation*
- **Texture12** (Object:Texture): *See documentation*
- **Texture13** (Object:Texture): *See documentation*
- **Texture14** (Object:Texture): *See documentation*
- **Texture15** (Object:Texture): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Texture** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/gsXwVJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SwitchTextures_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.SwitchTextures_v2](https://cables.gl/op/Ops.Gl.Textures.SwitchTextures_v2)

---

### TextTexture_v6
![TextTexture_v6 op](images/ops/Ops_Gl_Textures_TextTexture_v6.svg)

**Full Name:** `Ops.Gl.Textures.TextTexture_v6`
**Description:** Generates a texture of Text using one of the font ops

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Text** (String): *See documentation*
- **Draw Mesh** (Number: Boolean): *See documentation*
- **Scale Mesh** (Number): *See documentation*
- **Width** (Number: Integer): *See documentation*
- **Height** (Number: Integer): *See documentation*
- **Auto Height** (Number: Boolean): *See documentation*
- **Auto Line Breaks** (Number: Boolean): *See documentation*
- **Font** (String): *See documentation*
- **Weight** (String): *See documentation*
- **FontSize** (Number): *See documentation*
- **Letter Spacing** (Number): *See documentation*
- **Line Height Add** (Number): *See documentation*
- **Padding Y Top** (Number: Integer): *See documentation*
- **Padding Y Bottom** (Number: Integer): *See documentation*
- **Padding X** (Number: Integer): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Reuse Texture** (Number: Boolean): *See documentation*
- **Show Debug** (Number: Boolean): *See documentation*
- **Redraw On Font Load** (Number: Boolean): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **Opacity** (Number): *See documentation*
- **Background R** (Number): *See documentation*
- **Background G** (Number): *See documentation*
- **Background B** (Number): *See documentation*
- **Background A** (Number): *See documentation*
- **Force Redraw** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Ratio** (Number): *See documentation*
- **Texture** (Object): *See documentation*
- **Canvas** (Object): *See documentation*
- **Aspect** (Number): *See documentation*
- **Num Lines** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/RZsPWU)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextTexture_v6"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.TextTexture_v6](https://cables.gl/op/Ops.Gl.Textures.TextTexture_v6)

---

### TextureArrayInfo
![TextureArrayInfo op](images/ops/Ops_Gl_Textures_TextureArrayInfo.svg)

**Full Name:** `Ops.Gl.Textures.TextureArrayInfo`
**Description:** Information about Textures in an array

**> Input Ports:**
- **Texture Array** (Array): *See documentation*

**< Output Ports:**
- **Names** (Array): *See documentation*
- **Widths** (Array): *See documentation*
- **Heights** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/vS5fjz)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureArrayInfo"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.TextureArrayInfo](https://cables.gl/op/Ops.Gl.Textures.TextureArrayInfo)

---

### TextureInfo_v2
![TextureInfo_v2 op](images/ops/Ops_Gl_Textures_TextureInfo_v2.svg)

**Full Name:** `Ops.Gl.Textures.TextureInfo_v2`
**Description:** Outputs information about the connected texture

**> Input Ports:**
- **Texture** (Object:Texture): *See documentation*

**< Output Ports:**
- **Name** (String): *See documentation*
- **PixelFormat** (String): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Ratio** (Number): *See documentation*
- **Filter** (Number): *See documentation*
- **Wrap** (Number): *See documentation*
- **Flipped** (booleanNumber): *See documentation*
- **HDR** (booleanNumber): *See documentation*
- **Is Empty Default Texture** (booleanNumber): *See documentation*
- **Is Default Texture** (booleanNumber): *See documentation*
- **Is Cubemap** (booleanNumber): *See documentation*
- **Id** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/y0A18i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureInfo_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.TextureInfo_v2](https://cables.gl/op/Ops.Gl.Textures.TextureInfo_v2)

---

### TextureSVG_v2
![TextureSVG_v2 op](images/ops/Ops_Gl_Textures_TextureSVG_v2.svg)

**Full Name:** `Ops.Gl.Textures.TextureSVG_v2`
**Description:** Load a SVG image and convert to a texture of pixels

**> Input Ports:**
- **File** (String): *See documentation*
- **Texture Width** (Number: Integer): *See documentation*
- **Texture Height** (Number: Integer): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Filter Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Texture** (Object): *See documentation*
- **Loaded** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/oqCKY6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureSVG_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.TextureSVG_v2](https://cables.gl/op/Ops.Gl.Textures.TextureSVG_v2)

---

### TextureToBase64_v5
![TextureToBase64_v5 op](images/ops/Ops_Gl_Textures_TextureToBase64_v5.svg)

**Full Name:** `Ops.Gl.Textures.TextureToBase64_v5`
**Description:** Converts a texture into a base-64 image string

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **Texture** (Object:Texture): *See documentation*
- **Quality** (Number): *See documentation*
- **Output DataUrl** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Binary Size** (Number): *See documentation*
- **Base64 String** (String): *See documentation*
- **Loading** (booleanNumber): *See documentation*
- **Finished** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dNuMWr)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureToBase64_v5"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.TextureToBase64_v5](https://cables.gl/op/Ops.Gl.Textures.TextureToBase64_v5)

---

### TextureToCoordinateGrid
![TextureToCoordinateGrid op](images/ops/Ops_Gl_Textures_TextureToCoordinateGrid.svg)

**Full Name:** `Ops.Gl.Textures.TextureToCoordinateGrid`
**Description:** convert a texture to a 3d coordinate grid storing coordinates in texture RGB channels

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Texture** (Object:Texture): *See documentation*
- **Aspect** (Number): *See documentation*
- **Threshold** (Number): *See documentation*
- **Repeats** (Number: Integer): *See documentation*
- **Repeats Spacing** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **HDR Texture** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/nMBUVW)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureToCoordinateGrid"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.TextureToCoordinateGrid](https://cables.gl/op/Ops.Gl.Textures.TextureToCoordinateGrid)

---

### VideoTexture_v3
![VideoTexture_v3 op](images/ops/Ops_Gl_Textures_VideoTexture_v3.svg)

**Full Name:** `Ops.Gl.Textures.VideoTexture_v3`
**Description:** Play a video file and use it as a texture

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **File** (String): *See documentation*
- **Play** (Number: Boolean): *See documentation*
- **Loop** (Number: Boolean): *See documentation*
- **Volume** (Number): *See documentation*
- **Mute** (Number: Boolean): *See documentation*
- **Update FPS** (Number): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Flip** (Number: Boolean): *See documentation*
- **Speed** (Number): *See documentation*
- **Set Time** (Number): *See documentation*
- **Rewind** (Trigger): *See documentation*
- **Preload** (Number: Boolean): *See documentation*
- **Show Interaction Needed Button** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Texture** (Object): *See documentation*
- **Duration** (Number): *See documentation*
- **Progress** (Number): *See documentation*
- **Interaction Needed** (booleanNumber): *See documentation*
- **CurrentTime** (Number): *See documentation*
- **Loading** (booleanNumber): *See documentation*
- **Playing** (booleanNumber): *See documentation*
- **Can Play Through** (booleanNumber): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Aspect Ratio** (Number): *See documentation*
- **Has Error** (booleanNumber): *See documentation*
- **Auto FPS** (booleanNumber): *See documentation*
- **Error Message** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/RQCm0m)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "VideoTexture_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.VideoTexture_v3](https://cables.gl/op/Ops.Gl.Textures.VideoTexture_v3)

---

### WebcamTexture_v3
![WebcamTexture_v3 op](images/ops/Ops_Gl_Textures_WebcamTexture_v3.svg)

**Full Name:** `Ops.Gl.Textures.WebcamTexture_v3`
**Description:** Use your webcam camera as a texture

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Generate Texture** (Number: Boolean): *See documentation*
- **Webcam Input Index** (Number: Integer): *See documentation*
- **Requested Width** (Number: Integer): *See documentation*
- **Requested Height** (Number: Integer): *See documentation*
- **Flip X** (Number: Boolean): *See documentation*
- **Flip Y** (Number: Boolean): *See documentation*
- **Show HTML Element** (Number: Boolean): *See documentation*
- **CSS** (String): *See documentation*
- **Element Flip X** (Number: Boolean): *See documentation*
- **Element Flip Y** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Texture** (Object): *See documentation*
- **Ratio** (Number): *See documentation*
- **Available** (booleanNumber): *See documentation*
- **Size Width** (Number): *See documentation*
- **Size Height** (Number): *See documentation*
- **Error** (String): *See documentation*
- **HTML Element** (Object): *See documentation*
- **Available Devices** (Array): *See documentation*
- **Active Device** (String): *See documentation*
- **Texture Updated** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/iwaEwm)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WebcamTexture_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.Textures.WebcamTexture_v3](https://cables.gl/op/Ops.Gl.Textures.WebcamTexture_v3)

---

