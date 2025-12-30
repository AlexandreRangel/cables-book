# Ops.Extension.HtmlElementArray

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Extension.HtmlElementArray

### DivElements
![DivElements op](images/ops/Ops_Extension_HtmlElementArray_DivElements.svg)

**Full Name:** `Ops.Extension.HtmlElementArray.DivElements`
**Description:** create an array of div elements

**> Input Ports:**
- **Class** (String)
- **Parent** (Object:Element)
- **Num** (Number: Integer)
- **Active** (Number: Boolean)
- **Text** (Array)
- **Reset Hover** (Trigger)

**< Output Ports:**
- **Elements** (Array)
- **Index Clicked** (Number)
- **Element Clicked** (Trigger)
- **Pointer Up** (Trigger)
- **Index Hovered** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/lYLMwk)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DivElements"*
**Docs:** [https://cables.gl/op/Ops.Extension.HtmlElementArray.DivElements](https://cables.gl/op/Ops.Extension.HtmlElementArray.DivElements)

---

### ElementArrayCssPropertyNumber
![ElementArrayCssPropertyNumber op](images/ops/Ops_Extension_HtmlElementArray_ElementArrayCssPropertyNumber.svg)

**Full Name:** `Ops.Extension.HtmlElementArray.ElementArrayCssPropertyNumber`
**Description:** Set css style properties of a html element

**> Input Ports:**
- **Element** (Object)
- **Update** (Trigger)
- **Property** (String)
- **Value** (Number)
- **Value Suffix** (String)

**< Output Ports:**
- **HTML Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.HtmlElementArray.ElementArrayCssPropertyNumber#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementArrayCssPropertyNumber"*
**Docs:** [https://cables.gl/op/Ops.Extension.HtmlElementArray.ElementArrayCssPropertyNumber](https://cables.gl/op/Ops.Extension.HtmlElementArray.ElementArrayCssPropertyNumber)

---

### ElementArrayCssPropertyString
![ElementArrayCssPropertyString op](images/ops/Ops_Extension_HtmlElementArray_ElementArrayCssPropertyString.svg)

**Full Name:** `Ops.Extension.HtmlElementArray.ElementArrayCssPropertyString`
**Description:** set css properties

**> Input Ports:**
- **Element** (Object)
- **Update** (Trigger)
- **Property** (String)
- **Value** (String)
- **Value Suffix** (String)

**< Output Ports:**
- **HTML Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.HtmlElementArray.ElementArrayCssPropertyString#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementArrayCssPropertyString"*
**Docs:** [https://cables.gl/op/Ops.Extension.HtmlElementArray.ElementArrayCssPropertyString](https://cables.gl/op/Ops.Extension.HtmlElementArray.ElementArrayCssPropertyString)

---

