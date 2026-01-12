# Ops.Extension.AmmoPhysics


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### AmmoBody
![AmmoBody op](images/ops/Ops_Extension_AmmoPhysics_AmmoBody.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.AmmoBody`

Create a physics body/collision shape using a any geometry or select a shape.

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **Name** (String)
- **Mass** (Number)
- **Friction** (Number)
- **Rolling Friction** (Number)
- **Restitution** (Number)
- **Shape Index** (Number: Integer)
- **Geometry** (Object:Geometry)
- **Simplify Max Triangles** (Number: Integer)
- **Radius** (Number)
- **Size X** (Number)
- **Size Y** (Number)
- **Size Z** (Number)
- **Positions** (Array)
- **Append Index To Name** (Number: Boolean)
- **Never Deactivate** (Number: Boolean)
- **Ghost Object** (Number: Boolean)
- **Active** (Number: Boolean)
- **Reset** (Trigger)
- **Activate** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Ray Hit** (booleanNumber)
- **Transformed** (Trigger)

**Example:** [cables.gl/edit/S_jPZ4](https://cables.gl/edit/S_jPZ4)

**Doc:** [cables.gl/op/Ops.Extension.AmmoPhysics.AmmoBody](https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoBody)

### AmmoBodyCollision
![AmmoBodyCollision op](images/ops/Ops_Extension_AmmoPhysics_AmmoBodyCollision.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.AmmoBodyCollision`

Check if physics bodies are colliding.

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **Name 1** (String)
- **Match Name 1 Index** (Number: Integer)
- **Name 2** (String)
- **name of physics object** (optional)
- **Match Name 2 Index** (Number: Integer)
- **match name 2** (if set)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Colliding** (Number)
- **collision detected** (Boolean)
- **Num Collisions** (Number)
- **Collisions** (Array)

**Example:** [cables.gl/edit/S_jPZ4](https://cables.gl/edit/S_jPZ4)

**Doc:** [cables.gl/op/Ops.Extension.AmmoPhysics.AmmoBodyCollision](https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoBodyCollision)

### AmmoCharacter
![AmmoCharacter op](images/ops/Ops_Extension_AmmoPhysics_AmmoCharacter.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.AmmoCharacter`

Control and move a character in a physics environment.

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **Radius** (Number)
- **View Index** (Number: Integer)
- **Height** (Number)
- **Mass** (Number)
- **Name** (String)
- **Activate** (Trigger)
- **Move X-** (Number: Boolean)
- **Move Y-** (Number: Boolean)
- **Move Z-** (Number: Boolean)
- **Dir X** (Number)
- **X axis rotation value** (from AmmoCharacterFpsCamera for example)
- **Dir Y** (Number)
- **Y axis ratation value** (from AmmoCharacterFpsCamera for example)
- **Dir Z** (Number)
- **Z axis rotation value** (from AmmoCharacterFpsCamera for example)
- **Set Pos X** (Number)
- **Set Pos Y** (Number)
- **Set Pos Z** (Number)
- **Reset** (Trigger)
- **Speed** (Number)
- **Add Velocity Y** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Position X** (Number)
- **Position Y** (Number)
- **Position Z** (Number)
- **Transformed** (Trigger)

**Example:** [cables.gl/edit/psyNZ4](https://cables.gl/edit/psyNZ4)

**Doc:** [cables.gl/op/Ops.Extension.AmmoPhysics.AmmoCharacter](https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoCharacter)

### AmmoCharacterFpsCamera
![AmmoCharacterFpsCamera op](images/ops/Ops_Extension_AmmoPhysics_AmmoCharacterFpsCamera.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.AmmoCharacterFpsCamera`

First person camera to use with AmmoCharacter.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Enable Pointer Lock** (Number: Boolean)
- **Height** (Number)
- **Character Name** (String)
- **Mouse Speed** (Number)
- **Active** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)
- **IsLocked** (Number)
- **has the mouse cursor been locked** (Boolean)
- **Mouse Left** (Trigger)
- **Mouse Right** (Trigger)
- **Dir X** (Number)
- **Dir Y** (Number)
- **Dir Z** (Number)
- **Rot X** (Number)
- **Rot Y** (Number)

**Example:** [cables.gl/edit/psyNZ4](https://cables.gl/edit/psyNZ4)

**Doc:** [cables.gl/op/Ops.Extension.AmmoPhysics.AmmoCharacterFpsCamera](https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoCharacterFpsCamera)

### AmmoDebugRenderer
![AmmoDebugRenderer op](images/ops/Ops_Extension_AmmoPhysics_AmmoDebugRenderer.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.AmmoDebugRenderer`

Visualize the physical bodies as lines and points.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Draw Wireframe** (Number: Boolean)
- **Draw AABB** (Number: Boolean)
- **Draw Contact Points** (Number: Boolean)
- **Draw Constraints** (Number: Boolean)
- **Depth** (Number: Boolean)
- **Active** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example:** [cables.gl/edit/psyNZ4](https://cables.gl/edit/psyNZ4)

**Doc:** [cables.gl/op/Ops.Extension.AmmoPhysics.AmmoDebugRenderer](https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoDebugRenderer)

### AmmoEmitter
![AmmoEmitter op](images/ops/Ops_Extension_AmmoPhysics_AmmoEmitter.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.AmmoEmitter`

Emit Ammo physics bodies by triggering.

**`\inputsymbol`{=latex} Inputs**

- **Exec** (Trigger)
- **Limit Bodies** (Number: Integer)
- **Radius** (Number)
- **Mass** (Number)
- **Add Index To Name** (Number: Boolean)
- **Name** (String)
- **Friction** (Number)
- **Rolling Friction** (Number)
- **Restitution** (Number)
- **Dir X** (Number)
- **Dir Y** (Number)
- **Dir Z** (Number)
- **Speed** (Number)
- **Spawn One** (Trigger)
- **Remove All** (Trigger)
- **Activate All** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Total Bodies** (Number)
- **Positions** (Array)
- **Rotations Quats** (Array)

**Example:** [cables.gl/edit/5hQROe](https://cables.gl/edit/5hQROe)

**Doc:** [cables.gl/op/Ops.Extension.AmmoPhysics.AmmoEmitter](https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoEmitter)

### AmmoRaycast
![AmmoRaycast op](images/ops/Ops_Extension_AmmoPhysics_AmmoRaycast.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.AmmoRaycast`

Cast a ray and detect colliding bodies.

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **Screen X** (Number)
- **Normalize screencoordinates on X Axis** (0-1)
- **Screen Y** (Number)
- **Normalize screencoordinates on Y Axis** (0-1)
- **Ray Points** (Array)
- **Active** (Number: Boolean)
- **Change Cursor** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Has Hit** (booleanNumber)
- **Hit Body Name** (String)
- **Hit X** (Number)
- **Hit Y** (Number)
- **Hit Z** (Number)

**Example:** [cables.gl/edit/Gh2f_4](https://cables.gl/edit/Gh2f_4)

**Doc:** [cables.gl/op/Ops.Extension.AmmoPhysics.AmmoRaycast](https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoRaycast)

### AmmoWorld
![AmmoWorld op](images/ops/Ops_Extension_AmmoPhysics_AmmoWorld.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.AmmoWorld`

Simulate physical world.

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **Simulate** (Number: Boolean)
- **Auto Remove Inactive** (Number: Boolean)
- **Gravity X** (Number)
- **Gravity Y** (Number)
- **Gravity Z** (Number)
- **Activate All** (Trigger)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Total Bodies** (Number)
- **Debug Points** (Array)
- **Bodies Meta** (Array)
- **Collisions** (Array)

**Example:** [cables.gl/edit/psyNZ4](https://cables.gl/edit/psyNZ4)

**Doc:** [cables.gl/op/Ops.Extension.AmmoPhysics.AmmoWorld](https://cables.gl/op/Ops.Extension.AmmoPhysics.AmmoWorld)

### GltfAmmoBodies
![GltfAmmoBodies op](images/ops/Ops_Extension_AmmoPhysics_GltfAmmoBodies.svg)

**Full Name:** `Ops.Extension.AmmoPhysics.GltfAmmoBodies`

Create physics bodies from a GLTF File.

**`\inputsymbol`{=latex} Inputs**

- **Exec** (Trigger)
- **Shape Index** (Number: Integer)
- **Filter Meshes** (String)
- **Mass Kg** (Number)
- **Active** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Meshes** (Number)

**Example:** [cables.gl/edit/Gh2f_4](https://cables.gl/edit/Gh2f_4)

**Doc:** [cables.gl/op/Ops.Extension.AmmoPhysics.GltfAmmoBodies](https://cables.gl/op/Ops.Extension.AmmoPhysics.GltfAmmoBodies)


