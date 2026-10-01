import json, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config_rubros import RUBROS, AI_RUBROS
from config_semaforo import NIVELES, MEDIDAS, REGLAS
from config_inertes import FAMILIAS, FORM_FAMILIA, INERTES, IMPUREZAS, SENALES_MAL_ESTADO, PRUEBA_CALIDAD_CASERA
from config_usos import OBJETIVOS, USOS, RESISTENCIA, PRINCIPIOS_ROTACION
from config_carryover import CULTIVOS, GRAM, HOJA, CARRY, SELECT, MOMENTOS
from config_reglas_extra import REGLAS_EXTRA, SEMAFORO_EXTRA, MEDIDAS_EXTRA, PROBLEMAS_EXTRA
import re

_AQUI = os.path.dirname(os.path.abspath(__file__))
# Busca la base: variable BASE_QUIMICA, datos/ del repositorio, o la carpeta consultas (arriba del repositorio)
_CAND = [os.environ.get("BASE_QUIMICA", ""), os.path.join(_AQUI, "..", "datos", "base_quimica_caldo.json"),
         os.path.join(_AQUI, "..", "..", "base_quimica_caldo.json")]
SRC = next((c for c in _CAND if c and os.path.exists(c)), None)
if not SRC:
    raise SystemExit("No encuentro base_quimica_caldo.json (en datos/ del repositorio, en la carpeta consultas o en BASE_QUIMICA=ruta).")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.js")
d = json.load(open(SRC, encoding="utf-8"))

def nopat(x):
    return {k: v for k, v in x.items() if k != "patron"}

faltan = set()
def rubros_producto(p):
    s = []
    solo_ady = True
    for c in p["componentes"]:
        if c["tipo"] == "ady":
            continue
        solo_ady = False
        r = AI_RUBROS.get(c["id"])
        if r is None:
            faltan.add(c["id"]); r = "AG"
        for x in r.split():
            if x not in s: s.append(x)
    if solo_ady:
        s = ["AG", "HO", "FO", "PA"]
    cu = (p.get("clase_uso") or "").upper()
    if "HORMIG" in cu:
        for x in ("FO", "PA"):
            if x not in s: s.append(x)
    if "GORGOJ" in cu or p["formulacion"] == "FUM":
        if "AL" not in s: s.append("AL")
    return "".join(x for x in s)

def compact(p, mant):
    return {
        "r": p["registro"], "n": p["producto"].strip(), "e": (p.get("registrante") or "").strip(),
        "fa": (p.get("fabricante") or "").strip(), "po": (p.get("pais_origen") or "").strip(),
        "c": p.get("clase_uso") or "", "t": (p.get("toxicologia") or "").strip(),
        "f": p["formulacion"], "fs": (p.get("formulacion_senave") or "").strip(), "u": p["uso"],
        "pa": (p.get("principio_activo_senave") or "").strip(),
        "k": [[c["tipo"], c["id"], c.get("forma"), c.get("concentracion_pct"), c.get("nombre_original")] for c in p["componentes"]],
        "d": p["derivado"], "s": rubros_producto(p), "m": mant,
        "v": p.get("vencimiento_registro"), "mh": p.get("mantenimiento_hasta"),
    }

prods = [compact(p, 0) for p in d["productos"]] + [compact(p, 1) for p in d["productos_mantenimiento_vencido"]]

# grupo de modo de acción normalizado (HRAC/IRAC/FRAC + código)
def grupo(moa):
    m = re.match(r"^(HRAC|IRAC|FRAC)\s+(M\d+|P\d+|UN|\d+(?:\.\d)?[A-Z]?)", moa or "")
    return f"{m.group(1)} {m.group(2)}" if m else None
activos = [nopat(x) for x in d["principios_activos"]]
for a in activos:
    a["grupo"] = grupo(a.get("modo_accion"))
    u = USOS.get(a["id"])
    if u: a["usos"], a["objetivos"] = u[0], u[1].split()
biologicos = [nopat(x) for x in d["biologicos"]] 
for b in biologicos:
    u = USOS.get(b["id"])
    if u: b["usos"], b["objetivos"] = u[0], u[1].split()
