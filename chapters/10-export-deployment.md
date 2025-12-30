# Export & Deployment in Cables.gl

## Introduction

Once you've created your cables.gl project, you'll want to share it with the world. This chapter covers all the ways to export and deploy your creations.

## Export Options

### 1. Public Patch Link

The simplest way to share - just make your patch public and share the URL.

**Pros:**
- Instant sharing
- Always up-to-date
- No hosting needed

**Cons:**
- Requires internet
- Cables.gl branding
- Limited customization

### 2. Embedded iframe

Embed your patch in any website:

```html
<iframe 
    src="https://cables.gl/view/YOUR_PATCH_ID" 
    width="800" 
    height="600"
    frameborder="0"
    allowfullscreen>
</iframe>
```

### 3. Standalone Export

Download your patch as a standalone web application.

**Includes:**
- HTML file
- JavaScript bundle
- Assets (textures, models, audio)
- No cables.gl dependency

### 4. npm Package Export

Export as an npm package for integration with other JavaScript projects.

## Standalone Export Process

### Step 1: Prepare Your Patch

1. Test thoroughly in the editor
2. Optimize assets (compress images, reduce model complexity)
3. Remove unused ops and connections
4. Set default camera/view position

### Step 2: Export

1. Click the export/download button in the editor
2. Choose "Standalone" export
3. Configure options:
   - Include minified code
   - Include source maps (for debugging)
   - Asset optimization level

### Step 3: Download

You'll receive a ZIP file containing:

```
exported-patch/
+-- index.html          # Main HTML file
+-- js/
|   +-- cables.min.js   # Cables runtime
|   +-- ops.js          # Your patch's operators
|   +-- patch.js        # Patch configuration
+-- assets/
|   +-- textures/       # Image files
|   +-- audio/          # Sound files
|   +-- models/         # 3D models
+-- css/
    +-- style.css       # Optional styles
```

### Step 4: Test Locally

```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve .

# Using PHP
php -S localhost:8000
```

Then open `http://localhost:8000` in your browser.

## Customizing the Export

### Custom HTML Template

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>My Cables Project</title>
    <style>
        body { margin: 0; overflow: hidden; }
        #cables-container { width: 100vw; height: 100vh; }
    </style>
</head>
<body>
    <div id="cables-container"></div>
    
    <script src="js/cables.min.js"></script>
    <script src="js/ops.js"></script>
    <script>
        CABLES.patch = new CABLES.Patch({
            patchFile: 'js/patch.js',
            prefixAssetPath: 'assets/',
            glCanvasId: 'cables-container',
            onFinishedLoading: function() {
                console.log('Patch loaded!');
            }
        });
    </script>
</body>
</html>
```

### Configuration Options

```javascript
new CABLES.Patch({
    patchFile: 'js/patch.js',
    prefixAssetPath: 'assets/',
    glCanvasId: 'myCanvas',
    glCanvasResizeToWindow: true,
    onFinishedLoading: callback,
    onError: errorCallback,
    variables: {
        // Pass custom variables to the patch
        customColor: '#ff0000',
        userName: 'Guest'
    }
});
```

## Communicating with Your Patch

### Setting Variables from JavaScript

```javascript
// Get the patch instance
const patch = CABLES.patch;

// Set a variable
patch.setVariable('myValue', 42);
patch.setVariable('myColor', [1, 0, 0, 1]);
```

### Getting Values from the Patch

```javascript
// Get a variable
const value = patch.getVariable('myValue');

// Listen for variable changes
patch.on('variableChanged', function(name, value) {
    console.log(name, 'changed to', value);
});
```

### Triggering Events

```javascript
// Trigger an op
patch.getOpById('YOUR_OP_ID').trigger();

// Or use variables as triggers
patch.setVariable('doSomething', true);
```

## Advanced Embedding & Integration

When cables.gl becomes part of a larger website/app, you want the embed to be **robust**:

- correct sizing and device pixel ratio handling
- pause/resume behavior when the tab is hidden
- a clean integration API (events in, telemetry out)
- predictable asset paths across dev/staging/prod

### Responsive Canvas: Beyond Width/Height

If you embed into dynamic layouts (resizable panels, CSS grid, etc.), treat resize as a first-class event:

- call your resize function on load
- call it on `resize`
- call it when layout changes (route changes, UI toggles, etc.)

### Pausing When Not Visible

For performance and battery life, consider pausing expensive animation when the page is hidden:

```javascript
document.addEventListener("visibilitychange", () => {
  if (!window.CABLES || !CABLES.patch) return;
  // Depending on your patch/runtime, you may gate updates via a variable:
  CABLES.patch.setVariable("isVisible", !document.hidden);
});
```

Then in your patch, use `isVisible` to reduce workload (lower particle count, skip effects, etc.).

### postMessage Integration (iframe Control)

If you embed via iframe, `postMessage` is the clean way to send commands and data.

**Parent page -> iframe:**

```javascript
const iframe = document.getElementById("cablesFrame");
iframe.contentWindow.postMessage(
  { type: "CABLES_SET", name: "myValue", value: 0.75 },
  "*"
);
```

**Inside the exported patch wrapper page:**

```javascript
window.addEventListener("message", (event) => {
  const msg = event.data;
  if (!msg || !window.CABLES || !CABLES.patch) return;

  if (msg.type === "CABLES_SET") {
    CABLES.patch.setVariable(msg.name, msg.value);
  }
});
```

### Environment-Specific Configuration (dev / test / prod)

Keep environment differences in **configuration**, not in the patch logic:

- dev: verbose logging, source maps, local asset path
- test/staging: production-like hosting + debug overlays
- prod: minified, caching enabled, stable URLs

Common patterns:

- query string flags: `?debug=1`
- separate `config.json` loaded at runtime
- environment variables handled by the site that embeds the patch

### Asset Path Gotchas

Most “works locally but not in prod” issues come down to:

- wrong `prefixAssetPath`
- case-sensitive paths on Linux hosts
- missing assets in the exported zip upload

If you deploy under a sub-path (e.g., `https://site.com/myproject/`), ensure all paths are relative or correctly prefixed.

## Hosting Options

### Static Hosting

Your exported patch is static files - host anywhere:

- **GitHub Pages** - Free, great for projects
- **Netlify** - Free tier, easy deployment
- **Vercel** - Free tier, automatic deploys
- **Amazon S3** - Scalable, pay-per-use
- **Any web server** - Apache, Nginx, etc.

### GitHub Pages Deployment

```bash
# Create a gh-pages branch
git checkout -b gh-pages

# Add your exported files
git add .
git commit -m "Deploy cables patch"

# Push to GitHub
git push origin gh-pages
```

Enable GitHub Pages in repository settings.

### Netlify Deployment

