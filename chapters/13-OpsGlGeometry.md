# Ops.Gl.Geometry

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.Geometry

### BoundingBoxVisible
![BoundingBoxVisible op](images/ops/Ops_Gl_Geometry_BoundingBoxVisible.svg)

**Full Name:** `Ops.Gl.Geometry.BoundingBoxVisible`
**Description:** Test if a boundingbox could be visible in the current viewport

**> Input Ports:**
- **Exec** (Trigger): *See documentation*
- **Boundings** (Object): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Draw** (Number: Boolean): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Length** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Visible** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/DAhGve)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BoundingBoxVisible"*
**Docs:** [https://cables.gl/op/Ops.Gl.Geometry.BoundingBoxVisible](https://cables.gl/op/Ops.Gl.Geometry.BoundingBoxVisible)

---

### GeometryBoundingBox
![GeometryBoundingBox op](images/ops/Ops_Gl_Geometry_GeometryBoundingBox.svg)

**Full Name:** `Ops.Gl.Geometry.GeometryBoundingBox`
**Description:** Calculate a bounding box from a geometry

**> Input Ports:**
- **Geometry** (Object): *See documentation*

**< Output Ports:**
- **Boundings** (Object): *See documentation*
- **Min X** (Number): *See documentation*
- **Min Y** (Number): *See documentation*
- **Min Z** (Number): *See documentation*
- **Max X** (Number): *See documentation*
- **Max Y** (Number): *See documentation*
- **Max Z** (Number): *See documentation*
- **MaxMin Points** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/DAhGve)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeometryBoundingBox"*
**Docs:** [https://cables.gl/op/Ops.Gl.Geometry.GeometryBoundingBox](https://cables.gl/op/Ops.Gl.Geometry.GeometryBoundingBox)

---

