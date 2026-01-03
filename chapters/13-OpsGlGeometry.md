# Ops.Gl.Geometry

---

## Ops.Gl.Geometry

### BoundingBoxVisible
![BoundingBoxVisible op](images/ops/Ops_Gl_Geometry_BoundingBoxVisible.svg)

**Full Name:** `Ops.Gl.Geometry.BoundingBoxVisible`

**Description:** Test if a boundingbox could be visible in the current viewport

**> Input Ports:**

- **Exec** (Trigger)
- **Boundings** (Object)
- **Active** (Number: Boolean)
- **Draw** (Number: Boolean)
- **Width** (Number)
- **Height** (Number)
- **Length** (Number)

**< Output Ports:**

- **Next** (Trigger)
- **Visible** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/DAhGve)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BoundingBoxVisible"*

**Docs:** [https://cables.gl/op/Ops.Gl.Geometry.BoundingBoxVisible](https://cables.gl/op/Ops.Gl.Geometry.BoundingBoxVisible)


### GeometryBoundingBox
![GeometryBoundingBox op](images/ops/Ops_Gl_Geometry_GeometryBoundingBox.svg)

**Full Name:** `Ops.Gl.Geometry.GeometryBoundingBox`

**Description:** Calculate a bounding box from a geometry

**> Input Ports:**

- **Geometry** (Object)

**< Output Ports:**

- **Boundings** (Object)
- **Min X** (Number)
- **Min Y** (Number)
- **Min Z** (Number)
- **Max X** (Number)
- **Max Y** (Number)
- **Max Z** (Number)
- **MaxMin Points** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/DAhGve)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryBoundingBox"*

**Docs:** [https://cables.gl/op/Ops.Gl.Geometry.GeometryBoundingBox](https://cables.gl/op/Ops.Gl.Geometry.GeometryBoundingBox)