1. Connect your GitHub repository
2. Set build command: (none needed for static)
3. Set publish directory: `/` or your export folder
4. Deploy!

## Embedding in Existing Websites

### As a Background

```html
<style>
    #cables-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
    }
</style>
<canvas id="cables-bg"></canvas>
<script>
    CABLES.patch = new CABLES.Patch({
        patchFile: 'patch.js',
        glCanvasId: 'cables-bg'
    });
</script>
```

### As a Hero Section

```html
<section class="hero">
    <div id="cables-hero"></div>
    <div class="hero-content">
        <h1>Welcome</h1>
        <p>Your content here</p>
    </div>
</section>
```

### Responsive Embedding

```javascript
function resizeCables() {
    const container = document.getElementById('cables-container');
    container.style.width = window.innerWidth + 'px';
    container.style.height = window.innerHeight + 'px';
    
    // Notify cables of resize
    if (CABLES.patch) {
        CABLES.patch.cgl.setSize(window.innerWidth, window.innerHeight);
    }
}

window.addEventListener('resize', resizeCables);
resizeCables();
```

## Performance Optimization

### Before Export

1. **Remove unused ops** - Clean up your patch
2. **Optimize textures** - Use appropriate sizes
3. **Reduce polygon count** - Simplify 3D models
4. **Minimize audio files** - Compress audio

### Asset Optimization

**Images:**
- Use WebP format when possible
- Use power-of-2 dimensions
- Compress with tools like TinyPNG

**3D Models:**
- Use glTF/GLB format
- Remove unnecessary detail
- Use Draco compression

**Audio:**
- Use MP3 or OGG
- Compress appropriately
- Consider streaming for long files

### Loading Optimization

```javascript
// Show loading progress
CABLES.patch = new CABLES.Patch({
    patchFile: 'patch.js',
    onLoadingProgress: function(percent) {
        document.getElementById('loader').style.width = percent + '%';
    },
    onFinishedLoading: function() {
        document.getElementById('loader').style.display = 'none';
    }
});
```

## Deployment Checklist (The Stuff That Breaks at the Worst Time)

Before you publish, run through this list:

- **Loading**: Do you show a loader/progress bar for heavy patches?
- **Autoplay policies**: If you use audio/video/webcam, do you require a user click?
- **Mobile sanity**: Does it run on a mid-tier phone without overheating?
- **Resize**: Does it handle orientation changes and dynamic layout resizing?
- **Asset paths**: Are all assets included and paths correct on a case-sensitive host?
- **Cache behavior**: Are you accidentally serving old JS after updates?
- **Console**: Is the browser console clean (no noisy logs, no repeated warnings)?

### Cache Busting and Versioning

Static hosts cache aggressively. If you deploy a new version and still see the old one:

- add a version/hash to filenames (e.g. `ops.v123.js`)
- or configure cache headers (short cache for HTML, long cache for hashed assets)

### MIME Types (Especially for Wasm / Binary Assets)

Some servers mis-serve file types. If a resource fails to load, check response headers:

- `.wasm` should be served as `application/wasm`
- `.json` as `application/json`
- textures as correct image mime types

### CORS (Cross-Origin Assets)

If you load assets from another domain:

- ensure that server sends correct CORS headers
- prefer hosting assets alongside the patch when possible (simpler)

### Content Security Policy (CSP)

If your patch is embedded into a site with strict CSP, you may need to allow:

- fetching assets from required domains
- media playback sources

When possible, avoid “unsafe-inline” and instead rely on your host app’s approved patterns.

## CI/CD Ideas (Optional, But Great for Teams)

If you repeatedly export and deploy:

- treat the export zip as a build artifact
- deploy to staging on every change
- promote to prod when approved

Even a simple workflow that publishes static files to GitHub Pages can save time and reduce mistakes.

## Offline/PWA

Make your patch work offline as a Progressive Web App:

### manifest.json

```json
{
    "name": "My Cables App",
    "short_name": "CablesApp",
    "start_url": "/",
    "display": "standalone",
    "background_color": "#000000",
    "theme_color": "#000000",
    "icons": [
        {
            "src": "icon-192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "icon-512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ]
}
```

### Service Worker

```javascript
// sw.js
const CACHE_NAME = 'cables-app-v1';
const urlsToCache = [
    '/',
    '/index.html',
    '/js/cables.min.js',
    '/js/ops.js',
    '/js/patch.js',
    // Add your assets
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(urlsToCache))
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => response || fetch(event.request))
    );
});
```

## Electron Desktop Applications

For a truly native desktop experience, you can package your cables.gl export as an Electron application. Electron allows you to create cross-platform desktop apps using web technologies, perfect for distributing your cables.gl creations as standalone applications.

### Why Electron?

**Advantages:**
- Native desktop experience (menus, system tray, notifications)
- Full file system access
- Better performance control
- No browser UI chrome
- Can work offline completely
- Access to native OS APIs
- Professional distribution via installers

**Considerations:**
- Larger app size (~100-200MB)
- Requires code signing for distribution
- More complex build process
- Platform-specific considerations

### Getting Started with Electron

#### Project Structure

After exporting your cables.gl patch, set up an Electron project:

```
electron-app/
+-- package.json
+-- main.js              # Main Electron process
+-- preload.js           # Preload script (optional)
+-- renderer/
|   +-- index.html       # Your exported cables HTML
|   +-- js/
|   |   +-- cables.min.js
|   |   +-- ops.js
|   |   +-- patch.js
|   +-- assets/          # Your exported assets
+-- assets/
|   +-- icon.ico         # Windows icon
|   +-- icon.icns        # macOS icon
|   +-- icon.png         # Linux icon
+-- build/               # Build configuration
    +-- mac/
    +-- win/
    +-- linux/
```

#### Initial Setup

**package.json:**

```json
{
  "name": "my-cables-app",
  "version": "1.0.0",
  "description": "My Cables.gl Desktop App",
  "main": "main.js",
  "scripts": {
    "start": "electron .",
    "build": "electron-builder",
    "build:mac": "electron-builder --mac",
    "build:win": "electron-builder --win",
    "build:linux": "electron-builder --linux"
  },
  "build": {
    "appId": "com.yourcompany.cablesapp",
    "productName": "My Cables App",
    "directories": {
      "output": "dist"
    },
    "files": [
      "main.js",
      "preload.js",
      "renderer/**/*"
    ],
    "mac": {
      "icon": "assets/icon.icns",
      "category": "public.app-category.graphics-design"
    },
    "win": {
      "icon": "assets/icon.ico",
      "target": ["nsis", "portable"]
    },
    "linux": {
      "icon": "assets/icon.png",
      "target": ["AppImage", "deb"]
    }
  },
  "devDependencies": {
    "electron": "^28.0.0",
    "electron-builder": "^24.9.1"
  }
}
```

