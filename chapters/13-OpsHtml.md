# Ops.Html

---

## Ops.Html

### ActiveElement
![ActiveElement op](images/ops/Ops_Html_ActiveElement.svg)

**Full Name:** `Ops.Html.ActiveElement`

**Description:** Outputs the currently active/focused element

**> Input Ports:**

- **Trigger** (Trigger)

**< Output Ports:**

- **Active Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/0iRDu1)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ActiveElement"*

**Docs:** [https://cables.gl/op/Ops.Html.ActiveElement](https://cables.gl/op/Ops.Html.ActiveElement)


### AlignElement
![AlignElement op](images/ops/Ops_Html_AlignElement.svg)

**Full Name:** `Ops.Html.AlignElement`

**Description:** Align a HTML element to another, keep positioning

**> Input Ports:**

- **Element** (Object:Element)
- **Align Element** (Object:Element)
- **Force Update** (Trigger)
- **Offset X** (Number)
- **Offset Y** (Number)

**< Output Ports:**

- **Element Passthrough** (Object)
- **Aligned Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/jKcTdv)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AlignElement"*

**Docs:** [https://cables.gl/op/Ops.Html.AlignElement](https://cables.gl/op/Ops.Html.AlignElement)


### AppendChild_v2
![AppendChild_v2 op](images/ops/Ops_Html_AppendChild_v2.svg)

**Full Name:** `Ops.Html.AppendChild_v2`

**Description:** Appends a HTML DOM Element to another

**> Input Ports:**

- **Parent** (Object:Element)
- **Child** (Object:Element)

**< Output Ports:**

- **Parent Out** (Object)
- **Child Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/PakK8i)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AppendChild_v2"*

