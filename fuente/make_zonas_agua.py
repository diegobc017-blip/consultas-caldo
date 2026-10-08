"""Genera datos/zonas_agua.json: zonas aproximadas de calidad del agua subterránea de Paraguay.

No existe (que hayamos encontrado) un mapa oficial de dureza del agua de Paraguay. Estas zonas se arman
con los estudios hidrogeológicos publicados y con la geología, y sirven solo como estimación inicial:
la app siempre recomienda el análisis del agua.

Requiere shapely (solo para regenerar el archivo; la app y build_data.py no lo necesitan):
    pip install shapely && python3 fuente/make_zonas_agua.py
"""
import json, os
from shapely.geometry import Polygon, box, mapping
from shapely.ops import unary_union

# Contorno aproximado de Paraguay (lon, lat), sentido horario desde el trifinio del Pilcomayo
PY = [(-62.64, -22.24), (-62.27, -21.03), (-61.77, -20.08), (-60.60, -19.62), (-59.10, -19.29), (-58.17, -19.85), (-58.16, -20.17),
      (-58.16, -20.60), (-57.87, -21.04), (-57.90, -21.70), (-57.95, -22.09),                     # río Paraguay (límite con Brasil)
      (-57.60, -22.14), (-57.00, -22.24), (-56.40, -22.25), (-55.85, -22.28),                     # río Apa
      (-55.68, -22.56), (-55.60, -23.00), (-55.45, -23.90), (-54.95, -24.00), (-54.30, -24.06),   # Amambay y Mbaracayú
      (-54.33, -24.50), (-54.40, -25.00), (-54.60, -25.55), (-54.65, -26.00), (-54.95, -26.70),   # río Paraná
      (-55.40, -27.16), (-55.87, -27.38), (-56.40, -27.50), (-56.90, -27.50), (-57.50, -27.35), (-58.00, -27.27), (-58.61, -27.30),
      (-58.36, -26.86), (-58.20, -26.55), (-58.13, -26.18), (-57.85, -25.85), (-57.56, -25.50), (-57.67, -25.36),  # río Paraguay (Argentina)
      (-58.13, -25.05), (-58.80, -24.60), (-59.50, -24.15), (-60.30, -23.65), (-61.00, -23.15), (-61.80, -22.60)]  # río Pilcomayo
# Río Paraguay entre la boca del Apa y Asunción (separa Chaco y Región Oriental)
RIO = [(-57.95, -22.09), (-57.93, -22.29), (-57.72, -23.00), (-57.47, -23.40), (-57.30, -24.00), (-57.15, -24.43),
       (-57.40, -24.80), (-57.47, -25.05), (-57.55, -25.20), (-57.665, -25.27), (-57.67, -25.36)]

py = Polygon(PY).buffer(0)
# Chaco: oeste del río Paraguay (polígono grande que usa el río como borde este)
chaco = py.intersection(Polygon([(-64, -26), (-64, -19)] + [(-58.16, -19.0), (-58.16, -20.17), (-58.16, -20.60), (-57.87, -21.04), (-57.90, -21.70)] + RIO + [(-57.67, -26)]))
oriental = py.difference(chaco)

# (id, región, recorte) en orden de prioridad
REC = [
    ("chaco_norte", chaco, box(-64, -21.3, -56, -19)),
    ("chaco_occidental", chaco, box(-64, -26, -61.0, -21.3)),
    ("chaco_central", chaco, box(-61.0, -23.7, -59.5, -21.3)),
    ("chaco_bajo", chaco, box(-64, -26, -56, -19)),
    ("patino", oriental, box(-57.72, -25.62, -57.25, -25.12)),
    ("caliza_norte", oriental, box(-58.0, -22.7, -57.35, -21.9)),
    ("basalto_este", oriental, box(-55.85, -27.0, -54.0, -23.8)),
    ("itapua_sur", oriental, box(-56.6, -27.6, -54.0, -26.85)),
    ("guarani_aflora", oriental, box(-57.5, -27.6, -56.6, -25.6)),
    ("neembucu", oriental, box(-59, -27.6, -57.5, -26.0)),
    ("oriental_norte", oriental, box(-58.5, -24.2, -54.0, -21.9)),
    ("oriental_centro", oriental, box(-59, -27.6, -54.0, -21.9)),
]