**Install dependencies:**

```bash
npm install --save-dev electron electron-builder
```

### Main Process (main.js)

The main process controls the application lifecycle and creates windows:

```javascript
const { app, BrowserWindow, Menu, ipcMain, dialog, shell } = require('electron');
const path = require('path');
const fs = require('fs').promises;

// Keep a global reference of the window object
let mainWindow;
let splashWindow;

// Determine if we're in development
const isDev = process.env.NODE_ENV === 'development' || !app.isPackaged;

function createSplashWindow() {
  splashWindow = new BrowserWindow({
    width: 400,
    height: 300,
    frame: false,
    transparent: true,
    alwaysOnTop: true,
    resizable: false,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true
    }
  });

  // Load splash screen HTML
  splashWindow.loadFile('splash.html');
  
  // Center the window
  splashWindow.center();
  
  return splashWindow;
}

function createMainWindow() {
  // Create the browser window
  mainWindow = new BrowserWindow({
    width: 1280,
    height: 720,
    minWidth: 800,
    minHeight: 600,
    show: false, // Don't show until ready
    frame: true,
    titleBarStyle: process.platform === 'darwin' ? 'hiddenInset' : 'default',
    backgroundColor: '#000000',
    icon: getIconPath(),
    webPreferences: {
      nodeIntegration: false, // Security: don't expose Node.js
      contextIsolation: true, // Security: isolate context
      preload: path.join(__dirname, 'preload.js'), // Preload script
      webSecurity: !isDev, // Disable in dev for easier debugging
      enableRemoteModule: false
    }
  });

  // Load your exported cables.gl patch
  if (isDev) {
    mainWindow.loadFile('renderer/index.html');
    // Open DevTools in development
    mainWindow.webContents.openDevTools();
  } else {
    mainWindow.loadFile(path.join(__dirname, 'renderer/index.html'));
  }

  // Show window when ready to prevent visual flash
  mainWindow.once('ready-to-show', () => {
    if (splashWindow) {
      splashWindow.close();
      splashWindow = null;
    }
    mainWindow.show();
    
    // Focus the window
    if (isDev) {
      mainWindow.focus();
    }
  });

  // Handle window closed
  mainWindow.on('closed', () => {
    mainWindow = null;
  });

  // Handle external links
  mainWindow.webContents.setWindowOpenHandler(({ url }) => {
    shell.openExternal(url);
    return { action: 'deny' };
  });

  // Prevent navigation to external URLs
  mainWindow.webContents.on('will-navigate', (event, navigationUrl) => {
    const parsedUrl = new URL(navigationUrl);
    
    if (parsedUrl.origin !== 'file://') {
      event.preventDefault();
      shell.openExternal(navigationUrl);
    }
  });

  return mainWindow;
}

function getIconPath() {
  if (process.platform === 'win32') {
    return path.join(__dirname, 'assets/icon.ico');
  } else if (process.platform === 'darwin') {
    return path.join(__dirname, 'assets/icon.icns');
  } else {
    return path.join(__dirname, 'assets/icon.png');
  }
}

function createMenu() {
  const template = [
    {
      label: 'File',
      submenu: [
        {
          label: 'Load Settings',
          accelerator: 'CmdOrCtrl+O',
          click: async () => {
            const result = await dialog.showOpenDialog(mainWindow, {
              properties: ['openFile'],
              filters: [
                { name: 'JSON Files', extensions: ['json'] },
                { name: 'All Files', extensions: ['*'] }
              ]
            });
            
            if (!result.canceled && result.filePaths.length > 0) {
              mainWindow.webContents.send('load-settings', result.filePaths[0]);
            }
          }
        },
        {
          label: 'Save Settings',
          accelerator: 'CmdOrCtrl+S',
          click: async () => {
            const result = await dialog.showSaveDialog(mainWindow, {
              filters: [
                { name: 'JSON Files', extensions: ['json'] },
                { name: 'All Files', extensions: ['*'] }
              ],
              defaultPath: 'settings.json'
            });
            
            if (!result.canceled) {
              mainWindow.webContents.send('save-settings', result.filePath);
            }
          }
        },
        { type: 'separator' },
        {
          label: 'Exit',
          accelerator: process.platform === 'darwin' ? 'Cmd+Q' : 'Ctrl+Q',
          click: () => {
            app.quit();
          }
        }
      ]
    },
    {
      label: 'Edit',
      submenu: [
        { role: 'undo', label: 'Undo' },
        { role: 'redo', label: 'Redo' },
        { type: 'separator' },
        { role: 'cut', label: 'Cut' },
        { role: 'copy', label: 'Copy' },
        { role: 'paste', label: 'Paste' },
        { role: 'selectAll', label: 'Select All' }
      ]
    },
    {
      label: 'View',
      submenu: [
        { role: 'reload', label: 'Reload' },
        { role: 'forceReload', label: 'Force Reload' },
        { role: 'toggleDevTools', label: 'Toggle Developer Tools' },
        { type: 'separator' },
        { role: 'resetZoom', label: 'Actual Size' },
        { role: 'zoomIn', label: 'Zoom In' },
        { role: 'zoomOut', label: 'Zoom Out' },
        { type: 'separator' },
        { role: 'togglefullscreen', label: 'Toggle Fullscreen' }
      ]
    },
    {
      label: 'Window',
      submenu: [
        { role: 'minimize', label: 'Minimize' },
        { role: 'close', label: 'Close' }
      ]
    },
    {
      label: 'Help',
      submenu: [
        {
          label: 'About',
          click: () => {
            dialog.showMessageBox(mainWindow, {
              type: 'info',
              title: 'About',
              message: 'My Cables App',
              detail: 'Version 1.0.0\nBuilt with cables.gl and Electron'
            });
          }
        }
      ]
    }
  ];

  // macOS specific menu adjustments
  if (process.platform === 'darwin') {
    template.unshift({
      label: app.getName(),
      submenu: [
        { role: 'about', label: 'About ' + app.getName() },
        { type: 'separator' },
        { role: 'services', label: 'Services' },
        { type: 'separator' },
        { role: 'hide', label: 'Hide ' + app.getName() },
        { role: 'hideOthers', label: 'Hide Others' },
        { role: 'unhide', label: 'Show All' },
        { type: 'separator' },
        { role: 'quit', label: 'Quit ' + app.getName() }
      ]
    });

    // Window menu
    template[4].submenu = [
      { role: 'close', label: 'Close' },
      { role: 'minimize', label: 'Minimize' },
      { role: 'zoom', label: 'Zoom' },
      { type: 'separator' },
      { role: 'front', label: 'Bring All to Front' }
    ];
  }

  const menu = Menu.buildFromTemplate(template);
  Menu.setApplicationMenu(menu);
}

// IPC Handlers for inter-process communication
function setupIpcHandlers() {
  // Handle file reading
  ipcMain.handle('read-file', async (event, filePath) => {
    try {
      const data = await fs.readFile(filePath, 'utf-8');
      return { success: true, data: JSON.parse(data) };
    } catch (error) {
      return { success: false, error: error.message };
    }
  });

  // Handle file writing
  ipcMain.handle('write-file', async (event, filePath, data) => {
    try {
      await fs.writeFile(filePath, JSON.stringify(data, null, 2), 'utf-8');
      return { success: true };
    } catch (error) {
      return { success: false, error: error.message };
    }
  });

  // Get app version
  ipcMain.handle('get-app-version', () => {
    return app.getVersion();
  });

  // Get user data path
  ipcMain.handle('get-user-data-path', () => {
    return app.getPath('userData');
  });

  // Window control
  ipcMain.on('window-minimize', () => {
    if (mainWindow) mainWindow.minimize();
  });

  ipcMain.on('window-maximize', () => {
    if (mainWindow) {
      if (mainWindow.isMaximized()) {
        mainWindow.unmaximize();
      } else {
        mainWindow.maximize();
      }
    }
  });

  ipcMain.on('window-close', () => {
    if (mainWindow) mainWindow.close();
  });
}

// App event handlers
app.whenReady().then(() => {
  // Create splash screen
  createSplashWindow();
  
  // Create main window after a short delay (simulate loading)
  setTimeout(() => {
    createMainWindow();
    createMenu();
    setupIpcHandlers();
  }, 1500);

  app.on('activate', () => {
    // On macOS, re-create window when dock icon is clicked
    if (BrowserWindow.getAllWindows().length === 0) {
      createMainWindow();
    }
  });
});

app.on('window-all-closed', () => {
  // On macOS, keep app running even when all windows are closed
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

// Security: Prevent new window creation
app.on('web-contents-created', (event, contents) => {
  contents.on('new-window', (event, navigationUrl) => {
    event.preventDefault();
    shell.openExternal(navigationUrl);
  });
});
```

