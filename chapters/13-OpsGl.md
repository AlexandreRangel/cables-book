# Ops.Gl

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl

### ArrayToTexture_v2
![ArrayToTexture_v2 op](images/ops/Ops_Gl_ArrayToTexture_v2.svg)

**Full Name:** `Ops.Gl.ArrayToTexture_v2`
**Description:** create a texture from an array of number values

**> Input Ports:**
- **Update** (Trigger)
- **Array** (Array)
- **Width** (Number: Integer)
- **Height** (Number: Integer)
- **Fill Up** (Number: Boolean)
- **Flip** (Number: Boolean)
- **Pixel Format Index** (Number: Integer)
- **Wrap Index** (Number: Integer)

**< Output Ports:**
- **Next** (Trigger)
- **Texture Out** (Object)
- **Tex Width** (Number)
- **Tex Height** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/cOlh_C)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayToTexture_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ArrayToTexture_v2](https://cables.gl/op/Ops.Gl.ArrayToTexture_v2)

---

### BlendMode
![BlendMode op](images/ops/Ops_Gl_BlendMode.svg)

**Full Name:** `Ops.Gl.BlendMode`
**Description:** change how colors are mixed (blending/mixing modes)

**> Input Ports:**
- **Render** (Trigger)
- **Blendmode Index** (Number: Integer)
- **Premultiplied** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/x1-Fvc)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BlendMode"*
**Docs:** [https://cables.gl/op/Ops.Gl.BlendMode](https://cables.gl/op/Ops.Gl.BlendMode)

---

### CanvasFocus
![CanvasFocus op](images/ops/Ops_Gl_CanvasFocus.svg)

**Full Name:** `Ops.Gl.CanvasFocus`
**Description:** is canvas focussed ?

**> Input Ports:**
- **Focus** (Trigger)

**< Output Ports:**
- **Has Focus** (booleanNumber)

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
- **CSS Width** (Number)
- **CSS Height** (Number)
- **Pixel Ratio** (Number)
- **Pixel Width** (Number)
- **Pixel Height** (Number)
- **Aspect Ratio** (Number)
- **Landscape** (booleanNumber)
- **Canvas** (Object)
- **Canvas Parent** (Object)
- **Resized** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/2yaD8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CanvasInfo_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.CanvasInfo_v3](https://cables.gl/op/Ops.Gl.CanvasInfo_v3)

---

### CanvasToTexture
![CanvasToTexture op](images/ops/Ops_Gl_CanvasToTexture.svg)

**Full Name:** `Ops.Gl.CanvasToTexture`
**Description:** convert a canvas to texture

**> Input Ports:**
- **Canvas** (Object)
- **Filter Index** (Number: Integer)
- **Wrap Index** (Number: Integer)
- **Force Update** (Trigger)

**< Output Ports:**
- **Texture** (Object)
- **Width** (Number)
- **Height** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/QjlEo-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CanvasToTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.CanvasToTexture](https://cables.gl/op/Ops.Gl.CanvasToTexture)

---

### ClearColor
![ClearColor op](images/ops/Ops_Gl_ClearColor.svg)

**Full Name:** `Ops.Gl.ClearColor`
**Description:** sets all cleared pixels to one colour. Use to change the background colour.

**> Input Ports:**
- **Render** (Trigger)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/_UEjvr)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ClearColor"*
**Docs:** [https://cables.gl/op/Ops.Gl.ClearColor](https://cables.gl/op/Ops.Gl.ClearColor)

---

### ClearDepth
![ClearDepth op](images/ops/Ops_Gl_ClearDepth.svg)

**Full Name:** `Ops.Gl.ClearDepth`
**Description:** Clears the depth buffer (zbuffer, z buffer)

**> Input Ports:**
- **Render** (Trigger)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/rEesag)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ClearDepth"*
**Docs:** [https://cables.gl/op/Ops.Gl.ClearDepth](https://cables.gl/op/Ops.Gl.ClearDepth)

---

### ColorMask
![ColorMask op](images/ops/Ops_Gl_ColorMask.svg)

**Full Name:** `Ops.Gl.ColorMask`
**Description:** enable/disable RGBA color channels of your entire scene

**> Input Ports:**
- **Execute** (Trigger)
- **Red** (Number: Boolean)
- **Green** (Number: Boolean)
- **Blue** (Number: Boolean)
- **Alpha** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/MqQSR7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorMask"*
**Docs:** [https://cables.gl/op/Ops.Gl.ColorMask](https://cables.gl/op/Ops.Gl.ColorMask)

---

### ColorPick
![ColorPick op](images/ops/Ops_Gl_ColorPick.svg)

**Full Name:** `Ops.Gl.ColorPick`
**Description:** pick a color at x,y coordinates of canvas

**> Input Ports:**
- **Render** (Trigger)
- **X** (Number)
- **Y** (Number)

**< Output Ports:**
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/YEjkgg)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorPick"*
**Docs:** [https://cables.gl/op/Ops.Gl.ColorPick](https://cables.gl/op/Ops.Gl.ColorPick)

---

### DirectionalTranslate
![DirectionalTranslate op](images/ops/Ops_Gl_DirectionalTranslate.svg)

**Full Name:** `Ops.Gl.DirectionalTranslate`
**Description:** translate away from a point in space

**> Input Ports:**
- **Exec** (Trigger)
- **Center Model Matrix** (Array)
- **Amount** (Number)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/5gL9On)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DirectionalTranslate"*
**Docs:** [https://cables.gl/op/Ops.Gl.DirectionalTranslate](https://cables.gl/op/Ops.Gl.DirectionalTranslate)

---

### DownloadTexture_v3
![DownloadTexture_v3 op](images/ops/Ops_Gl_DownloadTexture_v3.svg)

**Full Name:** `Ops.Gl.DownloadTexture_v3`
**Description:** Download a texture as an image file

**> Input Ports:**
- **Texture** (Object:Texture)
- **Quality** (Number)
- **Filename** (String)
- **Download** (Trigger)

**< Output Ports:**
- **Jcrmz8mnz** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/15LaTs)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DownloadTexture_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.DownloadTexture_v3](https://cables.gl/op/Ops.Gl.DownloadTexture_v3)

---

### DrawTextureMapping
![DrawTextureMapping op](images/ops/Ops_Gl_DrawTextureMapping.svg)

**Full Name:** `Ops.Gl.DrawTextureMapping`
**Description:** draw texture mapping coordinates

**> Input Ports:**
- **Render** (Trigger)
- **Geometry** (Object:Geometry)
- **Num Points** (Number)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Nu7dJ5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DrawTextureMapping"*
**Docs:** [https://cables.gl/op/Ops.Gl.DrawTextureMapping](https://cables.gl/op/Ops.Gl.DrawTextureMapping)

---

### ElementInBrowserViewport
![ElementInBrowserViewport op](images/ops/Ops_Gl_ElementInBrowserViewport.svg)

**Full Name:** `Ops.Gl.ElementInBrowserViewport`
**Description:** check if webgl canvas element is in the current browser viewport

**> Input Ports:**
- **Update** (Trigger)
- **Element** (Object:Element)

**< Output Ports:**
- **Next** (Trigger)
- **Fully Visible** (booleanNumber)
- **Partly Visible** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.ElementInBrowserViewport#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementInBrowserViewport"*
**Docs:** [https://cables.gl/op/Ops.Gl.ElementInBrowserViewport](https://cables.gl/op/Ops.Gl.ElementInBrowserViewport)

---

### ExternalCanvas
![ExternalCanvas op](images/ops/Ops_Gl_ExternalCanvas.svg)

**Full Name:** `Ops.Gl.ExternalCanvas`
**Description:** Open a new window that shows a copy of the patch canvas

**> Input Ports:**
- **Update** (Trigger)
- **Pos X** (Number: Integer)
- **Pos Y** (Number: Integer)
- **Width** (Number: Integer)
- **Height** (Number: Integer)
- **Smoothing** (Number: Boolean)
- **Stretch** (Number: Boolean)
- **Title** (String)
- **Open Window** (Trigger)
- **Fullscreen** (Trigger)
- **Close** (Trigger)

**< Output Ports:**
- **Next** (Trigger)
- **Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/HnG3fB)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ExternalCanvas"*
**Docs:** [https://cables.gl/op/Ops.Gl.ExternalCanvas](https://cables.gl/op/Ops.Gl.ExternalCanvas)

---

### FaceCulling_v2
![FaceCulling_v2 op](images/ops/Ops_Gl_FaceCulling_v2.svg)

**Full Name:** `Ops.Gl.FaceCulling_v2`
**Description:** Disable the rendering of front or back facing triangles with culling

**> Input Ports:**
- **Render** (Trigger)
- **Active** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/mPwnD-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FaceCulling_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.FaceCulling_v2](https://cables.gl/op/Ops.Gl.FaceCulling_v2)

---

### FontMSDF_v2
![FontMSDF_v2 op](images/ops/Ops_Gl_FontMSDF_v2.svg)

**Full Name:** `Ops.Gl.FontMSDF_v2`
**Description:** Load MSDF Font data and texture to use

**> Input Ports:**
- **Font Name** (String)
- **Font Data** (String)
- **Font Image** (String)
- **Font Image 1** (String)
- **Font Image 2** (String)
- **Font Image 3** (String)

**< Output Ports:**
- **Loaded** (booleanNumber)
- **Total Chars** (Number)
- **Chars** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/9COr26)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FontMSDF_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.FontMSDF_v2](https://cables.gl/op/Ops.Gl.FontMSDF_v2)

---

### ForceCanvasSize
![ForceCanvasSize op](images/ops/Ops_Gl_ForceCanvasSize.svg)

**Full Name:** `Ops.Gl.ForceCanvasSize`
**Description:** Resize canvas element to a specific pixel size or aspect ratio

**> Input Ports:**
- **Trigger** (Trigger)
- **Active** (Number: Boolean)
- **Center In Parent** (Number: Boolean)
- **Scale To Fit Parent** (Number: Boolean)
- **Set Width** (Number: Integer)
- **Set Height** (Number: Integer)
- **Aspect Ratio Index** (Number: Integer)
- **Ratio** (Number)
- **Fill Parent Index** (Number: Integer)

**< Output Ports:**
- **Next** (Trigger)
- **Width** (Number)
- **Height** (Number)
- **Margin Left** (Number)
- **Margin Top** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/f9UbD-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ForceCanvasSize"*
**Docs:** [https://cables.gl/op/Ops.Gl.ForceCanvasSize](https://cables.gl/op/Ops.Gl.ForceCanvasSize)

---

### GateTexture
![GateTexture op](images/ops/Ops_Gl_GateTexture.svg)

**Full Name:** `Ops.Gl.GateTexture`
**Description:** Will only allow an Object to to be output if the the pass through parameter evaluates to true

**> Input Ports:**
- **Object In** (Object:Texture)
- **Pass Through** (Number: Boolean)
- **Only Valid Textures** (Number: Boolean)

**< Output Ports:**
- **Object Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.GateTexture#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GateTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.GateTexture](https://cables.gl/op/Ops.Gl.GateTexture)

---

### GlBlendFunc
![GlBlendFunc op](images/ops/Ops_Gl_GlBlendFunc.svg)

**Full Name:** `Ops.Gl.GlBlendFunc`
**Description:** set gl blendmodes directly

**> Input Ports:**
- **Exec** (Trigger)
- **Src RGB Index** (Number: Integer)
- **Dst RGB Index** (Number: Integer)
- **Src Alpha Index** (Number: Integer)
- **Dst Alpha Index** (Number: Integer)
- **Blend Equation Index** (Number: Integer)

**< Output Ports:**
- **Next** (Trigger)

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
- **WebGl Version Short** (Number)
- **WebGl Version** (String)
- **GLSL Version** (String)
- **Max Frag Uniforms** (Number)
- **Max Vert Uniforms** (Number)
- **Max Texture Size** (Number)
- **Max Texture Units** (Number)
- **Max Varying Vectors** (Number)
- **Max MSAA Samples** (Number)
- **Extensions** (Array)
- **Vendor** (String)
- **Renderer** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/0zHu8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GlInfo_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.GlInfo_v2](https://cables.gl/op/Ops.Gl.GlInfo_v2)

---

### GlPrimitive
![GlPrimitive op](images/ops/Ops_Gl_GlPrimitive.svg)

**Full Name:** `Ops.Gl.GlPrimitive`
**Description:** force rendering of meshes using points,lines or triangles

**> Input Ports:**
- **Execute** (Trigger)
- **Primitive Index** (Number: Integer)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/a5Mz8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GlPrimitive"*
**Docs:** [https://cables.gl/op/Ops.Gl.GlPrimitive](https://cables.gl/op/Ops.Gl.GlPrimitive)

---

### GradientTexture
![GradientTexture op](images/ops/Ops_Gl_GradientTexture.svg)

**Full Name:** `Ops.Gl.GradientTexture`
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
- **Wrap Index** (Number: Integer)
- **Dither** (Number)
- **Gradient Array** (Array)
- **Randomize Colors** (Trigger)

**< Output Ports:**
- **Texture** (Object)
- **Alpha Mask** (Object)
- **Colors** (Array)
- **Colors Pos** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/_wQNDW)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GradientTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.GradientTexture](https://cables.gl/op/Ops.Gl.GradientTexture)

---

### GridTransform
![GridTransform op](images/ops/Ops_Gl_GridTransform.svg)

**Full Name:** `Ops.Gl.GridTransform`
**Description:** transform and arrange elements into a grid

**> Input Ports:**
- **Render** (Trigger)
- **Num X** (Number: Integer)
- **Num Y** (Number: Integer)
- **Space X** (Number)
- **Space Y** (Number)

**< Output Ports:**
- **Next** (Trigger)
- **Index** (Number)
- **X Index** (Number)
- **Y Index** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/J-XMNQ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GridTransform"*
**Docs:** [https://cables.gl/op/Ops.Gl.GridTransform](https://cables.gl/op/Ops.Gl.GridTransform)

---

### Identity
![Identity op](images/ops/Ops_Gl_Identity.svg)

**Full Name:** `Ops.Gl.Identity`
**Description:** reset all transforms (modelmatrix)

**> Input Ports:**
- **Exe** (Trigger)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/KUVJ8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Identity"*
**Docs:** [https://cables.gl/op/Ops.Gl.Identity](https://cables.gl/op/Ops.Gl.Identity)

---

### IdentityViewMatrix
![IdentityViewMatrix op](images/ops/Ops_Gl_IdentityViewMatrix.svg)

**Full Name:** `Ops.Gl.IdentityViewMatrix`
**Description:** reset the view matrix (cameras etc.)

**> Input Ports:**
- **Exe** (Trigger)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/H01Ici)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "IdentityViewMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.IdentityViewMatrix](https://cables.gl/op/Ops.Gl.IdentityViewMatrix)

---

### ImageSequenceAnim_v2
![ImageSequenceAnim_v2 op](images/ops/Ops_Gl_ImageSequenceAnim_v2.svg)

**Full Name:** `Ops.Gl.ImageSequenceAnim_v2`
**Description:** play a image sprite animation

**> Input Ports:**
- **Time** (Number)
- **FPS** (Number)
- **Num X** (Number)
- **Num Y** (Number)
- **Max Frames** (Number: Integer)
- **Flip Y** (Number: Boolean)

**< Output Ports:**
- **Repeat X** (Number)
- **Repeat Y** (Number)
- **Offset X** (Number)
- **Offset Y** (Number)
- **Frame** (Number)
- **Progress** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/n0iMSq)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ImageSequenceAnim_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ImageSequenceAnim_v2](https://cables.gl/op/Ops.Gl.ImageSequenceAnim_v2)

---

### InteractiveRectangle_v2
![InteractiveRectangle_v2 op](images/ops/Ops_Gl_InteractiveRectangle_v2.svg)

**Full Name:** `Ops.Gl.InteractiveRectangle_v2`
**Description:** An area which is interactive

**> Input Ports:**
- **Trigger In** (Trigger)
- **Width** (Number)
- **Height** (Number)
- **ID** (String)
- **Class** (String)
- **Pivot X Index** (Number: Integer)
- **Pivot Y Index** (Number: Integer)
- **Axis Index** (Number: Integer)
- **Is Interactive** (Number: Boolean)
- **Render Rectangle** (Number: Boolean)
- **Show Boundings** (Number: Boolean)
- **Cursor Index** (Number: Integer)
- **Active** (Number: Boolean)

**< Output Ports:**
- **Trigger Out** (Trigger)
- **Geometry** (Object)
- **Pointer Hover** (booleanNumber)
- **Pointer Down** (booleanNumber)
- **Pointer X** (Number)
- **Pointer Y** (Number)
- **Top** (Number)
- **Left** (Number)
- **Right** (Number)
- **Bottom** (Number)
- **Left Click** (Trigger)
- **Dom Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/P_SED0)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InteractiveRectangle_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.InteractiveRectangle_v2](https://cables.gl/op/Ops.Gl.InteractiveRectangle_v2)

---

### LayerSequence
![LayerSequence op](images/ops/Ops_Gl_LayerSequence.svg)

**Full Name:** `Ops.Gl.LayerSequence`
**Description:** Render Multiple Layers in a specific order

**> Input Ports:**
- **Exe** (Trigger)

**< Output Ports:**
- **Trigger 0** (Trigger)
- **Trigger 1** (Trigger)
- **Trigger 2** (Trigger)
- **Trigger 3** (Trigger)
- **Trigger 4** (Trigger)
- **Trigger 5** (Trigger)
- **Trigger 6** (Trigger)
- **Trigger 7** (Trigger)
- **Trigger 8** (Trigger)
- **Trigger 9** (Trigger)
- **Trigger 10** (Trigger)
- **Trigger 11** (Trigger)
- **Trigger 12** (Trigger)
- **Trigger 13** (Trigger)
- **Trigger 14** (Trigger)
- **Trigger 15** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/VH4Oxj)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LayerSequence"*
**Docs:** [https://cables.gl/op/Ops.Gl.LayerSequence](https://cables.gl/op/Ops.Gl.LayerSequence)

---

### LineFont_v2
![LineFont_v2 op](images/ops/Ops_Gl_LineFont_v2.svg)

**Full Name:** `Ops.Gl.LineFont_v2`
**Description:** A Simple way to write text on the screen.

**> Input Ports:**
- **Render** (Trigger)
- **Text** (String)
- **Letter Spacing** (Number)

**< Output Ports:**
- **Lines** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/1JzPLu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LineFont_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.LineFont_v2](https://cables.gl/op/Ops.Gl.LineFont_v2)

---

### MainLoop_v2
![MainLoop_v2 op](images/ops/Ops_Gl_MainLoop_v2.svg)

**Full Name:** `Ops.Gl.MainLoop_v2`
**Description:** Trigger other ops once every frame to create smooth animations

**> Input Ports:**
- **FPS Limit** (Number)
- **Reduce FPS Unfocussed** (Number: Boolean)
- **Transparent** (Number: Boolean)
- **Active** (Number: Boolean)
- **Focus Canvas** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)
- **Width** (Number)
- **Height** (Number)
- **Pixel Density** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/uZxfQc)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MainLoop_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.MainLoop_v2](https://cables.gl/op/Ops.Gl.MainLoop_v2)

---

### MediaRecorder_v2
![MediaRecorder_v2 op](images/ops/Ops_Gl_MediaRecorder_v2.svg)

**Full Name:** `Ops.Gl.MediaRecorder_v2`
**Description:** Record the renderer-output to video

**> Input Ports:**
- **Recording** (Number: Boolean)
- **Filename** (String)
- **Download Video** (Number: Boolean)
- **Mimetype Index** (Number: Integer)
- **MBit** (Number)
- **Max FPS** (Number)
- **Force FPS** (Number)
- **Audio In** (Object:AudioNode)
- **Video Canvas Id** (String)

**< Output Ports:**
- **State** (String)
- **Error** (String)
- **Final Mimetype** (String)
- **Valid Mimetypes** (Array)
- **Duration** (Number)
- **Finished Recording** (Trigger)
- **Video DataUrl** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/ioiDIR)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MediaRecorder_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.MediaRecorder_v2](https://cables.gl/op/Ops.Gl.MediaRecorder_v2)

---

### MeshInstancer_v4
![MeshInstancer_v4 op](images/ops/Ops_Gl_MeshInstancer_v4.svg)

**Full Name:** `Ops.Gl.MeshInstancer_v4`
**Description:** Draw the same mesh multiple times on the GPU

**> Input Ports:**
- **Exe** (Trigger)
- **Geom** (Object:Geometry)
- **Scale** (Number)
- **Limit Instances** (Number: Boolean)
- **Limit** (Number: Integer)
- **Positions** (Array)
- **Scale Array** (Array)
- **Rotations** (Array)
- **Colors** (Array)
- **TexCoords** (Array)

**< Output Ports:**
- **Trigger Out** (Trigger)
- **Num** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/oOsjJ5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MeshInstancer_v4"*
**Docs:** [https://cables.gl/op/Ops.Gl.MeshInstancer_v4](https://cables.gl/op/Ops.Gl.MeshInstancer_v4)

---

### MeshMorph
![MeshMorph op](images/ops/Ops_Gl_MeshMorph.svg)

**Full Name:** `Ops.Gl.MeshMorph`
**Description:** morph from one geometry to another

**> Input Ports:**
- **Render** (Trigger)
- **Geometry** (Number: Integer)
- **Duration** (Number)
- **Index** (Number)
- **Index 2** (Number)
- **Fade** (Number)
- **Easing Index** (Number: Integer)
- **Geometry 0** (Object)
- **Geometry 1** (Object)
- **Geometry 2** (Object)
- **Geometry 3** (Object)
- **Geometry 4** (Object)
- **Geometry 5** (Object)
- **Geometry 6** (Object)
- **Geometry 7** (Object)
- **Geometry 8** (Object)
- **Geometry 9** (Object)
- **Geometry 10** (Object)
- **Geometry 11** (Object)
- **Geometry 12** (Object)
- **Geometry 13** (Object)
- **Geometry 14** (Object)
- **Geometry 15** (Object)

**< Output Ports:**
- **Finished** (booleanNumber)
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/PdhglN)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MeshMorph"*
**Docs:** [https://cables.gl/op/Ops.Gl.MeshMorph](https://cables.gl/op/Ops.Gl.MeshMorph)

---

### NormalizeScreenCoordinates
![NormalizeScreenCoordinates op](images/ops/Ops_Gl_NormalizeScreenCoordinates.svg)

**Full Name:** `Ops.Gl.NormalizeScreenCoordinates`
**Description:** convert screen pixel coordinates to range 0-1

**> Input Ports:**
- **X** (Number)
- **Y** (Number)

**< Output Ports:**
- **Result X** (Number)
- **Result Y** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.NormalizeScreenCoordinates#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "NormalizeScreenCoordinates"*
**Docs:** [https://cables.gl/op/Ops.Gl.NormalizeScreenCoordinates](https://cables.gl/op/Ops.Gl.NormalizeScreenCoordinates)

---

### OrTexture
![OrTexture op](images/ops/Ops_Gl_OrTexture.svg)

**Full Name:** `Ops.Gl.OrTexture`
**Description:** outputs the first valid texture of the

**> Input Ports:**
- **Texture 1** (Object:Texture)
- **Texture 2** (Object:Texture)
- **Texture 3** (Object:Texture)
- **Texture 4** (Object:Texture)
- **Texture 5** (Object:Texture)
- **Texture 6** (Object:Texture)
- **Texture 7** (Object:Texture)
- **Texture 8** (Object:Texture)

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/oKRY7i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "OrTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.OrTexture](https://cables.gl/op/Ops.Gl.OrTexture)

---

### Orthogonal_v2
![Orthogonal_v2 op](images/ops/Ops_Gl_Orthogonal_v2.svg)

**Full Name:** `Ops.Gl.Orthogonal_v2`
**Description:** Orthogonal projection / objects in distance don't appear smaller (isometric)

**> Input Ports:**
- **Render** (Trigger)
- **Bounds** (Number)
- **Axis Index** (Number: Integer)
- **Frustum Near** (Number)
- **Frustum Far** (Number)

**< Output Ports:**
- **Trigger** (Trigger)
- **Ratio** (Number)
- **Width** (Number)
- **Height** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/94Aycg)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Orthogonal_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Orthogonal_v2](https://cables.gl/op/Ops.Gl.Orthogonal_v2)

---

### OverwriteViewportSize
![OverwriteViewportSize op](images/ops/Ops_Gl_OverwriteViewportSize.svg)

**Full Name:** `Ops.Gl.OverwriteViewportSize`
**Description:** Force a manually set viewport size for connected ops

**> Input Ports:**
- **Exec** (Trigger)
- **Width** (Number: Integer)
- **Height** (Number: Integer)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.OverwriteViewportSize#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "OverwriteViewportSize"*
**Docs:** [https://cables.gl/op/Ops.Gl.OverwriteViewportSize](https://cables.gl/op/Ops.Gl.OverwriteViewportSize)

---

### Performance
![Performance op](images/ops/Ops_Gl_Performance.svg)

**Full Name:** `Ops.Gl.Performance`
**Description:** Show WebGl Performance Statistics

**> Input Ports:**
- **Exe** (Trigger)
- **Active** (Number: Boolean)
- **Visible** (Number: Boolean)
- **Measure GPU** (Number: Boolean)
- **Open** (Number: Boolean)
- **Smooth Graph** (Number: Boolean)
- **Scale** (Number)
- **Size** (Number)

**< Output Ports:**
- **Childs** (Trigger)
- **Canvas** (Object)
- **FPS** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/zFR8z5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Performance"*
**Docs:** [https://cables.gl/op/Ops.Gl.Performance](https://cables.gl/op/Ops.Gl.Performance)

---

### PerformanceMeasure
![PerformanceMeasure op](images/ops/Ops_Gl_PerformanceMeasure.svg)

**Full Name:** `Ops.Gl.PerformanceMeasure`
**Description:** Measure the time used to execute all child ops

**> Input Ports:**
- **Execute** (Trigger)
- **Name** (String)

**< Output Ports:**
- **Childs** (Trigger)
- **Time Used** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.PerformanceMeasure#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PerformanceMeasure"*
**Docs:** [https://cables.gl/op/Ops.Gl.PerformanceMeasure](https://cables.gl/op/Ops.Gl.PerformanceMeasure)

---

### Perspective
![Perspective op](images/ops/Ops_Gl_Perspective.svg)

**Full Name:** `Ops.Gl.Perspective`
**Description:** Adjust FOV, field of view, and frustum clipping

**> Input Ports:**
- **Render** (Trigger)
- **FOV Degrees** (Number)
- **Frustum Near** (Number)
- **Frustum Far** (Number)
- **Auto Aspect Ratio** (Number: Boolean)
- **Aspect Ratio** (Number)

**< Output Ports:**
- **Trigger** (Trigger)
- **Aspect** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/RJXV7i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Perspective"*
**Docs:** [https://cables.gl/op/Ops.Gl.Perspective](https://cables.gl/op/Ops.Gl.Perspective)

---

### PixelProjection_v3
![PixelProjection_v3 op](images/ops/Ops_Gl_PixelProjection_v3.svg)

**Full Name:** `Ops.Gl.PixelProjection_v3`
**Description:** Remaps world co-ordinates to a pixel co-ordinate system

**> Input Ports:**
- **Render** (Trigger)
- **Width** (Number)
- **Height** (Number)
- **Frustum Near** (Number)
- **Frustum Far** (Number)
- **Flip X** (Number: Boolean)
- **Flip Y** (Number: Boolean)
- **Zero Y** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)
- **Size Width** (Number)
- **Size Height** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/fsOPNS)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PixelProjection_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.PixelProjection_v3](https://cables.gl/op/Ops.Gl.PixelProjection_v3)

---

### PointCollector
![PointCollector op](images/ops/Ops_Gl_PointCollector.svg)

**Full Name:** `Ops.Gl.PointCollector`
**Description:** save points/coordinates in an array

**> Input Ports:**
- **Render** (Trigger)
- **Absolute** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)
- **Points** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.PointCollector#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointCollector"*
**Docs:** [https://cables.gl/op/Ops.Gl.PointCollector](https://cables.gl/op/Ops.Gl.PointCollector)

---

### PointCollectorCollect
![PointCollectorCollect op](images/ops/Ops_Gl_PointCollectorCollect.svg)

**Full Name:** `Ops.Gl.PointCollectorCollect`
**Description:** collect world space coordinates into an array

**> Input Ports:**
- **Render** (Trigger)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.PointCollectorCollect#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointCollectorCollect"*
**Docs:** [https://cables.gl/op/Ops.Gl.PointCollectorCollect](https://cables.gl/op/Ops.Gl.PointCollectorCollect)

---

### PointCollectorScreenCoords
![PointCollectorScreenCoords op](images/ops/Ops_Gl_PointCollectorScreenCoords.svg)

**Full Name:** `Ops.Gl.PointCollectorScreenCoords`
**Description:** collect screen pixel coordinates into an array

**> Input Ports:**
- **Render** (Trigger)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.PointCollectorScreenCoords#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointCollectorScreenCoords"*
**Docs:** [https://cables.gl/op/Ops.Gl.PointCollectorScreenCoords](https://cables.gl/op/Ops.Gl.PointCollectorScreenCoords)

---

### RandomCluster
![RandomCluster op](images/ops/Ops_Gl_RandomCluster.svg)

**Full Name:** `Ops.Gl.RandomCluster`
**Description:** Transforms objects randomly in space

**> Input Ports:**
- **Exe** (Trigger)
- **Num** (Number: Integer)
- **Random Seed** (Number)
- **Round** (Number: Boolean)
- **Size** (Number)
- **ScaleX** (Number)
- **ScaleY** (Number)
- **ScaleZ** (Number)
- **Rotate X** (Number)
- **Rotate Y** (Number)
- **Rotate Z** (Number)
- **Scroll X** (Number)

**< Output Ports:**
- **Trigger** (Trigger)
- **Index** (Number)
- **Rnd** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Ah6Rj6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RandomCluster"*
**Docs:** [https://cables.gl/op/Ops.Gl.RandomCluster](https://cables.gl/op/Ops.Gl.RandomCluster)

---

### RenderAnim_v2
![RenderAnim_v2 op](images/ops/Ops_Gl_RenderAnim_v2.svg)

**Full Name:** `Ops.Gl.RenderAnim_v2`
**Description:** record, render an animation and save as webm video file or png image sequence

**> Input Ports:**
- **Render** (Trigger)
- **File Type Index** (Number: Integer)
- **ZIP Multiple Files** (Number: Boolean)
- **Download Files** (Number: Boolean)
- **Filename** (String)
- **Quality** (Number)
- **Duration** (Number: Integer)
- **FPS** (Number: Integer)
- **Transparency** (Number: Boolean)
- **Use Canvas Size** (Number: Boolean)
- **Texture Width** (Number: Integer)
- **Texture Height** (Number: Integer)
- **Start** (Trigger)

**< Output Ports:**
- **Next** (Trigger)
- **Progress** (Number)
- **Frame** (Number)
- **Status** (String)
- **Started** (booleanNumber)
- **Data URL** (String)
- **Finished** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/bQhm8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RenderAnim_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.RenderAnim_v2](https://cables.gl/op/Ops.Gl.RenderAnim_v2)

---

### RenderGeometry_v2
![RenderGeometry_v2 op](images/ops/Ops_Gl_RenderGeometry_v2.svg)

**Full Name:** `Ops.Gl.RenderGeometry_v2`
**Description:** Render a geometry as mesh

**> Input Ports:**
- **Render** (Trigger)
- **Geometry** (Object:Geometry)
- **Add Vertex Numbers** (Number: Boolean)
- **Render Mesh** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/w6QYlH)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RenderGeometry_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.RenderGeometry_v2](https://cables.gl/op/Ops.Gl.RenderGeometry_v2)

---

### RenderToTexture_v3
![RenderToTexture_v3 op](images/ops/Ops_Gl_RenderToTexture_v3.svg)

**Full Name:** `Ops.Gl.RenderToTexture_v3`
**Description:** Render into an Image

**> Input Ports:**
- **Render** (Trigger)
- **Texture Width** (Number: Integer)
- **Texture Height** (Number: Integer)
- **Auto Aspect** (Number: Boolean)
- **Pixel Format Index** (Number: Integer)
- **Depth** (Number: Boolean)
- **Clear** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)
- **Texture** (Object)
- **TextureDepth** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/G2_my7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RenderToTexture_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.RenderToTexture_v3](https://cables.gl/op/Ops.Gl.RenderToTexture_v3)

---

### RenderToTextures_v3
![RenderToTextures_v3 op](images/ops/Ops_Gl_RenderToTextures_v3.svg)

**Full Name:** `Ops.Gl.RenderToTextures_v3`
**Description:** render to multiple textures at the same time

**> Input Ports:**
- **Render** (Trigger)
- **Texture Width** (Number: Integer)
- **Texture Height** (Number: Integer)
- **Auto Aspect** (Number: Boolean)
- **Pixel Format Index** (Number: Integer)
- **Wrap Index** (Number: Integer)
- **Clear** (Number: Boolean)
- **Texture 0 Index** (Number: Integer)
- **Texture 1 Index** (Number: Integer)
- **Texture 2 Index** (Number: Integer)
- **Texture 3 Index** (Number: Integer)
- **Texture 4 Index** (Number: Integer)
- **Texture 5 Index** (Number: Integer)
- **Texture 6 Index** (Number: Integer)
- **Texture 7 Index** (Number: Integer)

**< Output Ports:**
- **Next** (Trigger)
- **Result Texture 0** (Object)
- **Result Texture 1** (Object)
- **Result Texture 2** (Object)
- **Result Texture 3** (Object)
- **Result Texture 4** (Object)
- **Result Texture 5** (Object)
- **Result Texture 6** (Object)
- **Result Texture 7** (Object)
- **TextureDepth** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/muH2jG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RenderToTextures_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.RenderToTextures_v3](https://cables.gl/op/Ops.Gl.RenderToTextures_v3)

---

### ResetTransform
![ResetTransform op](images/ops/Ops_Gl_ResetTransform.svg)

**Full Name:** `Ops.Gl.ResetTransform`
**Description:** reset current transforms to initial value (identity)

**> Input Ports:**
- **Exe** (Trigger)
- **Reset Model Transform** (Number: Boolean)
- **Reset View Transform** (Number: Boolean)
- **Default View** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/kY3J8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ResetTransform"*
**Docs:** [https://cables.gl/op/Ops.Gl.ResetTransform](https://cables.gl/op/Ops.Gl.ResetTransform)

---

### SaveScreenShot_v3
![SaveScreenShot_v3 op](images/ops/Ops_Gl_SaveScreenShot_v3.svg)

**Full Name:** `Ops.Gl.SaveScreenShot_v3`
**Description:** Download the current screen content as png file

**> Input Ports:**
- **Filename** (String)
- **Use Canvas Size** (Number: Boolean)
- **Screenshot** (Trigger)
- **Width** (Number: Integer)
- **Height** (Number: Integer)

**< Output Ports:**
- **Finished** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/OB0Qmi)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SaveScreenShot_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.SaveScreenShot_v3](https://cables.gl/op/Ops.Gl.SaveScreenShot_v3)

---

### ShowNormals_v2
![ShowNormals_v2 op](images/ops/Ops_Gl_ShowNormals_v2.svg)

**Full Name:** `Ops.Gl.ShowNormals_v2`
**Description:** visualize normals, tangents or bitangents

**> Input Ports:**
- **Render** (Trigger)
- **Draw** (Number: Boolean)
- **Geometry** (Object:Geometry)
- **Length** (Number)
- **Colorize** (Number: Boolean)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)

**< Output Ports:**
- **Trigger** (Trigger)
- **Line Geom** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/4NeG02)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ShowNormals_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.ShowNormals_v2](https://cables.gl/op/Ops.Gl.ShowNormals_v2)

---

### SurfaceScatter_v2
![SurfaceScatter_v2 op](images/ops/Ops_Gl_SurfaceScatter_v2.svg)

**Full Name:** `Ops.Gl.SurfaceScatter_v2`
**Description:** Scatter an object on the surface of a mesh with different distribution methods

**> Input Ports:**
- **Render** (Trigger)
- **Draw** (Number: Boolean)
- **Num** (Number: Integer)
- **Geom Surface** (Object)
- **Distribution Index** (Number: Integer)
- **Selection Index** (Number: Integer)
- **Random Seed** (Number)
- **Size Min** (Number)
- **Size Max** (Number)
- **Limit** (Number: Boolean)
- **Limit Num** (Number: Integer)
- **Random Rotate** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)
- **Positions** (Array)
- **Scale** (Array)
- **Quaternions** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/cfUzre)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SurfaceScatter_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.SurfaceScatter_v2](https://cables.gl/op/Ops.Gl.SurfaceScatter_v2)

---

### TextMeshMSDF_v2
![TextMeshMSDF_v2 op](images/ops/Ops_Gl_TextMeshMSDF_v2.svg)

**Full Name:** `Ops.Gl.TextMeshMSDF_v2`
**Description:** draw text using the FontMSDF operator

**> Input Ports:**
- **Render** (Trigger)
- **Text** (String)
- **Scale** (Number)
- **Letter Spacing** (Number)
- **Line Height** (Number)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)
- **SDF** (Number: Boolean)
- **Smoothing** (Number)
- **Border** (Number: Boolean)
- **Border Width** (Number)
- **Smoothness** (Number)
- **Border R** (Number)
- **Border G** (Number)
- **Border B** (Number)
- **Shadow** (Number: Boolean)
- **Texture Color** (Object:Texture)
- **Texture Mask** (Object:Texture)
- **Positions** (Array)
- **Scalings** (Array)
- **Rotations** (Array)
- **Colors** (Array)
- **Premultiply** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)
- **Positions Original** (Array)
- **Scales** (Array)
- **Num Lines** (Number)
- **Width** (Number)
- **Height** (Number)
- **Start Y** (Number)
- **Num Chars** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/9COr26)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextMeshMSDF_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.TextMeshMSDF_v2](https://cables.gl/op/Ops.Gl.TextMeshMSDF_v2)

---

### Texture_v2
![Texture_v2 op](images/ops/Ops_Gl_Texture_v2.svg)

**Full Name:** `Ops.Gl.Texture_v2`
**Description:** Load an image as a texture

**> Input Ports:**
- **File** (String)
- **Wrap Index** (Number: Integer)
- **Flip** (Number: Boolean)
- **Active** (Number: Boolean)
- **Save Memory** (Number: Boolean)
- **Add Cachebuster** (Number: Boolean)
- **Reload** (Trigger)

**< Output Ports:**
- **Texture** (Object)
- **Width** (Number)
- **Height** (Number)
- **Aspect Ratio** (Number)
- **Loaded** (booleanNumber)
- **Loading** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/iRKrD-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Texture_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Texture_v2](https://cables.gl/op/Ops.Gl.Texture_v2)

---

### TextureArray
![TextureArray op](images/ops/Ops_Gl_TextureArray.svg)

**Full Name:** `Ops.Gl.TextureArray`
**Description:** create an array of textures

**> Input Ports:**
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

**< Output Ports:**
- **Array** (Array)
- **Count** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/vS5fjz)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureArray"*
**Docs:** [https://cables.gl/op/Ops.Gl.TextureArray](https://cables.gl/op/Ops.Gl.TextureArray)

---

### TextureArrayLoader_v2
![TextureArrayLoader_v2 op](images/ops/Ops_Gl_TextureArrayLoader_v2.svg)

**Full Name:** `Ops.Gl.TextureArrayLoader_v2`
**Description:** load multiple images into an array

**> Input Ports:**
- **Url** (String)
- **Left Pad** (Number: Boolean)
- **Index Start** (Number: Integer)
- **Index End** (Number: Integer)
- **Filter Index** (Number: Integer)
- **Wrap Index** (Number: Integer)
- **Flip** (Number: Boolean)
- **UnpackPreMultipliedAlpha** (Number: Boolean)

**< Output Ports:**
- **TextureArray** (Array)
- **Width** (Number)
- **Height** (Number)
- **Loading** (booleanNumber)
- **Aspect Ratio** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/OeGdjT)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureArrayLoader_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.TextureArrayLoader_v2](https://cables.gl/op/Ops.Gl.TextureArrayLoader_v2)

---

### TextureArrayLoaderFromArray_v3
![TextureArrayLoaderFromArray_v3 op](images/ops/Ops_Gl_TextureArrayLoaderFromArray_v3.svg)

**Full Name:** `Ops.Gl.TextureArrayLoaderFromArray_v3`
**Description:** load multiple texture from filenames given as an array

**> Input Ports:**
- **Urls** (Array)
- **Filter Index** (Number: Integer)
- **Wrap Index** (Number: Integer)
- **Flip** (Number: Boolean)
- **UnpackPreMultipliedAlpha** (Number: Boolean)
- **Caching** (Number: Boolean)
- **Asset In Patch** (Number: Boolean)

**< Output Ports:**
- **TextureArray** (Array)
- **Width** (Number)
- **Height** (Number)
- **Loading** (booleanNumber)
- **Aspect Ratio** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/jFv097)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureArrayLoaderFromArray_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.TextureArrayLoaderFromArray_v3](https://cables.gl/op/Ops.Gl.TextureArrayLoaderFromArray_v3)

---

### TextureColorPick
![TextureColorPick op](images/ops/Ops_Gl_TextureColorPick.svg)

**Full Name:** `Ops.Gl.TextureColorPick`
**Description:** get the color of a pixel in a texture

**> Input Ports:**
- **Update** (Trigger)
- **X** (Number: Integer)
- **Y** (Number: Integer)
- **Texture** (Object:Texture)
- **Active** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)
- **Red** (Number)
- **Green** (Number)
- **Blue** (Number)
- **Alpha** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/bzVSwn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureColorPick"*
**Docs:** [https://cables.gl/op/Ops.Gl.TextureColorPick](https://cables.gl/op/Ops.Gl.TextureColorPick)

---

### TextureToArray_v4
![TextureToArray_v4 op](images/ops/Ops_Gl_TextureToArray_v4.svg)

**Full Name:** `Ops.Gl.TextureToArray_v4`
**Description:** extract colors from a texture

**> Input Ports:**
- **Update** (Trigger)
- **Texture** (Object)

**< Output Ports:**
- **Trigger** (Trigger)
- **Colors** (Array)
- **Floating Point** (booleanNumber)
- **Num Pixel** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/uZkd3x)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureToArray_v4"*
**Docs:** [https://cables.gl/op/Ops.Gl.TextureToArray_v4](https://cables.gl/op/Ops.Gl.TextureToArray_v4)

---

### TextureToPointArray3
![TextureToPointArray3 op](images/ops/Ops_Gl_TextureToPointArray3.svg)

**Full Name:** `Ops.Gl.TextureToPointArray3`
**Description:** generate an array3 of grid positions from a texture

**> Input Ports:**
- **Update** (Trigger)
- **Center** (Number: Boolean)
- **Threshold Remove** (Number)
- **Z Multiply** (Number)
- **Texture** (Object)
- **Width** (Number)
- **Height** (Number)

**< Output Ports:**
- **Trigger** (Trigger)
- **Points** (Array)
- **Total Points** (Number)
- **Min Z** (Number)
- **Max Z** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/U8IO1k)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureToPointArray3"*
**Docs:** [https://cables.gl/op/Ops.Gl.TextureToPointArray3](https://cables.gl/op/Ops.Gl.TextureToPointArray3)

---

### TextureToRandomPoints
![TextureToRandomPoints op](images/ops/Ops_Gl_TextureToRandomPoints.svg)

**Full Name:** `Ops.Gl.TextureToRandomPoints`
**Description:** Create points by sampling texture

**> Input Ports:**
- **Update** (Trigger)
- **Num Points** (Number: Integer)
- **Seed** (Number)
- **Z Position Index** (Number: Integer)
- **Z Multiply** (Number)
- **Texture** (Object)

**< Output Ports:**
- **Trigger** (Trigger)
- **Points** (Array)
- **NumPoints** (Number)

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
- **Resized** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.TriggerOnCanvasResize#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerOnCanvasResize"*
**Docs:** [https://cables.gl/op/Ops.Gl.TriggerOnCanvasResize](https://cables.gl/op/Ops.Gl.TriggerOnCanvasResize)

---

### ValidTexture
![ValidTexture op](images/ops/Ops_Gl_ValidTexture.svg)

**Full Name:** `Ops.Gl.ValidTexture`
**Description:** output current input texture or a default texture

**> Input Ports:**
- **Texture** (Object:Texture)

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.ValidTexture#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ValidTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.ValidTexture](https://cables.gl/op/Ops.Gl.ValidTexture)

---

### ViewPortSize
![ViewPortSize op](images/ops/Ops_Gl_ViewPortSize.svg)

**Full Name:** `Ops.Gl.ViewPortSize`
**Description:** Outputs current viewport size

**> Input Ports:**
- **Exec** (Trigger)

**< Output Ports:**
- **Next** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Width** (Number)
- **Height** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.ViewPortSize#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ViewPortSize"*
**Docs:** [https://cables.gl/op/Ops.Gl.ViewPortSize](https://cables.gl/op/Ops.Gl.ViewPortSize)

---