botanicos = [nopat(x) for x in d["extractos_botanicos"]]
for b in botanicos:
    u = USOS.get(b["id"])
    if u: b["usos"], b["objetivos"] = u[0], u[1].split()
sin_usos = [a["id"] for a in activos if a["id"] not in USOS]
print("activos sin usos:", sin_usos)
for k, v in USOS.items():
    for t in v[1].split(): assert t in OBJETIVOS, (k, t)
catalogo = d["catalogo_problemas"] + PROBLEMAS_EXTRA
diag = [dict(x) for x in d["diagnostico_por_sintoma"]]
for x in diag:
    if x["sintoma"].startswith("Daño en cultivos vecinos") or x["sintoma"].startswith("Más deriva"):
        x["problemas"] = x["problemas"] + ["PR32"]
    if x["sintoma"].startswith("El caldo se ve normal"):
        x["problemas"] = x["problemas"] + ["PR33"]
reglas = d["reglas_compatibilidad"] + REGLAS_EXTRA
REGLAS_ALL = dict(REGLAS); REGLAS_ALL.update(SEMAFORO_EXTRA)
MEDIDAS_ALL = dict(MEDIDAS); MEDIDAS_ALL.update(MEDIDAS_EXTRA)

DB = {
    "meta": {k: d["meta"][k] for k in ("titulo", "version", "fecha_generacion", "fuente_productos", "criterio_productos_actuales", "advertencias", "estadisticas", "fuentes_datos_quimicos")},
    "categorias_problemas": d["categorias_problemas"],
    "catalogo_problemas": catalogo,
    "diagnostico": diag,
    "calidad_agua": d["calidad_agua"],
    "orden_carga": d["orden_carga"],
    "formulaciones": [nopat(x) for x in d["formulaciones"]],
    "activos": activos,
    "coadyuvantes": [nopat(x) for x in d["coadyuvantes"]],
    "biologicos": biologicos,
    "botanicos": botanicos,
    "reglas": reglas,
    "reglas_generales": d["reglas_generales"],
    "prueba_jarra": d["prueba_de_jarra"],
    "productos": prods,
    "rubros": RUBROS, "ai_rubros": AI_RUBROS,
    "niveles": NIVELES, "medidas": MEDIDAS_ALL, "semaforo": REGLAS_ALL,
    "objetivos": OBJETIVOS, "resistencia": RESISTENCIA, "principios_rotacion": PRINCIPIOS_ROTACION,
    "familias": FAMILIAS, "form_familia": FORM_FAMILIA, "inertes": INERTES, "impurezas": IMPUREZAS,
    "cultivos": CULTIVOS, "cult_gram": GRAM, "cult_hoja": HOJA, "carry": CARRY, "select": SELECT, "momentos": MOMENTOS,
    "senales_mal_estado": SENALES_MAL_ESTADO, "prueba_calidad": PRUEBA_CALIDAD_CASERA,
}
# chequeos
_ids = {a['id'] for a in activos}
assert set(CARRY) <= _ids, set(CARRY) - _ids
assert set(SELECT) <= _ids, set(SELECT) - _ids
_herb = {a['id'] for a in activos if a['clase'] == 'herbicida'}
print('herbicidas sin carry-over:', sorted(_herb - set(CARRY)))
ids_reglas = {r["id"] for r in reglas}
assert ids_reglas == set(REGLAS_ALL), (ids_reglas ^ set(REGLAS_ALL))
for rid, (b, piso, meds) in REGLAS_ALL.items():
    for m in meds: assert m in MEDIDAS_ALL, (rid, m)
forms = {f["codigo"] for f in d["formulaciones"]}
assert forms <= set(FORM_FAMILIA), forms - set(FORM_FAMILIA)
print("sin rubro:", faltan)
print("sin inertes:", forms - set(INERTES))
cnt = collections.Counter(ch for p in prods for ch in [p["s"][i:i+2] for i in range(0, len(p["s"]), 2)])
print("productos por rubro:", cnt)
js = "window.DB=" + json.dumps(DB, ensure_ascii=False, separators=(",", ":")) + ";"
open(OUT, "w", encoding="utf-8").write(js)
print("data.js", round(len(js.encode()) / 1e6, 2), "MB")