### Preload Script (preload.js)

The preload script safely exposes Node.js APIs to the renderer process:

```javascript
const { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods that allow the renderer process
// to use ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld('electronAPI', {
  // File operations
  readFile: (filePath) => ipcRenderer.invoke('read-file', filePath),
  writeFile: (filePath, data) => ipcRenderer.invoke('write-file', filePath, data),
  
  // App info
  getAppVersion: () => ipcRenderer.invoke('get-app-version'),
  getUserDataPath: () => ipcRenderer.invoke('get-user-data-path'),
  
  // Window control
  minimizeWindow: () => ipcRenderer.send('window-minimize'),
  maximizeWindow: () => ipcRenderer.send('window-maximize'),
  closeWindow: () => ipcRenderer.send('window-close'),
  
  // Listen for messages from main process
  onLoadSettings: (callback) => {
    ipcRenderer.on('load-settings', (event, filePath) => callback(filePath));
  },
  onSaveSettings: (callback) => {
    ipcRenderer.on('save-settings', (event, filePath) => callback(filePath));
  },
  
  // Remove listeners
  removeAllListeners: (channel) => {
    ipcRenderer.removeAllListeners(channel);
  }
});
```

### Advanced Window Configuration

#### Window Options Deep Dive

```javascript
const mainWindow = new BrowserWindow({
  // Size and position
  width: 1280,
  height: 720,
  minWidth: 800,
  minHeight: 600,
  maxWidth: 3840,
  maxHeight: 2160,
  x: undefined, // Center if undefined
  y: undefined,
  center: true, // Center on screen
  
  // Appearance
  frame: true, // Show window frame
  titleBarStyle: 'default', // 'default', 'hidden', 'hiddenInset', 'customButtonsOnHover'
  transparent: false, // Transparent window (performance impact)
  backgroundColor: '#000000', // Background color before content loads
  opacity: 1.0, // Window opacity (0.0 to 1.0)
  vibrancy: 'ultra-dark', // macOS only: 'appearance-based', 'light', 'dark', etc.
  visualEffectState: 'active', // macOS only: 'active', 'inactive', 'followsWindowActiveState'
  
  // Behavior
  show: false, // Don't show until ready
  alwaysOnTop: false, // Keep window on top
  fullscreen: false, // Start in fullscreen
  fullscreenable: true, // Allow fullscreen
  simpleFullscreen: false, // macOS simple fullscreen
  skipTaskbar: false, // Don't show in taskbar
  kiosk: false, // Kiosk mode (fullscreen, no exit)
  closable: true, // Allow closing
  minimizable: true, // Allow minimizing
  maximizable: true, // Allow maximizing
  resizable: true, // Allow resizing
  movable: true, // Allow moving
  focusable: true, // Can receive focus
  
  // Window state
  autoHideMenuBar: false, // Auto-hide menu bar
  useContentSize: false, // Use content size instead of window size
  title: 'My Cables App', // Window title
  
  // Icon
  icon: getIconPath(), // Window icon
  
  // Web preferences
  webPreferences: {
    nodeIntegration: false,
    contextIsolation: true,
    preload: path.join(__dirname, 'preload.js'),
    webSecurity: true,
    allowRunningInsecureContent: false,
    experimentalFeatures: false,
    enableBlinkFeatures: '',
    disableBlinkFeatures: '',
    sandbox: false, // Enable sandbox for extra security
    enableRemoteModule: false,
    backgroundThrottling: true, // Throttle when backgrounded
    offscreen: false, // Use offscreen rendering
    webviewTag: false // Disable webview tag
  }
});
```

#### Window State Persistence

Save and restore window position and size:

```javascript
const Store = require('electron-store');

const store = new Store({
  name: 'window-state',
  defaults: {
    width: 1280,
    height: 720,
    x: undefined,
    y: undefined,
    isMaximized: false
  }
});

function createMainWindow() {
  const windowState = store.get('windowState', {});
  
  const mainWindow = new BrowserWindow({
    width: windowState.width || 1280,
    height: windowState.height || 720,
    x: windowState.x,
    y: windowState.y,
    // ... other options
  });

  // Restore maximized state
  if (windowState.isMaximized) {
    mainWindow.maximize();
  }

  // Save window state on move/resize
  const saveWindowState = () => {
    const bounds = mainWindow.getBounds();
    store.set('windowState', {
      width: bounds.width,
      height: bounds.height,
      x: bounds.x,
      y: bounds.y,
      isMaximized: mainWindow.isMaximized()
    });
  };

  mainWindow.on('moved', saveWindowState);
  mainWindow.on('resized', saveWindowState);
  mainWindow.on('maximize', () => {
    store.set('windowState.isMaximized', true);
  });
  mainWindow.on('unmaximize', () => {
    store.set('windowState.isMaximized', false);
  });

  return mainWindow;
}
```

