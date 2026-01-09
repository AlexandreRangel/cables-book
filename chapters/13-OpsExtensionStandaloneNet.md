# Ops.Extension.Standalone.Net


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### HttpServer
![HttpServer op](images/ops/Ops_Extension_Standalone_Net_HttpServer.svg)

**Full Name:** `Ops.Extension.Standalone.Net.HttpServer`

Create a Web/Http server locally.

**`\inputsymbol`{=latex} Inputs**

- **Hostname** (String)
- **Port** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Trigger Request** (Trigger)
- **Response** (Object)
- **Request URL** (String)
- **Request** (Object)
- **Running** (booleanNumber)

**Example Patch:** [cables.gl/edit/lke9pn](https://cables.gl/edit/lke9pn)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Net.HttpServer](https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServer)

### HttpServerResponse
![HttpServerResponse op](images/ops/Ops_Extension_Standalone_Net_HttpServerResponse.svg)

**Full Name:** `Ops.Extension.Standalone.Net.HttpServerResponse`

Answer http requests by sending string to the browser/client.

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Response** (Object)
- **Body** (String)

**Example Patch:** [cables.gl/edit/lke9pn](https://cables.gl/edit/lke9pn)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Net.HttpServerResponse](https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServerResponse)

### IpAddress
![IpAddress op](images/ops/Ops_Extension_Standalone_Net_IpAddress.svg)

**Full Name:** `Ops.Extension.Standalone.Net.IpAddress`

Outputs your local IP Adress.

**`\outputsymbol`{=latex} Output**

- **Local IP** (String)
- **Interface** (String)
- **Data** (Object)

**Example Patch:** [cables.gl/edit/lCYxun](https://cables.gl/edit/lCYxun)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Net.IpAddress](https://cables.gl/op/Ops.Extension.Standalone.Net.IpAddress)

### Osc_v2
![Osc_v2 op](images/ops/Ops_Extension_Standalone_Net_Osc_v2.svg)

**Full Name:** `Ops.Extension.Standalone.Net.Osc_v2`

*Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.Osc_v2) for details*.

**`\inputsymbol`{=latex} Inputs**

- **Port** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Message Received** (Trigger)
- **Message** (Object)
- **Connection** (Object)
- **Status** (String)

**Example Patch:** [cables.gl/edit/PCZCun](https://cables.gl/edit/PCZCun)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Net.Osc_v2](https://cables.gl/op/Ops.Extension.Standalone.Net.Osc_v2)

### OscSend
![OscSend op](images/ops/Ops_Extension_Standalone_Net_OscSend.svg)

**Full Name:** `Ops.Extension.Standalone.Net.OscSend`

send data to a OSC device.

**`\inputsymbol`{=latex} Inputs**

- **Connection** (Object)
- **Net Address** (String)
- **Port** (Number: Integer)
- **OSC Address** (String)
- **Number** (Number)
- **Send** (Trigger)
- **Public** (1): OSC: READ / SEND

**Example Patch:** [cables.gl/op/Ops.Extension.Standalone.Net.OscSend#example](https://cables.gl/op/Ops.Extension.Standalone.Net.OscSend#example)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Net.OscSend](https://cables.gl/op/Ops.Extension.Standalone.Net.OscSend)

### ReadTextFile
![ReadTextFile op](images/ops/Ops_Extension_Standalone_Net_ReadTextFile.svg)

**Full Name:** `Ops.Extension.Standalone.Net.ReadTextFile`

Read a text file as string from the local file system.

**`\inputsymbol`{=latex} Inputs**

- **Filename** (String)
- **Read** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Content** (String)
- **Has Error** (booleanNumber)
- **Error** (String)

**Example Patch:** [cables.gl/edit/PT9Aun](https://cables.gl/edit/PT9Aun)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Net.ReadTextFile](https://cables.gl/op/Ops.Extension.Standalone.Net.ReadTextFile)

### SocketClusterServer
![SocketClusterServer op](images/ops/Ops_Extension_Standalone_Net_SocketClusterServer.svg)

**Full Name:** `Ops.Extension.Standalone.Net.SocketClusterServer`

start a socketcluster server.

**`\inputsymbol`{=latex} Inputs**

- **Active** (Number: Boolean)
- **Hostname** (String)
- **Port** (Number: Integer)
- **Path** (String)

**`\outputsymbol`{=latex} Output**

- **Receiving** (Trigger)
- **Data** (Object)
- **Listening** (booleanNumber)
- **Clients** (Number)
- **Error** (String)

**Example Patch:** [cables.gl/op/Ops.Extension.Standalone.Net.SocketClusterServer#example](https://cables.gl/op/Ops.Extension.Standalone.Net.SocketClusterServer#example)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Net.SocketClusterServer](https://cables.gl/op/Ops.Extension.Standalone.Net.SocketClusterServer)


