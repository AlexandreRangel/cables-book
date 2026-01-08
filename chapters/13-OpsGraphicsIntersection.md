# Ops.Graphics.Intersection


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### FilterIntersections
![FilterIntersections op](images/ops/Ops_Graphics_Intersection_FilterIntersections.svg)

**Full Name:** `Ops.Graphics.Intersection.FilterIntersections`

Define filters to get colliding and intersecting bodies.

**`\inputsymbol`{=latex} Inputs**

- **Collisions** (Array)
- **Name 1** (String)
- **Match Name 1 Index** (Number: Integer)
- **Name 2** (String)
- **Match Name 2 Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Colliding** (booleanNumber)
- **Num Collisions** (Number)
- **Result Collisions** (Array)

**Example Patch:** [cables.gl/op/Ops.Graphics.Intersection.FilterIntersections#example](https://cables.gl/op/Ops.Graphics.Intersection.FilterIntersections#example)

**Doc:** [cables.gl/op/Ops.Graphics.Intersection.FilterIntersections](https://cables.gl/op/Ops.Graphics.Intersection.FilterIntersections)

### IntersectBody
![IntersectBody op](images/ops/Ops_Graphics_Intersection_IntersectBody.svg)

**Full Name:** `Ops.Graphics.Intersection.IntersectBody`

Add Bodies and check if they intersect/collide with each other.

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Name** (String)
- **Radius** (Number)
- **Size X** (Number)
- **Size Y** (Number)
- **Size Z** (Number)
- **Positions** (Array)
- **Append Index To Name** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/ffRjjz](https://cables.gl/edit/ffRjjz)

**Doc:** [cables.gl/op/Ops.Graphics.Intersection.IntersectBody](https://cables.gl/op/Ops.Graphics.Intersection.IntersectBody)

### IntersectTestBody
![IntersectTestBody op](images/ops/Ops_Graphics_Intersection_IntersectTestBody.svg)

**Full Name:** `Ops.Graphics.Intersection.IntersectTestBody`

test one body against all bodies in the world.

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Name** (String)
- **Active** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Has Hit** (booleanNumber)
- **Hit Body Name** (String)

**Example Patch:** [cables.gl/edit/bg73Qc](https://cables.gl/edit/bg73Qc)

**Doc:** [cables.gl/op/Ops.Graphics.Intersection.IntersectTestBody](https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestBody)

### IntersectTestPoint
![IntersectTestPoint op](images/ops/Ops_Graphics_Intersection_IntersectTestPoint.svg)

**Full Name:** `Ops.Graphics.Intersection.IntersectTestPoint`

test intersect bodies collision against a point/coordinate.

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Active** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Has Hit** (booleanNumber)
- **Hit Body Name** (String)
- **Hit X** (Number)
- **Hit Y** (Number)
- **Hit Z** (Number)

**Example Patch:** [cables.gl/edit/c2DAO8](https://cables.gl/edit/c2DAO8)

**Doc:** [cables.gl/op/Ops.Graphics.Intersection.IntersectTestPoint](https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestPoint)

### IntersectTestRaycast
![IntersectTestRaycast op](images/ops/Ops_Graphics_Intersection_IntersectTestRaycast.svg)

**Full Name:** `Ops.Graphics.Intersection.IntersectTestRaycast`

Cast a ray and check if it intersect/collide with bodies.

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **To X** (Number)
- **To Y** (Number)
- **To Z** (Number)
- **Active** (Number: Boolean)
- **Change Cursor** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Has Hit** (booleanNumber)
- **Hit Body Name** (String)
- **Hit X** (Number)
- **Hit Y** (Number)
- **Hit Z** (Number)

**Example Patch:** [cables.gl/edit/ffRjjz](https://cables.gl/edit/ffRjjz)

**Doc:** [cables.gl/op/Ops.Graphics.Intersection.IntersectTestRaycast](https://cables.gl/op/Ops.Graphics.Intersection.IntersectTestRaycast)

### IntersectWorld
![IntersectWorld op](images/ops/Ops_Graphics_Intersection_IntersectWorld.svg)

**Full Name:** `Ops.Graphics.Intersection.IntersectWorld`

Define a world to check for intersections and collisions.

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Check Body Collisions** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Total Bodies** (Number)
- **Collisions** (Array)

**Example Patch:** [cables.gl/edit/ffRjjz](https://cables.gl/edit/ffRjjz)

**Doc:** [cables.gl/op/Ops.Graphics.Intersection.IntersectWorld](https://cables.gl/op/Ops.Graphics.Intersection.IntersectWorld)


