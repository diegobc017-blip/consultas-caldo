import json, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config_rubros import RUBROS, AI_RUBROS
from config_semaforo import NIVELES, MEDIDAS, REGLAS
from config_inertes import FAMILIAS, FORM_FAMILIA, INERTES, IMPUREZAS, SENALES_MAL_ESTADO, PRUEBA_CALIDAD_CASERA
from config_usos import OBJETIVOS, USOS, RESISTENCIA, PRINCIPIOS_ROTACION
from config_carryover import CULTIVOS, GRAM, HOJA, CARRY, SELECT, MOMENTOS
from config_rubro_uso import USO_RUBRO
import config_correcciones as CORR
import config_equipos as EQ
import config_silvo as SV
import config_clima as CL
from config_reglas_extra import REGLAS_EXTRA, SEMAFORO_EXTRA, MEDIDAS_EXTRA, PROBLEMAS_EXTRA
import config_problemas as PB
import config_catalogo as CAT
import config_limpieza as LP
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
d["reglas_compatibilidad"] = d["reglas_compatibilidad"] + CORR.REGLAS_NUEVAS + EQ.REGLAS_AEREAS + SV.REGLAS_SILVO + CL.REGLAS_CLIMA

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

_AI_CLASE = {a["id"]: a["clase"] for a in d["principios_activos"]}
_BIO_CLASE = {"bio_bt": "insecticida", "bio_virus": "insecticida", "bio_hongo_entomo": "insecticida", "bio_macro": "insecticida",
              "bio_trichoderma": "fungicida", "bio_bacillus": "fungicida", "bio_pseudomonas": "fungicida", "bio_consorcio": "fungicida"}
_FAM = {"insecticida": "animal", "acaricida": "animal", "nematicida": "animal", "molusquicida": "animal", "rodenticida": "animal",
        "fungicida": "enf", "bactericida": "enf"}
_ORD = list(CAT.CLASES)
catalogo_notas = collections.Counter()
def catalogar(p):
    """Clase normalizada, origen, forma de uso y función (coadyuvantes) de un producto comercial."""
    cu = p.get("clase_uso") or ""
    sen = CAT.clases_senave(cu)
    comps = p["componentes"]
    tiene_ai = any(c["tipo"] in ("ai", "bio", "bot") for c in comps)
    comp = []
    for c in comps:
        x = None
        if c["tipo"] == "ai": x = CAT.COMP_CLASE.get(c["id"]) or CAT.CLASE_ACTIVO.get(_AI_CLASE.get(c["id"]))
        elif c["tipo"] == "bio" and not sen: x = _BIO_CLASE.get(c["id"])
        elif c["tipo"] == "bot" and not sen: x = "insecticida"
        elif c["tipo"] == "ady" and not tiene_ai and (not sen or "coadyuvante" in sen): x = CAT.COMP_CLASE.get(c["id"]) or "coadyuvante"
        if x and x not in comp: comp.append(x)
    cl = [k for k in _ORD if k in sen or k in comp]
    cx = None
    if sen and comp:
        fs = {_FAM.get(k, k) for k in sen}
        extra = [k for k in comp if _FAM.get(k, k) not in fs and k not in ("protector", "regulador")]
        if extra:
            cx = f"El SENAVE lo lista como {cu.strip()}; por su composición también es {', '.join(CAT.CLASES[k].lower() for k in extra)}."
            catalogo_notas[cu.strip() + " -> " + ",".join(extra)] += 1
    lt = CAT.LIMPIADORES.get(p["registro"])
    if lt: cl = ["limpiador"]
    elif p["registro"] in CAT.DESINFECTANTES: cl = ["desinfectante"]
    if any(c["tipo"] == "bio" for c in comps): org = "biologico"
    elif any(c["tipo"] == "bot" for c in comps): org = "botanico"
    elif any(_AI_CLASE.get(c["id"]) == "feromona" for c in comps if c["tipo"] == "ai"): org = "semioquimico"
    else: org = CAT.origen_senave(cu) or "quimico"
    cun = CAT._nk(cu)
    if p["uso"] == "tratamiento_semillas" or "SEMILLA" in cun or "CURASEM" in cun: us = "curasemillas"
    elif p["formulacion"] == "GB": us = "cebo"
    elif p["formulacion"] == "FUM": us = "fumigante"
    elif p["uso"] == "no_caldo": us = "otro"
    else: us = "pulverizacion"
    fn = []
    if lt: fn = ["limpiador"]
    elif "coadyuvante" in cl or "desinfectante" in cl:
        for c in comps:
            f = CAT.ADY_FUNCION.get(c["id"]) if c["tipo"] == "ady" else ("desinfectante" if CAT.COMP_CLASE.get(c["id"]) == "desinfectante" else None)
            if f and f not in fn: fn.append(f)
    out = {"cl": cl}
    if org != "quimico": out["or"] = org          # por defecto: químico
    if us != "pulverizacion": out["us"] = us      # por defecto: pulverización
    if fn: out["fn"] = fn
    if cx: out["cx"] = cx
    if lt: out["lt"] = lt
    elif p["registro"] in CAT.DESINFECTANTES: out["lt"] = {"conf": "desinfectante", "tipo": "desinfectante", "nota": CAT.DESINFECTANTES[p["registro"]]}
    return out

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
        **catalogar(p),
    }