# Valores: [mínimo, típico, máximo]. dureza en mg/L de CaCO3, ce = conductividad en µS/cm, na = sodio mg/L.
# typ None = sin dato para cargar automáticamente.
Z = {
 "chaco_bajo": {"n": "Bajo Chaco (Presidente Hayes, cerca de los ríos Paraguay y Pilcomayo)", "reg": "Chaco", "acu": "Sistema Acuífero Yrendá, zona de descarga",
   "conf": "media", "dureza": [500, 3000, 8000], "pH": [7.2, 7.8, 8.3], "ce": [5000, 30000, 88000], "na": [2000, 8000, 14000],
   "txt": "El agua de pozo es salada (cloruros y sulfatos de sodio, con mucho calcio y magnesio): en Irala Fernández llega a 59 000 µS/cm y cerca del río Paraguay a 87 700 µS/cm. No sirve para pulverizar sin tratar.",
   "uso": "Usar agua de tajamar, de aljibe o del río, y medir la conductividad antes de cargar.", "f": ["say", "irala"]},
 "chaco_central": {"n": "Chaco Central (Filadelfia, Loma Plata, Neuland, Mariscal Estigarribia)", "reg": "Chaco", "acu": "Sistema Acuífero Yrendá, zona de tránsito",
   "conf": "media", "dureza": [300, 1500, 5000], "pH": [7.0, 7.6, 8.2], "ce": [2000, 15000, 30000], "na": [500, 3000, 7000],
   "txt": "Los pozos dan agua salobre a salada (en Filadelfia, 17 000 µS/cm a 93–108 m). Hay lentes de agua dulce poco profundas en paleocauces, pero son locales. Por eso se usa mucha agua de lluvia (aljibes) y de tajamar.",
   "uso": "Para pulverizar, preferir tajamar o aljibe; si es de pozo, analizarla siempre.", "f": ["say"]},
 "chaco_occidental": {"n": "Chaco occidental (límite con Bolivia: Infante Rivarola, Pozo Hondo)", "reg": "Chaco", "acu": "Sistema Acuífero Yrendá, zona de recarga",
   "conf": "baja", "dureza": [300, 1000, 4000], "pH": [7.0, 7.6, 8.2], "ce": [2000, 8000, 20000], "na": None,
   "pp": {"n": "pozo profundo (120 a 400 m)", "dureza": [100, 250, 450], "pH": [7.0, 7.5, 8.0], "ce": [500, 900, 1500],
          "txt": "En profundidad hay acuíferos de agua dulce (menos de 1 000 mg/L de sales), bicarbonatada cálcico-magnésica: dura pero usable."},
   "txt": "Los acuíferos someros suelen ser salobres; el agua dulce aparece más abajo (desde unos 120 m en Infante Rivarola, 198–212 m en Pozo Hondo).",
   "uso": "Pozo profundo: corregir la dureza. Pozo somero: analizar antes de usar.", "f": ["say"]},
 "chaco_norte": {"n": "Alto Paraguay y norte del Chaco", "reg": "Chaco", "acu": "Sin estudios publicados encontrados",
   "conf": "sin datos", "dureza": [50, None, 3000], "pH": [6.5, None, 8.2], "ce": [100, None, 20000], "na": None,
   "txt": "No encontramos datos publicados de calidad del agua para esta zona; por la geología del Chaco, los pozos pueden ser salobres.",
   "uso": "Hacer el análisis antes de usar agua de pozo.", "f": []},
 "patino": {"n": "Gran Asunción y Central (Acuífero Patiño)", "reg": "Oriental", "acu": "Acuífero Patiño",
   "conf": "media", "dureza": [6, 27, 58], "pH": [5.3, 5.8, 6.8], "ce": [32, 170, 1100], "na": None,
   "txt": "Agua muy blanda y algo ácida (dureza media 27 mg/L, pH 5,8). Cerca del río Paraguay (Mariano Roque Alonso) hay pozos con algo de sal (cloruros hasta 450 mg/L).",
   "uso": "No hace falta corregir la dureza; puede hacer más espuma.", "f": ["patino"]},
 "caliza_norte": {"n": "Norte de Concepción (Vallemí, San Lázaro, zona de calizas)", "reg": "Oriental", "acu": "Calizas y dolomías del Grupo Itapucumí",
   "conf": "baja", "dureza": [150, 250, 400], "pH": [7.2, 7.6, 8.2], "ce": [400, 700, 1200], "na": None,
   "txt": "Estimado por la geología: el agua que pasa por calizas sale dura y alcalina. No encontramos mediciones publicadas.",
   "uso": "Probable corrección de dureza; confirmar con análisis.", "f": []},
 "basalto_este": {"n": "Alto Paraná, Canindeyú y este de Itapúa y Caaguazú (basalto)", "reg": "Oriental", "acu": "Basaltos de la Formación Alto Paraná sobre el Acuífero Guaraní",
   "conf": "media", "dureza": [10, 45, 110], "pH": [6.0, 6.8, 7.5], "ce": [25, 120, 250], "na": None,
   "pp": {"n": "pozo profundo o artesiano (bajo el basalto)", "dureza": [16, 35, 130], "pH": [8.1, 8.3, 8.5], "ce": [1260, 3300, 4500], "na": [260, 730, 885],
          "txt": "Los pozos profundos y termales (Ciudad del Este, Minga Guazú, Presidente Franco) dan agua sódica, alcalina (pH 8 a 8,5) y con mucho flúor."},
   "txt": "El acuífero del basalto da agua blanda a moderadamente dura (conductividad de 25 a 250 µS/cm).",
   "uso": "Pozo común: poca corrección. Pozo profundo: bajar el pH antes de cargar productos sensibles a la hidrólisis alcalina.", "f": ["sag"]},
 "itapua_sur": {"n": "Sur de Itapúa (Encarnación, Hohenau, Bella Vista, Coronel Bogado)", "reg": "Oriental", "acu": "Areniscas del Acuífero Guaraní",
   "conf": "media", "dureza": [30, 65, 95], "pH": [5.7, 6.6, 7.2], "ce": [90, 180, 220], "na": None,
   "pp": {"n": "pozo profundo cerca del río Paraná", "dureza": [6, 10, 15], "pH": [8.0, 8.5, 9.1], "ce": [200, 450, 580], "na": [47, 90, 126],
          "txt": "Cerca del Paraná (Capitán Meza, Coronel Bogado) el acuífero confinado da agua blanda pero sódica y alcalina (pH 8 a 9)."},
   "txt": "Agua bicarbonatada cálcico-magnésica, blanda a moderadamente dura (Hohenau 32–55, Jesús 82, Bella Vista 69 mg/L).",
   "uso": "Corregir solo con productos muy sensibles a la dureza o dosis bajas de glifosato.", "f": ["sag"]},
 "guarani_aflora": {"n": "Misiones, sur de Paraguarí y oeste de Caazapá (afloramiento del Acuífero Guaraní)", "reg": "Oriental", "acu": "Acuífero Guaraní libre (areniscas)",
   "conf": "media", "dureza": [6, 15, 60], "pH": [5.2, 5.7, 7.5], "ce": [25, 60, 430], "na": None,
   "txt": "Agua muy blanda y ácida, parecida al agua de lluvia (San Ignacio, San Patricio: 25–35 µS/cm). Algunos pozos son más duros (San Juan Bautista 54, Compañía San Gabriel 207 mg/L).",
   "uso": "Sin corrección de dureza; cuidar el pH bajo con sulfonilureas y cobre.", "f": ["sag"]},
 "neembucu": {"n": "Ñeembucú (planicie del río Paraguay)", "reg": "Oriental", "acu": "Sedimentos aluviales",
   "conf": "baja", "dureza": [20, 80, 400], "pH": [6.0, 7.0, 8.0], "ce": [100, 500, 3000], "na": None,
   "txt": "Planicie inundable con pocos datos; los pozos someros pueden salir salobres en algunos lugares.",
   "uso": "Analizar el agua de pozo antes de usarla.", "f": []},
 "oriental_norte": {"n": "Norte de la Región Oriental (Concepción, Amambay, San Pedro)", "reg": "Oriental", "acu": "Areniscas (Acuífero Guaraní en Amambay) y otras formaciones",
   "conf": "baja", "dureza": [10, 40, 150], "pH": [5.5, 6.5, 7.5], "ce": [30, 150, 500], "na": None,
   "txt": "Por la geología, el agua suele ser blanda a moderadamente dura; hay pocos datos publicados.",
   "uso": "Confirmar con análisis.", "f": []},
 "oriental_centro": {"n": "Centro de la Región Oriental (Cordillera, Caaguazú, Guairá, Caazapá, Paraguarí)", "reg": "Oriental", "acu": "Areniscas y rocas cristalinas",
   "conf": "baja", "dureza": [10, 45, 150], "pH": [5.5, 6.5, 7.5], "ce": [40, 180, 600], "na": None,
   "txt": "Por la geología, agua blanda a moderadamente dura; hay pocos datos publicados.",
   "uso": "Confirmar con análisis.", "f": []},
}

