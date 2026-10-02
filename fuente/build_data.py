import json, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config_rubros import RUBROS, AI_RUBROS
from config_semaforo import NIVELES, MEDIDAS, REGLAS
from config_inertes import FAMILIAS, FORM_FAMILIA, INERTES, IMPUREZAS, SENALES_MAL_ESTADO, PRUEBA_CALIDAD_CASERA
from config_usos import OBJETIVOS, USOS, RESISTENCIA, PRINCIPIOS_ROTACION
from config_carryover import CULTIVOS, GRAM, HOJA, CARRY, SELECT, MOMENTOS
from config_rubro_uso import USO_RUBRO
import config_correcciones as CORR
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
# fecha de habilitación del registro (columna "Habilitación" del Excel del SENAVE)
_HAB = os.path.join(os.path.dirname(SRC), "habilitacion_senave.json")
if not os.path.exists(_HAB): _HAB = os.path.join(_AQUI, "..", "datos", "habilitacion_senave.json")
HAB = json.load(open(_HAB, encoding="utf-8"))["habilitacion"] if os.path.exists(_HAB) else {}

# ---- correcciones de la revisión (config_correcciones.py) ----
_todos = {x["id"]: x for x in d["principios_activos"] + d["biologicos"] + d["extractos_botanicos"]}
for _id, campos in CORR.ACTIVOS.items():
    assert _id in _todos, _id
    for k, v in campos.items():
        if k == "_nota": _todos[_id].setdefault("notas", []).append(v)
        else: _todos[_id][k] = v
for _p in d["productos"] + d["productos_mantenimiento_vencido"]:
    for _c in _p["componentes"]:
        if _p["registro"] in CORR.COMPONENTES and _c["id"] in CORR.COMPONENTES[_p["registro"]]:
            _c["concentracion_pct"] = CORR.COMPONENTES[_p["registro"]][_c["id"]]
_reg = {r["id"]: r for r in d["reglas_compatibilidad"]}
for _id, campos in CORR.REGLAS.items():
    assert _id in _reg, _id
    _reg[_id].update(campos)
for _o in d["orden_carga"]:
    if _o["paso"] in CORR.ORDEN_CARGA: _o["descripcion"] = CORR.ORDEN_CARGA[_o["paso"]]
d["reglas_compatibilidad"] = d["reglas_compatibilidad"] + CORR.REGLAS_NUEVAS

def nopat(x):
    return {k: v for k, v in x.items() if k != "patron"}

faltan = set()
def _rest_ok(rest, n, form):
    for t in rest.split():
        if t == "solo" and n != 1: return False
        if t.startswith("f:") and form not in t[2:].split(","): return False
    return True
def _es_sec(id_, x):
    e = USO_RUBRO.get(id_, {}).get(x)
    return bool(e and "sec" in e[2].split())
def _es_pri(id_, x):
    r = (AI_RUBROS.get(id_) or "").split()
    if r and r[0] == x: return True
    e = USO_RUBRO.get(id_, {}).get(x)
    return bool(e and "pri" in e[2].split())
def especificos(p, s):
    """Rubros donde el producto es específico: es exclusivo de ese rubro o alguno de sus activos
    tiene ese rubro como principal (los demás activos también se usan ahí)."""
    ids = list(dict.fromkeys(c["id"] for c in p["componentes"] if c["tipo"] != "ady"))
    if not ids: return ""
    rs = [s[i:i+2] for i in range(0, len(s), 2)]
    return "".join(x for x in rs if len(rs) == 1 or any(_es_pri(i, x) for i in ids))
def rubros_producto(p):
    """Devuelve (rubros propios, rubros de uso secundario) del producto comercial."""
    comps = [c for c in p["componentes"] if c["tipo"] != "ady"]
    if not comps:
        return "AGHOFOPA", ""
    ids = list(dict.fromkeys(c["id"] for c in comps))
    n = len(ids)
    sets, union, crudo = [], [], []
    for i in ids:
        r = AI_RUBROS.get(i)
        if r is None:
            faltan.add(i); r = "AG"
        crudo.append(r.split())
        ok = []
        for x in r.split():
            if x not in union: union.append(x)
            e = USO_RUBRO.get(i, {}).get(x)
            if e is None or _rest_ok(e[2], n, p["formulacion"]): ok.append(x)
        sets.append(ok)
    # el producto va en los rubros que comparten TODOS sus activos
    s = [x for x in union if all(x in o for o in sets)]
    if not s:   # sin rubro común con las restricciones: el rubro donde coinciden más activos
        cnt = collections.Counter(x for o in crudo for x in o)
        mx = max(cnt.values()); s = [x for x in union if cnt.get(x) == mx]
    if p["uso"] == "tratamiento_semillas" and "AG" in s:
        s = ["AG"]
    # uso secundario: algún activo solo se usa dirigido en ese rubro
    sec = [x for x in s if any(_es_sec(i, x) for i in ids)]
    s = [x for x in s if x not in sec]
    if not s and sec:   # todos sus rubros son secundarios: queda en el primero
        s = [sec.pop(0)]
    cu = (p.get("clase_uso") or "").upper()
    if "HORMIG" in cu:
        for x in ("FO", "PA"):
            if x not in s: s.append(x)
            if x in sec: sec.remove(x)
    if "GORGOJ" in cu or p["formulacion"] == "FUM":
        if "AL" not in s: s.append("AL")
    return "".join(s), "".join(sec)

