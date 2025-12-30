# Ops.Html

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Html

### ActiveElement
![ActiveElement op](images/ops/Ops_Html_ActiveElement.svg)

**Full Name:** `Ops.Html.ActiveElement`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ActiveElement) for details*

**> Input Ports:**
- **Trigger** (Trigger)

**< Output Ports:**
- **Active Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ActiveElement#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ActiveElement"*
**Docs:** [https://cables.gl/op/Ops.Html.ActiveElement](https://cables.gl/op/Ops.Html.ActiveElement)

---

### AlignElement
![AlignElement op](images/ops/Ops_Html_AlignElement.svg)

**Full Name:** `Ops.Html.AlignElement`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.AlignElement) for details*

**> Input Ports:**
- **Element** (Object:Element)
- **Align Element** (Object:Element)
- **Force Update** (Trigger)
- **Offset X** (Number)
- **Offset Y** (Number)

**< Output Ports:**
- **Element Passthrough** (Object)
- **Aligned Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.AlignElement#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AlignElement"*
**Docs:** [https://cables.gl/op/Ops.Html.AlignElement](https://cables.gl/op/Ops.Html.AlignElement)

---

### AppendChild_v2
![AppendChild_v2 op](images/ops/Ops_Html_AppendChild_v2.svg)

**Full Name:** `Ops.Html.AppendChild_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.AppendChild_v2) for details*

**> Input Ports:**
- **Parent** (Object:Element)
- **Child** (Object:Element)

**< Output Ports:**
- **Parent Out** (Object)
- **Child Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.AppendChild_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AppendChild_v2"*
**Docs:** [https://cables.gl/op/Ops.Html.AppendChild_v2](https://cables.gl/op/Ops.Html.AppendChild_v2)

---

### BrowserSpecificFile_v2
![BrowserSpecificFile_v2 op](images/ops/Ops_Html_BrowserSpecificFile_v2.svg)

**Full Name:** `Ops.Html.BrowserSpecificFile_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.BrowserSpecificFile_v2) for details*

**> Input Ports:**
- **Chrome File** (String)
- **Firefox File** (String)
- **Safari File** (String)
- **Edge File** (String)
- **Opera File** (String)
- **Default File** (String)

**< Output Ports:**
- **Browser Specific File** (String)
- **Detected Browser** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.BrowserSpecificFile_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BrowserSpecificFile_v2"*
**Docs:** [https://cables.gl/op/Ops.Html.BrowserSpecificFile_v2](https://cables.gl/op/Ops.Html.BrowserSpecificFile_v2)

---

### CanvasToBase64
![CanvasToBase64 op](images/ops/Ops_Html_CanvasToBase64.svg)

**Full Name:** `Ops.Html.CanvasToBase64`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.CanvasToBase64) for details*

**> Input Ports:**
- **Trigger** (Trigger)
- **Texture** (Object)
- **Quality** (Number)
- **Output DataUrl** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)
- **Binary Size** (Number)
- **Base64 String** (String)
- **Loading** (booleanNumber)
- **Finished** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.CanvasToBase64#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CanvasToBase64"*
**Docs:** [https://cables.gl/op/Ops.Html.CanvasToBase64](https://cables.gl/op/Ops.Html.CanvasToBase64)

---

### CompareImages_v2
![CompareImages_v2 op](images/ops/Ops_Html_CompareImages_v2.svg)

**Full Name:** `Ops.Html.CompareImages_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.CompareImages_v2) for details*

**> Input Ports:**
- **Image 1** (String)
- **Image 2** (String)
- **Start** (Trigger)

**< Output Ports:**
- **Difference Image** (String)
- **Mismatch Percentage** (Number)
- **Same Dimensions** (booleanNumber)
- **Resemble Data** (Object)
- **Finished** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.CompareImages_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CompareImages_v2"*
**Docs:** [https://cables.gl/op/Ops.Html.CompareImages_v2](https://cables.gl/op/Ops.Html.CompareImages_v2)

---

### DocumentBody
![DocumentBody op](images/ops/Ops_Html_DocumentBody.svg)

**Full Name:** `Ops.Html.DocumentBody`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.DocumentBody) for details*

**> Input Ports:**
- *Visit [Ops.Html.DocumentBody documentation](https://cables.gl/op/Ops.Html.DocumentBody) for input port details*

**< Output Ports:**
- **Body** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.DocumentBody#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DocumentBody"*
**Docs:** [https://cables.gl/op/Ops.Html.DocumentBody](https://cables.gl/op/Ops.Html.DocumentBody)

---

### DraggableElement
![DraggableElement op](images/ops/Ops_Html_DraggableElement.svg)

**Full Name:** `Ops.Html.DraggableElement`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.DraggableElement) for details*

**> Input Ports:**
- **Element** (Object:Element)

**< Output Ports:**
- **Element Out** (Object)
- **X** (Number)
- **Y** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.DraggableElement#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DraggableElement"*
**Docs:** [https://cables.gl/op/Ops.Html.DraggableElement](https://cables.gl/op/Ops.Html.DraggableElement)

---

### ElementAsHtmlString
![ElementAsHtmlString op](images/ops/Ops_Html_ElementAsHtmlString.svg)

**Full Name:** `Ops.Html.ElementAsHtmlString`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ElementAsHtmlString) for details*

**> Input Ports:**
- **Parent** (Object:Element)

**< Output Ports:**
- **HTML String** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ElementAsHtmlString#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementAsHtmlString"*
**Docs:** [https://cables.gl/op/Ops.Html.ElementAsHtmlString](https://cables.gl/op/Ops.Html.ElementAsHtmlString)

---

### ElementChilds_v2
![ElementChilds_v2 op](images/ops/Ops_Html_ElementChilds_v2.svg)

**Full Name:** `Ops.Html.ElementChilds_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ElementChilds_v2) for details*

