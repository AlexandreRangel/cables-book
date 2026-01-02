# Ops.Extension.Lottie

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Extension.Lottie

### LottieSVGPlayer
![LottieSVGPlayer op](images/ops/Ops_Extension_Lottie_LottieSVGPlayer.svg)

**Full Name:** `Ops.Extension.Lottie.LottieSVGPlayer`
**Description:** Play Bodymovin/Lottie animations as SVG in a HTML element

**> Input Ports:**

- **HTML Element** (Object:Element)
- **JSON Data** (Object)
- **Render Frame** (Number)
- **Loop** (Number: Boolean)
- **Play** (Number: Boolean)
- **Play Backward** (Number: Boolean)
- **Rewind** (Trigger)
- **Active** (Number: Boolean)

**< Output Ports:**

- **Completed** (booleanNumber)
- **Progress** (Number)
- **Total Frames** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/3ezRZH)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LottieSVGPlayer"*
**Docs:** [https://cables.gl/op/Ops.Extension.Lottie.LottieSVGPlayer](https://cables.gl/op/Ops.Extension.Lottie.LottieSVGPlayer)

---

### LottieTexturePlayer_v2
![LottieTexturePlayer_v2 op](images/ops/Ops_Extension_Lottie_LottieTexturePlayer_v2.svg)

**Full Name:** `Ops.Extension.Lottie.LottieTexturePlayer_v2`
**Description:** Play a Lottie animation in a texture

**> Input Ports:**

- **Exe** (Trigger)
- **JSON Data** (Object)
- **Play Mode Index** (Number: Integer)
- **Frame** (Number)
- **Play** (Number: Boolean)
- **Rewind** (Trigger)
- **Speed** (Number)
- **Texture Width** (Number: Integer)
- **Texture Height** (Number: Integer)
- **Filter Index** (Number: Integer)
- **Wrap Index** (Number: Integer)
- **Scale Index** (Number: Integer)

**< Output Ports:**

- **Texture** (Object)
- **Total Frames** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/zW0RFn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LottieTexturePlayer_v2"*
**Docs:** [https://cables.gl/op/Ops.Extension.Lottie.LottieTexturePlayer_v2](https://cables.gl/op/Ops.Extension.Lottie.LottieTexturePlayer_v2)

---

