# Ops.Extension.SocketCluster.Deprecated


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### SocketClusterReceiveArray
![SocketClusterReceiveArray op](images/ops/Ops_Extension_SocketCluster_Deprecated_SocketClusterReceiveArray.svg)

**Full Name:** `Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveArray`

receive an array from the socketcluster topic.

**`\inputsymbol`{=latex} Inputs**

- **Socket** (Object)
- **Topic** (String)

**`\outputsymbol`{=latex} Output**

- **Client Id** (String)
- **Data** (Array)
- **Received** (Trigger)

**Example Patch:** [cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveArray#example](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveArray#example)

**Doc:** [cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveArray](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveArray)

### SocketClusterReceiveBoolean
![SocketClusterReceiveBoolean op](images/ops/Ops_Extension_SocketCluster_Deprecated_SocketClusterReceiveBoolean.svg)

**Full Name:** `Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveBoolean`

Receive boolean value from the socketcluster socket/topic.

**`\inputsymbol`{=latex} Inputs**

- **Socket** (Object)
- **Topic** (String)

**`\outputsymbol`{=latex} Output**

- **Client Id** (String)
- **Data** (booleanNumber)
- **Received** (Trigger)

**Example Patch:** [cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveBoolean#example](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveBoolean#example)

**Doc:** [cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveBoolean](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveBoolean)

### SocketClusterReceiveNumber
![SocketClusterReceiveNumber op](images/ops/Ops_Extension_SocketCluster_Deprecated_SocketClusterReceiveNumber.svg)

**Full Name:** `Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveNumber`

receive number from the socketcluster socket/topic.

**`\inputsymbol`{=latex} Inputs**

- **Socket** (Object)
- **Topic** (String)

**`\outputsymbol`{=latex} Output**

- **Client Id** (String)
- **Data** (Number)
- **Received** (Trigger)

**Example Patch:** [cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveNumber#example](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveNumber#example)

**Doc:** [cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveNumber](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveNumber)

### SocketClusterReceiveString
![SocketClusterReceiveString op](images/ops/Ops_Extension_SocketCluster_Deprecated_SocketClusterReceiveString.svg)

**Full Name:** `Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveString`

receives string from the socketcluster socket/topic.

**`\inputsymbol`{=latex} Inputs**

- **Socket** (Object:Socketcluster)
- **Topic** (String)

**`\outputsymbol`{=latex} Output**

- **Data** (String)
- **Client Id** (String)
- **Received** (Trigger)

**Example Patch:** [cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveString#example](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveString#example)

**Doc:** [cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveString](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterReceiveString)

### SocketClusterSendArray
![SocketClusterSendArray op](images/ops/Ops_Extension_SocketCluster_Deprecated_SocketClusterSendArray.svg)

**Full Name:** `Ops.Extension.SocketCluster.Deprecated.SocketClusterSendArray`

sends an array via socketcluster/websocket.

**`\inputsymbol`{=latex} Inputs**

- **Send** (Trigger)
- **Socket** (Object:Socketcluster)
- **Topic** (String)
- **Data** (Array)
- **Public** (2): MOUSE MOVEMENT SEND

**`\outputsymbol`{=latex} Output**

- *Visit [Ops.Extension.SocketCluster.Deprecated.SocketClusterSendArray documentation](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendArray) for output port details*

**Example Patch:** [cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendArray#example](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendArray#example)

**Doc:** [cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendArray](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendArray)

### SocketClusterSendBoolean
![SocketClusterSendBoolean op](images/ops/Ops_Extension_SocketCluster_Deprecated_SocketClusterSendBoolean.svg)

**Full Name:** `Ops.Extension.SocketCluster.Deprecated.SocketClusterSendBoolean`

Sends boolean value via socketcluster/websocket.

**`\inputsymbol`{=latex} Inputs**

- **Send** (Trigger)
- **Socket** (Object)
- **Topic** (String)
- **Data** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- *Visit [Ops.Extension.SocketCluster.Deprecated.SocketClusterSendBoolean documentation](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendBoolean) for output port details*

**Example Patch:** [cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendBoolean#example](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendBoolean#example)

**Doc:** [cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendBoolean](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendBoolean)

### SocketClusterSendNumber
![SocketClusterSendNumber op](images/ops/Ops_Extension_SocketCluster_Deprecated_SocketClusterSendNumber.svg)

**Full Name:** `Ops.Extension.SocketCluster.Deprecated.SocketClusterSendNumber`

sends a number via socketcluster/websocket.

**`\inputsymbol`{=latex} Inputs**

- **Send** (Trigger)
- **Socket** (Object)
- **Topic** (String)
- **Data** (Number)

**`\outputsymbol`{=latex} Output**

- *Visit [Ops.Extension.SocketCluster.Deprecated.SocketClusterSendNumber documentation](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendNumber) for output port details*

**Example Patch:** [cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendNumber#example](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendNumber#example)

**Doc:** [cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendNumber](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendNumber)

### SocketClusterSendString
![SocketClusterSendString op](images/ops/Ops_Extension_SocketCluster_Deprecated_SocketClusterSendString.svg)

**Full Name:** `Ops.Extension.SocketCluster.Deprecated.SocketClusterSendString`

sends a string via socketcluster/websocket.

**`\inputsymbol`{=latex} Inputs**

- **Send** (Trigger)
- **Socket** (Object:Socketcluster)
- **Topic** (String)
- **Data** (String)

**`\outputsymbol`{=latex} Output**

- *Visit [Ops.Extension.SocketCluster.Deprecated.SocketClusterSendString documentation](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendString) for output port details*

**Example Patch:** [cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendString#example](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendString#example)

**Doc:** [cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendString](https://cables.gl/op/Ops.Extension.SocketCluster.Deprecated.SocketClusterSendString)