def compact(p, mant):
    rp = rubros_producto(p)
    return {
        "r": p["registro"], "n": p["producto"].strip(), "e": (p.get("registrante") or "").strip(),
        "fa": (p.get("fabricante") or "").strip(), "po": (p.get("pais_origen") or "").strip(),
        "c": p.get("clase_uso") or "", "t": (p.get("toxicologia") or "").strip(),
        "f": p["formulacion"], "fs": (p.get("formulacion_senave") or "").strip(), "u": p["uso"],
        "pa": (p.get("principio_activo_senave") or "").strip(),
        "k": [[c["tipo"], c["id"], c.get("forma"), c.get("concentracion_pct"), c.get("nombre_original")] for c in p["componentes"]],
        "d": p["derivado"], "s": rp[0], "s2": rp[1], "es": especificos(p, rp[0]), "m": mant,
        "ha": HAB.get(p["registro"]), **({"nt": CORR.NOTAS_PRODUCTO[p["registro"]]} if p["registro"] in CORR.NOTAS_PRODUCTO else {}),
        "v": p.get("vencimiento_registro"), "mh": p.get("mantenimiento_hasta"),
    }

prods = [compact(p, 0) for p in d["productos"]] + [compact(p, 1) for p in d["productos_mantenimiento_vencido"]]

# grupo de modo de acción normalizado (HRAC/IRAC/FRAC + código)
def grupo(moa):
    m = re.match(r"^(HRAC|IRAC|FRAC)\s+(M\d+|P\d+|UN[A-Z]?|\d+(?:\.\d)?[A-Z]?)", moa or "")
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
def uso_rubros(a):
    ur = {}
    for x in (AI_RUBROS.get(a["id"]) or "").split():
        e = USO_RUBRO.get(a["id"], {}).get(x)
        if e:
            ur[x] = {"u": e[0], "o": e[1].split()}
            if "sec" in e[2].split(): ur[x]["sec"] = 1
        elif a.get("usos"): ur[x] = {"u": a["usos"], "o": a.get("objetivos", [])}
    if ur: a["ur"] = ur
for a in activos + biologicos + botanicos: uso_rubros(a)
for k, v in USO_RUBRO.items():
    assert k in AI_RUBROS, k
    assert set(v) <= set(AI_RUBROS[k].split()), (k, set(v) - set(AI_RUBROS[k].split()))
    for x, e in v.items():
        for t in e[1].split(): assert t in OBJETIVOS, (k, x, t)
_multi = [k for k, v in AI_RUBROS.items() if len(v.split()) > 1 and set(v.split()) - set(USO_RUBRO.get(k, {}))]
print("multirubro sin uso por rubro:", _multi)
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
REGLAS_ALL = dict(REGLAS); REGLAS_ALL.update(SEMAFORO_EXTRA); REGLAS_ALL.update(CORR.SEMAFORO_NUEVAS)
for _id, v in CORR.SEMAFORO_MOD.items():
    assert _id in REGLAS_ALL, _id
    REGLAS_ALL[_id] = v
MEDIDAS_ALL = {k: dict(v) for k, v in MEDIDAS.items()}; MEDIDAS_ALL.update(MEDIDAS_EXTRA)
for _id, campos in CORR.MEDIDAS.items(): MEDIDAS_ALL[_id].update(campos)

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
print("específicos por rubro:", collections.Counter(p["es"][i:i+2] for p in prods if not p["m"] for i in range(0, len(p["es"]), 2)))
print("uso secundario:", collections.Counter(p["s2"][i:i+2] for p in prods for i in range(0, len(p["s2"]), 2)))
js = "window.DB=" + json.dumps(DB, ensure_ascii=False, separators=(",", ":")) + ";"
open(OUT, "w", encoding="utf-8").write(js)
print("data.js", round(len(js.encode()) / 1e6, 2), "MB")