Install electron-store:
```bash
npm install electron-store
```

### Inter-Window Communication

Electron supports multiple windows with various communication patterns:

#### Method 1: IPC (Inter-Process Communication)

**Main Process -> Renderer Process:**

```javascript
// In main.js
mainWindow.webContents.send('message-from-main', {
  type: 'update',
  data: { value: 42 }
});

// In renderer (index.html or your cables patch)
window.electronAPI.onMessage((data) => {
  console.log('Received:', data);
});
```

**Renderer Process -> Main Process:**

```javascript
// In preload.js
contextBridge.exposeInMainWorld('electronAPI', {
  sendToMain: (channel, data) => {
    ipcRenderer.send(channel, data);
  },
  onMessage: (callback) => {
    ipcRenderer.on('message-from-main', (event, data) => callback(data));
  }
});

// In renderer
window.electronAPI.sendToMain('message-from-renderer', {
  action: 'save',
  data: { settings: {...} }
});
```

#### Method 2: Multiple Windows Communication

```javascript
// In main.js
let windows = [];

function createWindow(id) {
  const window = new BrowserWindow({
    // ... window options
    webPreferences: {
      // ... web preferences
    }
  });

  window.id = id;
  windows.push(window);

  window.on('closed', () => {
    windows = windows.filter(w => w.id !== id);
  });

  return window;
}

// Broadcast to all windows
function broadcastToAllWindows(channel, data) {
  windows.forEach(window => {
    if (window && !window.isDestroyed()) {
      window.webContents.send(channel, data);
    }
  });
}

// Send to specific window
function sendToWindow(windowId, channel, data) {
  const window = windows.find(w => w.id === windowId);
  if (window && !window.isDestroyed()) {
    window.webContents.send(channel, data);
  }
}

// Example: Sync settings across windows
ipcMain.on('update-settings', (event, settings) => {
  // Save settings
  store.set('settings', settings);
  
  // Broadcast to all windows
  broadcastToAllWindows('settings-updated', settings);
});
```

#### Method 3: Shared Data via Main Process

```javascript
// In main.js
let sharedData = {
  settings: {},
  state: {}
};

// Get shared data
ipcMain.handle('get-shared-data', (event, key) => {
  return sharedData[key];
});

// Set shared data
ipcMain.handle('set-shared-data', (event, key, value) => {
  sharedData[key] = value;
  // Notify all windows
  broadcastToAllWindows('shared-data-changed', { key, value });
  return true;
});
```

#### Method 4: Window-to-Window via Main Process

```javascript
// Window A sends message to Window B
ipcMain.on('send-to-window', (event, targetWindowId, channel, data) => {
  sendToWindow(targetWindowId, channel, data);
});

// In preload.js
contextBridge.exposeInMainWorld('electronAPI', {
  sendToWindow: (targetWindowId, channel, data) => {
    ipcRenderer.send('send-to-window', targetWindowId, channel, data);
  },
  onWindowMessage: (callback) => {
    ipcRenderer.on('window-message', (event, data) => callback(data));
  }
});
```

### Splash Screen Implementation

A professional splash screen improves perceived performance:

**splash.html:**

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    body {
      width: 400px;
      height: 300px;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: white;
      overflow: hidden;
    }
    
    .logo {
      width: 80px;
      height: 80px;
      margin-bottom: 20px;
      animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.1); opacity: 0.8; }
    }
    
    .app-name {
      font-size: 24px;
      font-weight: 600;
      margin-bottom: 10px;
    }
    
    .version {
      font-size: 12px;
      opacity: 0.8;
      margin-bottom: 30px;
    }
    
    .loader {
      width: 200px;
      height: 4px;
      background: rgba(255, 255, 255, 0.2);
      border-radius: 2px;
      overflow: hidden;
      position: relative;
    }
    
    .loader-bar {
      height: 100%;
      background: white;
      width: 0%;
      animation: loading 2s ease-in-out infinite;
      border-radius: 2px;
    }
    
    @keyframes loading {
      0% { width: 0%; }
      50% { width: 70%; }
      100% { width: 100%; }
    }
    
    .status {
      margin-top: 20px;
      font-size: 12px;
      opacity: 0.7;
    }
  </style>
</head>
<body>
  <div class="logo">
    <!-- Your logo SVG or image -->
    <svg viewBox="0 0 100 100" fill="white">
      <circle cx="50" cy="50" r="40" stroke="white" stroke-width="2" fill="none"/>
      <path d="M30 50 L45 65 L70 35" stroke="white" stroke-width="3" fill="none"/>
    </svg>
  </div>
  <div class="app-name">My Cables App</div>
  <div class="version">Version 1.0.0</div>
  <div class="loader">
    <div class="loader-bar"></div>
  </div>
  <div class="status" id="status">Loading...</div>
  
  <script>
    // Update status from main process
    const { ipcRenderer } = require('electron');
    
    ipcRenderer.on('splash-status', (event, message) => {
      document.getElementById('status').textContent = message;
    });
    
    ipcRenderer.on('splash-progress', (event, percent) => {
      document.querySelector('.loader-bar').style.width = percent + '%';
    });
  </script>
</body>
</html>
```

**Enhanced main.js with splash screen:**

```javascript
function createSplashWindow() {
  splashWindow = new BrowserWindow({
    width: 400,
    height: 300,
    frame: false,
    transparent: true,
    alwaysOnTop: true,
    resizable: false,
    webPreferences: {
      nodeIntegration: true, // Needed for splash screen
      contextIsolation: false
    }
  });

  splashWindow.loadFile('splash.html');
  splashWindow.center();
  
  // Update splash screen status
  const updateSplashStatus = (message) => {
    if (splashWindow && !splashWindow.isDestroyed()) {
      splashWindow.webContents.send('splash-status', message);
    }
  };
  
  const updateSplashProgress = (percent) => {
    if (splashWindow && !splashWindow.isDestroyed()) {
      splashWindow.webContents.send('splash-progress', percent);
    }
  };
  
  // Simulate loading progress
  updateSplashStatus('Initializing...');
  updateSplashProgress(10);
  
  setTimeout(() => {
    updateSplashStatus('Loading assets...');
    updateSplashProgress(40);
  }, 300);
  
  setTimeout(() => {
    updateSplashStatus('Preparing renderer...');
    updateSplashProgress(70);
  }, 800);
  
  setTimeout(() => {
    updateSplashStatus('Almost ready...');
    updateSplashProgress(90);
  }, 1200);
  
  return { splashWindow, updateSplashStatus, updateSplashProgress };
}

