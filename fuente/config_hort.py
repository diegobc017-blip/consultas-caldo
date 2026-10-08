# Cultivos hortícolas y frutales con selectividad de herbicidas propia (rubro HO).
#
# Antes la app tenía un solo cultivo "Hortalizas" y cítricos/frutales sin datos. Acá se separan los
# cultivos hortícolas más comunes de Paraguay y se carga la selectividad SOLO con principios activos
# que tienen productos vigentes en el SENAVE. Criterio: el cultivo figura en etiquetas de la región
# (Brasil/Argentina/Chile) o de EE. UU. para ese activo y ese momento; la etiqueta del producto que se
# use en Paraguay manda siempre. Fuentes: etiquetas (Sencor/metribuzina, Dual Gold/S-metolacloro,
# Treflan/trifluralina, Prowl H2O/pendimetalina, Goal/oxifluorfen, Lorox/linurón, Caparol/prometrina,
# Command/clomazona, Select/cletodim, Stinger/clopiralida, Aim/carfentrazona, Treevix-Heat/saflufenacil,
# Chateau/flumioxazin, Karmex/diurón, Princep/simazina) y guías de malezas en hortalizas (UC IPM,
# Univ. de Florida Vegetable Production Handbook, Embrapa Hortaliças).
#
# "dir" = solo aplicación dirigida a las malezas o al suelo, sin mojar hojas, frutos ni tronco verde
# (cultivos perennes: cítricos y frutales establecidos).

CULTIVOS_HO = {
    "tomate": "Tomate", "locote": "Locote / pimiento", "papa": "Papa", "cebolla": "Cebolla / ajo",
    "zanahoria": "Zanahoria", "lechuga": "Lechuga y hojas verdes", "cruciferas": "Repollo, brócoli, coliflor",
    "cucurbitas": "Sandía, melón, zapallo, pepino", "frutilla": "Frutilla",
}
# hortalizas de hoja ancha (dicotiledóneas): toleran graminicidas FOP/DIM
DICOT_HO = ["tomate", "locote", "papa", "zanahoria", "lechuga", "cruciferas", "cucurbitas", "frutilla"]
ANUALES_HO = DICOT_HO + ["cebolla"]
PERENNES = ["citricos", "frutales"]

# nombre del genérico existente
RENOMBRAR = {"hortalizas": "Otras hortalizas"}

# Agregados a SELECT: activo -> {momento: [cultivos]} ; "n" agrega una nota
SELECT_HO = {
    "metribuzina": {"pre": ["tomate", "papa"], "post": ["tomate", "papa"],
                    "n": "Tomate: trasplantado y prendido (no en almácigo). Papa: algunas variedades son sensibles; locote, cucurbitáceas, cebolla y hojas verdes no la toleran."},
    "s_metolacloro": {"pre": ["tomate", "locote", "papa", "cruciferas"], "post": ["cebolla"],
                      "n": "Cebolla: recién desde 2 hojas verdaderas (no controla malezas ya nacidas). En tomate, locote y repollo, antes del trasplante."},
    "trifluralina": {"pre": ["tomate", "locote", "zanahoria", "cruciferas", "papa"],
                     "n": "Incorporar al suelo antes de sembrar o trasplantar; no en cucurbitáceas ni en hojas verdes de siembra directa."},
    "pendimetalina": {"pre": ["tomate", "locote", "papa", "cebolla", "zanahoria"], "post": ["cebolla"],
                      "n": "Cebolla y ajo: también sobre el cultivo desde 2 a 3 hojas verdaderas."},
    "oxifluorfen": {"pre": ["tomate", "cruciferas", "citricos", "frutales"], "post": ["cebolla"],
                    "n": "Tomate y repollo: antes del trasplante (no sobre las plantas). Cebolla y ajo trasplantados: desde 2 a 3 hojas verdaderas. En cítricos y frutales, al suelo bajo la copa, sin mojar hojas."},
    "linuron": {"pre": ["papa", "zanahoria"], "post": ["zanahoria"],
                "n": "Zanahoria: también sobre el cultivo desde 3 hojas."},
    "prometrina": {"pre": ["zanahoria"], "post": ["zanahoria"]},
    "clomazona": {"pre": ["locote", "cucurbitas"],
                  "n": "Puede blanquear hojas por unos días. Su vapor y su deriva dañan cultivos vecinos sensibles."},
    "clopiralida": {"post": ["cruciferas"]},
    # perennes: residuales al suelo bajo los árboles establecidos (3 años o más)
    "diuron": {"pre": ["citricos"], "n": "Cítricos establecidos (3 años o más), al suelo; no en suelos arenosos."},
    "simazina": {"pre": ["citricos", "frutales"], "n": "Cítricos y frutales establecidos, al suelo bajo la copa."},
    "flumioxazin": {"pre": ["frutales"], "n": "Frutales y vid establecidos, al suelo; sin mojar hojas ni frutos."},
}
# graminicidas sobre hortalizas de hoja ancha
GRAMINICIDAS_HO = {"cletodim": DICOT_HO + ["cebolla"], "haloxifop": DICOT_HO, "quizalofop": DICOT_HO, "propaquizafop": DICOT_HO}
# solo dirigidos en cítricos y frutales
DIRIGIDOS = ["glifosato", "glufosinato", "glufosinato_p", "paraquat", "diquat", "carfentrazona", "saflufenacil", "cletodim", "haloxifop"]

CULT_HO = ["tomate", "locote", "papa", "cebolla", "zanahoria", "lechuga", "cruciferas", "cucurbitas", "frutilla",
           "hortalizas", "citricos", "frutales", "mandioca", "poroto"]


def aplicar(CULTIVOS, HOJA, CARRY, SELECT, LIMP_GRUPOS):
    """Agrega los cultivos hortícolas a las estructuras de carry-over, selectividad y limpieza."""
    # copia las listas (algunas apuntan a la misma lista HOJA) antes de modificar HOJA
    for ai, s in list(SELECT.items()):
        SELECT[ai] = {k: (list(v) if isinstance(v, list) else v) for k, v in s.items()}
    for k, v in RENOMBRAR.items():
        CULTIVOS[k] = v
    CULTIVOS.update(CULTIVOS_HO)
    for c in ANUALES_HO + PERENNES:
        if c not in HOJA:
            HOJA.append(c)
    # carry-over: las hortalizas nuevas heredan la excepción de "hortalizas"
    for ai, c in CARRY.items():
        if "hortalizas" in c:
            for k in ANUALES_HO:
                c.setdefault(k, c["hortalizas"])
    for ai, extra in SELECT_HO.items():
        s = SELECT[ai] = dict(SELECT.get(ai, {"post": [], "pre": []}))
        for mom in ("pre", "post"):
            if mom in extra:
                base = s.get(mom, [])
                if base != "*":
                    s[mom] = list(dict.fromkeys(list(base) + extra[mom]))
        if extra.get("n"):
            s["n"] = (s.get("n", "") + " " + extra["n"]).strip()
    for ai, cs in GRAMINICIDAS_HO.items():
        s = SELECT[ai] = dict(SELECT[ai])
        s["post"] = list(dict.fromkeys(list(s["post"]) + cs))
    for ai in DIRIGIDOS:
        s = SELECT[ai] = dict(SELECT[ai])
        s["dir"] = list(dict.fromkeys(s.get("dir", []) + PERENNES))
    for g in LIMP_GRUPOS:
        if "hortalizas" in g.get("sensibles", []):
            g["sensibles"] = g["sensibles"] + [c for c in ANUALES_HO if c not in g["sensibles"]]