**> Input Ports:**
- **Parent** (Object:Element)
- **Child 1** (Object:Element)
- **Child 2** (Object:Element)
- **Child 3** (Object:Element)
- **Child 4** (Object:Element)
- **Child 5** (Object:Element)
- **Child 6** (Object:Element)
- **Child 7** (Object:Element)
- **Child 8** (Object:Element)
- **Child 9** (Object:Element)
- **Child 10** (Object:Element)

**< Output Ports:**
- **Parent Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ElementChilds_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementChilds_v2"*
**Docs:** [https://cables.gl/op/Ops.Html.ElementChilds_v2](https://cables.gl/op/Ops.Html.ElementChilds_v2)

---

### ElementChildsMultiPort_v2
![ElementChildsMultiPort_v2 op](images/ops/Ops_Html_ElementChildsMultiPort_v2.svg)

**Full Name:** `Ops.Html.ElementChildsMultiPort_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ElementChildsMultiPort_v2) for details*

**> Input Ports:**
- **Parent** (Object:Element)
- **Childs_0** (Object)
- **Add Port** (Object)

**< Output Ports:**
- **Parent Out** (Object)
- **Num Values** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ElementChildsMultiPort_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementChildsMultiPort_v2"*
**Docs:** [https://cables.gl/op/Ops.Html.ElementChildsMultiPort_v2](https://cables.gl/op/Ops.Html.ElementChildsMultiPort_v2)

---

### ElementClientRect
![ElementClientRect op](images/ops/Ops_Html_ElementClientRect.svg)

**Full Name:** `Ops.Html.ElementClientRect`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ElementClientRect) for details*

**> Input Ports:**
- **Update** (Trigger)
- **Element** (Object:Element)

**< Output Ports:**
- **X** (Number)
- **Y** (Number)
- **Width** (Number)
- **Height** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ElementClientRect#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementClientRect"*
**Docs:** [https://cables.gl/op/Ops.Html.ElementClientRect](https://cables.gl/op/Ops.Html.ElementClientRect)

---

### ElementCssCursor_v3
![ElementCssCursor_v3 op](images/ops/Ops_Html_ElementCssCursor_v3.svg)

**Full Name:** `Ops.Html.ElementCssCursor_v3`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ElementCssCursor_v3) for details*

**> Input Ports:**
- **Element** (Object:Element)
- **CSS Cursors Index** (Number: Integer)
- **File** (String)
- **Offset X** (Number: Integer)
- **Offset Y** (Number: Integer)

**< Output Ports:**
- **HTML Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ElementCssCursor_v3#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementCssCursor_v3"*
**Docs:** [https://cables.gl/op/Ops.Html.ElementCssCursor_v3](https://cables.gl/op/Ops.Html.ElementCssCursor_v3)

---

### ElementCssString
![ElementCssString op](images/ops/Ops_Html_ElementCssString.svg)

**Full Name:** `Ops.Html.ElementCssString`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ElementCssString) for details*

**> Input Ports:**
- **Element** (Object:Element)

**< Output Ports:**
- **CSS** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ElementCssString#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementCssString"*
**Docs:** [https://cables.gl/op/Ops.Html.ElementCssString](https://cables.gl/op/Ops.Html.ElementCssString)

---

### ElementDataSet
![ElementDataSet op](images/ops/Ops_Html_ElementDataSet.svg)

**Full Name:** `Ops.Html.ElementDataSet`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ElementDataSet) for details*

**> Input Ports:**
- **HTML Element** (Object:Element)

**< Output Ports:**
- **Dataset** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ElementDataSet#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementDataSet"*
**Docs:** [https://cables.gl/op/Ops.Html.ElementDataSet](https://cables.gl/op/Ops.Html.ElementDataSet)

---

### ElementEquals
![ElementEquals op](images/ops/Ops_Html_ElementEquals.svg)

**Full Name:** `Ops.Html.ElementEquals`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ElementEquals) for details*

**> Input Ports:**
- **HTML Element** (Object:Element)
- **HTML Element 2** (Object:Element)

**< Output Ports:**
- **Equal** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ElementEquals#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementEquals"*
**Docs:** [https://cables.gl/op/Ops.Html.ElementEquals](https://cables.gl/op/Ops.Html.ElementEquals)

---

### ElementFadeInOut_v2
![ElementFadeInOut_v2 op](images/ops/Ops_Html_ElementFadeInOut_v2.svg)

**Full Name:** `Ops.Html.ElementFadeInOut_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ElementFadeInOut_v2) for details*

