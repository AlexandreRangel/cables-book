# Ops.Extension.Standalone.Net

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Extension.Standalone.Net

### HttpServer
![HttpServer op](images/ops/Ops_Extension_Standalone_Net_HttpServer.svg)

**Full Name:** `Ops.Extension.Standalone.Net.HttpServer`

**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServer) for details*

**> Input Ports:**
- **Hostname** (String)
- **Port** (Number: Integer)

**< Output Ports:**
- **Trigger Request** (Trigger)
- **Response** (Object)
- **Request URL** (String)
- **Request** (Object)
- **Running** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServer#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HttpServer"*

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServer](https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServer)

---

### HttpServerResponse
![HttpServerResponse op](images/ops/Ops_Extension_Standalone_Net_HttpServerResponse.svg)

**Full Name:** `Ops.Extension.Standalone.Net.HttpServerResponse`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServerResponse) for details*

**> Input Ports:**
- **Trigger** (Trigger)
- **Response** (Object)
- **Body** (String)

**< Output Ports:**
- *Visit [Ops.Extension.Standalone.Net.HttpServerResponse documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServerResponse) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServerResponse#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HttpServerResponse"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServerResponse](https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServerResponse)

---

### IpAddress
![IpAddress op](images/ops/Ops_Extension_Standalone_Net_IpAddress.svg)

**Full Name:** `Ops.Extension.Standalone.Net.IpAddress`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.IpAddress) for details*

**> Input Ports:**
- *Visit [Ops.Extension.Standalone.Net.IpAddress documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.IpAddress) for input port details*

**< Output Ports:**
- **Local IP** (String)
- **Interface** (String)
- **Data** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Net.IpAddress#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "IpAddress"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.IpAddress](https://cables.gl/op/Ops.Extension.Standalone.Net.IpAddress)

---

### Osc_v2
![Osc_v2 op](images/ops/Ops_Extension_Standalone_Net_Osc_v2.svg)

**Full Name:** `Ops.Extension.Standalone.Net.Osc_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.Osc_v2) for details*

**> Input Ports:**
- **Port** (Number: Integer)

**< Output Ports:**
- **Message Received** (Trigger)
- **Message** (Object)
- **Connection** (Object)
- **Status** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Net.Osc_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Osc_v2"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.Osc_v2](https://cables.gl/op/Ops.Extension.Standalone.Net.Osc_v2)

---

### OscSend
![OscSend op](images/ops/Ops_Extension_Standalone_Net_OscSend.svg)

**Full Name:** `Ops.Extension.Standalone.Net.OscSend`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.OscSend) for details*

**> Input Ports:**
- **Connection** (Object)
- **Net Address** (String)
- **Port** (Number: Integer)
- **OSC Address** (String)
- **Number** (Number)
- **Send** (Trigger)
- **Public** (1): OSC: READ / SEND

**< Output Ports:**
- *Visit [Ops.Extension.Standalone.Net.OscSend documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.OscSend) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Net.OscSend#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "OscSend"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.OscSend](https://cables.gl/op/Ops.Extension.Standalone.Net.OscSend)

---

### ReadTextFile
![ReadTextFile op](images/ops/Ops_Extension_Standalone_Net_ReadTextFile.svg)

**Full Name:** `Ops.Extension.Standalone.Net.ReadTextFile`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.ReadTextFile) for details*

**> Input Ports:**
- **Filename** (String)
- **Read** (Trigger)

**< Output Ports:**
- **Next** (Trigger)
- **Content** (String)
- **Has Error** (booleanNumber)
- **Error** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Net.ReadTextFile#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ReadTextFile"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.ReadTextFile](https://cables.gl/op/Ops.Extension.Standalone.Net.ReadTextFile)

---

### SocketClusterServer
![SocketClusterServer op](images/ops/Ops_Extension_Standalone_Net_SocketClusterServer.svg)

**Full Name:** `Ops.Extension.Standalone.Net.SocketClusterServer`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.SocketClusterServer) for details*

**> Input Ports:**
- **Active** (Number: Boolean)
- **Hostname** (String)
- **Port** (Number: Integer)
- **Path** (String)

**< Output Ports:**
- **Receiving** (Trigger)
- **Data** (Object)
- **Listening** (booleanNumber)
- **Clients** (Number)
- **Error** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Net.SocketClusterServer#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SocketClusterServer"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.SocketClusterServer](https://cables.gl/op/Ops.Extension.Standalone.Net.SocketClusterServer)

---