// In app.whenReady()
app.whenReady().then(() => {
  const { splashWindow: splash, updateSplashStatus } = createSplashWindow();
  
  updateSplashStatus('Creating main window...');
  
  setTimeout(() => {
    createMainWindow();
    createMenu();
    setupIpcHandlers();
    
    // Close splash when main window is ready
    mainWindow.once('ready-to-show', () => {
      setTimeout(() => {
        if (splash && !splash.isDestroyed()) {
          splash.close();
        }
        mainWindow.show();
      }, 500); // Small delay for smooth transition
    });
  }, 1500);
});
```

### JSON File Operations

Saving and loading JSON data is essential for app settings, user preferences, and state persistence:

#### Method 1: Using IPC Handlers (Recommended)

**In main.js:**

```javascript
const fs = require('fs').promises;
const path = require('path');

// Get user data directory
const getUserDataPath = () => {
  return app.getPath('userData');
};

// Ensure directory exists
async function ensureDirectory(dirPath) {
  try {
    await fs.mkdir(dirPath, { recursive: true });
  } catch (error) {
    console.error('Error creating directory:', error);
  }
}

// IPC Handlers for JSON operations
ipcMain.handle('save-json', async (event, filename, data) => {
  try {
    const userDataPath = getUserDataPath();
    const filePath = path.join(userDataPath, filename);
    
    await ensureDirectory(path.dirname(filePath));
    await fs.writeFile(filePath, JSON.stringify(data, null, 2), 'utf-8');
    
    return { success: true, path: filePath };
  } catch (error) {
    console.error('Error saving JSON:', error);
    return { success: false, error: error.message };
  }
});

ipcMain.handle('load-json', async (event, filename) => {
  try {
    const userDataPath = getUserDataPath();
    const filePath = path.join(userDataPath, filename);
    
    const data = await fs.readFile(filePath, 'utf-8');
    return { success: true, data: JSON.parse(data) };
  } catch (error) {
    if (error.code === 'ENOENT') {
      // File doesn't exist, return default
      return { success: true, data: null };
    }
    console.error('Error loading JSON:', error);
    return { success: false, error: error.message };
  }
});

ipcMain.handle('delete-json', async (event, filename) => {
  try {
    const userDataPath = getUserDataPath();
    const filePath = path.join(userDataPath, filename);
    
    await fs.unlink(filePath);
    return { success: true };
  } catch (error) {
    if (error.code === 'ENOENT') {
      return { success: true }; // Already deleted
    }
    console.error('Error deleting JSON:', error);
    return { success: false, error: error.message };
  }
});

ipcMain.handle('list-json-files', async (event, directory = '') => {
  try {
    const userDataPath = getUserDataPath();
    const dirPath = path.join(userDataPath, directory);
    
    const files = await fs.readdir(dirPath);
    const jsonFiles = files.filter(file => file.endsWith('.json'));
    
    return { success: true, files: jsonFiles };
  } catch (error) {
    console.error('Error listing JSON files:', error);
    return { success: false, error: error.message };
  }
});
```

**In preload.js:**

```javascript
contextBridge.exposeInMainWorld('electronAPI', {
  // JSON file operations
  saveJSON: async (filename, data) => {
    return await ipcRenderer.invoke('save-json', filename, data);
  },
  
  loadJSON: async (filename) => {
    return await ipcRenderer.invoke('load-json', filename);
  },
  
  deleteJSON: async (filename) => {
    return await ipcRenderer.invoke('delete-json', filename);
  },
  
  listJSONFiles: async (directory = '') => {
    return await ipcRenderer.invoke('list-json-files', directory);
  }
});
```

**In your renderer (cables patch or HTML):**

```javascript
// Save settings
async function saveSettings(settings) {
  const result = await window.electronAPI.saveJSON('settings.json', settings);
  if (result.success) {
    console.log('Settings saved to:', result.path);
  } else {
    console.error('Failed to save settings:', result.error);
  }
}

// Load settings
async function loadSettings() {
  const result = await window.electronAPI.loadJSON('settings.json');
  if (result.success) {
    if (result.data) {
      console.log('Settings loaded:', result.data);
      return result.data;
    } else {
      // Return default settings
      return getDefaultSettings();
    }
  } else {
    console.error('Failed to load settings:', result.error);
    return getDefaultSettings();
  }
}

// Example usage with cables.gl patch
async function initializeApp() {
  // Load saved settings
  const settings = await loadSettings();
  
  // Apply settings to cables patch
  if (window.CABLES && window.CABLES.patch) {
    Object.keys(settings).forEach(key => {
      window.CABLES.patch.setVariable(key, settings[key]);
    });
  }
  
  // Listen for settings changes and auto-save
  if (window.CABLES && window.CABLES.patch) {
    window.CABLES.patch.on('variableChanged', async (name, value) => {
      const currentSettings = await loadSettings();
      currentSettings[name] = value;
      await saveSettings(currentSettings);
    });
  }
}

// Save cables patch state
async function savePatchState() {
  if (!window.CABLES || !window.CABLES.patch) return;
  
  const state = {
    timestamp: new Date().toISOString(),
    variables: {},
    camera: {
      position: window.CABLES.patch.cgl?.camera?.position || null,
      rotation: window.CABLES.patch.cgl?.camera?.rotation || null
    }
  };
  
  // Save all variables
  // (You'll need to track variable names or get them from your patch)
  const variableNames = ['color', 'speed', 'intensity']; // Your variable names
  variableNames.forEach(name => {
    state.variables[name] = window.CABLES.patch.getVariable(name);
  });
  
  await window.electronAPI.saveJSON('patch-state.json', state);
}

// Load patch state
async function loadPatchState() {
  const result = await window.electronAPI.loadJSON('patch-state.json');
  if (result.success && result.data) {
    const state = result.data;
    
    // Restore variables
    Object.keys(state.variables).forEach(name => {
      window.CABLES.patch.setVariable(name, state.variables[name]);
    });
    
    // Restore camera if available
    if (state.camera && window.CABLES.patch.cgl?.camera) {
      // Camera restoration depends on your cables setup
    }
  }
}
```

#### Method 2: Using electron-store (Simpler)

```bash
npm install electron-store
```

```javascript
// In main.js
const Store = require('electron-store');

const store = new Store({
  name: 'app-settings',
  defaults: {
    theme: 'dark',
    windowState: {
      width: 1280,
      height: 720
    },
    cablesSettings: {
      color: [1, 0, 0, 1],
      speed: 1.0
    }
  }
});

// Expose store to renderer
ipcMain.handle('store-get', (event, key) => {
  return store.get(key);
});

ipcMain.handle('store-set', (event, key, value) => {
  store.set(key, value);
  return true;
});

ipcMain.handle('store-delete', (event, key) => {
  store.delete(key);
  return true;
});

ipcMain.handle('store-clear', () => {
  store.clear();
  return true;
});

