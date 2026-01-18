// Custom Op: Animated dots + connecting lines (Texture via HtmlToTexture)
// Name: Ops.User.Rangel.DotsNetworkTexture
//
// Usage:
// 1) Create a Custom Op in cables.gl and paste this code.
// 2) Connect MainLoop -> Render.
// 3) Use HtmlToTexture with Element = #dots-network-canvas to get a texture.

const inRender = op.inTrigger("Render");

const inResX = op.inInt("Res X", 1024);
const inResY = op.inInt("Res Y", 1024);

const inNumPoints = op.inInt("Points", 80);
const inPointSize = op.inFloat("Point Size", 2.5);
const inPointSizeRand = op.inFloat("Point Size Random", 0.4);

const inLinesPerPoint = op.inInt("Lines Per Point", 2);

const inPointR = op.inFloat("Point R", 1.0);
const inPointG = op.inFloat("Point G", 1.0);
const inPointB = op.inFloat("Point B", 1.0);
const inPointA = op.inFloat("Point A", 0.9);

const inLineR = op.inFloat("Line R", 0.6);
const inLineG = op.inFloat("Line G", 0.6);
const inLineB = op.inFloat("Line B", 0.6);
const inLineA = op.inFloat("Line A", 0.4);

const inColorJitter = op.inFloat("Color Randomize", 0.15);
const inSpeed = op.inFloat("Speed", 1.0);

const inDirectTexture = op.inBool("Direct Texture", true);
const outTexture = op.outTexture("Texture Out");
const outCanvas = op.outObject("Canvas");
const outCanvasSelector = op.outString("Canvas Selector");
const outNext = op.outTrigger("Next");

let canvas = null;
let ctx = null;
let points = [];
let time = 0;
let lastTime = null;
let canvasReady = false;
let cglTexture = null;
let directTextureFailed = false;

function clamp01(v) {
    return Math.max(0, Math.min(1, v));
}

function ensureCanvas() {
    const w = Math.max(16, inResX.get() | 0);
    const h = Math.max(16, inResY.get() | 0);

    if (!canvas) {
        canvas = document.createElement("canvas");
        canvas.id = "dots-network-canvas";
        canvas.style.position = "fixed";
        canvas.style.left = "-10000px";
        canvas.style.top = "-10000px";
        document.body.appendChild(canvas);
        ctx = canvas.getContext("2d");
        outCanvasSelector.set("#" + canvas.id);
    }

    if (canvas.width !== w || canvas.height !== h) {
        canvas.width = w;
        canvas.height = h;
    }
}

function rebuildPoints() {
    const w = canvas.width;
    const h = canvas.height;
    const n = Math.max(2, inNumPoints.get() | 0);
    const sizeRand = Math.max(0, inPointSizeRand.get());
    points = [];

    for (let i = 0; i < n; i++) {
        const scale = 1 - sizeRand + Math.random() * sizeRand * 2;
        points.push({
            x: Math.random() * w,
            y: Math.random() * h,
            vx: (Math.random() * 2 - 1) * 40,
            vy: (Math.random() * 2 - 1) * 40,
            sizeMul: scale,
            seed: Math.random() * 1000
        });
    }
}

function updatePoints(dt) {
    const w = canvas.width;
    const h = canvas.height;
    const speed = Math.max(0, inSpeed.get());

    for (let i = 0; i < points.length; i++) {
        const p = points[i];
        p.x += p.vx * dt * speed;
        p.y += p.vy * dt * speed;

        if (p.x < 0) p.x += w;
        if (p.x > w) p.x -= w;
        if (p.y < 0) p.y += h;
        if (p.y > h) p.y -= h;
    }
}

function findNearest(pointIndex, count) {
    const p = points[pointIndex];
    const best = [];

    for (let i = 0; i < points.length; i++) {
        if (i === pointIndex) continue;
        const q = points[i];
        const dx = p.x - q.x;
        const dy = p.y - q.y;
        const d2 = dx * dx + dy * dy;

        if (best.length < count) {
            best.push({ i, d2 });
            continue;
        }

        let worstIdx = 0;
        for (let j = 1; j < best.length; j++) {
            if (best[j].d2 > best[worstIdx].d2) worstIdx = j;
        }
        if (d2 < best[worstIdx].d2) best[worstIdx] = { i, d2 };
    }
    return best;
}

