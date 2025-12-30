# Ops.Net.WebSocket

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Net.WebSocket

### WebSocket_v2
![WebSocket_v2 op](images/ops/Ops_Net_WebSocket_WebSocket_v2.svg)

**Full Name:** `Ops.Net.WebSocket.WebSocket_v2`
**Description:** Create a websocket connection and receive data from it

**> Input Ports:**
- **URL** (String): *See documentation*

**< Output Ports:**
- **Result** (Object): *See documentation*
- **Valid JSON** (booleanNumber): *See documentation*
- **Connection** (Object): *See documentation*
- **Connected** (booleanNumber): *See documentation*
- **Received Data** (Trigger): *See documentation*
- **Raw Data** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/gu7DBo)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WebSocket_v2"*
**Docs:** [https://cables.gl/op/Ops.Net.WebSocket.WebSocket_v2](https://cables.gl/op/Ops.Net.WebSocket.WebSocket_v2)

---

### WebSocketSend
![WebSocketSend op](images/ops/Ops_Net_WebSocket_WebSocketSend.svg)

**Full Name:** `Ops.Net.WebSocket.WebSocketSend`
**Description:** send an object to a websocket connection

**> Input Ports:**
- **Connection** (Object:Websocket): *See documentation*
- **Object** (Object): *See documentation*
- **Send** (Trigger): *See documentation*
- **Send String** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Sent** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/gu7DBo)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WebSocketSend"*
**Docs:** [https://cables.gl/op/Ops.Net.WebSocket.WebSocketSend](https://cables.gl/op/Ops.Net.WebSocket.WebSocketSend)

---

