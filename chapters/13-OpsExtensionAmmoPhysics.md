# Ops.Extension.AmmoPhysics

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Extension.AmmoPhysics

### AmmoBody
![AmmoBody op](images/ops/Ops_Extension_AmmoPhysics_AmmoBody.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.AmmoBody`
**Description:** Create a physics body/collision shape using a any geometry or select a shape

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Name** (String): *See documentation*
- **Mass** (Number): *See documentation*
- **Friction** (Number): *See documentation*
- **Rolling Friction** (Number): *See documentation*
- **Restitution** (Number): *See documentation*
- **Shape Index** (Number: Integer): *See documentation*
- **Geometry** (Object:Geometry): *See documentation*
- **Simplify Max Triangles** (Number: Integer): *See documentation*
- **Radius** (Number): *See documentation*
- **Size X** (Number): *See documentation*
- **Size Y** (Number): *See documentation*
- **Size Z** (Number): *See documentation*
- **Positions** (Array): *See documentation*
- **Append Index To Name** (Number: Boolean): *See documentation*
- **Never Deactivate** (Number: Boolean): *See documentation*
- **Ghost Object** (Number: Boolean): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Reset** (Trigger): *See documentation*
- **Activate** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Ray Hit** (booleanNumber): *See documentation*
- **Transformed** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/S_jPZ4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AmmoBody"*
**Docs:** [https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoBody](https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoBody)

---

### AmmoBodyCollision
![AmmoBodyCollision op](images/ops/Ops_Extension_AmmoPhysics_AmmoBodyCollision.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.AmmoBodyCollision`
**Description:** Check if physics bodies are colliding

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Name 1** (String): *See documentation*
- **Match Name 1 Index** (Number: Integer): *See documentation*
- **Name 2** (String): *See documentation*
- **name of physics object** (optional): *See documentation*
- **Match Name 2 Index** (Number: Integer): *See documentation*
- **match name 2** (if set): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Colliding** (Number): *See documentation*
- **collision detected** (Boolean): *See documentation*
- **Num Collisions** (Number): *See documentation*
- **Collisions** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/S_jPZ4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AmmoBodyCollision"*
**Docs:** [https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoBodyCollision](https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoBodyCollision)

---

### AmmoCharacter
![AmmoCharacter op](images/ops/Ops_Extension_AmmoPhysics_AmmoCharacter.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.AmmoCharacter`
**Description:** Control and move a character in a physics environment

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Radius** (Number): *See documentation*
- **View Index** (Number: Integer): *See documentation*
- **Height** (Number): *See documentation*
- **Mass** (Number): *See documentation*
- **Name** (String): *See documentation*
- **Activate** (Trigger): *See documentation*
- **Move X-** (Number: Boolean): *See documentation*
- **Move Y-** (Number: Boolean): *See documentation*
- **Move Z-** (Number: Boolean): *See documentation*
- **Dir X** (Number): *See documentation*
- **X axis rotation value** (from AmmoCharacterFpsCamera for example): *See documentation*
- **Dir Y** (Number): *See documentation*
- **Y axis ratation value** (from AmmoCharacterFpsCamera for example): *See documentation*
- **Dir Z** (Number): *See documentation*
- **Z axis rotation value** (from AmmoCharacterFpsCamera for example): *See documentation*
- **Set Pos X** (Number): *See documentation*
- **Set Pos Y** (Number): *See documentation*
- **Set Pos Z** (Number): *See documentation*
- **Reset** (Trigger): *See documentation*
- **Speed** (Number): *See documentation*
- **Add Velocity Y** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Position X** (Number): *See documentation*
- **Position Y** (Number): *See documentation*
- **Position Z** (Number): *See documentation*
- **Transformed** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/psyNZ4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AmmoCharacter"*
**Docs:** [https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoCharacter](https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoCharacter)

---

### AmmoCharacterFpsCamera
![AmmoCharacterFpsCamera op](images/ops/Ops_Extension_AmmoPhysics_AmmoCharacterFpsCamera.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.AmmoCharacterFpsCamera`
**Description:** First person camera to use with AmmoCharacter

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Enable Pointer Lock** (Number: Boolean): *See documentation*
- **Height** (Number): *See documentation*
- **Character Name** (String): *See documentation*
- **Mouse Speed** (Number): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **IsLocked** (Number): *See documentation*
- **has the mouse cursor been locked** (Boolean): *See documentation*
- **Mouse Left** (Trigger): *See documentation*
- **Mouse Right** (Trigger): *See documentation*
- **Dir X** (Number): *See documentation*
- **Dir Y** (Number): *See documentation*
- **Dir Z** (Number): *See documentation*
- **Rot X** (Number): *See documentation*
- **Rot Y** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/psyNZ4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AmmoCharacterFpsCamera"*
**Docs:** [https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoCharacterFpsCamera](https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoCharacterFpsCamera)

---

### AmmoDebugRenderer
![AmmoDebugRenderer op](images/ops/Ops_Extension_AmmoPhysics_AmmoDebugRenderer.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.AmmoDebugRenderer`
**Description:** Visualize the physical bodies as lines and points

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Draw Wireframe** (Number: Boolean): *See documentation*
- **Draw AABB** (Number: Boolean): *See documentation*
- **Draw Contact Points** (Number: Boolean): *See documentation*
- **Draw Constraints** (Number: Boolean): *See documentation*
- **Depth** (Number: Boolean): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/psyNZ4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AmmoDebugRenderer"*
**Docs:** [https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoDebugRenderer](https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoDebugRenderer)

---

### AmmoEmitter
![AmmoEmitter op](images/ops/Ops_Extension_AmmoPhysics_AmmoEmitter.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.AmmoEmitter`
**Description:** Emit Ammo physics bodies by triggering

**> Input Ports:**
- **Exec** (Trigger): *See documentation*
- **Limit Bodies** (Number: Integer): *See documentation*
- **Radius** (Number): *See documentation*
- **Mass** (Number): *See documentation*
- **Add Index To Name** (Number: Boolean): *See documentation*
- **Name** (String): *See documentation*
- **Friction** (Number): *See documentation*
- **Rolling Friction** (Number): *See documentation*
- **Restitution** (Number): *See documentation*
- **Dir X** (Number): *See documentation*
- **Dir Y** (Number): *See documentation*
- **Dir Z** (Number): *See documentation*
- **Speed** (Number): *See documentation*
- **Spawn One** (Trigger): *See documentation*
- **Remove All** (Trigger): *See documentation*
- **Activate All** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Total Bodies** (Number): *See documentation*
- **Positions** (Array): *See documentation*
- **Rotations Quats** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/5hQROe)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AmmoEmitter"*
**Docs:** [https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoEmitter](https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoEmitter)

---

### AmmoRaycast
![AmmoRaycast op](images/ops/Ops_Extension_AmmoPhysics_AmmoRaycast.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.AmmoRaycast`
**Description:** Cast a ray and detect colliding bodies

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Screen X** (Number): *See documentation*
- **Normalize screencoordinates on X Axis** (0-1): *See documentation*
- **Screen Y** (Number): *See documentation*
- **Normalize screencoordinates on Y Axis** (0-1): *See documentation*
- **Ray Points** (Array): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Change Cursor** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Has Hit** (booleanNumber): *See documentation*
- **Hit Body Name** (String): *See documentation*
- **Hit X** (Number): *See documentation*
- **Hit Y** (Number): *See documentation*
- **Hit Z** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Gh2f_4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AmmoRaycast"*
**Docs:** [https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoRaycast](https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoRaycast)

---

### AmmoWorld
![AmmoWorld op](images/ops/Ops_Extension_AmmoPhysics_AmmoWorld.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.AmmoWorld`
**Description:** Simulate physical world

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Simulate** (Number: Boolean): *See documentation*
- **Auto Remove Inactive** (Number: Boolean): *See documentation*
- **Gravity X** (Number): *See documentation*
- **Gravity Y** (Number): *See documentation*
- **Gravity Z** (Number): *See documentation*
- **Activate All** (Trigger): *See documentation*
- **Reset** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Total Bodies** (Number): *See documentation*
- **Debug Points** (Array): *See documentation*
- **Bodies Meta** (Array): *See documentation*
- **Collisions** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/psyNZ4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AmmoWorld"*
**Docs:** [https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoWorld](https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoWorld)

---

### GltfAmmoBodies
![GltfAmmoBodies op](images/ops/Ops_Extension_AmmoPhysics_GltfAmmoBodies.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.GltfAmmoBodies`
**Description:** Create physics bodies from a GLTF File

**> Input Ports:**
- **Exec** (Trigger): *See documentation*
- **Shape Index** (Number: Integer): *See documentation*
- **Filter Meshes** (String): *See documentation*
- **Mass Kg** (Number): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Meshes** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Gh2f_4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfAmmoBodies"*
**Docs:** [https://cables.gl/op/Ops.Extension.AmmoPhysics.GltfAmmoBodies](https://cables.gl/op/Ops.Extension.AmmoPhysics.GltfAmmoBodies)

---