ipcMain.handle('store-all', () => {
  return store.store;
});
```

```javascript
// In preload.js
contextBridge.exposeInMainWorld('electronAPI', {
  store: {
    get: (key) => ipcRenderer.invoke('store-get', key),
    set: (key, value) => ipcRenderer.invoke('store-set', key, value),
    delete: (key) => ipcRenderer.invoke('store-delete', key),
    clear: () => ipcRenderer.invoke('store-clear'),
    all: () => ipcRenderer.invoke('store-all')
  }
});
```

```javascript
// In renderer
// Get setting
const theme = await window.electronAPI.store.get('theme');

// Set setting
await window.electronAPI.store.set('cablesSettings.color', [0, 1, 0, 1]);

// Get all settings
const allSettings = await window.electronAPI.store.all();
```

### Code Signing for Distribution

Code signing is essential for smooth app distribution on macOS and Windows. Unsigned apps trigger security warnings and may be blocked.

#### macOS Code Signing

**Requirements:**
- Apple Developer Account ($99/year)
- Valid code signing certificate
- Notarization (required for macOS 10.15+)

**package.json configuration:**

```json
{
  "build": {
    "appId": "com.yourcompany.cablesapp",
    "mac": {
      "icon": "assets/icon.icns",
      "category": "public.app-category.graphics-design",
      "target": [
        {
          "target": "dmg",
          "arch": ["x64", "arm64"]
        },
        {
          "target": "zip",
          "arch": ["x64", "arm64"]
        }
      ],
      "hardenedRuntime": true,
      "gatekeeperAssess": false,
      "entitlements": "build/mac/entitlements.mac.plist",
      "entitlementsInherit": "build/mac/entitlements.mac.plist"
    },
    "afterSign": "scripts/notarize.js",
    "notarize": {
      "teamId": "YOUR_TEAM_ID"
    }
  }
}
```

**entitlements.mac.plist:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>com.apple.security.cs.allow-jit</key>
  <true/>
  <key>com.apple.security.cs.allow-unsigned-executable-memory</key>
  <true/>
  <key>com.apple.security.cs.allow-dyld-environment-variables</key>
  <true/>
  <key>com.apple.security.cs.disable-library-validation</key>
  <true/>
</dict>
</plist>
```

**scripts/notarize.js:**

```javascript
const { notarize } = require('@electron/notarize');

exports.default = async function notarizing(context) {
  const { electronPlatformName, appOutDir } = context;
  
  if (electronPlatformName !== 'darwin') {
    return;
  }

  const appName = context.packager.appInfo.productFilename;

  return await notarize({
    appBundleId: 'com.yourcompany.cablesapp',
    appPath: `${appOutDir}/${appName}.app`,
    appleId: process.env.APPLE_ID,
    appleIdPassword: process.env.APPLE_ID_PASSWORD,
    teamId: process.env.APPLE_TEAM_ID
  });
};
```

**Environment variables (.env or export):**

```bash
export APPLE_ID="your@email.com"
export APPLE_ID_PASSWORD="app-specific-password"
export APPLE_TEAM_ID="YOUR_TEAM_ID"
```

**Build command:**

```bash
npm run build:mac
```

#### Windows Code Signing

**Requirements:**
- Code signing certificate (purchased from certificate authority)
- Or use self-signed certificate for testing (not recommended for distribution)

**package.json configuration:**

```json
{
  "build": {
    "win": {
      "icon": "assets/icon.ico",
      "target": [
        {
          "target": "nsis",
          "arch": ["x64", "ia32"]
        },
        {
          "target": "portable",
          "arch": ["x64"]
        }
      ],
      "signingHashAlgorithms": ["sha256"],
      "sign": "build/win/sign.js",
      "certificateFile": "path/to/certificate.pfx",
      "certificatePassword": "${env.CERTIFICATE_PASSWORD}"
    }
  }
}
```

**build/win/sign.js:**

```javascript
const path = require('path');

exports.default = async function(configuration) {
  const { path: filePath } = configuration;
  
  // Only sign on Windows
  if (process.platform !== 'win32') {
    return;
  }

  // Use electron-builder's built-in signing
  // Or use signtool directly
  const { execSync } = require('child_process');
  
  const certPath = process.env.CERTIFICATE_PATH;
  const certPassword = process.env.CERTIFICATE_PASSWORD;
  
  if (!certPath || !certPassword) {
    console.warn('Certificate not configured, skipping signing');
    return;
  }

  try {
    execSync(
      `signtool sign /f "${certPath}" /p "${certPassword}" /t http://timestamp.digicert.com /d "My Cables App" "${filePath}"`,
      { stdio: 'inherit' }
    );
  } catch (error) {
    console.error('Signing failed:', error);
    throw error;
  }
};
```

**Alternative: Using electron-builder's built-in signing:**

```json
{
  "build": {
    "win": {
      "certificateFile": "path/to/certificate.pfx",
      "certificatePassword": "${env.CERTIFICATE_PASSWORD}",
      "signingHashAlgorithms": ["sha256"],
      "signDlls": true
    }
  }
}
```

**Build command:**

```bash
npm run build:win
```

#### App Registration and Metadata

**package.json - Complete build configuration:**

```json
{
  "name": "my-cables-app",
  "version": "1.0.0",
  "description": "My amazing Cables.gl application",
  "author": {
    "name": "Your Name",
    "email": "your@email.com"
  },
  "license": "MIT",
  "main": "main.js",
  "build": {
    "appId": "com.yourcompany.cablesapp",
    "productName": "My Cables App",
    "copyright": "Copyright © 2024 Your Company",
    "directories": {
      "output": "dist",
      "buildResources": "build"
    },
    "files": [
      "main.js",
      "preload.js",
      "renderer/**/*",
      "!renderer/**/*.map"
    ],
    "extraResources": [
      {
        "from": "assets/",
        "to": "assets/",
        "filter": ["**/*"]
      }
    ],
    "mac": {
      "icon": "assets/icon.icns",
      "category": "public.app-category.graphics-design",
      "minimumSystemVersion": "10.13",
      "darkModeSupport": true,
      "target": [
        {
          "target": "dmg",
          "arch": ["x64", "arm64"]
        }
      ],
      "hardenedRuntime": true,
      "entitlements": "build/mac/entitlements.mac.plist",
      "entitlementsInherit": "build/mac/entitlements.mac.plist"
    },
    "win": {
      "icon": "assets/icon.ico",
      "target": [
        {
          "target": "nsis",
          "arch": ["x64"]
        }
      ],
      "publisherName": "Your Company Name",
      "verifyUpdateCodeSignature": false
    },
    "linux": {
      "icon": "assets/icon.png",
      "target": [
        {
          "target": "AppImage",
          "arch": ["x64"]
        },
        {
          "target": "deb",
          "arch": ["x64"]
        }
      ],
      "category": "Graphics"
    },
    "nsis": {
      "oneClick": false,
      "allowToChangeInstallationDirectory": true,
      "createDesktopShortcut": true,
      "createStartMenuShortcut": true,
      "shortcutName": "My Cables App"
    },
    "dmg": {
      "title": "${productName} ${version}",
      "icon": "assets/icon.icns",
      "background": "build/mac/dmg-background.png",
      "contents": [
        {
          "x": 410,
          "y": 150,
          "type": "link",
          "path": "/Applications"
        },
        {
          "x": 130,
          "y": 150,
          "type": "file"
        }
      ],
      "window": {
        "width": 540,
        "height": 380
      }
    }
  }
}
```

### Building and Distributing

#### Development Build

```bash
# Start in development mode
npm start
```

#### Production Build

```bash
# Build for current platform
npm run build

