# Ops.Graphics.Intersection

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Graphics.Intersection

### FilterIntersections
![FilterIntersections op](images/ops/Ops_Graphics_Intersection_FilterIntersections.svg)

**Full Name:** `Ops.Graphics.Intersection.FilterIntersections`
**Description:** Define filters to get colliding and intersecting bodies

**> Input Ports:**
- **Collisions** (Array): *See documentation*
- **Name 1** (String): *See documentation*
- **Match Name 1 Index** (Number: Integer): *See documentation*
- **Name 2** (String): *See documentation*
- **Match Name 2 Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Colliding** (booleanNumber): *See documentation*
- **Num Collisions** (Number): *See documentation*
- **Result Collisions** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Graphics.Intersection.FilterIntersections#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FilterIntersections"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Intersection.FilterIntersections](https://cables.gl/op/Ops.Graphics.Intersection.FilterIntersections)

---

### IntersectBody
![IntersectBody op](images/ops/Ops_Graphics_Intersection_IntersectBody.svg)

**Full Name:** `Ops.Graphics.Intersection.IntersectBody`
**Description:** Add Bodies and check if they intersect/collide with each other

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **Name** (String): *See documentation*
- **Radius** (Number): *See documentation*
- **Size X** (Number): *See documentation*
- **Size Y** (Number): *See documentation*
- **Size Z** (Number): *See documentation*
- **Positions** (Array): *See documentation*
- **Append Index To Name** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ffRjjz)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "IntersectBody"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Intersection.IntersectBody](https://cables.gl/op/Ops.Graphics.Intersection.IntersectBody)

---

### IntersectTestBody
![IntersectTestBody op](images/ops/Ops_Graphics_Intersection_IntersectTestBody.svg)

**Full Name:** `Ops.Graphics.Intersection.IntersectTestBody`
**Description:** test one body against all bodies in the world

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **Name** (String): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Has Hit** (booleanNumber): *See documentation*
- **Hit Body Name** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/bg73Qc)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "IntersectTestBody"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestBody](https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestBody)

---

### IntersectTestPoint
![IntersectTestPoint op](images/ops/Ops_Graphics_Intersection_IntersectTestPoint.svg)

**Full Name:** `Ops.Graphics.Intersection.IntersectTestPoint`
**Description:** test intersect bodies collision against a point/coordinate

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Has Hit** (booleanNumber): *See documentation*
- **Hit Body Name** (String): *See documentation*
- **Hit X** (Number): *See documentation*
- **Hit Y** (Number): *See documentation*
- **Hit Z** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/c2DAO8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "IntersectTestPoint"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestPoint](https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestPoint)

---

### IntersectTestRaycast
![IntersectTestRaycast op](images/ops/Ops_Graphics_Intersection_IntersectTestRaycast.svg)

**Full Name:** `Ops.Graphics.Intersection.IntersectTestRaycast`
**Description:** Cast a ray and check if it intersect/collide with bodies

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **To X** (Number): *See documentation*
- **To Y** (Number): *See documentation*
- **To Z** (Number): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Change Cursor** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Has Hit** (booleanNumber): *See documentation*
- **Hit Body Name** (String): *See documentation*
- **Hit X** (Number): *See documentation*
- **Hit Y** (Number): *See documentation*
- **Hit Z** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ffRjjz)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "IntersectTestRaycast"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestRaycast](https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestRaycast)

---

### IntersectWorld
![IntersectWorld op](images/ops/Ops_Graphics_Intersection_IntersectWorld.svg)

**Full Name:** `Ops.Graphics.Intersection.IntersectWorld`
**Description:** Define a world to check for intersections and collisions

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **Check Body Collisions** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Total Bodies** (Number): *See documentation*
- **Collisions** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ffRjjz)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "IntersectWorld"*
**Docs:** [https://cables.gl/op/Ops.Graphics.Intersection.IntersectWorld](https://cables.gl/op/Ops.Graphics.Intersection.IntersectWorld)

---

