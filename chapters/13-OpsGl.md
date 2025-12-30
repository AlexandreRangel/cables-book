# Ops.Gl

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl

### ArrayToTexture_v2
![ArrayToTexture_v2 op](images/ops/Ops_Gl_ArrayToTexture_v2.svg)

**Full Name:** `Ops.Gl.ArrayToTexture_v2`
**Description:** create a texture from an array of number values

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Array** (Array): *See documentation*
- **Width** (Number: Integer): *See documentation*
- **Height** (Number: Integer): *See documentation*
- **Fill Up** (Number: Boolean): *See documentation*
- **Flip** (Number: Boolean): *See documentation*
- **Pixel Format Index** (Number: Integer): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Texture Out** (Object): *See documentation*
- **Tex Width** (Number): *See documentation*
- **Tex Height** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/cOlh_C)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayToTexture_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ArrayToTexture_v2](https://cables.gl/op/Ops.Gl.ArrayToTexture_v2)

---

### BlendMode
![BlendMode op](images/ops/Ops_Gl_BlendMode.svg)

**Full Name:** `Ops.Gl.BlendMode`
**Description:** change how colors are mixed (blending/mixing modes)

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Blendmode Index** (Number: Integer): *See documentation*
- **Premultiplied** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/x1-Fvc)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BlendMode"*
**Docs:** [https://cables.gl/op/Ops.Gl.BlendMode](https://cables.gl/op/Ops.Gl.BlendMode)

---

### CanvasFocus
![CanvasFocus op](images/ops/Ops_Gl_CanvasFocus.svg)

**Full Name:** `Ops.Gl.CanvasFocus`
**Description:** is canvas focussed ?

**> Input Ports:**
- **Focus** (Trigger): *See documentation*

**< Output Ports:**
- **Has Focus** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/vGwM7f)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CanvasFocus"*
**Docs:** [https://cables.gl/op/Ops.Gl.CanvasFocus](https://cables.gl/op/Ops.Gl.CanvasFocus)

---

### CanvasInfo_v3
![CanvasInfo_v3 op](images/ops/Ops_Gl_CanvasInfo_v3.svg)

**Full Name:** `Ops.Gl.CanvasInfo_v3`
**Description:** the size of the canvas in pixels, aspect ratio and pixel density

**> Input Ports:**
- *Visit [Ops.Gl.CanvasInfo_v3 documentation](https://cables.gl/op/Ops.Gl.CanvasInfo_v3) for input port details*

**< Output Ports:**
- **CSS Width** (Number): *See documentation*
- **CSS Height** (Number): *See documentation*
- **Pixel Ratio** (Number): *See documentation*
- **Pixel Width** (Number): *See documentation*
- **Pixel Height** (Number): *See documentation*
- **Aspect Ratio** (Number): *See documentation*
- **Landscape** (booleanNumber): *See documentation*
- **Canvas** (Object): *See documentation*
- **Canvas Parent** (Object): *See documentation*
- **Resized** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/2yaD8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CanvasInfo_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.CanvasInfo_v3](https://cables.gl/op/Ops.Gl.CanvasInfo_v3)

---

### CanvasToTexture
![CanvasToTexture op](images/ops/Ops_Gl_CanvasToTexture.svg)

**Full Name:** `Ops.Gl.CanvasToTexture`
**Description:** convert a canvas to texture

**> Input Ports:**
- **Canvas** (Object): *See documentation*
- **Filter Index** (Number: Integer): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Force Update** (Trigger): *See documentation*

**< Output Ports:**
- **Texture** (Object): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/QjlEo-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CanvasToTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.CanvasToTexture](https://cables.gl/op/Ops.Gl.CanvasToTexture)

---

### ClearColor
![ClearColor op](images/ops/Ops_Gl_ClearColor.svg)

**Full Name:** `Ops.Gl.ClearColor`
**Description:** sets all cleared pixels to one colour. Use to change the background colour.

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/_UEjvr)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ClearColor"*
**Docs:** [https://cables.gl/op/Ops.Gl.ClearColor](https://cables.gl/op/Ops.Gl.ClearColor)

---

### ClearDepth
![ClearDepth op](images/ops/Ops_Gl_ClearDepth.svg)

**Full Name:** `Ops.Gl.ClearDepth`
**Description:** Clears the depth buffer (zbuffer, z buffer)

**> Input Ports:**
- **Render** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/rEesag)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ClearDepth"*
**Docs:** [https://cables.gl/op/Ops.Gl.ClearDepth](https://cables.gl/op/Ops.Gl.ClearDepth)

---

### ColorMask
![ColorMask op](images/ops/Ops_Gl_ColorMask.svg)

**Full Name:** `Ops.Gl.ColorMask`
**Description:** enable/disable RGBA color channels of your entire scene

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Red** (Number: Boolean): *See documentation*
- **Green** (Number: Boolean): *See documentation*
- **Blue** (Number: Boolean): *See documentation*
- **Alpha** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/MqQSR7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorMask"*
**Docs:** [https://cables.gl/op/Ops.Gl.ColorMask](https://cables.gl/op/Ops.Gl.ColorMask)

---

### ColorPick
![ColorPick op](images/ops/Ops_Gl_ColorPick.svg)

**Full Name:** `Ops.Gl.ColorPick`
**Description:** pick a color at x,y coordinates of canvas

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*

**< Output Ports:**
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/YEjkgg)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorPick"*
**Docs:** [https://cables.gl/op/Ops.Gl.ColorPick](https://cables.gl/op/Ops.Gl.ColorPick)

---

### DirectionalTranslate
![DirectionalTranslate op](images/ops/Ops_Gl_DirectionalTranslate.svg)

**Full Name:** `Ops.Gl.DirectionalTranslate`
**Description:** translate away from a point in space

**> Input Ports:**
- **Exec** (Trigger): *See documentation*
- **Center Model Matrix** (Array): *See documentation*
- **Amount** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/5gL9On)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DirectionalTranslate"*
**Docs:** [https://cables.gl/op/Ops.Gl.DirectionalTranslate](https://cables.gl/op/Ops.Gl.DirectionalTranslate)

---

### DownloadTexture_v3
![DownloadTexture_v3 op](images/ops/Ops_Gl_DownloadTexture_v3.svg)

**Full Name:** `Ops.Gl.DownloadTexture_v3`
**Description:** Download a texture as an image file

**> Input Ports:**
- **Texture** (Object:Texture): *See documentation*
- **Quality** (Number): *See documentation*
- **Filename** (String): *See documentation*
- **Download** (Trigger): *See documentation*

**< Output Ports:**
- **Jcrmz8mnz** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/15LaTs)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DownloadTexture_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.DownloadTexture_v3](https://cables.gl/op/Ops.Gl.DownloadTexture_v3)

---

### DrawTextureMapping
![DrawTextureMapping op](images/ops/Ops_Gl_DrawTextureMapping.svg)

**Full Name:** `Ops.Gl.DrawTextureMapping`
**Description:** draw texture mapping coordinates

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Geometry** (Object:Geometry): *See documentation*
- **Num Points** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Nu7dJ5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DrawTextureMapping"*
**Docs:** [https://cables.gl/op/Ops.Gl.DrawTextureMapping](https://cables.gl/op/Ops.Gl.DrawTextureMapping)

---

### ElementInBrowserViewport
![ElementInBrowserViewport op](images/ops/Ops_Gl_ElementInBrowserViewport.svg)

**Full Name:** `Ops.Gl.ElementInBrowserViewport`
**Description:** check if webgl canvas element is in the current browser viewport

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Element** (Object:Element): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Fully Visible** (booleanNumber): *See documentation*
- **Partly Visible** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.ElementInBrowserViewport#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementInBrowserViewport"*
**Docs:** [https://cables.gl/op/Ops.Gl.ElementInBrowserViewport](https://cables.gl/op/Ops.Gl.ElementInBrowserViewport)

---

### ExternalCanvas
![ExternalCanvas op](images/ops/Ops_Gl_ExternalCanvas.svg)

**Full Name:** `Ops.Gl.ExternalCanvas`
**Description:** Open a new window that shows a copy of the patch canvas

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Pos X** (Number: Integer): *See documentation*
- **Pos Y** (Number: Integer): *See documentation*
- **Width** (Number: Integer): *See documentation*
- **Height** (Number: Integer): *See documentation*
- **Smoothing** (Number: Boolean): *See documentation*
- **Stretch** (Number: Boolean): *See documentation*
- **Title** (String): *See documentation*
- **Open Window** (Trigger): *See documentation*
- **Fullscreen** (Trigger): *See documentation*
- **Close** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Element** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/HnG3fB)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ExternalCanvas"*
**Docs:** [https://cables.gl/op/Ops.Gl.ExternalCanvas](https://cables.gl/op/Ops.Gl.ExternalCanvas)

---

### FaceCulling_v2
![FaceCulling_v2 op](images/ops/Ops_Gl_FaceCulling_v2.svg)

**Full Name:** `Ops.Gl.FaceCulling_v2`
**Description:** Disable the rendering of front or back facing triangles with culling

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/mPwnD-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FaceCulling_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.FaceCulling_v2](https://cables.gl/op/Ops.Gl.FaceCulling_v2)

---

### FontMSDF_v2
![FontMSDF_v2 op](images/ops/Ops_Gl_FontMSDF_v2.svg)

**Full Name:** `Ops.Gl.FontMSDF_v2`
**Description:** Load MSDF Font data and texture to use

**> Input Ports:**
- **Font Name** (String): *See documentation*
- **Font Data** (String): *See documentation*
- **Font Image** (String): *See documentation*
- **Font Image 1** (String): *See documentation*
- **Font Image 2** (String): *See documentation*
- **Font Image 3** (String): *See documentation*

**< Output Ports:**
- **Loaded** (booleanNumber): *See documentation*
- **Total Chars** (Number): *See documentation*
- **Chars** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/9COr26)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FontMSDF_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.FontMSDF_v2](https://cables.gl/op/Ops.Gl.FontMSDF_v2)

---

### ForceCanvasSize
![ForceCanvasSize op](images/ops/Ops_Gl_ForceCanvasSize.svg)

**Full Name:** `Ops.Gl.ForceCanvasSize`
**Description:** Resize canvas element to a specific pixel size or aspect ratio

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Center In Parent** (Number: Boolean): *See documentation*
- **Scale To Fit Parent** (Number: Boolean): *See documentation*
- **Set Width** (Number: Integer): *See documentation*
- **Set Height** (Number: Integer): *See documentation*
- **Aspect Ratio Index** (Number: Integer): *See documentation*
- **Ratio** (Number): *See documentation*
- **Fill Parent Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Margin Left** (Number): *See documentation*
- **Margin Top** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/f9UbD-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ForceCanvasSize"*
**Docs:** [https://cables.gl/op/Ops.Gl.ForceCanvasSize](https://cables.gl/op/Ops.Gl.ForceCanvasSize)

---

### GateTexture
![GateTexture op](images/ops/Ops_Gl_GateTexture.svg)

**Full Name:** `Ops.Gl.GateTexture`
**Description:** Will only allow an Object to to be output if the the pass through parameter evaluates to true

**> Input Ports:**
- **Object In** (Object:Texture): *See documentation*
- **Pass Through** (Number: Boolean): *See documentation*
- **Only Valid Textures** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Object Out** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.GateTexture#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GateTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.GateTexture](https://cables.gl/op/Ops.Gl.GateTexture)

---

### GlBlendFunc
![GlBlendFunc op](images/ops/Ops_Gl_GlBlendFunc.svg)

**Full Name:** `Ops.Gl.GlBlendFunc`
**Description:** set gl blendmodes directly

**> Input Ports:**
- **Exec** (Trigger): *See documentation*
- **Src RGB Index** (Number: Integer): *See documentation*
- **Dst RGB Index** (Number: Integer): *See documentation*
- **Src Alpha Index** (Number: Integer): *See documentation*
- **Dst Alpha Index** (Number: Integer): *See documentation*
- **Blend Equation Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/24qZz7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GlBlendFunc"*
**Docs:** [https://cables.gl/op/Ops.Gl.GlBlendFunc](https://cables.gl/op/Ops.Gl.GlBlendFunc)

---

### GlInfo_v2
![GlInfo_v2 op](images/ops/Ops_Gl_GlInfo_v2.svg)

**Full Name:** `Ops.Gl.GlInfo_v2`
**Description:** information about the webgl context

**> Input Ports:**
- *Visit [Ops.Gl.GlInfo_v2 documentation](https://cables.gl/op/Ops.Gl.GlInfo_v2) for input port details*

**< Output Ports:**
- **WebGl Version Short** (Number): *See documentation*
- **WebGl Version** (String): *See documentation*
- **GLSL Version** (String): *See documentation*
- **Max Frag Uniforms** (Number): *See documentation*
- **Max Vert Uniforms** (Number): *See documentation*
- **Max Texture Size** (Number): *See documentation*
- **Max Texture Units** (Number): *See documentation*
- **Max Varying Vectors** (Number): *See documentation*
- **Max MSAA Samples** (Number): *See documentation*
- **Extensions** (Array): *See documentation*
- **Vendor** (String): *See documentation*
- **Renderer** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/0zHu8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GlInfo_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.GlInfo_v2](https://cables.gl/op/Ops.Gl.GlInfo_v2)

---

### GlPrimitive
![GlPrimitive op](images/ops/Ops_Gl_GlPrimitive.svg)

**Full Name:** `Ops.Gl.GlPrimitive`
**Description:** force rendering of meshes using points,lines or triangles

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Primitive Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/a5Mz8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GlPrimitive"*
**Docs:** [https://cables.gl/op/Ops.Gl.GlPrimitive](https://cables.gl/op/Ops.Gl.GlPrimitive)

---

### GradientTexture
![GradientTexture op](images/ops/Ops_Gl_GradientTexture.svg)

**Full Name:** `Ops.Gl.GradientTexture`
**Description:** texture containing a colour gradient that can be altered with an editor

**> Input Ports:**
- **Gradient** (Number): *See documentation*
- **Direction Index** (Number: Integer): *See documentation*
- **Smoothstep** (Number: Boolean): *See documentation*
- **Step** (Number: Boolean): *See documentation*
- **Flip** (Number: Boolean): *See documentation*
- **SRGB** (Number: Boolean): *See documentation*
- **Oklab** (Number: Boolean): *See documentation*
- **Size** (Number: Integer): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Dither** (Number): *See documentation*
- **Gradient Array** (Array): *See documentation*
- **Randomize Colors** (Trigger): *See documentation*

**< Output Ports:**
- **Texture** (Object): *See documentation*
- **Alpha Mask** (Object): *See documentation*
- **Colors** (Array): *See documentation*
- **Colors Pos** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/_wQNDW)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GradientTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.GradientTexture](https://cables.gl/op/Ops.Gl.GradientTexture)

---

### GridTransform
![GridTransform op](images/ops/Ops_Gl_GridTransform.svg)

**Full Name:** `Ops.Gl.GridTransform`
**Description:** transform and arrange elements into a grid

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Num X** (Number: Integer): *See documentation*
- **Num Y** (Number: Integer): *See documentation*
- **Space X** (Number): *See documentation*
- **Space Y** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Index** (Number): *See documentation*
- **X Index** (Number): *See documentation*
- **Y Index** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/J-XMNQ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GridTransform"*
**Docs:** [https://cables.gl/op/Ops.Gl.GridTransform](https://cables.gl/op/Ops.Gl.GridTransform)

---

### Identity
![Identity op](images/ops/Ops_Gl_Identity.svg)

**Full Name:** `Ops.Gl.Identity`
**Description:** reset all transforms (modelmatrix)

**> Input Ports:**
- **Exe** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/KUVJ8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Identity"*
**Docs:** [https://cables.gl/op/Ops.Gl.Identity](https://cables.gl/op/Ops.Gl.Identity)

---

### IdentityViewMatrix
![IdentityViewMatrix op](images/ops/Ops_Gl_IdentityViewMatrix.svg)

**Full Name:** `Ops.Gl.IdentityViewMatrix`
**Description:** reset the view matrix (cameras etc.)

**> Input Ports:**
- **Exe** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/H01Ici)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "IdentityViewMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.IdentityViewMatrix](https://cables.gl/op/Ops.Gl.IdentityViewMatrix)

---

### ImageSequenceAnim_v2
![ImageSequenceAnim_v2 op](images/ops/Ops_Gl_ImageSequenceAnim_v2.svg)

**Full Name:** `Ops.Gl.ImageSequenceAnim_v2`
**Description:** play a image sprite animation

**> Input Ports:**
- **Time** (Number): *See documentation*
- **FPS** (Number): *See documentation*
- **Num X** (Number): *See documentation*
- **Num Y** (Number): *See documentation*
- **Max Frames** (Number: Integer): *See documentation*
- **Flip Y** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Repeat X** (Number): *See documentation*
- **Repeat Y** (Number): *See documentation*
- **Offset X** (Number): *See documentation*
- **Offset Y** (Number): *See documentation*
- **Frame** (Number): *See documentation*
- **Progress** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/n0iMSq)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ImageSequenceAnim_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageSequenceAnim_v2](https://cables.gl/op/Ops.Gl.ImageSequenceAnim_v2)

---

### InteractiveRectangle_v2
![InteractiveRectangle_v2 op](images/ops/Ops_Gl_InteractiveRectangle_v2.svg)

**Full Name:** `Ops.Gl.InteractiveRectangle_v2`
**Description:** An area which is interactive

**> Input Ports:**
- **Trigger In** (Trigger): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **ID** (String): *See documentation*
- **Class** (String): *See documentation*
- **Pivot X Index** (Number: Integer): *See documentation*
- **Pivot Y Index** (Number: Integer): *See documentation*
- **Axis Index** (Number: Integer): *See documentation*
- **Is Interactive** (Number: Boolean): *See documentation*
- **Render Rectangle** (Number: Boolean): *See documentation*
- **Show Boundings** (Number: Boolean): *See documentation*
- **Cursor Index** (Number: Integer): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*
- **Pointer Hover** (booleanNumber): *See documentation*
- **Pointer Down** (booleanNumber): *See documentation*
- **Pointer X** (Number): *See documentation*
- **Pointer Y** (Number): *See documentation*
- **Top** (Number): *See documentation*
- **Left** (Number): *See documentation*
- **Right** (Number): *See documentation*
- **Bottom** (Number): *See documentation*
- **Left Click** (Trigger): *See documentation*
- **Dom Element** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/P_SED0)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InteractiveRectangle_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.InteractiveRectangle_v2](https://cables.gl/op/Ops.Gl.InteractiveRectangle_v2)

---

### LayerSequence
![LayerSequence op](images/ops/Ops_Gl_LayerSequence.svg)

**Full Name:** `Ops.Gl.LayerSequence`
**Description:** Render Multiple Layers in a specific order

**> Input Ports:**
- **Exe** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger 0** (Trigger): *See documentation*
- **Trigger 1** (Trigger): *See documentation*
- **Trigger 2** (Trigger): *See documentation*
- **Trigger 3** (Trigger): *See documentation*
- **Trigger 4** (Trigger): *See documentation*
- **Trigger 5** (Trigger): *See documentation*
- **Trigger 6** (Trigger): *See documentation*
- **Trigger 7** (Trigger): *See documentation*
- **Trigger 8** (Trigger): *See documentation*
- **Trigger 9** (Trigger): *See documentation*
- **Trigger 10** (Trigger): *See documentation*
- **Trigger 11** (Trigger): *See documentation*
- **Trigger 12** (Trigger): *See documentation*
- **Trigger 13** (Trigger): *See documentation*
- **Trigger 14** (Trigger): *See documentation*
- **Trigger 15** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/VH4Oxj)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LayerSequence"*
**Docs:** [https://cables.gl/op/Ops.Gl.LayerSequence](https://cables.gl/op/Ops.Gl.LayerSequence)

---

### LineFont_v2
![LineFont_v2 op](images/ops/Ops_Gl_LineFont_v2.svg)

**Full Name:** `Ops.Gl.LineFont_v2`
**Description:** A Simple way to write text on the screen.

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Text** (String): *See documentation*
- **Letter Spacing** (Number): *See documentation*

**< Output Ports:**
- **Lines** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/1JzPLu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LineFont_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.LineFont_v2](https://cables.gl/op/Ops.Gl.LineFont_v2)

---

### MainLoop_v2
![MainLoop_v2 op](images/ops/Ops_Gl_MainLoop_v2.svg)

**Full Name:** `Ops.Gl.MainLoop_v2`
**Description:** Trigger other ops once every frame to create smooth animations

**> Input Ports:**
- **FPS Limit** (Number): *See documentation*
- **Reduce FPS Unfocussed** (Number: Boolean): *See documentation*
- **Transparent** (Number: Boolean): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Focus Canvas** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Pixel Density** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/uZxfQc)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MainLoop_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.MainLoop_v2](https://cables.gl/op/Ops.Gl.MainLoop_v2)

---

### MediaRecorder_v2
![MediaRecorder_v2 op](images/ops/Ops_Gl_MediaRecorder_v2.svg)

**Full Name:** `Ops.Gl.MediaRecorder_v2`
**Description:** Record the renderer-output to video

**> Input Ports:**
- **Recording** (Number: Boolean): *See documentation*
- **Filename** (String): *See documentation*
- **Download Video** (Number: Boolean): *See documentation*
- **Mimetype Index** (Number: Integer): *See documentation*
- **MBit** (Number): *See documentation*
- **Max FPS** (Number): *See documentation*
- **Force FPS** (Number): *See documentation*
- **Audio In** (Object:AudioNode): *See documentation*
- **Video Canvas Id** (String): *See documentation*

**< Output Ports:**
- **State** (String): *See documentation*
- **Error** (String): *See documentation*
- **Final Mimetype** (String): *See documentation*
- **Valid Mimetypes** (Array): *See documentation*
- **Duration** (Number): *See documentation*
- **Finished Recording** (Trigger): *See documentation*
- **Video DataUrl** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ioiDIR)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MediaRecorder_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.MediaRecorder_v2](https://cables.gl/op/Ops.Gl.MediaRecorder_v2)

---

### MeshInstancer_v4
![MeshInstancer_v4 op](images/ops/Ops_Gl_MeshInstancer_v4.svg)

**Full Name:** `Ops.Gl.MeshInstancer_v4`
**Description:** Draw the same mesh multiple times on the GPU

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Geom** (Object:Geometry): *See documentation*
- **Scale** (Number): *See documentation*
- **Limit Instances** (Number: Boolean): *See documentation*
- **Limit** (Number: Integer): *See documentation*
- **Positions** (Array): *See documentation*
- **Scale Array** (Array): *See documentation*
- **Rotations** (Array): *See documentation*
- **Colors** (Array): *See documentation*
- **TexCoords** (Array): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*
- **Num** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/oOsjJ5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MeshInstancer_v4"*
**Docs:** [https://cables.gl/op/Ops.Gl.MeshInstancer_v4](https://cables.gl/op/Ops.Gl.MeshInstancer_v4)

---

### MeshMorph
![MeshMorph op](images/ops/Ops_Gl_MeshMorph.svg)

**Full Name:** `Ops.Gl.MeshMorph`
**Description:** morph from one geometry to another

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Geometry** (Number: Integer): *See documentation*
- **Duration** (Number): *See documentation*
- **Index** (Number): *See documentation*
- **Index 2** (Number): *See documentation*
- **Fade** (Number): *See documentation*
- **Easing Index** (Number: Integer): *See documentation*
- **Geometry 0** (Object): *See documentation*
- **Geometry 1** (Object): *See documentation*
- **Geometry 2** (Object): *See documentation*
- **Geometry 3** (Object): *See documentation*
- **Geometry 4** (Object): *See documentation*
- **Geometry 5** (Object): *See documentation*
- **Geometry 6** (Object): *See documentation*
- **Geometry 7** (Object): *See documentation*
- **Geometry 8** (Object): *See documentation*
- **Geometry 9** (Object): *See documentation*
- **Geometry 10** (Object): *See documentation*
- **Geometry 11** (Object): *See documentation*
- **Geometry 12** (Object): *See documentation*
- **Geometry 13** (Object): *See documentation*
- **Geometry 14** (Object): *See documentation*
- **Geometry 15** (Object): *See documentation*

**< Output Ports:**
- **Finished** (booleanNumber): *See documentation*
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/PdhglN)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MeshMorph"*
**Docs:** [https://cables.gl/op/Ops.Gl.MeshMorph](https://cables.gl/op/Ops.Gl.MeshMorph)

---

### NormalizeScreenCoordinates
![NormalizeScreenCoordinates op](images/ops/Ops_Gl_NormalizeScreenCoordinates.svg)

**Full Name:** `Ops.Gl.NormalizeScreenCoordinates`
**Description:** convert screen pixel coordinates to range 0-1

**> Input Ports:**
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*

**< Output Ports:**
- **Result X** (Number): *See documentation*
- **Result Y** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.NormalizeScreenCoordinates#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "NormalizeScreenCoordinates"*
**Docs:** [https://cables.gl/op/Ops.Gl.NormalizeScreenCoordinates](https://cables.gl/op/Ops.Gl.NormalizeScreenCoordinates)

---

### OrTexture
![OrTexture op](images/ops/Ops_Gl_OrTexture.svg)

**Full Name:** `Ops.Gl.OrTexture`
**Description:** outputs the first valid texture of the

**> Input Ports:**
- **Texture 1** (Object:Texture): *See documentation*
- **Texture 2** (Object:Texture): *See documentation*
- **Texture 3** (Object:Texture): *See documentation*
- **Texture 4** (Object:Texture): *See documentation*
- **Texture 5** (Object:Texture): *See documentation*
- **Texture 6** (Object:Texture): *See documentation*
- **Texture 7** (Object:Texture): *See documentation*
- **Texture 8** (Object:Texture): *See documentation*

**< Output Ports:**
- **Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/oKRY7i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "OrTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.OrTexture](https://cables.gl/op/Ops.Gl.OrTexture)

---

### Orthogonal_v2
![Orthogonal_v2 op](images/ops/Ops_Gl_Orthogonal_v2.svg)

**Full Name:** `Ops.Gl.Orthogonal_v2`
**Description:** Orthogonal projection / objects in distance don't appear smaller (isometric)

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Bounds** (Number): *See documentation*
- **Axis Index** (Number: Integer): *See documentation*
- **Frustum Near** (Number): *See documentation*
- **Frustum Far** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Ratio** (Number): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/94Aycg)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Orthogonal_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Orthogonal_v2](https://cables.gl/op/Ops.Gl.Orthogonal_v2)

---

### OverwriteViewportSize
![OverwriteViewportSize op](images/ops/Ops_Gl_OverwriteViewportSize.svg)

**Full Name:** `Ops.Gl.OverwriteViewportSize`
**Description:** Force a manually set viewport size for connected ops

**> Input Ports:**
- **Exec** (Trigger): *See documentation*
- **Width** (Number: Integer): *See documentation*
- **Height** (Number: Integer): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.OverwriteViewportSize#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "OverwriteViewportSize"*
**Docs:** [https://cables.gl/op/Ops.Gl.OverwriteViewportSize](https://cables.gl/op/Ops.Gl.OverwriteViewportSize)

---

### Performance
![Performance op](images/ops/Ops_Gl_Performance.svg)

**Full Name:** `Ops.Gl.Performance`
**Description:** Show WebGl Performance Statistics

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Visible** (Number: Boolean): *See documentation*
- **Measure GPU** (Number: Boolean): *See documentation*
- **Open** (Number: Boolean): *See documentation*
- **Smooth Graph** (Number: Boolean): *See documentation*
- **Scale** (Number): *See documentation*
- **Size** (Number): *See documentation*

**< Output Ports:**
- **Childs** (Trigger): *See documentation*
- **Canvas** (Object): *See documentation*
- **FPS** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/zFR8z5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Performance"*
**Docs:** [https://cables.gl/op/Ops.Gl.Performance](https://cables.gl/op/Ops.Gl.Performance)

---

### PerformanceMeasure
![PerformanceMeasure op](images/ops/Ops_Gl_PerformanceMeasure.svg)

**Full Name:** `Ops.Gl.PerformanceMeasure`
**Description:** Measure the time used to execute all child ops

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Name** (String): *See documentation*

**< Output Ports:**
- **Childs** (Trigger): *See documentation*
- **Time Used** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.PerformanceMeasure#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PerformanceMeasure"*
**Docs:** [https://cables.gl/op/Ops.Gl.PerformanceMeasure](https://cables.gl/op/Ops.Gl.PerformanceMeasure)

---

### Perspective
![Perspective op](images/ops/Ops_Gl_Perspective.svg)

**Full Name:** `Ops.Gl.Perspective`
**Description:** Adjust FOV, field of view, and frustum clipping

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **FOV Degrees** (Number): *See documentation*
- **Frustum Near** (Number): *See documentation*
- **Frustum Far** (Number): *See documentation*
- **Auto Aspect Ratio** (Number: Boolean): *See documentation*
- **Aspect Ratio** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Aspect** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/RJXV7i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Perspective"*
**Docs:** [https://cables.gl/op/Ops.Gl.Perspective](https://cables.gl/op/Ops.Gl.Perspective)

---

### PixelProjection_v3
![PixelProjection_v3 op](images/ops/Ops_Gl_PixelProjection_v3.svg)

**Full Name:** `Ops.Gl.PixelProjection_v3`
**Description:** Remaps world co-ordinates to a pixel co-ordinate system

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Frustum Near** (Number): *See documentation*
- **Frustum Far** (Number): *See documentation*
- **Flip X** (Number: Boolean): *See documentation*
- **Flip Y** (Number: Boolean): *See documentation*
- **Zero Y** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Size Width** (Number): *See documentation*
- **Size Height** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/fsOPNS)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PixelProjection_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.PixelProjection_v3](https://cables.gl/op/Ops.Gl.PixelProjection_v3)

---

### PointCollector
![PointCollector op](images/ops/Ops_Gl_PointCollector.svg)

**Full Name:** `Ops.Gl.PointCollector`
**Description:** save points/coordinates in an array

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Absolute** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Points** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.PointCollector#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointCollector"*
**Docs:** [https://cables.gl/op/Ops.Gl.PointCollector](https://cables.gl/op/Ops.Gl.PointCollector)

---

### PointCollectorCollect
![PointCollectorCollect op](images/ops/Ops_Gl_PointCollectorCollect.svg)

**Full Name:** `Ops.Gl.PointCollectorCollect`
**Description:** collect world space coordinates into an array

**> Input Ports:**
- **Render** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.PointCollectorCollect#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointCollectorCollect"*
**Docs:** [https://cables.gl/op/Ops.Gl.PointCollectorCollect](https://cables.gl/op/Ops.Gl.PointCollectorCollect)

---

### PointCollectorScreenCoords
![PointCollectorScreenCoords op](images/ops/Ops_Gl_PointCollectorScreenCoords.svg)

**Full Name:** `Ops.Gl.PointCollectorScreenCoords`
**Description:** collect screen pixel coordinates into an array

**> Input Ports:**
- **Render** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.PointCollectorScreenCoords#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointCollectorScreenCoords"*
**Docs:** [https://cables.gl/op/Ops.Gl.PointCollectorScreenCoords](https://cables.gl/op/Ops.Gl.PointCollectorScreenCoords)

---

### RandomCluster
![RandomCluster op](images/ops/Ops_Gl_RandomCluster.svg)

**Full Name:** `Ops.Gl.RandomCluster`
**Description:** Transforms objects randomly in space

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Num** (Number: Integer): *See documentation*
- **Random Seed** (Number): *See documentation*
- **Round** (Number: Boolean): *See documentation*
- **Size** (Number): *See documentation*
- **ScaleX** (Number): *See documentation*
- **ScaleY** (Number): *See documentation*
- **ScaleZ** (Number): *See documentation*
- **Rotate X** (Number): *See documentation*
- **Rotate Y** (Number): *See documentation*
- **Rotate Z** (Number): *See documentation*
- **Scroll X** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Index** (Number): *See documentation*
- **Rnd** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Ah6Rj6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RandomCluster"*
**Docs:** [https://cables.gl/op/Ops.Gl.RandomCluster](https://cables.gl/op/Ops.Gl.RandomCluster)

---

### RenderAnim_v2
![RenderAnim_v2 op](images/ops/Ops_Gl_RenderAnim_v2.svg)

**Full Name:** `Ops.Gl.RenderAnim_v2`
**Description:** record, render an animation and save as webm video file or png image sequence

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **File Type Index** (Number: Integer): *See documentation*
- **ZIP Multiple Files** (Number: Boolean): *See documentation*
- **Download Files** (Number: Boolean): *See documentation*
- **Filename** (String): *See documentation*
- **Quality** (Number): *See documentation*
- **Duration** (Number: Integer): *See documentation*
- **FPS** (Number: Integer): *See documentation*
- **Transparency** (Number: Boolean): *See documentation*
- **Use Canvas Size** (Number: Boolean): *See documentation*
- **Texture Width** (Number: Integer): *See documentation*
- **Texture Height** (Number: Integer): *See documentation*
- **Start** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Progress** (Number): *See documentation*
- **Frame** (Number): *See documentation*
- **Status** (String): *See documentation*
- **Started** (booleanNumber): *See documentation*
- **Data URL** (String): *See documentation*
- **Finished** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/bQhm8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RenderAnim_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.RenderAnim_v2](https://cables.gl/op/Ops.Gl.RenderAnim_v2)

---

### RenderGeometry_v2
![RenderGeometry_v2 op](images/ops/Ops_Gl_RenderGeometry_v2.svg)

**Full Name:** `Ops.Gl.RenderGeometry_v2`
**Description:** Render a geometry as mesh

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Geometry** (Object:Geometry): *See documentation*
- **Add Vertex Numbers** (Number: Boolean): *See documentation*
- **Render Mesh** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/w6QYlH)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RenderGeometry_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.RenderGeometry_v2](https://cables.gl/op/Ops.Gl.RenderGeometry_v2)

---

### RenderToTexture_v3
![RenderToTexture_v3 op](images/ops/Ops_Gl_RenderToTexture_v3.svg)

**Full Name:** `Ops.Gl.RenderToTexture_v3`
**Description:** Render into an Image

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Texture Width** (Number: Integer): *See documentation*
- **Texture Height** (Number: Integer): *See documentation*
- **Auto Aspect** (Number: Boolean): *See documentation*
- **Pixel Format Index** (Number: Integer): *See documentation*
- **Depth** (Number: Boolean): *See documentation*
- **Clear** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Texture** (Object): *See documentation*
- **TextureDepth** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/G2_my7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RenderToTexture_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.RenderToTexture_v3](https://cables.gl/op/Ops.Gl.RenderToTexture_v3)

---

### RenderToTextures_v3
![RenderToTextures_v3 op](images/ops/Ops_Gl_RenderToTextures_v3.svg)

**Full Name:** `Ops.Gl.RenderToTextures_v3`
**Description:** render to multiple textures at the same time

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Texture Width** (Number: Integer): *See documentation*
- **Texture Height** (Number: Integer): *See documentation*
- **Auto Aspect** (Number: Boolean): *See documentation*
- **Pixel Format Index** (Number: Integer): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Clear** (Number: Boolean): *See documentation*
- **Texture 0 Index** (Number: Integer): *See documentation*
- **Texture 1 Index** (Number: Integer): *See documentation*
- **Texture 2 Index** (Number: Integer): *See documentation*
- **Texture 3 Index** (Number: Integer): *See documentation*
- **Texture 4 Index** (Number: Integer): *See documentation*
- **Texture 5 Index** (Number: Integer): *See documentation*
- **Texture 6 Index** (Number: Integer): *See documentation*
- **Texture 7 Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Result Texture 0** (Object): *See documentation*
- **Result Texture 1** (Object): *See documentation*
- **Result Texture 2** (Object): *See documentation*
- **Result Texture 3** (Object): *See documentation*
- **Result Texture 4** (Object): *See documentation*
- **Result Texture 5** (Object): *See documentation*
- **Result Texture 6** (Object): *See documentation*
- **Result Texture 7** (Object): *See documentation*
- **TextureDepth** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/muH2jG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RenderToTextures_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.RenderToTextures_v3](https://cables.gl/op/Ops.Gl.RenderToTextures_v3)

---

### ResetTransform
![ResetTransform op](images/ops/Ops_Gl_ResetTransform.svg)

**Full Name:** `Ops.Gl.ResetTransform`
**Description:** reset current transforms to initial value (identity)

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Reset Model Transform** (Number: Boolean): *See documentation*
- **Reset View Transform** (Number: Boolean): *See documentation*
- **Default View** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/kY3J8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ResetTransform"*
**Docs:** [https://cables.gl/op/Ops.Gl.ResetTransform](https://cables.gl/op/Ops.Gl.ResetTransform)

---

### SaveScreenShot_v3
![SaveScreenShot_v3 op](images/ops/Ops_Gl_SaveScreenShot_v3.svg)

**Full Name:** `Ops.Gl.SaveScreenShot_v3`
**Description:** Download the current screen content as png file

**> Input Ports:**
- **Filename** (String): *See documentation*
- **Use Canvas Size** (Number: Boolean): *See documentation*
- **Screenshot** (Trigger): *See documentation*
- **Width** (Number: Integer): *See documentation*
- **Height** (Number: Integer): *See documentation*

**< Output Ports:**
- **Finished** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/OB0Qmi)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SaveScreenShot_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.SaveScreenShot_v3](https://cables.gl/op/Ops.Gl.SaveScreenShot_v3)

---

### ShowNormals_v2
![ShowNormals_v2 op](images/ops/Ops_Gl_ShowNormals_v2.svg)

**Full Name:** `Ops.Gl.ShowNormals_v2`
**Description:** visualize normals, tangents or bitangents

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Draw** (Number: Boolean): *See documentation*
- **Geometry** (Object:Geometry): *See documentation*
- **Length** (Number): *See documentation*
- **Colorize** (Number: Boolean): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Line Geom** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/4NeG02)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ShowNormals_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShowNormals_v2](https://cables.gl/op/Ops.Gl.ShowNormals_v2)

---

### SurfaceScatter_v2
![SurfaceScatter_v2 op](images/ops/Ops_Gl_SurfaceScatter_v2.svg)

**Full Name:** `Ops.Gl.SurfaceScatter_v2`
**Description:** Scatter an object on the surface of a mesh with different distribution methods

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Draw** (Number: Boolean): *See documentation*
- **Num** (Number: Integer): *See documentation*
- **Geom Surface** (Object): *See documentation*
- **Distribution Index** (Number: Integer): *See documentation*
- **Selection Index** (Number: Integer): *See documentation*
- **Random Seed** (Number): *See documentation*
- **Size Min** (Number): *See documentation*
- **Size Max** (Number): *See documentation*
- **Limit** (Number: Boolean): *See documentation*
- **Limit Num** (Number: Integer): *See documentation*
- **Random Rotate** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Positions** (Array): *See documentation*
- **Scale** (Array): *See documentation*
- **Quaternions** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/cfUzre)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SurfaceScatter_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.SurfaceScatter_v2](https://cables.gl/op/Ops.Gl.SurfaceScatter_v2)

---

### TextMeshMSDF_v2
![TextMeshMSDF_v2 op](images/ops/Ops_Gl_TextMeshMSDF_v2.svg)

**Full Name:** `Ops.Gl.TextMeshMSDF_v2`
**Description:** draw text using the FontMSDF operator

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Text** (String): *See documentation*
- **Scale** (Number): *See documentation*
- **Letter Spacing** (Number): *See documentation*
- **Line Height** (Number): *See documentation*
- **R** (Number): *See documentation*
- **G** (Number): *See documentation*
- **B** (Number): *See documentation*
- **A** (Number): *See documentation*
- **SDF** (Number: Boolean): *See documentation*
- **Smoothing** (Number): *See documentation*
- **Border** (Number: Boolean): *See documentation*
- **Border Width** (Number): *See documentation*
- **Smoothness** (Number): *See documentation*
- **Border R** (Number): *See documentation*
- **Border G** (Number): *See documentation*
- **Border B** (Number): *See documentation*
- **Shadow** (Number: Boolean): *See documentation*
- **Texture Color** (Object:Texture): *See documentation*
- **Texture Mask** (Object:Texture): *See documentation*
- **Positions** (Array): *See documentation*
- **Scalings** (Array): *See documentation*
- **Rotations** (Array): *See documentation*
- **Colors** (Array): *See documentation*
- **Premultiply** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Positions Original** (Array): *See documentation*
- **Scales** (Array): *See documentation*
- **Num Lines** (Number): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Start Y** (Number): *See documentation*
- **Num Chars** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/9COr26)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextMeshMSDF_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.TextMeshMSDF_v2](https://cables.gl/op/Ops.Gl.TextMeshMSDF_v2)

---

### Texture_v2
![Texture_v2 op](images/ops/Ops_Gl_Texture_v2.svg)

**Full Name:** `Ops.Gl.Texture_v2`
**Description:** Load an image as a texture

**> Input Ports:**
- **File** (String): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Flip** (Number: Boolean): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Save Memory** (Number: Boolean): *See documentation*
- **Add Cachebuster** (Number: Boolean): *See documentation*
- **Reload** (Trigger): *See documentation*

**< Output Ports:**
- **Texture** (Object): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Aspect Ratio** (Number): *See documentation*
- **Loaded** (booleanNumber): *See documentation*
- **Loading** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/iRKrD-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Texture_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Texture_v2](https://cables.gl/op/Ops.Gl.Texture_v2)

---

### TextureArray
![TextureArray op](images/ops/Ops_Gl_TextureArray.svg)

**Full Name:** `Ops.Gl.TextureArray`
**Description:** create an array of textures

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

**< Output Ports:**
- **Array** (Array): *See documentation*
- **Count** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/vS5fjz)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureArray"*
**Docs:** [https://cables.gl/op/Ops.Gl.TextureArray](https://cables.gl/op/Ops.Gl.TextureArray)

---

### TextureArrayLoader_v2
![TextureArrayLoader_v2 op](images/ops/Ops_Gl_TextureArrayLoader_v2.svg)

**Full Name:** `Ops.Gl.TextureArrayLoader_v2`
**Description:** load multiple images into an array

**> Input Ports:**
- **Url** (String): *See documentation*
- **Left Pad** (Number: Boolean): *See documentation*
- **Index Start** (Number: Integer): *See documentation*
- **Index End** (Number: Integer): *See documentation*
- **Filter Index** (Number: Integer): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Flip** (Number: Boolean): *See documentation*
- **UnpackPreMultipliedAlpha** (Number: Boolean): *See documentation*

**< Output Ports:**
- **TextureArray** (Array): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Loading** (booleanNumber): *See documentation*
- **Aspect Ratio** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/OeGdjT)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureArrayLoader_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.TextureArrayLoader_v2](https://cables.gl/op/Ops.Gl.TextureArrayLoader_v2)

---

### TextureArrayLoaderFromArray_v3
![TextureArrayLoaderFromArray_v3 op](images/ops/Ops_Gl_TextureArrayLoaderFromArray_v3.svg)

**Full Name:** `Ops.Gl.TextureArrayLoaderFromArray_v3`
**Description:** load multiple texture from filenames given as an array

**> Input Ports:**
- **Urls** (Array): *See documentation*
- **Filter Index** (Number: Integer): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Flip** (Number: Boolean): *See documentation*
- **UnpackPreMultipliedAlpha** (Number: Boolean): *See documentation*
- **Caching** (Number: Boolean): *See documentation*
- **Asset In Patch** (Number: Boolean): *See documentation*

**< Output Ports:**
- **TextureArray** (Array): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Loading** (booleanNumber): *See documentation*
- **Aspect Ratio** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/jFv097)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureArrayLoaderFromArray_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.TextureArrayLoaderFromArray_v3](https://cables.gl/op/Ops.Gl.TextureArrayLoaderFromArray_v3)

---

### TextureColorPick
![TextureColorPick op](images/ops/Ops_Gl_TextureColorPick.svg)

**Full Name:** `Ops.Gl.TextureColorPick`
**Description:** get the color of a pixel in a texture

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **X** (Number: Integer): *See documentation*
- **Y** (Number: Integer): *See documentation*
- **Texture** (Object:Texture): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Red** (Number): *See documentation*
- **Green** (Number): *See documentation*
- **Blue** (Number): *See documentation*
- **Alpha** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/bzVSwn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureColorPick"*
**Docs:** [https://cables.gl/op/Ops.Gl.TextureColorPick](https://cables.gl/op/Ops.Gl.TextureColorPick)

---

### TextureToArray_v4
![TextureToArray_v4 op](images/ops/Ops_Gl_TextureToArray_v4.svg)

**Full Name:** `Ops.Gl.TextureToArray_v4`
**Description:** extract colors from a texture

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Texture** (Object): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Colors** (Array): *See documentation*
- **Floating Point** (booleanNumber): *See documentation*
- **Num Pixel** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/uZkd3x)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureToArray_v4"*
**Docs:** [https://cables.gl/op/Ops.Gl.TextureToArray_v4](https://cables.gl/op/Ops.Gl.TextureToArray_v4)

---

### TextureToPointArray3
![TextureToPointArray3 op](images/ops/Ops_Gl_TextureToPointArray3.svg)

**Full Name:** `Ops.Gl.TextureToPointArray3`
**Description:** generate an array3 of grid positions from a texture

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Center** (Number: Boolean): *See documentation*
- **Threshold Remove** (Number): *See documentation*
- **Z Multiply** (Number): *See documentation*
- **Texture** (Object): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Points** (Array): *See documentation*
- **Total Points** (Number): *See documentation*
- **Min Z** (Number): *See documentation*
- **Max Z** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/U8IO1k)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureToPointArray3"*
**Docs:** [https://cables.gl/op/Ops.Gl.TextureToPointArray3](https://cables.gl/op/Ops.Gl.TextureToPointArray3)

---

### TextureToRandomPoints
![TextureToRandomPoints op](images/ops/Ops_Gl_TextureToRandomPoints.svg)

**Full Name:** `Ops.Gl.TextureToRandomPoints`
**Description:** Create points by sampling texture

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Num Points** (Number: Integer): *See documentation*
- **Seed** (Number): *See documentation*
- **Z Position Index** (Number: Integer): *See documentation*
- **Z Multiply** (Number): *See documentation*
- **Texture** (Object): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Points** (Array): *See documentation*
- **NumPoints** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/LAoKVJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureToRandomPoints"*
**Docs:** [https://cables.gl/op/Ops.Gl.TextureToRandomPoints](https://cables.gl/op/Ops.Gl.TextureToRandomPoints)

---

### TriggerOnCanvasResize
![TriggerOnCanvasResize op](images/ops/Ops_Gl_TriggerOnCanvasResize.svg)

**Full Name:** `Ops.Gl.TriggerOnCanvasResize`
**Description:** will trigger when canvas was resized

**> Input Ports:**
- *Visit [Ops.Gl.TriggerOnCanvasResize documentation](https://cables.gl/op/Ops.Gl.TriggerOnCanvasResize) for input port details*

**< Output Ports:**
- **Resized** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.TriggerOnCanvasResize#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerOnCanvasResize"*
**Docs:** [https://cables.gl/op/Ops.Gl.TriggerOnCanvasResize](https://cables.gl/op/Ops.Gl.TriggerOnCanvasResize)

---

### ValidTexture
![ValidTexture op](images/ops/Ops_Gl_ValidTexture.svg)

**Full Name:** `Ops.Gl.ValidTexture`
**Description:** output current input texture or a default texture

**> Input Ports:**
- **Texture** (Object:Texture): *See documentation*

**< Output Ports:**
- **Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.ValidTexture#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ValidTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.ValidTexture](https://cables.gl/op/Ops.Gl.ValidTexture)

---

### ViewPortSize
![ViewPortSize op](images/ops/Ops_Gl_ViewPortSize.svg)

**Full Name:** `Ops.Gl.ViewPortSize`
**Description:** Outputs current viewport size

**> Input Ports:**
- **Exec** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.ViewPortSize#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ViewPortSize"*
**Docs:** [https://cables.gl/op/Ops.Gl.ViewPortSize](https://cables.gl/op/Ops.Gl.ViewPortSize)

---

