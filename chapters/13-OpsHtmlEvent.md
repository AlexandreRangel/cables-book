# Ops.Html.Event

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Html.Event

### ElementEventListener_v2
![ElementEventListener_v2 op](images/ops/Ops_Html_Event_ElementEventListener_v2.svg)

**Full Name:** `Ops.Html.Event.ElementEventListener_v2`
**Description:** Add a custom event listener

**> Input Ports:**
- **Element** (Object): *See documentation*
- **Event Name** (String): *See documentation*
- **Use Capture** (Number: Boolean): *See documentation*
- **Prevent Default** (Number: Boolean): *See documentation*
- **Stop Propagation** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Element Passthrough** (Object): *See documentation*
- **Event Trigger** (Trigger): *See documentation*
- **Event Object** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/9ixt13)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementEventListener_v2"*
**Docs:** [https://cables.gl/op/Ops.Html.Event.ElementEventListener_v2](https://cables.gl/op/Ops.Html.Event.ElementEventListener_v2)

---

### ElementPointerEvents
![ElementPointerEvents op](images/ops/Ops_Html_Event_ElementPointerEvents.svg)

**Full Name:** `Ops.Html.Event.ElementPointerEvents`
**Description:** Listen to events of an element

**> Input Ports:**
- **Dom Element** (Object): *See documentation*
- **Mouse Down Active** (Number: Boolean): *See documentation*
- **Mouse Up Active** (Number: Boolean): *See documentation*
- **Click Active** (Number: Boolean): *See documentation*
- **Mouse Move Active** (Number: Boolean): *See documentation*
- **Touch Start Active** (Number: Boolean): *See documentation*
- **Touch Move Active** (Number: Boolean): *See documentation*
- **Touch End Active** (Number: Boolean): *See documentation*
- **Touch Cancel Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Event Object** (Object): *See documentation*
- **Mouse Down** (Trigger): *See documentation*
- **Mouse Up** (Trigger): *See documentation*
- **Click** (Trigger): *See documentation*
- **Mouse Move** (Trigger): *See documentation*
- **Touch Start** (Trigger): *See documentation*
- **Touch Move** (Trigger): *See documentation*
- **Touch End** (Trigger): *See documentation*
- **Touch Cancel** (Trigger): *See documentation*
- **Event Name** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.Event.ElementPointerEvents#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementPointerEvents"*
**Docs:** [https://cables.gl/op/Ops.Html.Event.ElementPointerEvents](https://cables.gl/op/Ops.Html.Event.ElementPointerEvents)

---

### ElementsArrayEventListener
![ElementsArrayEventListener op](images/ops/Ops_Html_Event_ElementsArrayEventListener.svg)

**Full Name:** `Ops.Html.Event.ElementsArrayEventListener`
**Description:** listen to events on multiple html elements

**> Input Ports:**
- **Elements** (Array): *See documentation*
- **Event Name** (String): *See documentation*
- **Use Capture** (Number: Boolean): *See documentation*
- **Prevent Default** (Number: Boolean): *See documentation*
- **Stop Propagation** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Event Trigger** (Trigger): *See documentation*
- **Index** (Number): *See documentation*
- **Event Object** (Object): *See documentation*
- **Event Element** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/4rKHP0)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementsArrayEventListener"*
**Docs:** [https://cables.gl/op/Ops.Html.Event.ElementsArrayEventListener](https://cables.gl/op/Ops.Html.Event.ElementsArrayEventListener)

---

### PreventDefault
![PreventDefault op](images/ops/Ops_Html_Event_PreventDefault.svg)

**Full Name:** `Ops.Html.Event.PreventDefault`
**Description:** Prevents the default on a JavaScript event

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Event In** (Object): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Event Out** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.Event.PreventDefault#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PreventDefault"*
**Docs:** [https://cables.gl/op/Ops.Html.Event.PreventDefault](https://cables.gl/op/Ops.Html.Event.PreventDefault)

---

### StopPropagation
![StopPropagation op](images/ops/Ops_Html_Event_StopPropagation.svg)

**Full Name:** `Ops.Html.Event.StopPropagation`
**Description:** Stop a JavaScript event (bubbling / capturing)

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Event In** (Object): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Event Out** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.Event.StopPropagation#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StopPropagation"*
**Docs:** [https://cables.gl/op/Ops.Html.Event.StopPropagation](https://cables.gl/op/Ops.Html.Event.StopPropagation)

---

