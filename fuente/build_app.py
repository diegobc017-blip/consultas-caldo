"""Arma la app Consultas de Caldo a partir de la base química.

Uso (desde la carpeta del repositorio consultas-caldo):   python fuente/build_app.py

Busca base_quimica_caldo.json en la carpeta consultas (la que contiene a este repositorio).
Genera, en la raíz del repositorio:
  index.html, data.js, sw.js, manifest.webmanifest, icons/, fonts/, vendor/  -> la app instalable (GitHub Pages)
  consultas_caldo.html                                                       -> la app en un solo archivo (sin internet)
Si la carpeta de arriba es la carpeta consultas, también copia ahí consultas_caldo.html.
Con el argumento --artifact genera además artifact.html (versión para la vista previa de Claude).
"""
import base64, hashlib, json, os, runpy, shutil, sys

FUENTE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(FUENTE)
ARRIBA = os.path.dirname(REPO)

runpy.run_path(os.path.join(FUENTE, "build_data.py"))
data_js = open(os.path.join(FUENTE, "data.js"), encoding="utf-8").read()
tpl = open(os.path.join(FUENTE, "template.html"), encoding="utf-8").read()
leaflet_js = open(os.path.join(FUENTE, "vendor", "leaflet.js"), encoding="utf-8").read()
leaflet_css = open(os.path.join(FUENTE, "vendor", "leaflet.css"), encoding="utf-8").read()
shp_js = open(os.path.join(FUENTE, "vendor", "shp.min.js"), encoding="utf-8").read()
proj4_js = open(os.path.join(FUENTE, "vendor", "proj4.js"), encoding="utf-8").read()
sql_js = open(os.path.join(FUENTE, "vendor", "sql-wasm.js"), encoding="utf-8").read()
sql_wasm_b64 = base64.b64encode(open(os.path.join(FUENTE, "vendor", "sql-wasm.wasm"), "rb").read()).decode()

FONTS = [
    ("Atkinson Hyperlegible", "400", "normal", "atkinson-hyperlegible-latin-400-normal.woff2", None),
    ("Atkinson Hyperlegible", "700", "normal", "atkinson-hyperlegible-latin-700-normal.woff2", None),
    ("Atkinson Hyperlegible", "400", "italic", "atkinson-hyperlegible-latin-400-italic.woff2", None),
    ("Archivo", "100 900", "normal", "archivo-latin-standard-normal.woff2", "62% 125%"),
]

def fontface(inline):
    out = []
    for fam, w, st, f, stretch in FONTS:
        if inline:
            b = base64.b64encode(open(os.path.join(FUENTE, "fonts", f), "rb").read()).decode()
            src = f"url(data:font/woff2;base64,{b}) format('woff2')"
        else:
            src = f"url(fonts/{f}) format('woff2')"
        fs = f"font-stretch:{stretch};" if stretch else ""
        out.append(f"@font-face{{font-family:'{fam}';font-style:{st};font-weight:{w};{fs}font-display:swap;src:{src}}}")
    return "".join(out)

def fill(t, fonts_css, leaflet_css_txt, libs, data_tag):
    return (t.replace("/*__FONTFACE__*/", fonts_css).replace("/*__LEAFLETCSS__*/", leaflet_css_txt)
             .replace("<!--__LIBS__-->", libs).replace("<script>\n/*__DATA__*/\n</script>", data_tag))

