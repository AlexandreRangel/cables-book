# Ops.Net.WebSocket

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Net.WebSocket

### WebSocket_v2
![WebSocket_v2 op](images/ops/Ops_Net_WebSocket_WebSocket_v2.svg)

**Full Name:** `Ops.Net.WebSocket.WebSocket_v2`
**Description:** Create a websocket connection and receive data from it

**> Input Ports:**

- **URL** (String)

**< Output Ports:**

- **Result** (Object)
- **Valid JSON** (booleanNumber)
- **Connection** (Object)
- **Connected** (booleanNumber)
- **Received Data** (Trigger)
- **Raw Data** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/gu7DBo)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WebSocket_v2"*
**Docs:** [https://cables.gl/op/Ops.Net.WebSocket.WebSocket_v2](https://cables.gl/op/Ops.Net.WebSocket.WebSocket_v2)

---

### WebSocketSend
![WebSocketSend op](images/ops/Ops_Net_WebSocket_WebSocketSend.svg)

**Full Name:** `Ops.Net.WebSocket.WebSocketSend`
**Description:** send an object to a websocket connection

**> Input Ports:**

- **Connection** (Object:Websocket)
- **Object** (Object)
- **Send** (Trigger)
- **Send String** (Number: Boolean)

**< Output Ports:**

- **Sent** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/gu7DBo)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WebSocketSend"*
**Docs:** [https://cables.gl/op/Ops.Net.WebSocket.WebSocketSend](https://cables.gl/op/Ops.Net.WebSocket.WebSocketSend)

---