# Fuente del agua que no es pozo (valores generales, para cualquier zona)
FUENTES_AGUA = {
 "pozo": {"n": "Pozo"},
 "pozo_profundo": {"n": "Pozo profundo o artesiano"},
 "tajamar": {"n": "Tajamar o represa", "dureza": [15, 40, 120], "pH": [6.5, 7.0, 7.8], "ce": [80, 250, 800], "turbidez": "alta",
             "txt": "Agua de lluvia acumulada: blanda pero turbia (arcilla y materia orgánica), que inactiva glifosato, paraquat y diquat. En el Chaco se va salando a medida que se evapora."},
 "aljibe": {"n": "Aljibe (agua de lluvia)", "dureza": [2, 10, 25], "pH": [5.5, 6.2, 7.0], "ce": [10, 30, 80], "turbidez": "baja",
            "txt": "Muy blanda y limpia; puede tener pH ácido. Es la mejor agua para pulverizar si alcanza."},
 "rio": {"n": "Río o arroyo", "dureza": [15, 35, 80], "pH": [6.5, 7.0, 7.6], "ce": [40, 100, 300], "turbidez": "media",
         "txt": "Blanda, pero con barro en crecidas (el Pilcomayo, muy turbio y algo salado). Dejar decantar o filtrar."},
 "red": {"n": "Red de agua potable", "dureza": [15, 40, 120], "pH": [6.5, 7.2, 8.0], "ce": [50, 200, 600], "cloro": 0.5,
         "txt": "Depende de la fuente de la red. Trae cloro residual, que daña biológicos (Bt, hongos y bacterias): dejar reposar o declorar."},
}