prods = [compact(p, 0) for p in d["productos"]] + [compact(p, 1) for p in d["productos_mantenimiento_vencido"]]
print("clases:", collections.Counter(k for p in prods for k in p["cl"]).most_common())
print("sin clase:", [(p["r"], p["n"], p["c"]) for p in prods if not p["cl"]])
print("origen:", collections.Counter(p.get("or", "quimico") for p in prods), "uso:", collections.Counter(p.get("us", "pulverizacion") for p in prods))
print("clase SENAVE distinta de la composición:", catalogo_notas.most_common())
for p in prods:
    if "cx" in p: print("  ", p["r"], p["n"], "|", p["c"], "|", p["pa"][:90])
# Silvopastoril (SP): productos de pasturas o forestal
def _rs(x): return [x[i:i+2] for i in range(0, len(x), 2)]
for p in prods:
    s_, s2_, es_ = _rs(p["s"]), _rs(p["s2"]), _rs(p["es"])
    if "PA" in s_ or "FO" in s_: s_.append("SP")
    elif "PA" in s2_ or "FO" in s2_: s2_.append("SP")
    if ("PA" in es_ or "FO" in es_) and "SP" in s_: es_.append("SP")
    p["s"], p["s2"], p["es"] = "".join(s_), "".join(s2_), "".join(es_)

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
for a in activos + biologicos + botanicos:
    ur = a.get("ur") or {}
    partes = [(k, ur[k]) for k in ("PA", "FO") if k in ur]
    if partes:
        nom = {"PA": "Pasturas", "FO": "Forestal"}
        a["ur"]["SP"] = {"u": " ".join(f"{nom[k]}: {e['u']}" for k, e in partes), "o": list(dict.fromkeys(o for k, e in partes for o in e["o"]))}
        if all(e.get("sec") for k, e in partes): a["ur"]["SP"]["sec"] = 1
# variantes de escritura (listado SENAVE, nombres en inglés, errores comunes) para el buscador
import unicodedata
def _nk(t):
    t = unicodedata.normalize("NFD", (t or "").lower())
    return "".join(ch for ch in t if ch.isalnum() and not unicodedata.combining(ch))
_var = collections.defaultdict(set)
for _p in d["productos"] + d["productos_mantenimiento_vencido"]:
    for _c in _p["componentes"]:
        o = re.split(r"[(\d]", _c.get("nombre_original") or "")[0]
        o = re.sub(r"\b(SAL|SALES|ACIDO|ÁCIDO|EQUIVALENTE|DE|DEL|ESTER|ÉSTER|DIMETILAMINA|AMONIO|POTASICA|POTÁSICA|SODICA|SÓDICA|ISOPROPILAMINA|AMINA|TRIETANOLAMINA|TRIISOPROPANOLAMINA|BUTOXI|ETIL|BUTOTIL|COLINA|DIGLICOLAMINA|AMONICA|AMÓNICA)\b", " ", o.upper()).strip()
        k = _nk(o)
        if len(k) >= 4: _var[_c["id"]].add(k)