**Docs:** [https://cables.gl/op/Ops.Html.AppendChild_v2](https://cables.gl/op/Ops.Html.AppendChild_v2)


### BrowserSpecificFile_v2
![BrowserSpecificFile_v2 op](images/ops/Ops_Html_BrowserSpecificFile_v2.svg)

**Full Name:** `Ops.Html.BrowserSpecificFile_v2`

**Description:** set file dependant on browser

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

**Example Patch:** [Open in Editor](https://cables.gl/edit/CfJkIk)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BrowserSpecificFile_v2"*

**Docs:** [https://cables.gl/op/Ops.Html.BrowserSpecificFile_v2](https://cables.gl/op/Ops.Html.BrowserSpecificFile_v2)


### CanvasToBase64
![CanvasToBase64 op](images/ops/Ops_Html_CanvasToBase64.svg)

**Full Name:** `Ops.Html.CanvasToBase64`

**Description:** Create an image file from a canvas

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


### CompareImages_v2
![CompareImages_v2 op](images/ops/Ops_Html_CompareImages_v2.svg)

**Full Name:** `Ops.Html.CompareImages_v2`

**Description:** compares two images and shows the difference as a pink color

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

**Example Patch:** [Open in Editor](https://cables.gl/edit/1xkRN8)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CompareImages_v2"*

**Docs:** [https://cables.gl/op/Ops.Html.CompareImages_v2](https://cables.gl/op/Ops.Html.CompareImages_v2)


### DocumentBody
![DocumentBody op](images/ops/Ops_Html_DocumentBody.svg)

**Full Name:** `Ops.Html.DocumentBody`

**Description:** Outputs the current document body element

**> Input Ports:**

- *Visit [Ops.Html.DocumentBody documentation](https://cables.gl/op/Ops.Html.DocumentBody) for input port details*

**< Output Ports:**

- **Body** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.DocumentBody#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DocumentBody"*

**Docs:** [https://cables.gl/op/Ops.Html.DocumentBody](https://cables.gl/op/Ops.Html.DocumentBody)


### DraggableElement
![DraggableElement op](images/ops/Ops_Html_DraggableElement.svg)

**Full Name:** `Ops.Html.DraggableElement`

**Description:** Make a HTML element draggable to move it around with the mouse

**> Input Ports:**

- **Element** (Object:Element)

**< Output Ports:**

- **Element Out** (Object)
- **X** (Number)
- **Y** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/WSi9iO)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DraggableElement"*

**Docs:** [https://cables.gl/op/Ops.Html.DraggableElement](https://cables.gl/op/Ops.Html.DraggableElement)


### ElementAsHtmlString
![ElementAsHtmlString op](images/ops/Ops_Html_ElementAsHtmlString.svg)

**Full Name:** `Ops.Html.ElementAsHtmlString`

**Description:** Serialize HTML/SVG elements to a string

**> Input Ports:**

- **Parent** (Object:Element)

**< Output Ports:**

- **HTML String** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/3kGgr5)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementAsHtmlString"*

**Docs:** [https://cables.gl/op/Ops.Html.ElementAsHtmlString](https://cables.gl/op/Ops.Html.ElementAsHtmlString)


### ElementChilds_v2
![ElementChilds_v2 op](images/ops/Ops_Html_ElementChilds_v2.svg)

**Full Name:** `Ops.Html.ElementChilds_v2`

**Description:** Set childs of a HTML Element

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

**Example Patch:** [Open in Editor](https://cables.gl/edit/S4VD0H)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementChilds_v2"*

**Docs:** [https://cables.gl/op/Ops.Html.ElementChilds_v2](https://cables.gl/op/Ops.Html.ElementChilds_v2)


### ElementChildsMultiPort_v2
![ElementChildsMultiPort_v2 op](images/ops/Ops_Html_ElementChildsMultiPort_v2.svg)

**Full Name:** `Ops.Html.ElementChildsMultiPort_v2`

**Description:** add child elements to another HTML Element

**> Input Ports:**

- **Parent** (Object:Element)
- **Childs_0** (Object)
- **Add Port** (Object)

**< Output Ports:**

- **Parent Out** (Object)
- **Num Values** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/zC9iWh)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementChildsMultiPort_v2"*

**Docs:** [https://cables.gl/op/Ops.Html.ElementChildsMultiPort_v2](https://cables.gl/op/Ops.Html.ElementChildsMultiPort_v2)


### ElementClientRect
![ElementClientRect op](images/ops/Ops_Html_ElementClientRect.svg)

**Full Name:** `Ops.Html.ElementClientRect`

**Description:** get html element absolute position and size in pixels on screen

**> Input Ports:**

- **Update** (Trigger)
- **Element** (Object:Element)

**< Output Ports:**

- **X** (Number)
- **Y** (Number)
- **Width** (Number)
- **Height** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/1Z8oLu)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementClientRect"*

**Docs:** [https://cables.gl/op/Ops.Html.ElementClientRect](https://cables.gl/op/Ops.Html.ElementClientRect)


### ElementCssCursor_v3
![ElementCssCursor_v3 op](images/ops/Ops_Html_ElementCssCursor_v3.svg)

**Full Name:** `Ops.Html.ElementCssCursor_v3`

**Description:** Set the mouse cursor

**> Input Ports:**

- **Element** (Object:Element)
- **CSS Cursors Index** (Number: Integer)
- **File** (String)
- **Offset X** (Number: Integer)
- **Offset Y** (Number: Integer)

**< Output Ports:**

- **HTML Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/_f5W8s)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementCssCursor_v3"*

**Docs:** [https://cables.gl/op/Ops.Html.ElementCssCursor_v3](https://cables.gl/op/Ops.Html.ElementCssCursor_v3)


### ElementCssString
![ElementCssString op](images/ops/Ops_Html_ElementCssString.svg)

**Full Name:** `Ops.Html.ElementCssString`

**Description:** Output css attributes of an element as a string

**> Input Ports:**

- **Element** (Object:Element)

**< Output Ports:**

- **CSS** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/8JmrBZ)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementCssString"*

**Docs:** [https://cables.gl/op/Ops.Html.ElementCssString](https://cables.gl/op/Ops.Html.ElementCssString)


### ElementDataSet
![ElementDataSet op](images/ops/Ops_Html_ElementDataSet.svg)

**Full Name:** `Ops.Html.ElementDataSet`

**Description:** Get the data-attributes and values of an HTML element

**> Input Ports:**

- **HTML Element** (Object:Element)

**< Output Ports:**

- **Dataset** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/MgdKjH)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementDataSet"*

**Docs:** [https://cables.gl/op/Ops.Html.ElementDataSet](https://cables.gl/op/Ops.Html.ElementDataSet)


### ElementEquals
![ElementEquals op](images/ops/Ops_Html_ElementEquals.svg)

**Full Name:** `Ops.Html.ElementEquals`

**Description:** Check if two HTML element objects are equal

**> Input Ports:**

- **HTML Element** (Object:Element)
- **HTML Element 2** (Object:Element)

**< Output Ports:**

- **Equal** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/LZSRjH)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementEquals"*

**Docs:** [https://cables.gl/op/Ops.Html.ElementEquals](https://cables.gl/op/Ops.Html.ElementEquals)


### ElementFadeInOut_v2
![ElementFadeInOut_v2 op](images/ops/Ops_Html_ElementFadeInOut_v2.svg)

**Full Name:** `Ops.Html.ElementFadeInOut_v2`

**Description:** fade html elements in or out

**> Input Ports:**

- **HTML Element** (Object)
- **Visible** (Number: Boolean)
- **Duration** (Number)
- **Opacity** (Number)

**< Output Ports:**

- **PassThrough** (Object)
- **Is Showing** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Whj018)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementFadeInOut_v2"*

**Docs:** [https://cables.gl/op/Ops.Html.ElementFadeInOut_v2](https://cables.gl/op/Ops.Html.ElementFadeInOut_v2)


### ElementGetClosest
![ElementGetClosest op](images/ops/Ops_Html_ElementGetClosest.svg)

**Full Name:** `Ops.Html.ElementGetClosest`

**Description:** get the closest parent element matching the query selector

**> Input Ports:**

- **HTML Element** (Object:Element)
- **Query** (String)

**< Output Ports:**

- **Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/ojHGjH)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementGetClosest"*

**Docs:** [https://cables.gl/op/Ops.Html.ElementGetClosest](https://cables.gl/op/Ops.Html.ElementGetClosest)


### ElementGradientBg
![ElementGradientBg op](images/ops/Ops_Html_ElementGradientBg.svg)

**Full Name:** `Ops.Html.ElementGradientBg`

**Description:** Use a cables gradient as HTML element background

**> Input Ports:**

- **Element** (Object:Element)
- **Rect Color Space Index** (Number: Integer)
- **Angle** (Number)
- **Gradient Object** (Object:Gradient)

**< Output Ports:**

- **HTML Element** (Object)
- **CSS String** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/QB7br5)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementGradientBg"*

**Docs:** [https://cables.gl/op/Ops.Html.ElementGradientBg](https://cables.gl/op/Ops.Html.ElementGradientBg)


### ElementHasClass
![ElementHasClass op](images/ops/Ops_Html_ElementHasClass.svg)

**Full Name:** `Ops.Html.ElementHasClass`

**Description:** Does the element currenty have a specific class set

**> Input Ports:**

- **Element** (Object:Element)
- **Classname** (String)
- **Update** (Trigger)

**< Output Ports:**

- **Has Class** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.ElementHasClass#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementHasClass"*

**Docs:** [https://cables.gl/op/Ops.Html.ElementHasClass](https://cables.gl/op/Ops.Html.ElementHasClass)


### ElementInfo
![ElementInfo op](images/ops/Ops_Html_ElementInfo.svg)

**Full Name:** `Ops.Html.ElementInfo`

**Description:** Get information about an element

**> Input Ports:**

- **Element** (Object)

**< Output Ports:**

- **Tagname** (String)
- **Id** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/0iRDu1)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementInfo"*

**Docs:** [https://cables.gl/op/Ops.Html.ElementInfo](https://cables.gl/op/Ops.Html.ElementInfo)


### ElementIsFocused
![ElementIsFocused op](images/ops/Ops_Html_ElementIsFocused.svg)

**Full Name:** `Ops.Html.ElementIsFocused`

**Description:** Is the connected element currently focused

**> Input Ports:**

- **Element** (Object:Element)
- **Update** (Trigger)

**< Output Ports:**

- **Has Focus** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/9jTwz1)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementIsFocused"*

**Docs:** [https://cables.gl/op/Ops.Html.ElementIsFocused](https://cables.gl/op/Ops.Html.ElementIsFocused)


### ElementsPositionsByClass
![ElementsPositionsByClass op](images/ops/Ops_Html_ElementsPositionsByClass.svg)

**Full Name:** `Ops.Html.ElementsPositionsByClass`

**Description:** get html element absolute positions and sizes by classname

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


### FontFile_v2
![FontFile_v2 op](images/ops/Ops_Html_FontFile_v2.svg)

**Full Name:** `Ops.Html.FontFile_v2`

**Description:** Load a font file like .otf, .ttf, .woff via css

**> Input Ports:**

- **File** (String)
- **Family** (String)
- **Active** (Number: Boolean)

**< Output Ports:**

- **Loaded** (booleanNumber)
- **Loaded Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/xR9zIR)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FontFile_v2"*

**Docs:** [https://cables.gl/op/Ops.Html.FontFile_v2](https://cables.gl/op/Ops.Html.FontFile_v2)


### FontsLoaded
![FontsLoaded op](images/ops/Ops_Html_FontsLoaded.svg)

**Full Name:** `Ops.Html.FontsLoaded`

**Description:** triggers when asynchronous requests finised loading

**> Input Ports:**

- *Visit [Ops.Html.FontsLoaded documentation](https://cables.gl/op/Ops.Html.FontsLoaded) for input port details*

**< Output Ports:**

- **Font Loaded** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/xP04r1)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FontsLoaded"*

**Docs:** [https://cables.gl/op/Ops.Html.FontsLoaded](https://cables.gl/op/Ops.Html.FontsLoaded)


### FullscreenMode
![FullscreenMode op](images/ops/Ops_Html_FullscreenMode.svg)

**Full Name:** `Ops.Html.FullscreenMode`

**Description:** Switch webgl to fullscreen

**> Input Ports:**

- **Request Fullscreen** (Trigger)
- **Exit Fullscreen** (Trigger)

**< Output Ports:**

- **Is Fullscreen** (booleanNumber)
- **Supported** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/CCoJji)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FullscreenMode"*

**Docs:** [https://cables.gl/op/Ops.Html.FullscreenMode](https://cables.gl/op/Ops.Html.FullscreenMode)


### GlCopyToCanvas
![GlCopyToCanvas op](images/ops/Ops_Html_GlCopyToCanvas.svg)

**Full Name:** `Ops.Html.GlCopyToCanvas`

**Description:** Copy GL canvas content to another canvas

**> Input Ports:**

- **Render** (Trigger)
- **Canvas** (Object:Element)
- **Smooth** (Number: Boolean)

**< Output Ports:**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/u2vAu1)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GlCopyToCanvas"*

**Docs:** [https://cables.gl/op/Ops.Html.GlCopyToCanvas](https://cables.gl/op/Ops.Html.GlCopyToCanvas)


### HyperLink_v3
![HyperLink_v3 op](images/ops/Ops_Html_HyperLink_v3.svg)

**Full Name:** `Ops.Html.HyperLink_v3`

**Description:** Open another website

**> Input Ports:**

- **Open** (Trigger)
- **URL** (String)
- **Frame Name** (String)
- **Win Specs** (String)
- **Rel Attribute** (String)

**< Output Ports:**

- *Visit [Ops.Html.HyperLink_v3 documentation](https://cables.gl/op/Ops.Html.HyperLink_v3) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ilts7O)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HyperLink_v3"*

**Docs:** [https://cables.gl/op/Ops.Html.HyperLink_v3](https://cables.gl/op/Ops.Html.HyperLink_v3)


### InnerHTML
![InnerHTML op](images/ops/Ops_Html_InnerHTML.svg)

**Full Name:** `Ops.Html.InnerHTML`

**Description:** Set innerHTML or innerTEXT of an HTML element

**> Input Ports:**

- **Element** (Object)
- **Value** (String)
- **Active** (Number: Boolean)
- **Clear** (Trigger)

**< Output Ports:**

- **HTML Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/jgArsw)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InnerHTML"*

**Docs:** [https://cables.gl/op/Ops.Html.InnerHTML](https://cables.gl/op/Ops.Html.InnerHTML)


### InnerHtmlAppend
![InnerHtmlAppend op](images/ops/Ops_Html_InnerHtmlAppend.svg)

**Full Name:** `Ops.Html.InnerHtmlAppend`

**Description:** Append string to the inner html or an element

**> Input Ports:**

- **Element** (Object:Element)
- **Html** (String)
- **Trigger** (Trigger)

**< Output Ports:**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/hmTiu1)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InnerHtmlAppend"*

**Docs:** [https://cables.gl/op/Ops.Html.InnerHtmlAppend](https://cables.gl/op/Ops.Html.InnerHtmlAppend)


### MailtoLink
![MailtoLink op](images/ops/Ops_Html_MailtoLink.svg)

**Full Name:** `Ops.Html.MailtoLink`

**Description:** creates a mailto: link to open the default email app

**> Input Ports:**

- **Email** (String)
- **Subject** (String)
- **Execute** (Trigger)

**< Output Ports:**

- *Visit [Ops.Html.MailtoLink documentation](https://cables.gl/op/Ops.Html.MailtoLink) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ilts7O)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MailtoLink"*

**Docs:** [https://cables.gl/op/Ops.Html.MailtoLink](https://cables.gl/op/Ops.Html.MailtoLink)


### MarkdownToHtml
![MarkdownToHtml op](images/ops/Ops_Html_MarkdownToHtml.svg)

**Full Name:** `Ops.Html.MarkdownToHtml`

**Description:** markdown markup language to html parser

**> Input Ports:**

- **Markdown** (String)
- **Active** (Number: Boolean)

**< Output Ports:**

- **Html** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/52Zlij)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MarkdownToHtml"*

**Docs:** [https://cables.gl/op/Ops.Html.MarkdownToHtml](https://cables.gl/op/Ops.Html.MarkdownToHtml)


### ModalOverlay
![ModalOverlay op](images/ops/Ops_Html_ModalOverlay.svg)

**Full Name:** `Ops.Html.ModalOverlay`

**Description:** create a modal HTML overlay with a darkened background

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

**Example Patch:** [Open in Editor](https://cables.gl/edit/RXU-K2)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ModalOverlay"*

**Docs:** [https://cables.gl/op/Ops.Html.ModalOverlay](https://cables.gl/op/Ops.Html.ModalOverlay)


### QuerySelector_v3
![QuerySelector_v3 op](images/ops/Ops_Html_QuerySelector_v3.svg)

**Full Name:** `Ops.Html.QuerySelector_v3`

**Description:** Selects an element in the DOM

**> Input Ports:**

- **Update** (Trigger)
- **Query** (String)
- **Type Index** (Number: Integer)
- **Document** (String)
- **Input Element** (Object:Element)

**< Output Ports:**

- **Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/C6z3GH)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "QuerySelector_v3"*

**Docs:** [https://cables.gl/op/Ops.Html.QuerySelector_v3](https://cables.gl/op/Ops.Html.QuerySelector_v3)


### QuerySelectorAll_v2
![QuerySelectorAll_v2 op](images/ops/Ops_Html_QuerySelectorAll_v2.svg)

**Full Name:** `Ops.Html.QuerySelectorAll_v2`

**Description:** Selects all matching elements in the DOM

**> Input Ports:**

- **Query** (String)
- **Mode Index** (Number: Integer)
- **Type Index** (Number: Integer)
- **Document** (String)
- **Element** (Object:Element)
- **Update** (Trigger)

**< Output Ports:**

- **Elements** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/QTs5GH)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "QuerySelectorAll_v2"*

**Docs:** [https://cables.gl/op/Ops.Html.QuerySelectorAll_v2](https://cables.gl/op/Ops.Html.QuerySelectorAll_v2)


### ReloadPage
![ReloadPage op](images/ops/Ops_Html_ReloadPage.svg)

**Full Name:** `Ops.Html.ReloadPage`

**Description:** reload the website

**> Input Ports:**

- **Exec** (Trigger)

**< Output Ports:**

- *Visit [Ops.Html.ReloadPage documentation](https://cables.gl/op/Ops.Html.ReloadPage) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/BPeCci)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ReloadPage"*

**Docs:** [https://cables.gl/op/Ops.Html.ReloadPage](https://cables.gl/op/Ops.Html.ReloadPage)


### ScrollIntoView
![ScrollIntoView op](images/ops/Ops_Html_ScrollIntoView.svg)

**Full Name:** `Ops.Html.ScrollIntoView`

**Description:** Scroll an area, so the html element is visible/in view

**> Input Ports:**

- **Element** (Object:Element)
- **Scroll Into View** (Trigger)

**< Output Ports:**

- **HTML Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/KmnVEm)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScrollIntoView"*

**Docs:** [https://cables.gl/op/Ops.Html.ScrollIntoView](https://cables.gl/op/Ops.Html.ScrollIntoView)


### ScrollPosition_v2
![ScrollPosition_v2 op](images/ops/Ops_Html_ScrollPosition_v2.svg)

**Full Name:** `Ops.Html.ScrollPosition_v2`

**Description:** the current x y top left scrolling position of html page or element

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


### ScrollTo
![ScrollTo op](images/ops/Ops_Html_ScrollTo.svg)

**Full Name:** `Ops.Html.ScrollTo`

**Description:** Trigger the browser to scroll to top or bottom of an element

**> Input Ports:**

- **Element** (Object:Element)
- **Scroll To Top** (Trigger)
- **Scroll To Bottom** (Trigger)

**< Output Ports:**

- *Visit [Ops.Html.ScrollTo documentation](https://cables.gl/op/Ops.Html.ScrollTo) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/JEThu1)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScrollTo"*

**Docs:** [https://cables.gl/op/Ops.Html.ScrollTo](https://cables.gl/op/Ops.Html.ScrollTo)


### WindowClose
![WindowClose op](images/ops/Ops_Html_WindowClose.svg)

**Full Name:** `Ops.Html.WindowClose`

**Description:** close current window

**> Input Ports:**

- **Close** (Trigger)

**< Output Ports:**

- *Visit [Ops.Html.WindowClose documentation](https://cables.gl/op/Ops.Html.WindowClose) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/WGBCci)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WindowClose"*

**Docs:** [https://cables.gl/op/Ops.Html.WindowClose](https://cables.gl/op/Ops.Html.WindowClose)


### WindowHasFocus
![WindowHasFocus op](images/ops/Ops_Html_WindowHasFocus.svg)

**Full Name:** `Ops.Html.WindowHasFocus`

**Description:** detect if the browser window/tab has focus

**> Input Ports:**

- *Visit [Ops.Html.WindowHasFocus documentation](https://cables.gl/op/Ops.Html.WindowHasFocus) for input port details*

**< Output Ports:**

- **Has Focus** (booleanNumber)
- **Tab Visible** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/uI9yOg)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WindowHasFocus"*

**Docs:** [https://cables.gl/op/Ops.Html.WindowHasFocus](https://cables.gl/op/Ops.Html.WindowHasFocus)


### WindowInfo
![WindowInfo op](images/ops/Ops_Html_WindowInfo.svg)

**Full Name:** `Ops.Html.WindowInfo`

**Description:** size of browser window in pixels

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

**Example Patch:** [Open in Editor](https://cables.gl/edit/DyHxSP)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WindowInfo"*

**Docs:** [https://cables.gl/op/Ops.Html.WindowInfo](https://cables.gl/op/Ops.Html.WindowInfo)


### WindowScroll
![WindowScroll op](images/ops/Ops_Html_WindowScroll.svg)

**Full Name:** `Ops.Html.WindowScroll`

**Description:** Get the current scroll position of the window

**> Input Ports:**

- **Update** (Trigger)

**< Output Ports:**

- **Scoll X** (Number)
- **Scoll Y** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.WindowScroll#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WindowScroll"*

**Docs:** [https://cables.gl/op/Ops.Html.WindowScroll](https://cables.gl/op/Ops.Html.WindowScroll)