REFS = {
 "say": ["Larroza, F. y otros: Caracterización hidrogeológica del Sistema Acuífero Yrendá (SAY) en Paraguay", "http://www.geologiadelparaguay.com.py/Caracterizaci%C3%B3n-Hidrogeol%C3%B3gica-del-Sistema-Acu%C3%ADfero-Yrenda.pdf"],
 "irala": ["Román, I.: Desalinización del agua cruda del Chaco paraguayo (Irala Fernández), CONACYT", "https://repositorio.conacyt.gov.py/handle/20.500.14066/4110"],
 "patino": ["Acosta Álvarez y Méndez (Corposana): El agua subterránea del Acuífero Patiño en el área metropolitana de Asunción", "http://www.geologiadelparaguay.com.py/Agua-Subterranea-Area-Metropolitana-Asuncion.pdf"],
 "sag": ["Caracterización hidrogeológica e hidrogeoquímica del Sistema Acuífero Guaraní en la Región Oriental del Paraguay al sur de 25°30′ (Águas Subterrâneas)", "https://aguassubterraneas.abas.org/asubterraneas/article/view/23408"],
}


def r3(geom):
    return json.loads(json.dumps(mapping(geom.simplify(0.01)), default=float), parse_float=lambda x: round(float(x), 3))


usado = Polygon()
feats = []
for zid, reg, rec in REC:
    g = reg.intersection(rec).difference(usado)
    if g.is_empty:
        continue
    usado = unary_union([usado, g])
    feats.append({"type": "Feature", "properties": {"id": zid}, "geometry": r3(g)})
assert usado.symmetric_difference(py).area < 1e-6, "las zonas no cubren todo el país"
out = {"zonas": Z, "fuentes": FUENTES_AGUA, "refs": REFS, "py": [[round(x, 2), round(y, 2)] for x, y in PY],
       "geo": {"type": "FeatureCollection", "features": feats}}
dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "datos", "zonas_agua.json")
json.dump(out, open(dst, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("zonas:", [f["properties"]["id"] for f in feats], round(os.path.getsize(dst) / 1024, 1), "KB")