**> Input Ports:**
- **HTML Element** (Object)
- **Visible** (Number: Boolean)
- **Duration** (Number)
- **Opacity** (Number)

**< Output Ports:**
- **PassThrough** (Object)
- **Is Showing** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ElementFadeInOut_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementFadeInOut_v2"*
**Docs:** [https://cables.gl/op/Ops.Html.ElementFadeInOut_v2](https://cables.gl/op/Ops.Html.ElementFadeInOut_v2)

---

### ElementGetClosest
![ElementGetClosest op](images/ops/Ops_Html_ElementGetClosest.svg)

**Full Name:** `Ops.Html.ElementGetClosest`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ElementGetClosest) for details*

**> Input Ports:**
- **HTML Element** (Object:Element)
- **Query** (String)

**< Output Ports:**
- **Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ElementGetClosest#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementGetClosest"*
**Docs:** [https://cables.gl/op/Ops.Html.ElementGetClosest](https://cables.gl/op/Ops.Html.ElementGetClosest)

---

### ElementGradientBg
![ElementGradientBg op](images/ops/Ops_Html_ElementGradientBg.svg)

**Full Name:** `Ops.Html.ElementGradientBg`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ElementGradientBg) for details*

**> Input Ports:**
- **Element** (Object:Element)
- **Rect Color Space Index** (Number: Integer)
- **Angle** (Number)
- **Gradient Object** (Object:Gradient)

**< Output Ports:**
- **HTML Element** (Object)
- **CSS String** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ElementGradientBg#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementGradientBg"*
**Docs:** [https://cables.gl/op/Ops.Html.ElementGradientBg](https://cables.gl/op/Ops.Html.ElementGradientBg)

---

### ElementHasClass
![ElementHasClass op](images/ops/Ops_Html_ElementHasClass.svg)

**Full Name:** `Ops.Html.ElementHasClass`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ElementHasClass) for details*

**> Input Ports:**
- **Element** (Object:Element)
- **Classname** (String)
- **Update** (Trigger)

**< Output Ports:**
- **Has Class** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ElementHasClass#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementHasClass"*
**Docs:** [https://cables.gl/op/Ops.Html.ElementHasClass](https://cables.gl/op/Ops.Html.ElementHasClass)

---

### ElementInfo
![ElementInfo op](images/ops/Ops_Html_ElementInfo.svg)

**Full Name:** `Ops.Html.ElementInfo`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ElementInfo) for details*

**> Input Ports:**
- **Element** (Object)

**< Output Ports:**
- **Tagname** (String)
- **Id** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ElementInfo#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementInfo"*
**Docs:** [https://cables.gl/op/Ops.Html.ElementInfo](https://cables.gl/op/Ops.Html.ElementInfo)

---

### ElementIsFocused
![ElementIsFocused op](images/ops/Ops_Html_ElementIsFocused.svg)

**Full Name:** `Ops.Html.ElementIsFocused`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ElementIsFocused) for details*

**> Input Ports:**
- **Element** (Object:Element)
- **Update** (Trigger)