ALIAS_EXTRA = {"24d": ["24d", "dosacuatrod"], "glifosato": ["glyphosate", "glifo"], "lambdacialotrina": ["lambda", "lambdacihalotrina", "lambdacyhalothrin"],
               "clorpirifos": ["chlorpyrifos"], "s_metolacloro": ["smetolaclor", "metolaclor"], "bio_bt": ["bt", "bacillusthuringiensis"],
               "cobre": ["oxicloruro", "hidroxidodecobre", "copper"], "fosfuros": ["fosfina", "fosfurodealuminio"], "emamectina": ["emamectina", "emamectin"]}
for a in activos + biologicos + botanicos:
    al = (_var.get(a["id"], set()) | set(ALIAS_EXTRA.get(a["id"], []))) - {_nk(a["nombre"])}
    if al: a["al"] = sorted(al)
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
catalogo = [dict(x) for x in d["catalogo_problemas"] + PROBLEMAS_EXTRA]
for x in catalogo:
    if x["id"] in PB.A_APLICACION: x["categoria"] = "aplicacion"
    if x["id"] in PB.RENOMBRAR: x.update(PB.RENOMBRAR[x["id"]])
catalogo += PB.PROBLEMAS_APLICACION
assert len({x["id"] for x in catalogo}) == len(catalogo)
diag = [dict(x) for x in d["diagnostico_por_sintoma"]]
for x in diag:
    if x["sintoma"].startswith("Daño en cultivos vecinos") or x["sintoma"].startswith("Más deriva"):
        x["problemas"] = x["problemas"] + ["PR32"]
    if x["sintoma"].startswith("El caldo se ve normal"):
        x["problemas"] = x["problemas"] + ["PR33"]
    for k, v in PB.DIAG_AGREGAR.items():
        if x["sintoma"].startswith(k): x["problemas"] = x["problemas"] + [i for i in v if i not in x["problemas"]]
diag += PB.DIAG_NUEVOS
ABEJAS_AI = sorted(a["id"] for a in activos if a["id"] not in PB.ABEJAS_EXCLUIR and any((a.get("modo_accion") or "").startswith(g + " ") or (a.get("modo_accion") or "") == g for g in PB.IRAC_ABEJAS))
print("activos tóxicos para abejas:", len(ABEJAS_AI))
ABEJAS_MEDIO_AI = sorted(a["id"] for a in activos if a["id"] not in ABEJAS_AI and a["id"] not in ("cadusafos", "sulfluramida") and (a["id"] in PB.ABEJAS_MEDIO_AI or any((a.get("modo_accion") or "").startswith(g + " ") for g in PB.IRAC_ABEJAS_MEDIO)))
print("tóxicos para abejas (medio):", ABEJAS_MEDIO_AI)
_aplic = json.loads(json.dumps(PB.REGLAS_APLIC).replace('"__ABEJAS__"', json.dumps(ABEJAS_AI)).replace('"__ABEJAS_MEDIO__"', json.dumps(ABEJAS_MEDIO_AI)))
reglas = d["reglas_compatibilidad"] + REGLAS_EXTRA + _aplic
reglas = [dict(r, problemas=PB.REGLAS_PROBLEMAS[r["id"]]) if r["id"] in PB.REGLAS_PROBLEMAS else r for r in reglas]
_ids_prob = {x["id"] for x in catalogo}
for r in reglas:
    for i in r.get("problemas", []): assert i in _ids_prob, (r["id"], i)
REGLAS_ALL = dict(REGLAS); REGLAS_ALL.update(SEMAFORO_EXTRA); REGLAS_ALL.update(CORR.SEMAFORO_NUEVAS); REGLAS_ALL.update(EQ.SEMAFORO_AEREAS); REGLAS_ALL.update(SV.SEMAFORO_SILVO); REGLAS_ALL.update(CL.SEMAFORO_CLIMA); REGLAS_ALL.update(PB.SEMAFORO_APLIC)
for _id, v in CORR.SEMAFORO_MOD.items():
    assert _id in REGLAS_ALL, _id
    REGLAS_ALL[_id] = v
MEDIDAS_ALL = {k: dict(v) for k, v in MEDIDAS.items()}; MEDIDAS_ALL.update(MEDIDAS_EXTRA)
for _id, campos in CORR.MEDIDAS.items(): MEDIDAS_ALL[_id].update(campos)
MEDIDAS_ALL.update(EQ.MEDIDAS_AEREAS); MEDIDAS_ALL.update(SV.MEDIDAS_SILVO); MEDIDAS_ALL.update(PB.MEDIDAS_APLIC)

