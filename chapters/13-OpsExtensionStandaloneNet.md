# Ops.Extension.Standalone.Net

---

## Ops.Extension.Standalone.Net

### HttpServer
![HttpServer op](images/ops/Ops_Extension_Standalone_Net_HttpServer.svg)

**Full Name:** `Ops.Extension.Standalone.Net.HttpServer`

**Description:** Create a Web/Http server locally

**`\inputsymbol`{=latex} Input Ports:**

- **Hostname** (String)
- **Port** (Number: Integer)

**`\outputsymbol`{=latex} Output Ports:**

- **Trigger Request** (Trigger)
- **Response** (Object)
- **Request URL** (String)
- **Request** (Object)
- **Running** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/lke9pn)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServer](https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServer)

### HttpServerResponse
![HttpServerResponse op](images/ops/Ops_Extension_Standalone_Net_HttpServerResponse.svg)

**Full Name:** `Ops.Extension.Standalone.Net.HttpServerResponse`

**Description:** Answer http requests by sending string to the browser/client

**`\inputsymbol`{=latex} Input Ports:**

- **Trigger** (Trigger)
- **Response** (Object)
- **Body** (String)

**`\outputsymbol`{=latex} Output Ports:**

- *Visit [Ops.Extension.Standalone.Net.HttpServerResponse documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServerResponse) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/lke9pn)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServerResponse](https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServerResponse)

### IpAddress
![IpAddress op](images/ops/Ops_Extension_Standalone_Net_IpAddress.svg)

**Full Name:** `Ops.Extension.Standalone.Net.IpAddress`

**Description:** Outputs your local IP Adress

**`\inputsymbol`{=latex} Input Ports:**

- *Visit [Ops.Extension.Standalone.Net.IpAddress documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.IpAddress) for input port details*

**`\outputsymbol`{=latex} Output Ports:**

- **Local IP** (String)
- **Interface** (String)
- **Data** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/lCYxun)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.IpAddress](https://cables.gl/op/Ops.Extension.Standalone.Net.IpAddress)

### Osc_v2
![Osc_v2 op](images/ops/Ops_Extension_Standalone_Net_Osc_v2.svg)

**Full Name:** `Ops.Extension.Standalone.Net.Osc_v2`

**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.Osc_v2) for details*

**`\inputsymbol`{=latex} Input Ports:**

- **Port** (Number: Integer)

**`\outputsymbol`{=latex} Output Ports:**

- **Message Received** (Trigger)
- **Message** (Object)
- **Connection** (Object)
- **Status** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/PCZCun)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.Osc_v2](https://cables.gl/op/Ops.Extension.Standalone.Net.Osc_v2)

### OscSend
![OscSend op](images/ops/Ops_Extension_Standalone_Net_OscSend.svg)

**Full Name:** `Ops.Extension.Standalone.Net.OscSend`

**Description:** send data to a OSC device

**`\inputsymbol`{=latex} Input Ports:**

- **Connection** (Object)
- **Net Address** (String)
- **Port** (Number: Integer)
- **OSC Address** (String)
- **Number** (Number)
- **Send** (Trigger)
- **Public** (1): OSC: READ / SEND

**`\outputsymbol`{=latex} Output Ports:**

- *Visit [Ops.Extension.Standalone.Net.OscSend documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.OscSend) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Net.OscSend#example)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.OscSend](https://cables.gl/op/Ops.Extension.Standalone.Net.OscSend)

### ReadTextFile
![ReadTextFile op](images/ops/Ops_Extension_Standalone_Net_ReadTextFile.svg)

**Full Name:** `Ops.Extension.Standalone.Net.ReadTextFile`

**Description:** Read a text file as string from the local file system

**`\inputsymbol`{=latex} Input Ports:**

- **Filename** (String)
- **Read** (Trigger)

**`\outputsymbol`{=latex} Output Ports:**

- **Next** (Trigger)
- **Content** (String)
- **Has Error** (booleanNumber)
- **Error** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/PT9Aun)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.ReadTextFile](https://cables.gl/op/Ops.Extension.Standalone.Net.ReadTextFile)

### SocketClusterServer
![SocketClusterServer op](images/ops/Ops_Extension_Standalone_Net_SocketClusterServer.svg)

**Full Name:** `Ops.Extension.Standalone.Net.SocketClusterServer`

**Description:** start a socketcluster server

**`\inputsymbol`{=latex} Input Ports:**

- **Active** (Number: Boolean)
- **Hostname** (String)
- **Port** (Number: Integer)
- **Path** (String)

**`\outputsymbol`{=latex} Output Ports:**

- **Receiving** (Trigger)
- **Data** (Object)
- **Listening** (booleanNumber)
- **Clients** (Number)
- **Error** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Net.SocketClusterServer#example)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.SocketClusterServer](https://cables.gl/op/Ops.Extension.Standalone.Net.SocketClusterServer)