HEAD_COMUN = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Productos SENAVE por rubro, armador de caldos con semáforo de compatibilidad, campos y lotes, historial y rotación de modos de acción.">
<meta name="theme-color" content="#18221D">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>
"""

def documento(head_extra, body_extra, **kw):
    t = fill(tpl, **kw)
    # cabeza: título y estilos; cuerpo: desde el encabezado de la app
    i = t.index("<header class=\"top\">")
    return f"<!doctype html>\n<html lang=\"es\">\n<head>\n{HEAD_COMUN}{head_extra}{t[:i]}\n</head>\n<body>\n{t[i:]}\n{body_extra}</body>\n</html>\n"

# 1) archivo único (todo adentro)
icon64 = base64.b64encode(open(os.path.join(FUENTE, "icons", "favicon-64.png"), "rb").read()).decode()
unico = documento(f'<link rel="icon" href="data:image/png;base64,{icon64}">\n', "",
                  fonts_css=fontface(True), leaflet_css_txt=leaflet_css,
                  libs=f"<script>{leaflet_js}</script>\n<script>{shp_js}</script>\n<script>{proj4_js}</script>\n<script>window.SQL_INLINE=true;</script>\n<script>{sql_js}</script>\n<script>window.SQL_WASM_B64=\"{sql_wasm_b64}\";</script>", data_tag="<script>\n" + data_js + "\n</script>")
open(os.path.join(REPO, "consultas_caldo.html"), "w", encoding="utf-8").write(unico)
if os.path.exists(os.path.join(ARRIBA, "base_quimica_caldo.json")):
    open(os.path.join(ARRIBA, "consultas_caldo.html"), "w", encoding="utf-8").write(unico)

# 2) app instalable (PWA) en la raíz del repositorio
for sub in ("fonts", "icons"):
    shutil.copytree(os.path.join(FUENTE, sub), os.path.join(REPO, sub), dirs_exist_ok=True)
os.makedirs(os.path.join(REPO, "vendor"), exist_ok=True)
for f in ("leaflet.js", "leaflet.css", "shp.min.js", "proj4.js", "sql-wasm.js", "sql-wasm.wasm"):
    shutil.copy(os.path.join(FUENTE, "vendor", f), os.path.join(REPO, "vendor", f))
open(os.path.join(REPO, "data.js"), "w", encoding="utf-8").write(data_js)
pwa_head = """<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/favicon-64.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="stylesheet" href="vendor/leaflet.css">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Caldo">
"""
sw_reg = """<script>
if ("serviceWorker" in navigator && location.protocol !== "file:") {
  addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
}
</script>
"""
index = documento(pwa_head, sw_reg, fonts_css=fontface(False), leaflet_css_txt="",
                  libs='<script src="vendor/leaflet.js"></script>\n<script src="vendor/shp.min.js"></script>\n<script src="vendor/proj4.js"></script>', data_tag='<script src="data.js"></script>')
open(os.path.join(REPO, "index.html"), "w", encoding="utf-8").write(index)

manifest = {
    "name": "Consultas de Caldo", "short_name": "Caldo", "lang": "es", "id": "./",
    "description": "Productos SENAVE por rubro, armador de caldos con semáforo de compatibilidad, campos, historial y rotación.",
    "start_url": "./", "scope": "./", "display": "standalone", "orientation": "any",
    "background_color": "#F2F4F1", "theme_color": "#18221D",
    "icons": [
        {"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": "icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
    ],
}
open(os.path.join(REPO, "manifest.webmanifest"), "w", encoding="utf-8").write(json.dumps(manifest, ensure_ascii=False, indent=1))

assets = ["./", "index.html", "data.js", "manifest.webmanifest", "vendor/leaflet.js", "vendor/leaflet.css", "vendor/shp.min.js", "vendor/proj4.js", "vendor/sql-wasm.js", "vendor/sql-wasm.wasm"] + \
    [f"icons/{f}" for f in sorted(os.listdir(os.path.join(REPO, "icons")))] + \
    [f"fonts/{f}" for f in sorted(os.listdir(os.path.join(REPO, "fonts")))]
version = hashlib.sha1((index + data_js).encode()).hexdigest()[:10]
sw = f"""// Service worker: guarda la app en el dispositivo para usarla sin internet.
// Solo borra sus propias versiones viejas (prefijo "caldo-"), nunca cachés de otras apps.
const VERSION = "caldo-{version}";
const ASSETS = {json.dumps(assets)};
self.addEventListener("install", e => {{
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()));
}});
self.addEventListener("activate", e => {{
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith("caldo-") && k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
}});
self.addEventListener("fetch", e => {{
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;          // mapas base: siempre de internet
  if (req.mode === "navigate") {{
    e.respondWith(fetch(req).then(r => {{ const c = r.clone(); caches.open(VERSION).then(x => x.put("index.html", c)); return r; }}).catch(() => caches.match("index.html")));
    return;
  }}
  e.respondWith(caches.match(req).then(r => r || fetch(req).then(res => {{
    const copy = res.clone(); caches.open(VERSION).then(c => c.put(req, copy)); return res;
  }})));
}});
"""
open(os.path.join(REPO, "sw.js"), "w", encoding="utf-8").write(sw)
open(os.path.join(REPO, ".nojekyll"), "w").write("")

# 3) versión para la vista previa de Claude (opcional)
if "--artifact" in sys.argv:
    art = fill(tpl, fonts_css=fontface(True), leaflet_css_txt=leaflet_css,
               libs='<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.js"></script>\n<script src="https://cdn.jsdelivr.net/npm/shpjs@4.0.4/dist/shp.min.js"></script>\n<script src="https://cdn.jsdelivr.net/npm/proj4@2.12.1/dist/proj4.js"></script>',
               data_tag="<script>\n" + data_js + "\n</script>")
    open(os.path.join(FUENTE, "artifact.html"), "w", encoding="utf-8").write(art)
print("App lista (versión", version + "): index.html y consultas_caldo.html")