RUBROS = dict(list(RUBROS.items())[:4] + [("SP", SV.RUBRO_SP)] + list(RUBROS.items())[4:])
AI_RUBROS_SP = {k: (v + " SP" if ("PA" in v.split() or "FO" in v.split()) else v) for k, v in AI_RUBROS.items()}
DB = {
    "meta": {k: d["meta"][k] for k in ("titulo", "version", "fecha_generacion", "fuente_productos", "criterio_productos_actuales", "advertencias", "estadisticas", "fuentes_datos_quimicos")},
    "categorias_problemas": dict(d["categorias_problemas"], aplicacion=PB.CATEGORIA_APLICACION),
    "estado_plantas": PB.ESTADO_PLANTAS,
    "limpieza": {"genericos": LP.GENERICOS, "registrados_para": LP.REGISTRADOS_PARA, "grupos": LP.GRUPOS, "residuo_grupo": LP.RESIDUO_GRUPO,
                 "pasos": LP.PASOS, "pasos_drone": LP.PASOS_DRONE, "advertencias": LP.ADVERTENCIAS},
    "catalogo": {"clases": CAT.CLASES, "origenes": CAT.ORIGENES, "usos": CAT.USOS, "funciones": CAT.FUNCIONES_ADY},
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
    "rubros": RUBROS, "ai_rubros": AI_RUBROS_SP,
    "niveles": NIVELES, "medidas": MEDIDAS_ALL, "semaforo": REGLAS_ALL,
    "objetivos": OBJETIVOS, "resistencia": RESISTENCIA, "principios_rotacion": PRINCIPIOS_ROTACION,
    "familias": FAMILIAS, "form_familia": FORM_FAMILIA, "inertes": INERTES, "impurezas": IMPUREZAS,
    "cultivos": CULTIVOS, "cult_gram": GRAM, "cult_hoja": HOJA, "carry": CARRY, "select": SELECT, "momentos": MOMENTOS,
    "equipos": {"pastillas": EQ.PASTILLAS_ISO, "tipos_pastilla": EQ.TIPOS_PASTILLA, "clases_gota": EQ.CLASES_GOTA,
                "gota_producto": EQ.GOTA_PRODUCTO, "gota_drone": EQ.GOTA_DRONE, "gota_clima": EQ.GOTA_CLIMA, "altura_barra": EQ.ALTURA_BARRA,
                "tolerancias": EQ.TOLERANCIAS, "tiempo_colecta": EQ.TIEMPO_COLECTA, "check_insp": EQ.CHECKLIST_INSPECCION,
                "check_drone": EQ.CHECKLIST_DRONE, "check_avion": EQ.CHECKLIST_AVION, "normativa": EQ.NORMATIVA, "vuelo": EQ.VUELO,
                "drones": EQ.MODELOS_DRONE, "aviones": EQ.MODELOS_AVION, "funciones": EQ.FUNCIONES,
                "terrestres": EQ.MODELOS_TERRESTRE, "mochilas": EQ.MODELOS_MOCHILA, "fun_drone": EQ.FUN_DRONE, "baterias": EQ.BATERIAS_DRONE},
    "silvo": {"arboles": SV.ARBOLES, "riesgo": SV.RIESGO_ARBOL, "riesgo_gram": SV.RIESGO_GRAMINICIDA, "reingreso": SV.REINGRESO, "practicas": SV.PRACTICAS_SILVO},
    "clima": {"om": CL.OPEN_METEO, "lavado": CL.LAVADO_H, "lavado_forma": CL.LAVADO_FORMA, "lavado_clase": CL.LAVADO_CLASE, "lavado_grupo": CL.LAVADO_GRUPO,
              "lavado_nota": CL.LAVADO_NOTA, "pre": CL.PREEMERGENTES, "pre_momento": CL.PRE_SEGUN_MOMENTO, "activacion": CL.LLUVIA_ACTIVACION, "aux_vol": CL.AUXINICOS_VOLATILES,
              "t_vol": CL.T_VOLATILIDAD, "t_aceite": CL.T_ACEITE_AZUFRE, "inversion": CL.INVERSION, "rafaga": CL.RAFAGA_ALTA},
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
