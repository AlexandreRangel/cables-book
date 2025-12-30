# Ops.Extension.ECharts

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Extension.ECharts

### ECharts
![ECharts op](images/ops/Ops_Extension_ECharts_ECharts.svg)

**Full Name:** `Ops.Extension.ECharts.ECharts`
**Description:** wrapper for echarts-library

**> Input Ports:**
- **Create** (Trigger): *See documentation*
- **Parent DOM Element** (Object): *See documentation*
- **Id** (String): *See documentation*
- **Width** (Number: Integer): *See documentation*
- **Height** (Number: Integer): *See documentation*
- **Chart Object** (Object): *See documentation*
- **Merge Options** (Object): *See documentation*
- **Renderer Index** (Number: Integer): *See documentation*
- **Renderer** (String): *See documentation*
- **Theme Index** (Number: Integer): *See documentation*
- **Theme** (String): *See documentation*
- **Custom Theme Obj** (Object): *See documentation*
- **Init Extra Options** (Object): *See documentation*
- **Style** (Number: String): *See documentation*
- **Visible** (Number: Boolean): *See documentation*

**< Output Ports:**
- **DOM Element** (Object): *See documentation*
- **ECharts Instance** (Object): *See documentation*
- **Chart Updated** (Trigger): *See documentation*
- **Theme Changed** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/iY6lbI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ECharts"*
**Docs:** [https://cables.gl/op/Ops.Extension.ECharts.ECharts](https://cables.gl/op/Ops.Extension.ECharts.ECharts)

---

### EChartsEvent
![EChartsEvent op](images/ops/Ops_Extension_ECharts_EChartsEvent.svg)

**Full Name:** `Ops.Extension.ECharts.EChartsEvent`
**Description:** capture echart-library-events

**> Input Ports:**
- **ECharts Instance** (Object): *See documentation*
- **Event Name** (String): *See documentation*
- **Query String** (String): *See documentation*
- **Query Object** (Object): *See documentation*
- **Refresh Event Binding** (Trigger): *See documentation*

**< Output Ports:**
- **Out Chart** (Object): *See documentation*
- **Trigger** (Trigger): *See documentation*
- **Event Params** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/iY6lbI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "EChartsEvent"*
**Docs:** [https://cables.gl/op/Ops.Extension.ECharts.EChartsEvent](https://cables.gl/op/Ops.Extension.ECharts.EChartsEvent)

---

