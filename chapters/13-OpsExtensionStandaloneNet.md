# Ops.Extension.Standalone.Net

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Extension.Standalone.Net

### HttpServer
![HttpServer op](images/ops/Ops_Extension_Standalone_Net_HttpServer.svg)

**Full Name:** `Ops.Extension.Standalone.Net.HttpServer`
**Description:** Create a Web/Http server locally

**> Input Ports:**
- **Hostname** (String): *See documentation*
- **Port** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger Request** (Trigger): *See documentation*
- **Response** (Object): *See documentation*
- **Request URL** (String): *See documentation*
- **Request** (Object): *See documentation*
- **Running** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/lke9pn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HttpServer"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServer](https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServer)

---

### HttpServerResponse
![HttpServerResponse op](images/ops/Ops_Extension_Standalone_Net_HttpServerResponse.svg)

**Full Name:** `Ops.Extension.Standalone.Net.HttpServerResponse`
**Description:** Answer http requests by sending string to the browser/client

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **Response** (Object): *See documentation*
- **Body** (String): *See documentation*

**< Output Ports:**
- *Visit [Ops.Extension.Standalone.Net.HttpServerResponse documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServerResponse) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/lke9pn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HttpServerResponse"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServerResponse](https://cables.gl/op/Ops.Extension.Standalone.Net.HttpServerResponse)

---

### IpAddress
![IpAddress op](images/ops/Ops_Extension_Standalone_Net_IpAddress.svg)

**Full Name:** `Ops.Extension.Standalone.Net.IpAddress`
**Description:** Outputs your local IP Adress

**> Input Ports:**
- *Visit [Ops.Extension.Standalone.Net.IpAddress documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.IpAddress) for input port details*

**< Output Ports:**
- **Local IP** (String): *See documentation*
- **Interface** (String): *See documentation*
- **Data** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/lCYxun)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "IpAddress"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.IpAddress](https://cables.gl/op/Ops.Extension.Standalone.Net.IpAddress)

---

### Osc_v2
![Osc_v2 op](images/ops/Ops_Extension_Standalone_Net_Osc_v2.svg)

**Full Name:** `Ops.Extension.Standalone.Net.Osc_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Net.Osc_v2) for details*

**> Input Ports:**
- **Port** (Number: Integer): *See documentation*

**< Output Ports:**
- **Message Received** (Trigger): *See documentation*
- **Message** (Object): *See documentation*
- **Connection** (Object): *See documentation*
- **Status** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/PCZCun)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Osc_v2"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.Osc_v2](https://cables.gl/op/Ops.Extension.Standalone.Net.Osc_v2)

---

### OscSend
![OscSend op](images/ops/Ops_Extension_Standalone_Net_OscSend.svg)

**Full Name:** `Ops.Extension.Standalone.Net.OscSend`
**Description:** send data to a OSC device

**> Input Ports:**
- **Connection** (Object): *See documentation*
- **Net Address** (String): *See documentation*
- **Port** (Number: Integer): *See documentation*
- **OSC Address** (String): *See documentation*
- **Number** (Number): *See documentation*
- **Send** (Trigger): *See documentation*
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
**Description:** Read a text file as string from the local file system

**> Input Ports:**
- **Filename** (String): *See documentation*
- **Read** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Content** (String): *See documentation*
- **Has Error** (booleanNumber): *See documentation*
- **Error** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/PT9Aun)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ReadTextFile"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.ReadTextFile](https://cables.gl/op/Ops.Extension.Standalone.Net.ReadTextFile)

---

### SocketClusterServer
![SocketClusterServer op](images/ops/Ops_Extension_Standalone_Net_SocketClusterServer.svg)

**Full Name:** `Ops.Extension.Standalone.Net.SocketClusterServer`
**Description:** start a socketcluster server

**> Input Ports:**
- **Active** (Number: Boolean): *See documentation*
- **Hostname** (String): *See documentation*
- **Port** (Number: Integer): *See documentation*
- **Path** (String): *See documentation*

**< Output Ports:**
- **Receiving** (Trigger): *See documentation*
- **Data** (Object): *See documentation*
- **Listening** (booleanNumber): *See documentation*
- **Clients** (Number): *See documentation*
- **Error** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Net.SocketClusterServer#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SocketClusterServer"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Net.SocketClusterServer](https://cables.gl/op/Ops.Extension.Standalone.Net.SocketClusterServer)

---

