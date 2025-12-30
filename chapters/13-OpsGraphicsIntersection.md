# Ops.Graphics.Intersection

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Graphics.Intersection

### FilterIntersections
![FilterIntersections op](images/ops/Ops_Graphics_Intersection_FilterIntersections.svg)

**Full Name:** `Ops.Graphics.Intersection.FilterIntersections`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Intersection.FilterIntersections) for details*

**> Input Ports:**
- **Collisions** (Array)
- **Name 1** (String)
- **Match Name 1 Index** (Number: Integer)
- **Name 2** (String)
- **Match Name 2 Index** (Number: Integer)

**< Output Ports:**
- **Colliding** (booleanNumber)
- **Num Collisions** (Number)
- **Result Collisions** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Intersection.FilterIntersections#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FilterIntersections"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Intersection.FilterIntersections](https://cables.gl/op/Ops.Graphics.Intersection.FilterIntersections)

---

### IntersectBody
![IntersectBody op](images/ops/Ops_Graphics_Intersection_IntersectBody.svg)

**Full Name:** `Ops.Graphics.Intersection.IntersectBody`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Intersection.IntersectBody) for details*

**> Input Ports:**
- **Trigger** (Trigger)
- **Name** (String)
- **Radius** (Number)
- **Size X** (Number)
- **Size Y** (Number)
- **Size Z** (Number)
- **Positions** (Array)
- **Append Index To Name** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Intersection.IntersectBody#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "IntersectBody"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Intersection.IntersectBody](https://cables.gl/op/Ops.Graphics.Intersection.IntersectBody)

---

### IntersectTestBody
![IntersectTestBody op](images/ops/Ops_Graphics_Intersection_IntersectTestBody.svg)

**Full Name:** `Ops.Graphics.Intersection.IntersectTestBody`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestBody) for details*

**> Input Ports:**
- **Trigger** (Trigger)
- **Name** (String)
- **Active** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)
- **Has Hit** (booleanNumber)
- **Hit Body Name** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestBody#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "IntersectTestBody"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestBody](https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestBody)

---

### IntersectTestPoint
![IntersectTestPoint op](images/ops/Ops_Graphics_Intersection_IntersectTestPoint.svg)

**Full Name:** `Ops.Graphics.Intersection.IntersectTestPoint`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestPoint) for details*

**> Input Ports:**
- **Trigger** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Active** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)
- **Has Hit** (booleanNumber)
- **Hit Body Name** (String)
- **Hit X** (Number)
- **Hit Y** (Number)
- **Hit Z** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestPoint#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "IntersectTestPoint"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestPoint](https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestPoint)

---

### IntersectTestRaycast
![IntersectTestRaycast op](images/ops/Ops_Graphics_Intersection_IntersectTestRaycast.svg)

**Full Name:** `Ops.Graphics.Intersection.IntersectTestRaycast`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestRaycast) for details*

**> Input Ports:**
- **Trigger** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **To X** (Number)
- **To Y** (Number)
- **To Z** (Number)
- **Active** (Number: Boolean)
- **Change Cursor** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)
- **Has Hit** (booleanNumber)
- **Hit Body Name** (String)
- **Hit X** (Number)
- **Hit Y** (Number)
- **Hit Z** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestRaycast#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "IntersectTestRaycast"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestRaycast](https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestRaycast)

---

### IntersectWorld
![IntersectWorld op](images/ops/Ops_Graphics_Intersection_IntersectWorld.svg)

**Full Name:** `Ops.Graphics.Intersection.IntersectWorld`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Graphics.Intersection.IntersectWorld) for details*

**> Input Ports:**
- **Trigger** (Trigger)
- **Check Body Collisions** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)
- **Total Bodies** (Number)
- **Collisions** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Intersection.IntersectWorld#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "IntersectWorld"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Intersection.IntersectWorld](https://cables.gl/op/Ops.Graphics.Intersection.IntersectWorld)

---

