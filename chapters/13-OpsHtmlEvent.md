# Ops.Html.Event

---

## Ops.Html.Event

### ElementEventListener_v2
![ElementEventListener_v2 op](images/ops/Ops_Html_Event_ElementEventListener_v2.svg)

**Full Name:** `Ops.Html.Event.ElementEventListener_v2`

**Description:** Add a custom event listener

**> Input Ports:**

- **Element** (Object)
- **Event Name** (String)
- **Use Capture** (Number: Boolean)
- **Prevent Default** (Number: Boolean)
- **Stop Propagation** (Number: Boolean)

**< Output Ports:**

- **Element Passthrough** (Object)
- **Event Trigger** (Trigger)
- **Event Object** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/9ixt13)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementEventListener_v2"*

**Docs:** [https://cables.gl/op/Ops.Html.Event.ElementEventListener_v2](https://cables.gl/op/Ops.Html.Event.ElementEventListener_v2)


### ElementPointerEvents
![ElementPointerEvents op](images/ops/Ops_Html_Event_ElementPointerEvents.svg)

**Full Name:** `Ops.Html.Event.ElementPointerEvents`

**Description:** Listen to events of an element

**> Input Ports:**

- **Dom Element** (Object)
- **Mouse Down Active** (Number: Boolean)
- **Mouse Up Active** (Number: Boolean)
- **Click Active** (Number: Boolean)
- **Mouse Move Active** (Number: Boolean)
- **Touch Start Active** (Number: Boolean)
- **Touch Move Active** (Number: Boolean)
- **Touch End Active** (Number: Boolean)
- **Touch Cancel Active** (Number: Boolean)

**< Output Ports:**

- **Event Object** (Object)
- **Mouse Down** (Trigger)
- **Mouse Up** (Trigger)
- **Click** (Trigger)
- **Mouse Move** (Trigger)
- **Touch Start** (Trigger)
- **Touch Move** (Trigger)
- **Touch End** (Trigger)
- **Touch Cancel** (Trigger)
- **Event Name** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.Event.ElementPointerEvents#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementPointerEvents"*

**Docs:** [https://cables.gl/op/Ops.Html.Event.ElementPointerEvents](https://cables.gl/op/Ops.Html.Event.ElementPointerEvents)


### ElementsArrayEventListener
![ElementsArrayEventListener op](images/ops/Ops_Html_Event_ElementsArrayEventListener.svg)

**Full Name:** `Ops.Html.Event.ElementsArrayEventListener`

**Description:** listen to events on multiple html elements

**> Input Ports:**

- **Elements** (Array)
- **Event Name** (String)
- **Use Capture** (Number: Boolean)
- **Prevent Default** (Number: Boolean)
- **Stop Propagation** (Number: Boolean)

**< Output Ports:**

- **Event Trigger** (Trigger)
- **Index** (Number)
- **Event Object** (Object)
- **Event Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/4rKHP0)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ElementsArrayEventListener"*

**Docs:** [https://cables.gl/op/Ops.Html.Event.ElementsArrayEventListener](https://cables.gl/op/Ops.Html.Event.ElementsArrayEventListener)


### PreventDefault
![PreventDefault op](images/ops/Ops_Html_Event_PreventDefault.svg)

**Full Name:** `Ops.Html.Event.PreventDefault`

**Description:** Prevents the default on a JavaScript event

**> Input Ports:**

- **Execute** (Trigger)
- **Event In** (Object)

**< Output Ports:**

- **Next** (Trigger)
- **Event Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.Event.PreventDefault#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PreventDefault"*

**Docs:** [https://cables.gl/op/Ops.Html.Event.PreventDefault](https://cables.gl/op/Ops.Html.Event.PreventDefault)


### StopPropagation
![StopPropagation op](images/ops/Ops_Html_Event_StopPropagation.svg)

**Full Name:** `Ops.Html.Event.StopPropagation`

**Description:** Stop a JavaScript event (bubbling / capturing)

**> Input Ports:**

- **Execute** (Trigger)
- **Event In** (Object)

**< Output Ports:**

- **Next** (Trigger)
- **Event Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.Event.StopPropagation#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StopPropagation"*

**Docs:** [https://cables.gl/op/Ops.Html.Event.StopPropagation](https://cables.gl/op/Ops.Html.Event.StopPropagation)


