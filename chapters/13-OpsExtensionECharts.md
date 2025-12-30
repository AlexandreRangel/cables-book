# Ops.Extension.ECharts

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Extension.ECharts

### ECharts
![ECharts op](images/ops/Ops_Extension_ECharts_ECharts.svg)

**Full Name:** `Ops.Extension.ECharts.ECharts`
**Description:** wrapper for echarts-library

**> Input Ports:**
- **Create** (Trigger)
- **Parent DOM Element** (Object)
- **Id** (String)
- **Width** (Number: Integer)
- **Height** (Number: Integer)
- **Chart Object** (Object)
- **Merge Options** (Object)
- **Renderer Index** (Number: Integer)
- **Renderer** (String)
- **Theme Index** (Number: Integer)
- **Theme** (String)
- **Custom Theme Obj** (Object)
- **Init Extra Options** (Object)
- **Style** (Number: String)
- **Visible** (Number: Boolean)

**< Output Ports:**
- **DOM Element** (Object)
- **ECharts Instance** (Object)
- **Chart Updated** (Trigger)
- **Theme Changed** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/iY6lbI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ECharts"*
**Docs:** [https://cables.gl/op/Ops.Extension.ECharts.ECharts](https://cables.gl/op/Ops.Extension.ECharts.ECharts)

---

### EChartsEvent
![EChartsEvent op](images/ops/Ops_Extension_ECharts_EChartsEvent.svg)

**Full Name:** `Ops.Extension.ECharts.EChartsEvent`
**Description:** capture echart-library-events

**> Input Ports:**
- **ECharts Instance** (Object)
- **Event Name** (String)
- **Query String** (String)
- **Query Object** (Object)
- **Refresh Event Binding** (Trigger)

**< Output Ports:**
- **Out Chart** (Object)
- **Trigger** (Trigger)
- **Event Params** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/iY6lbI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "EChartsEvent"*
**Docs:** [https://cables.gl/op/Ops.Extension.ECharts.EChartsEvent](https://cables.gl/op/Ops.Extension.ECharts.EChartsEvent)

---