function draw() {
    const w = canvas.width;
    const h = canvas.height;
    const nLines = Math.max(0, inLinesPerPoint.get() | 0);
    const maxDist = Math.hypot(w, h) * 0.35;
    const jitter = Math.max(0, inColorJitter.get());

    ctx.clearRect(0, 0, w, h);
    ctx.globalCompositeOperation = "source-over";

    for (let i = 0; i < points.length; i++) {
        const p = points[i];
        const neighbors = findNearest(i, nLines);
        for (let j = 0; j < neighbors.length; j++) {
            const q = points[neighbors[j].i];
            const dx = p.x - q.x;
            const dy = p.y - q.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            const alphaFade = 1 - Math.min(1, dist / maxDist);

            const t = time * 0.7 + p.seed;
            const jr = (Math.sin(t) * 0.5 + 0.5) * jitter;
            const jg = (Math.sin(t + 2.1) * 0.5 + 0.5) * jitter;
            const jb = (Math.sin(t + 4.2) * 0.5 + 0.5) * jitter;

            const r = clamp01(inLineR.get() + jr);
            const g = clamp01(inLineG.get() + jg);
            const b = clamp01(inLineB.get() + jb);
            const a = clamp01(inLineA.get()) * alphaFade;

            ctx.strokeStyle = `rgba(${(r * 255) | 0}, ${(g * 255) | 0}, ${(b * 255) | 0}, ${a})`;
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(q.x, q.y);
            ctx.stroke();
        }
    }

    for (let i = 0; i < points.length; i++) {
        const p = points[i];
        const size = Math.max(0.25, inPointSize.get() * p.sizeMul);

        const t = time + p.seed * 0.5;
        const jr = (Math.sin(t) * 0.5 + 0.5) * jitter;
        const jg = (Math.sin(t + 1.7) * 0.5 + 0.5) * jitter;
        const jb = (Math.sin(t + 3.4) * 0.5 + 0.5) * jitter;

        const r = clamp01(inPointR.get() + jr);
        const g = clamp01(inPointG.get() + jg);
        const b = clamp01(inPointB.get() + jb);
        const a = clamp01(inPointA.get());

        ctx.fillStyle = `rgba(${(r * 255) | 0}, ${(g * 255) | 0}, ${(b * 255) | 0}, ${a})`;
        ctx.beginPath();
        ctx.arc(p.x, p.y, size, 0, Math.PI * 2);
        ctx.fill();
    }
}

function getDeltaSafe() {
    const now = op.patch.timer && typeof op.patch.timer.getTime === "function"
        ? op.patch.timer.getTime()
        : performance.now() / 1000;
    if (lastTime === null) {
        lastTime = now;
        return 0;
    }
    const dt = Math.max(0, now - lastTime);
    lastTime = now;
    return dt;
}

function updateDirectTexture() {
    if (!inDirectTexture.get() || directTextureFailed || !canvas) return;
    const cgl = op.patch && op.patch.cgl ? op.patch.cgl : null;
    if (!cgl) return;

    try {
        if (!cglTexture) {
            if (typeof cgl.createTextureFromCanvas === "function") {
                cglTexture = cgl.createTextureFromCanvas(canvas);
            } else if (typeof cgl.createTexture === "function") {
                cglTexture = cgl.createTexture(canvas);
            } else if (cgl.Texture) {
                cglTexture = new cgl.Texture(canvas);
            } else if (typeof CGL !== "undefined" && CGL.Texture) {
                cglTexture = new CGL.Texture(canvas);
            }
        } else if (typeof cglTexture.setSource === "function") {
            cglTexture.setSource(canvas);
        } else if (typeof cglTexture.updateFromCanvas === "function") {
            cglTexture.updateFromCanvas(canvas);
        } else if (typeof cglTexture.update === "function") {
            cglTexture.update(canvas);
        }

        if (cglTexture) {
            outTexture.set(cglTexture);
        }
    } catch (e) {
        directTextureFailed = true;
        op.logWarn("Direct texture update failed, use HtmlToTexture instead.");
    }
}

function refreshLayout() {
    ensureCanvas();
    rebuildPoints();
}

inResX.onChange = refreshLayout;
inResY.onChange = refreshLayout;
inNumPoints.onChange = refreshLayout;
inPointSizeRand.onChange = refreshLayout;

refreshLayout();

inRender.onTriggered = function () {
    ensureCanvas();
    if (!canvasReady && canvas) {
        outCanvas.set(canvas);
        canvasReady = true;
    }
    const dt = getDeltaSafe();
    time += dt;
    updatePoints(dt);
    draw();
    updateDirectTexture();
    outNext.trigger();
};