**< Output Ports:**
- **Has Focus** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ElementIsFocused#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementIsFocused"*
**Docs:** [https://cables.gl/op/Ops.Html.ElementIsFocused](https://cables.gl/op/Ops.Html.ElementIsFocused)

---

### ElementsPositionsByClass
![ElementsPositionsByClass op](images/ops/Ops_Html_ElementsPositionsByClass.svg)

**Full Name:** `Ops.Html.ElementsPositionsByClass`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ElementsPositionsByClass) for details*

**> Input Ports:**
- **Update** (Trigger)
- **Classname** (String)

**< Output Ports:**
- **Position** (Array)
- **Size** (Array)
- **Total Elements** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ElementsPositionsByClass#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementsPositionsByClass"*
**Docs:** [https://cables.gl/op/Ops.Html.ElementsPositionsByClass](https://cables.gl/op/Ops.Html.ElementsPositionsByClass)

---

### FontFile_v2
![FontFile_v2 op](images/ops/Ops_Html_FontFile_v2.svg)

**Full Name:** `Ops.Html.FontFile_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.FontFile_v2) for details*

**> Input Ports:**
- **File** (String)
- **Family** (String)
- **Active** (Number: Boolean)

**< Output Ports:**
- **Loaded** (booleanNumber)
- **Loaded Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.FontFile_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FontFile_v2"*
**Docs:** [https://cables.gl/op/Ops.Html.FontFile_v2](https://cables.gl/op/Ops.Html.FontFile_v2)

---

### FontsLoaded
![FontsLoaded op](images/ops/Ops_Html_FontsLoaded.svg)

**Full Name:** `Ops.Html.FontsLoaded`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.FontsLoaded) for details*

**> Input Ports:**
- *Visit [Ops.Html.FontsLoaded documentation](https://cables.gl/op/Ops.Html.FontsLoaded) for input port details*

**< Output Ports:**
- **Font Loaded** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.FontsLoaded#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FontsLoaded"*
**Docs:** [https://cables.gl/op/Ops.Html.FontsLoaded](https://cables.gl/op/Ops.Html.FontsLoaded)

---

### FullscreenMode
![FullscreenMode op](images/ops/Ops_Html_FullscreenMode.svg)

**Full Name:** `Ops.Html.FullscreenMode`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.FullscreenMode) for details*

**> Input Ports:**
- **Request Fullscreen** (Trigger)
- **Exit Fullscreen** (Trigger)

**< Output Ports:**
- **Is Fullscreen** (booleanNumber)
- **Supported** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.FullscreenMode#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FullscreenMode"*
**Docs:** [https://cables.gl/op/Ops.Html.FullscreenMode](https://cables.gl/op/Ops.Html.FullscreenMode)

---

### GlCopyToCanvas
![GlCopyToCanvas op](images/ops/Ops_Html_GlCopyToCanvas.svg)

**Full Name:** `Ops.Html.GlCopyToCanvas`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.GlCopyToCanvas) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Canvas** (Object:Element)
- **Smooth** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.GlCopyToCanvas#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GlCopyToCanvas"*
**Docs:** [https://cables.gl/op/Ops.Html.GlCopyToCanvas](https://cables.gl/op/Ops.Html.GlCopyToCanvas)

---

### HyperLink_v3
![HyperLink_v3 op](images/ops/Ops_Html_HyperLink_v3.svg)

**Full Name:** `Ops.Html.HyperLink_v3`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.HyperLink_v3) for details*

**> Input Ports:**
- **Open** (Trigger)
- **URL** (String)
- **Frame Name** (String)
- **Win Specs** (String)
- **Rel Attribute** (String)

**< Output Ports:**
- *Visit [Ops.Html.HyperLink_v3 documentation](https://cables.gl/op/Ops.Html.HyperLink_v3) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.HyperLink_v3#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HyperLink_v3"*
**Docs:** [https://cables.gl/op/Ops.Html.HyperLink_v3](https://cables.gl/op/Ops.Html.HyperLink_v3)

---

### InnerHTML
![InnerHTML op](images/ops/Ops_Html_InnerHTML.svg)

**Full Name:** `Ops.Html.InnerHTML`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.InnerHTML) for details*

**> Input Ports:**
- **Element** (Object)
- **Value** (String)
- **Active** (Number: Boolean)
- **Clear** (Trigger)

**< Output Ports:**
- **HTML Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.InnerHTML#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InnerHTML"*
**Docs:** [https://cables.gl/op/Ops.Html.InnerHTML](https://cables.gl/op/Ops.Html.InnerHTML)

---

### InnerHtmlAppend
![InnerHtmlAppend op](images/ops/Ops_Html_InnerHtmlAppend.svg)

**Full Name:** `Ops.Html.InnerHtmlAppend`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.InnerHtmlAppend) for details*

**> Input Ports:**
- **Element** (Object:Element)
- **Html** (String)
- **Trigger** (Trigger)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.InnerHtmlAppend#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InnerHtmlAppend"*
**Docs:** [https://cables.gl/op/Ops.Html.InnerHtmlAppend](https://cables.gl/op/Ops.Html.InnerHtmlAppend)

---

### MailtoLink
![MailtoLink op](images/ops/Ops_Html_MailtoLink.svg)

**Full Name:** `Ops.Html.MailtoLink`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.MailtoLink) for details*

**> Input Ports:**
- **Email** (String)
- **Subject** (String)
- **Execute** (Trigger)

**< Output Ports:**
- *Visit [Ops.Html.MailtoLink documentation](https://cables.gl/op/Ops.Html.MailtoLink) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.MailtoLink#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MailtoLink"*
**Docs:** [https://cables.gl/op/Ops.Html.MailtoLink](https://cables.gl/op/Ops.Html.MailtoLink)

---

### MarkdownToHtml
![MarkdownToHtml op](images/ops/Ops_Html_MarkdownToHtml.svg)

**Full Name:** `Ops.Html.MarkdownToHtml`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.MarkdownToHtml) for details*

**> Input Ports:**
- **Markdown** (String)
- **Active** (Number: Boolean)

**< Output Ports:**
- **Html** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.MarkdownToHtml#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MarkdownToHtml"*
**Docs:** [https://cables.gl/op/Ops.Html.MarkdownToHtml](https://cables.gl/op/Ops.Html.MarkdownToHtml)

---

### ModalOverlay
![ModalOverlay op](images/ops/Ops_Html_ModalOverlay.svg)

**Full Name:** `Ops.Html.ModalOverlay`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ModalOverlay) for details*

**> Input Ports:**
- **Content Element** (Object)
- **Show** (Trigger)
- **Close** (Trigger)
- **Show Closebutton** (Number: Boolean)
- **Opacity** (Number)

**< Output Ports:**
- **Visible** (booleanNumber)
- **Closed** (Trigger)
- **Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ModalOverlay#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ModalOverlay"*
**Docs:** [https://cables.gl/op/Ops.Html.ModalOverlay](https://cables.gl/op/Ops.Html.ModalOverlay)

---

### QuerySelector_v3
![QuerySelector_v3 op](images/ops/Ops_Html_QuerySelector_v3.svg)

**Full Name:** `Ops.Html.QuerySelector_v3`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.QuerySelector_v3) for details*

**> Input Ports:**
- **Update** (Trigger)
- **Query** (String)
- **Type Index** (Number: Integer)
- **Document** (String)
- **Input Element** (Object:Element)

**< Output Ports:**
- **Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.QuerySelector_v3#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "QuerySelector_v3"*
**Docs:** [https://cables.gl/op/Ops.Html.QuerySelector_v3](https://cables.gl/op/Ops.Html.QuerySelector_v3)

---

### QuerySelectorAll_v2
![QuerySelectorAll_v2 op](images/ops/Ops_Html_QuerySelectorAll_v2.svg)

**Full Name:** `Ops.Html.QuerySelectorAll_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.QuerySelectorAll_v2) for details*