# Build for specific platforms
npm run build:mac
npm run build:win
npm run build:linux

# Build for all platforms (requires platform-specific tools)
npm run build:all
```

#### Distribution Checklist

**Before Building:**
- [ ] Update version in package.json
- [ ] Test app thoroughly
- [ ] Optimize assets
- [ ] Prepare code signing certificates
- [ ] Set up environment variables
- [ ] Test on target platforms

**After Building:**
- [ ] Test installer on clean system
- [ ] Verify code signing
- [ ] Test auto-updater (if implemented)
- [ ] Check file associations
- [ ] Verify menu items work
- [ ] Test file operations
- [ ] Check window state persistence

### Advanced Electron Features

#### Auto-Updater

```bash
npm install electron-updater
```

```javascript
// In main.js
const { autoUpdater } = require('electron-updater');

autoUpdater.checkForUpdatesAndNotify();

autoUpdater.on('update-available', () => {
  dialog.showMessageBox(mainWindow, {
    type: 'info',
    title: 'Update Available',
    message: 'A new version is available. It will be downloaded in the background.',
    buttons: ['OK']
  });
});

autoUpdater.on('update-downloaded', () => {
  dialog.showMessageBox(mainWindow, {
    type: 'info',
    title: 'Update Ready',
    message: 'Update downloaded. The application will restart to apply the update.',
    buttons: ['Restart Now', 'Later']
  }).then(result => {
    if (result.response === 0) {
      autoUpdater.quitAndInstall();
    }
  });
});
```

#### System Tray

```javascript
const { Tray, Menu } = require('electron');
const path = require('path');

let tray = null;

function createTray() {
  const iconPath = path.join(__dirname, 'assets', 'tray-icon.png');
  tray = new Tray(iconPath);
  
  const contextMenu = Menu.buildFromTemplate([
    {
      label: 'Show App',
      click: () => {
        mainWindow.show();
      }
    },
    {
      label: 'Quit',
      click: () => {
        app.quit();
      }
    }
  ]);
  
  tray.setToolTip('My Cables App');
  tray.setContextMenu(contextMenu);
  
  tray.on('click', () => {
    mainWindow.isVisible() ? mainWindow.hide() : mainWindow.show();
  });
}
```

#### Native Notifications

```javascript
const { Notification } = require('electron');

function showNotification(title, body) {
  if (Notification.isSupported()) {
    new Notification({
      title: title,
      body: body,
      icon: getIconPath()
    }).show();
  }
}
```

### Performance Optimization for Electron

1. **Disable Node Integration in Renderer** - Use contextBridge instead
2. **Enable Context Isolation** - Better security and performance
3. **Use Hardware Acceleration** - Enabled by default
4. **Optimize Asset Loading** - Lazy load when possible
5. **Throttle Background Processes** - Use `backgroundThrottling: true`
6. **Monitor Memory Usage** - Use DevTools memory profiler

### Security Best Practices

1. **Never use `nodeIntegration: true`** - Use preload scripts instead
2. **Always use `contextIsolation: true`** - Isolates your code
3. **Validate all IPC messages** - Don't trust renderer input
4. **Use Content Security Policy** - Restrict resource loading
5. **Keep Electron updated** - Security patches are important
6. **Sanitize file paths** - Prevent directory traversal attacks

### Troubleshooting Electron Issues

**App won't start:**
- Check main.js for syntax errors
- Verify all dependencies are installed
- Check console for error messages

**Window is blank:**
- Verify file paths are correct
- Check DevTools for errors
- Ensure renderer files are included in build

**Code signing fails:**
- Verify certificate is valid
- Check environment variables are set
- Ensure certificate password is correct

**App is slow:**
- Check for memory leaks
- Optimize asset loading
- Use performance profiling tools

## Troubleshooting

### Common Issues

**"Assets not loading"**
- Check file paths are correct
- Ensure CORS headers are set for cross-origin assets
- Verify assets are included in export

**"Blank screen"**
- Check browser console for errors
- Verify all JavaScript files loaded
- Test on a local server (not file://)

**"Poor performance"**
- Reduce canvas resolution
- Lower texture sizes
- Simplify shaders
- Check for memory leaks

**"Works locally but not on server"**
- Check file paths (case-sensitive on Linux)
- Verify all files uploaded
- Check server MIME types

## Featured Videos

```vid
https://youtu.be/hVxrxXhH7vQ
Title: Cables.gl Standalone (Offline) Build: Create Without Limits!
Author: Decode GL
Thumbnail: https://i.ytimg.com/vi/hVxrxXhH7vQ/mqdefault.jpg
AuthorUrl: https://www.youtube.com/@Decode_gl
```

<!-- Add more export/deployment videos here -->

## Exercises

1. Export a simple patch and host it on GitHub Pages
2. Embed a cables patch as a website background
3. Create a loading screen for your patch
4. Set up communication between your patch and external JavaScript
5. **Electron Exercise**: Package your cables.gl export as an Electron app with a custom splash screen
6. **Electron Exercise**: Implement JSON save/load functionality to persist your patch settings
7. **Electron Exercise**: Set up code signing for macOS or Windows (requires developer account/certificate)
8. **Electron Exercise**: Create a multi-window Electron app with inter-window communication
9. **Electron Exercise**: Implement window state persistence (save/restore window position and size)
10. **Electron Exercise**: Add a system tray icon with context menu for your Electron app

---

---

## Congratulations!

You've completed the Cables.gl book! You now have the knowledge to:

- Create stunning 2D and 3D graphics
- Apply textures and materials
- Write custom shaders
- Build custom operators
- Create audio-reactive visuals
- Animate with timeline and code
- Export and deploy your creations

Keep experimenting, join the community, and share your creations!

**Resources:**
- [cables.gl](https://cables.gl) - Official website
- [cables.gl/docs](https://cables.gl/docs) - Documentation
- [Discord](https://discord.gg/cables) - Community chat