**> Input Ports:**
- **Query** (String)
- **Mode Index** (Number: Integer)
- **Type Index** (Number: Integer)
- **Document** (String)
- **Element** (Object:Element)
- **Update** (Trigger)

**< Output Ports:**
- **Elements** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.QuerySelectorAll_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "QuerySelectorAll_v2"*
**Docs:** [https://cables.gl/op/Ops.Html.QuerySelectorAll_v2](https://cables.gl/op/Ops.Html.QuerySelectorAll_v2)

---

### ReloadPage
![ReloadPage op](images/ops/Ops_Html_ReloadPage.svg)

**Full Name:** `Ops.Html.ReloadPage`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ReloadPage) for details*

**> Input Ports:**
- **Exec** (Trigger)

**< Output Ports:**
- *Visit [Ops.Html.ReloadPage documentation](https://cables.gl/op/Ops.Html.ReloadPage) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ReloadPage#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ReloadPage"*
**Docs:** [https://cables.gl/op/Ops.Html.ReloadPage](https://cables.gl/op/Ops.Html.ReloadPage)

---

### ScrollIntoView
![ScrollIntoView op](images/ops/Ops_Html_ScrollIntoView.svg)

**Full Name:** `Ops.Html.ScrollIntoView`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ScrollIntoView) for details*

**> Input Ports:**
- **Element** (Object:Element)
- **Scroll Into View** (Trigger)

**< Output Ports:**
- **HTML Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ScrollIntoView#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScrollIntoView"*
**Docs:** [https://cables.gl/op/Ops.Html.ScrollIntoView](https://cables.gl/op/Ops.Html.ScrollIntoView)

---

### ScrollPosition_v2
![ScrollPosition_v2 op](images/ops/Ops_Html_ScrollPosition_v2.svg)

**Full Name:** `Ops.Html.ScrollPosition_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ScrollPosition_v2) for details*

**> Input Ports:**
- **Update** (Trigger)
- **Element** (Object:Element)
- **Scroll To Top** (Trigger)

**< Output Ports:**
- **Next** (Trigger)
- **Left** (Number)
- **Top** (Number)
- **Percentage X** (Number)
- **Percentage Y** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ScrollPosition_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScrollPosition_v2"*
**Docs:** [https://cables.gl/op/Ops.Html.ScrollPosition_v2](https://cables.gl/op/Ops.Html.ScrollPosition_v2)

---

### ScrollTo
![ScrollTo op](images/ops/Ops_Html_ScrollTo.svg)

**Full Name:** `Ops.Html.ScrollTo`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.ScrollTo) for details*

**> Input Ports:**
- **Element** (Object:Element)
- **Scroll To Top** (Trigger)
- **Scroll To Bottom** (Trigger)

**< Output Ports:**
- *Visit [Ops.Html.ScrollTo documentation](https://cables.gl/op/Ops.Html.ScrollTo) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ScrollTo#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScrollTo"*
**Docs:** [https://cables.gl/op/Ops.Html.ScrollTo](https://cables.gl/op/Ops.Html.ScrollTo)

---

### WindowClose
![WindowClose op](images/ops/Ops_Html_WindowClose.svg)

**Full Name:** `Ops.Html.WindowClose`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.WindowClose) for details*

**> Input Ports:**
- **Close** (Trigger)

**< Output Ports:**
- *Visit [Ops.Html.WindowClose documentation](https://cables.gl/op/Ops.Html.WindowClose) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.WindowClose#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WindowClose"*
**Docs:** [https://cables.gl/op/Ops.Html.WindowClose](https://cables.gl/op/Ops.Html.WindowClose)

---

### WindowHasFocus
![WindowHasFocus op](images/ops/Ops_Html_WindowHasFocus.svg)

**Full Name:** `Ops.Html.WindowHasFocus`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.WindowHasFocus) for details*

**> Input Ports:**
- *Visit [Ops.Html.WindowHasFocus documentation](https://cables.gl/op/Ops.Html.WindowHasFocus) for input port details*

**< Output Ports:**
- **Has Focus** (booleanNumber)
- **Tab Visible** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.WindowHasFocus#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WindowHasFocus"*
**Docs:** [https://cables.gl/op/Ops.Html.WindowHasFocus](https://cables.gl/op/Ops.Html.WindowHasFocus)

---

### WindowInfo
![WindowInfo op](images/ops/Ops_Html_WindowInfo.svg)

**Full Name:** `Ops.Html.WindowInfo`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.WindowInfo) for details*

**> Input Ports:**
- *Visit [Ops.Html.WindowInfo documentation](https://cables.gl/op/Ops.Html.WindowInfo) for input port details*

**< Output Ports:**
- **ClientWidth** (Number)
- **ClientHeight** (Number)
- **Body Scroll Height** (Number)
- **Device Pixel Ratio** (Number)
- **Iframe Parent** (booleanNumber)
- **Orientation Angle** (Number)
- **Orientation Type** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.WindowInfo#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WindowInfo"*
**Docs:** [https://cables.gl/op/Ops.Html.WindowInfo](https://cables.gl/op/Ops.Html.WindowInfo)

---

### WindowScroll
![WindowScroll op](images/ops/Ops_Html_WindowScroll.svg)

**Full Name:** `Ops.Html.WindowScroll`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.WindowScroll) for details*

**> Input Ports:**
- **Update** (Trigger)

**< Output Ports:**
- **Scoll X** (Number)
- **Scoll Y** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.WindowScroll#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WindowScroll"*
**Docs:** [https://cables.gl/op/Ops.Html.WindowScroll](https://cables.gl/op/Ops.Html.WindowScroll)

---

