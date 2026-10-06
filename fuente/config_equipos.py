# Equipos de aplicación, calibración y aplicación aérea (drone y avión).
# Fuentes (revisadas el 02/10/2026):
#  - ISO 10625:2018 (código de colores de pastillas); ISO 16122 / EN 13790 (inspección de pulverizadoras)
#  - INTA Pergamino, Protocolo de calibración (P. D. Leiva) e INTA "Aplicación eficiente de fitosanitarios" cap. 6
#  - ASABE S572.3 (clases de gota); GRDC (selección de pastillas, Delta T); IDR-Paraná (inspección)
#  - Ley 3742/09 arts. 59-68; Decreto 2048/04; DINAC R 1103 (Res. 2170/2017, RPAS); DINAC R137 (aviación agrícola)
#  - SENAVE: requisitos de registro de aplicadoras (cat. A.8, Res. 979/11) y de Piloto Aviador Agrícola (PAAG)
#  - CropLife Latin America, Procedimiento operativo estándar para aplicación con drones
#  - UGA Extension (Virk y Li, 2023); Purdue PPP-154; ESALQ (cobertura); especificaciones de DJI, XAG, Air Tractor, Embraer, Thrush
#  - Revista AVAG (franjas medidas en aviones agrícolas)

# Pastillas: tamaño ISO -> (color, código hex, L/min a 3 bar)
PASTILLAS_ISO = [
 ["01", "Naranja", "#F28C28", 0.4], ["015", "Verde", "#2E9E44", 0.6], ["02", "Amarillo", "#F2C200", 0.8],
 ["025", "Lila", "#9B6FC7", 1.0], ["03", "Azul", "#2463B8", 1.2], ["04", "Rojo", "#D33A2C", 1.6],
 ["05", "Marrón", "#8A5A2B", 2.0], ["06", "Gris", "#8C8C8C", 2.4], ["08", "Blanco", "#F4F4F4", 3.2],
 ["10", "Celeste", "#6EC6F0", 4.0], ["15", "Verde claro", "#A8D86E", 6.0],
]

# Tipos de pastilla: presión mínima y máxima (bar), gota típica y uso
TIPOS_PASTILLA = {
 "std":   {"nombre": "Abanico plano estándar", "pmin": 2, "pmax": 4, "gota": "F–M", "uso": "Uso general con viento bajo; más deriva que las de baja deriva."},
 "xr":    {"nombre": "Abanico de rango extendido (XR)", "pmin": 1, "pmax": 4, "gota": "F–M", "uso": "Fungicidas e insecticidas que necesitan cobertura; cuidar la deriva por encima de 3 bar."},
 "bd":    {"nombre": "Baja deriva (pre-orificio)", "pmin": 2, "pmax": 4, "gota": "M–C", "uso": "Herbicidas y uso general con algo de viento."},
 "turbo": {"nombre": "Turbo / gran angular", "pmin": 1, "pmax": 6, "gota": "M–C", "uso": "Herbicidas; buena uniformidad con barra baja."},
 "twin":  {"nombre": "Doble abanico", "pmin": 2, "pmax": 6, "gota": "F–M", "uso": "Fungicidas e insecticidas en cultivos densos (penetración por los dos lados)."},
 "ai":    {"nombre": "Inducción de aire (AI, AIXR, TTI, IDK)", "pmin": 2, "pmax": 8, "gota": "C–UC", "uso": "Herbicidas sistémicos y hormonales; la mejor para reducir deriva. TTI rinde mejor por encima de 4 bar."},
 "conoh": {"nombre": "Cono hueco", "pmin": 5, "pmax": 20, "gota": "VF–F", "uso": "Insecticidas y fungicidas de contacto en frutales y hortalizas; mucha deriva."},
 "conol": {"nombre": "Cono lleno", "pmin": 1, "pmax": 3, "gota": "M–C", "uso": "Aplicaciones dirigidas al suelo."},
}

# Clases de gota ASABE S572.3: código, nombre, DMV mínimo (µm)
CLASES_GOTA = [
 ["XF", "Extremadamente fina", 0], ["VF", "Muy fina", 100], ["F", "Fina", 150], ["M", "Media", 195],
 ["C", "Gruesa", 270], ["VC", "Muy gruesa", 350], ["XC", "Extremadamente gruesa", 485], ["UC", "Ultra gruesa", 665],
]

# Gota y cobertura recomendadas según el tipo de producto (impactos/cm² en tarjeta hidrosensible: FAO citado por INTA; ESALQ)
GOTA_PRODUCTO = {
 "herb_sist":  {"nombre": "Herbicida sistémico", "clase": "C a VC", "um": [270, 450], "impactos": "20–30"},
 "herb_cont":  {"nombre": "Herbicida de contacto", "clase": "M a C", "um": [195, 350], "impactos": "30–40"},
 "hormonal":   {"nombre": "Herbicida hormonal (2,4-D, dicamba, picloram…)", "clase": "XC a UC", "um": [485, 800], "impactos": "20–30"},
 "fung_sist":  {"nombre": "Fungicida sistémico", "clase": "F a M", "um": [150, 270], "impactos": "40–60"},
 "fung_cont":  {"nombre": "Fungicida de contacto", "clase": "F a M", "um": [150, 270], "impactos": "50–70"},
 "insect":     {"nombre": "Insecticida", "clase": "F a M", "um": [150, 270], "impactos": "50–70 (contacto) o 40 (sistémico)"},
}
# Para drones con atomizador centrífugo (UGA): 250–320 µm sirve para la mayoría de los usos
GOTA_DRONE = {"general": [250, 320], "fino": [150, 250], "grueso": [350, 500]}

# Ajuste de gota por clima (Agrolink, fungicidas)
GOTA_CLIMA = "Con menos de 25 °C y más de 70 % de HR se puede usar gota fina; entre 25 y 28 °C con 60–70 % de HR, fina a media; con más de 28 °C o menos de 60 % de HR, media a gruesa."

# Altura de barra con separación de 50 cm (práctica de campo; INTA, Syngenta AR, GRDC)
ALTURA_BARRA = {"110": 50, "80": 75, "65": 80}

# Tolerancias de calibración e inspección (ISO 16122 / EN 13790, INTA)
TOLERANCIAS = {
 "pastilla_nominal_pct": 10,      # caudal ≥ 1 L/min: ±10 % del nominal; si < 1 L/min: ±15 %
 "pastilla_nominal_bajo_pct": 15,
 "pastilla_media_pct": 5,         # sin nominal: cada pastilla a ≤ 5 % de la media
 "volumen_pct": 5,                # error aceptado del volumen aplicado (L/ha)
 "mochila_pct": 10,               # mochila: la marcha y la presión varían más
 "cv_barra_pct": 10,              # CV de la distribución transversal (mesa de canales)
 "caida_presion_pct": 10,
 "eficiencia_campo_pct": 60,      # INTA usa ~60 % para la capacidad efectiva
 "dias_recalibrar": 180,          # al empezar cada campaña o al cambiar pastillas / producto
}

# Tiempos de colecta por color (INTA): para que todas las pastillas junten un volumen parecido
TIEMPO_COLECTA = {"015": 90, "02": 60, "03": 45, "04": 30}

CHECKLIST_INSPECCION = [
 "Sin pérdidas en tanque, mangueras y conexiones",
 "Bomba sin pulsaciones (caudal ≥ 90 % del nominal)",
 "Agitación visible a la presión máxima",
 "Manómetro de 63 mm o más, que vuelve a cero y lee bien entre 25 y 75 % de su escala",
 "Regulador y válvulas de sección mantienen la presión (±10 %)",
 "Filtros de carga, de bomba, de línea y de pastilla limpios y con la malla correcta",
 "Todas las pastillas del mismo tipo, tamaño y ángulo; ninguna con más de 10 % de desgaste",
 "Antigoteos sin goteo pasados 5 s del cierre",
 "Barra estable, a la misma altura en todo el ancho y separación entre pastillas pareja",
 "Velocidad real medida en el lote",
 "Lavado del tanque y volumen remanente conocido",
]
CHECKLIST_DRONE = [
 "Drone registrado en la DINAC (Registro Aeronáutico Nacional) y con placa de identificación",
 "Autorización expresa de la DINAC para operaciones de pulverización (DINAC R 1103)",
 "Piloto mayor de edad, con apto médico vigente y examen aprobado",
 "Seguro de responsabilidad civil vigente",
 "Empresa aplicadora registrada en el SENAVE y aviso al SENAVE 24 h antes (Ley 3742/09, arts. 59 y 60)",
 "Etiqueta del producto que permita la aplicación aérea o con drone",
 "Calibración de caudal hecha en la app del drone y ancho de faja verificado con tarjetas",
 "Baterías cargadas, hélices y atomizadores revisados, filtro del tanque limpio",
 "Zona reconocida antes del vuelo: personas, animales, viviendas, cursos de agua y cultivos sensibles (art. 62)",
 "Solo de día y con el drone siempre a la vista (VLOS)",
]
CHECKLIST_AVION = [
 "Empresa aplicadora registrada en el SENAVE con COA de la DINAC y aeronave habilitada (Res. 979/11, cat. A.8)",
 "Piloto con licencia, habilitación agrícola y registro PAAG en el SENAVE",
 "Aviso al SENAVE 24 h antes de la aplicación (Ley 3742/09, art. 60)",
 "Etiqueta del producto que permita la aplicación aérea",
 "Atomizadores o picos calibrados y ancho de faja verificado (prueba con tarjetas o colector)",
 "Banderillero satelital (DGPS) con el ancho de faja real cargado",
 "Reconocimiento previo de la zona y franja de 200 m respetada (arts. 62 y 67)",
 "Registro de la aplicación como declaración jurada (art. 61)",
]

NORMATIVA = {
 "terrestre": [
  "Ley 3742/09, art. 63: suspender la aplicación con más de 32 °C, menos de 60 % de humedad relativa o viento de más de 10 km/h.",
  "Ley 3742/09, art. 68: franja de 100 m sin aplicar junto a asentamientos, escuelas, centros de salud, templos, plazas y cursos de agua.",
  "Junto a caminos poblados: barrera viva de al menos 5 m de ancho y 2 m de alto o, sin barrera, 50 m sin aplicar (art. 68 y Decreto 2048/04, art. 13).",
  "Cargar y lavar los equipos lejos de los cursos de agua (Decreto 2048/04, art. 11).",
 ],
 "aereo": [
  "Ley 3742/09, art. 67: en aplicación aérea, franja de protección de 200 m respecto de asentamientos humanos, escuelas, centros de salud, templos, plazas, lugares de concurrencia pública y cursos de agua.",
  "Art. 60: el aplicador aéreo avisa al SENAVE 24 h antes. Art. 61: registro de cada aplicación como declaración jurada. Art. 62: reconocimiento previo de la zona.",
  "Art. 63: suspender con más de 32 °C, menos de 60 % de humedad relativa o viento de más de 10 km/h, o si hay personas o animales expuestos.",
  "Empresa aplicadora registrada en el SENAVE (cat. A.8) con habilitación de la DINAC; piloto agrícola registrado (PAAG).",
 ],
 "drone": [
  "DINAC R 1103 (Res. 2170/2017): drones registrados, piloto con apto médico y examen, vuelo solo de día y a la vista, seguro de responsabilidad civil, 50 m de edificaciones, vehículos y personas ajenas y 100 m de reuniones de personas; prohibido sobre zonas pobladas y cerca de aeródromos.",
  "La pulverización con drone requiere autorización expresa de la DINAC.",
  "La Ley 3742/09 no menciona los drones. Mientras no haya norma específica conviene tratarlos como aplicación aérea: franja de 200 m (art. 67), aviso al SENAVE 24 h antes y registro de la aplicación.",
  "Referencia regional: Brasil exige 20 m de distancia para drones (Portaria MAPA 298/2021); Argentina creó en 2026 un procedimiento excepcional y transitorio para autorizar la aplicación con drone de productos ya registrados, a pedido de la autoridad provincial (SENASA Res. 869/2026).",
 ],
}

# Recomendaciones de vuelo
VUELO = {
 "drone": {
  "volumen": "Lo habitual es de 10 a 30 L/ha. Para fungicidas e insecticidas de contacto o cultivos densos conviene ir a 20–30 L/ha; con menos de 15 L/ha la cobertura suele quedar corta. Respetar el mínimo de la etiqueta.",
  "altura": "1,5 a 3 m sobre el cultivo (más alto en terreno ondulado). Volar más alto no agranda la faja útil y aumenta la deriva.",
  "velocidad": "4 a 7 m/s. No usar la faja ni la velocidad máximas del fabricante.",
  "faja": "Usar el ancho de faja verificado con tarjetas hidrosensibles, no el máximo del catálogo.",
  "gota": "250 a 320 µm para la mayoría de los usos; más gruesa (350 µm o más) con herbicidas y cerca de cultivos sensibles.",
  "clima": "Viento de 3 a 10 km/h (hasta 3 m/s), sin inversión térmica; temperatura hasta 32 °C y humedad de 60 % o más (Ley 3742/09); Delta T entre 2 y 8.",
  "mezcla": "El tanque del drone casi no agita: preparar el caldo en un tanque nodriza con agitación, pasarlo por un filtro y aplicar cada carga enseguida. Prueba de jarra a la concentración real: debe quedar homogénea 8 a 10 minutos. Como máximo 2 productos por mezcla.",
 },
 "avion": {
  "volumen": "Con agua, de 10 a 50 L/ha. En bajo volumen oleoso (BVO) o ultra bajo volumen se usan menos litros con aceite como vehículo; seguir la etiqueta.",
  "altura": "Unos 3 a 6 m sobre el cultivo según el avión; con más viento, volar más bajo.",
  "velocidad": "La de trabajo del avión (unos 190 a 240 km/h en los modelos comunes).",
  "faja": "Usar la faja medida para ese avión y volumen (por ejemplo AT-502 unos 28 m, Ipanema 202 unos 19 m) y cargarla en el banderillero satelital.",
  "gota": "Con atomizadores rotativos (Micronair) la gota se regula con las revoluciones y el ángulo de las palas (60 a 750 µm).",
  "clima": "Viento de 3 a 10 km/h; nunca con calma (riesgo de inversión). Temperatura hasta 32 °C y humedad de 60 % o más (Ley 3742/09).",
  "mezcla": "Preparar en un tanque nodriza con agitación y cargar la tolva por filtro. En bajo volumen el caldo está mucho más concentrado: prueba de jarra a la concentración real.",
 },
}

# Modelos de drones (especificaciones del fabricante)
MODELOS_DRONE = [
 {"id": "dji_t10",  "nombre": "DJI Agras T10",  "tanque": 8,   "caudal": 1.8, "faja": [3, 5.5], "vel": 7,   "atom": "hidraulico", "n": 4,  "gota": [130, 300]},
 {"id": "dji_t20p", "nombre": "DJI Agras T20P", "tanque": 20,  "caudal": 12,  "faja": [4, 7],   "vel": 7,   "atom": "centrifugo", "n": 2,  "gota": [50, 500]},
 {"id": "dji_t25",  "nombre": "DJI Agras T25",  "tanque": 20,  "caudal": 16,  "faja": [4, 7],   "vel": 7,   "atom": "centrifugo", "n": 2,  "gota": [50, 500]},
 {"id": "dji_t30",  "nombre": "DJI Agras T30",  "tanque": 30,  "caudal": 8,   "faja": [4, 9],   "vel": 7,   "atom": "hidraulico", "n": 16, "gota": [130, 265]},
 {"id": "dji_t40",  "nombre": "DJI Agras T40",  "tanque": 40,  "caudal": 12,  "faja": [4, 11],  "vel": 7,   "atom": "centrifugo", "n": 2,  "gota": [50, 500]},
 {"id": "dji_t50",  "nombre": "DJI Agras T50",  "tanque": 40,  "caudal": 16,  "faja": [4, 11],  "vel": 7,   "atom": "centrifugo", "n": 2,  "gota": [50, 500]},
 {"id": "dji_t100", "nombre": "DJI Agras T100", "tanque": 100, "caudal": 30,  "faja": [5, 13],  "vel": 7,   "atom": "centrifugo", "n": 2,  "gota": [50, 500]},
 {"id": "xag_p100", "nombre": "XAG P100 Pro",   "tanque": 50,  "caudal": 22,  "faja": [5, 10],  "vel": 7,   "atom": "rotativo",   "n": 2,  "gota": [60, 400]},
]
# Aviones agrícolas (tolva, velocidad de trabajo, faja medida si la hay)
MODELOS_AVION = [
 {"id": "at402b", "nombre": "Air Tractor AT-402B", "tanque": 1514, "vel": 200, "faja": 27},
 {"id": "at502b", "nombre": "Air Tractor AT-502B", "tanque": 1893, "vel": 210, "faja": 28},
 {"id": "at602",  "nombre": "Air Tractor AT-602",  "tanque": 2385, "vel": 230, "faja": None},
 {"id": "at802a", "nombre": "Air Tractor AT-802A", "tanque": 3028, "vel": 230, "faja": None},
 {"id": "ipa202", "nombre": "Embraer EMB-202 Ipanema", "tanque": 950, "vel": 200, "faja": 19},
 {"id": "ipa203", "nombre": "Embraer EMB-203 Ipanema", "tanque": 950, "vel": 200, "faja": 22},
 {"id": "thr510", "nombre": "Thrush 510P2", "tanque": 1930, "vel": 210, "faja": None},
]

# Reglas del semáforo para aplicación aérea (modo en el caldo: "terrestre", "mochila", "drone" o "avion")
AEREO = ["drone", "avion"]
DERIVA_AI_AEREO = ["24d", "dicamba", "picloram", "triclopir", "fluroxipir", "aminopiralida", "clopiralida", "clomazona",
                   "halauxifen", "florpirauxifen", "fluchloraminopyr"]
REGLAS_AEREAS = [
 {"id": "DRN01", "tipo": "fisica_sedimento", "severidad": "alta",
  "titulo": "Tanque del drone sin agitación: suspensiones y polvos se asientan",
  "condiciones": {"presentes": [{"formulacion": ["WG", "WP", "WS", "SC", "SE", "CS", "ZC", "OD", "DC"]}], "agua": {}, "caldo": {"dron_sin_agitador": {"==": True}}},
  "mecanismo": "El tanque del drone casi no tiene agitación: con el caldo muy concentrado, las partículas de WG, WP y SC sedimentan en minutos, tapan el filtro y el caudal real baja sin aviso.",
  "recomendacion": "Preparar el caldo en un tanque nodriza con agitación, pasarlo por filtro y cargar el drone justo antes de cada vuelo. No dejar caldo quieto en el drone entre vuelos.",
  "confianza": "alta", "problemas": ["PR04", "PR27"]},
 {"id": "DRN02", "tipo": "fisica_queso", "severidad": "media",
  "titulo": "Más de 2 productos en el caldo de bajo volumen",
  "condiciones": {"presentes": [], "agua": {}, "caldo": {"modo": {"en": AEREO}, "n_productos": {">": 2}}},
  "mecanismo": "A 10–30 L/ha el caldo está 5 a 15 veces más concentrado que en una pulverizadora terrestre: cada producto extra multiplica el riesgo de grumos, capas o gel.",
  "recomendacion": "Limitar a 2 productos por mezcla o dividir la aplicación; hacer prueba de jarra a la concentración real (homogénea 8 a 10 min).",
  "confianza": "media", "problemas": ["PR01", "PR31"]},
 {"id": "DRN03", "tipo": "fisica_queso", "severidad": "alta",
  "titulo": "Polvo mojable (WP) en aplicación aérea",
  "condiciones": {"presentes": [{"formulacion": ["WP"]}], "agua": {}, "caldo": {"modo": {"en": AEREO}}},
  "mecanismo": "Los polvos mojables tienen cargas minerales que, concentradas, se asientan y tapan filtros, picos y atomizadores.",
  "recomendacion": "Preferir formulaciones SC, SL, EC u OD del mismo activo; si no hay, pre-dispersar en el tanque nodriza y filtrar.",
  "confianza": "media", "problemas": ["PR04", "PR27"]},
 {"id": "AER01", "tipo": "deriva", "severidad": "alta",
  "titulo": "Herbicidas hormonales o volátiles en aplicación aérea",
  "condiciones": {"presentes": [{"ai": DERIVA_AI_AEREO, "volatil": True}], "agua": {}, "caldo": {"modo": {"en": AEREO}}},
  "mecanismo": "Desde el aire la deriva llega más lejos: unas pocas gotas de auxínicos o de clomazona dañan algodón, soja no tolerante, hortalizas, frutales y eucalipto vecinos.",
  "recomendacion": "Preferir aplicación terrestre con pastillas de inducción de aire. Si se aplica por aire: gota extremadamente gruesa, antideriva, viento de 3 a 10 km/h alejándose de lo sensible y etiqueta que permita la aplicación aérea.",
  "confianza": "alta", "problemas": ["PR32"]},
 {"id": "AER02", "tipo": "deriva", "severidad": "media",
  "titulo": "Aplicación aérea: gotas finas que se evaporan y derivan",
  "condiciones": {"presentes": [], "agua": {}, "caldo": {"modo": {"en": AEREO}}},
  "mecanismo": "Con 10–30 L/ha se trabaja con gotas más finas y caldo concentrado; la evaporación y la deriva pesan más que en terrestre.",
  "recomendacion": "Gota de 250–320 µm o más gruesa con herbicidas, antievaporante o antideriva según etiqueta, horas frescas y franja de 200 m (Ley 3742/09, art. 67).",
  "confianza": "alta", "problemas": ["PR32", "PR33"]},
]
SEMAFORO_AEREAS = {
 "DRN01": [None, 0, {"premezcla": 1, "inmed": 1, "jarra": 1}],
 "DRN02": [None, 0, {"jarra": 1}],
 "DRN03": [None, 1, {"premezcla": 1, "jarra": 1}],
 "AER01": [None, 2, {"antideriva": 1, "gota": 1}],
 "AER02": [None, 0, {"gota": 1, "antievap": 1, "horario": 1}],
}
MEDIDAS_AEREAS = {
 "premezcla": {"tipo": "practica", "nombre": "Premezcla en tanque nodriza", "detalle": "Preparar el caldo en un tanque aparte con agitación, cargar el drone o la tolva por un filtro y aplicar enseguida."},
 "gota": {"tipo": "practica", "nombre": "Gota regulada para el producto", "detalle": "Ajustar el atomizador o los picos al tamaño de gota recomendado (más gruesa con herbicidas y cerca de cultivos sensibles) y verificar con tarjetas hidrosensibles."},
}

# ---------------- Funciones de cada tipo de equipo ----------------
# Fuentes: fichas Revista Cultivar "Compara Pulverizadores", folletos Jacto, Stara, John Deere, Case IH, New Holland;
# DJI Agras (T25, T50, T70P, T100) y XAG P100 Pro; Satloc G4; Micronair; GRDC (PWM).
# [id, nombre, por qué importa]
FUNCIONES = {
 "terrestre": [
  ["computadora", "Computadora de caudal", "Mantiene los litros por hectárea cuando cambia la velocidad, subiendo o bajando la presión. Ojo: al cambiar la presión cambia el tamaño de gota; conviene trabajar a velocidad pareja."],
  ["secciones", "Corte de secciones por GPS", "Cierra secciones en cabeceras y zonas ya aplicadas: menos superposición y menos producto fuera del lote. Cuantas más secciones, menos superposición."],
  ["picoapico", "Control pico a pico", "Cada pastilla se abre o cierra sola: superposición casi nula en cabeceras y bordes irregulares."],
  ["pwm", "PWM (modulación por ancho de pulso)", "Las pastillas pulsan muchas veces por segundo: el caudal cambia con la velocidad sin cambiar la presión, así la gota queda igual. Mantener el ciclo de trabajo por encima de 70 %. Compensa las curvas."],
  ["altura", "Control automático de altura de barra", "Sensores de ultrasonido mantienen la barra a la altura justa: distribución pareja y menos deriva."],
  ["suspension", "Suspensión y estabilización de barra", "Evita que la barra rebote o se adelante y atrase, que dejan franjas con más y menos producto."],
  ["piloto", "Piloto automático o RTK", "Pasadas paralelas exactas: sin huecos ni superposición entre pasadas; mejora el corte de secciones."],
  ["inyeccion", "Inyección directa", "El producto se dosifica en la línea y el tanque lleva solo agua: evita incompatibilidades de mezcla y sobrantes de caldo."],
  ["recirculacion", "Recirculación de barra", "El caldo circula por la barra antes de abrir: sin sedimento ni agua sola al empezar la pasada."],
  ["agitador", "Agitador del tanque", "Mantiene en suspensión WG, WP y SC durante la aplicación y los traslados."],
  ["incorporador", "Incorporador de productos", "Carga segura de los productos y triple lavado de envases; ayuda a respetar el orden de carga."],
  ["agua_limpia", "Tanque de agua limpia", "Permite lavar el circuito en el lote y reducir la contaminación entre productos."],
  ["selectiva", "Aplicación selectiva con cámaras", "Detecta las malezas y aplica solo sobre ellas (por ejemplo See & Spray): ahorra herbicida no residual."],
  ["estacion", "Estación meteorológica a bordo", "Registra viento, temperatura y humedad durante la aplicación."],
 ],
 "mochila": [
  ["cfvalve", "Válvula de caudal constante", "Mantiene la presión fija (1, 1,5 o 2 bar) aunque cambie el bombeo: caudal parejo (±1,5 %) y gota uniforme."],
  ["bateria", "Bomba a batería con presión constante", "La presión no depende del bombeo manual; varios niveles de presión elegibles."],
  ["motor", "Motorizada (atomizador)", "Gota fina transportada por aire, para frutales y cultivos altos; más deriva."],
  ["pantalla", "Pantalla o campana protectora", "Para aplicaciones dirigidas de herbicidas sin mojar el cultivo o los árboles."],
 ],
 "drone": [
  ["rtk", "RTK", "Posición al centímetro: pasadas exactas y faja real constante."],
  ["radar", "Radar y visión para evitar obstáculos", "Detecta árboles, cables y postes; necesario en silvopastoriles y lotes con cortinas."],
  ["terreno", "Seguimiento del terreno", "Mantiene la altura sobre el cultivo en terreno ondulado: faja y deriva estables."],
  ["centrifugo", "Atomizadores centrífugos con ajuste de gota", "El tamaño de gota se elige por las revoluciones del disco, no por la pastilla."],
  ["caudalimetro", "Caudalímetro", "Mide el caudal real: calibrarlo con agua antes de cada campaña o al cambiar de producto."],
  ["rutas", "Planificación de rutas y mapas", "Vuelo automático por el lote con las fajas y zonas de exclusión cargadas."],
  ["esparcidor", "Sistema de esparcido de granulados", "Permite aplicar cebos, semillas o fertilizantes granulados."],
  ["agitador", "Agitación en el tanque", "Pocos drones la tienen: sin ella el caldo con WG, WP o SC se asienta en minutos."],
 ],
 "avion": [
  ["dgps", "Banderillero satelital (DGPS)", "Guía las pasadas con el ancho de faja real y registra el vuelo (por ejemplo Satloc o AgNav)."],
  ["caudal_auto", "Control automático de caudal", "Mantiene la dosis cuando cambia la velocidad; algunos permiten dosis variable."],
  ["rotativos", "Atomizadores rotativos (tipo Micronair)", "Espectro de gotas más angosto; la gota depende del ángulo de las palas y de la velocidad del avión."],
  ["hidraulicos", "Picos hidráulicos", "La gota depende del pico, la presión y el ángulo respecto al viento."],
  ["registro", "Registro de vuelo y mapas", "Sirve de respaldo de la aplicación ante el SENAVE (registro de aplicaciones, art. 61)."],
 ],
}

# Catálogo de pulverizadoras terrestres (mercado brasileño/regional; verificar la versión vendida en Paraguay)
MODELOS_TERRESTRE = [
 {"id": "jacto_up2030", "nombre": "Jacto Uniport 2030", "tipo": "autopropulsada", "tanque": 2000, "barras": [24, 30], "esp": [35, 50], "vel": 40, "bomba": 190, "secciones": 8, "fun": ["computadora", "secciones", "suspension"]},
 {"id": "jacto_up3030", "nombre": "Jacto Uniport 3030", "tipo": "autopropulsada", "tanque": 3000, "barras": [36, 28, 32], "esp": [35, 50], "vel": 55, "bomba": 300, "fun": ["computadora", "picoapico", "suspension"]},
 {"id": "jacto_up4530", "nombre": "Jacto Uniport 4530", "tipo": "autopropulsada", "tanque": 4500, "barras": [42, 36], "esp": [35], "vel": 55, "bomba": 300, "fun": ["computadora", "picoapico", "suspension", "piloto"]},
 {"id": "stara_imp30", "nombre": "Stara Imperador 3.0", "tipo": "autopropulsada", "tanque": 2400, "agua_limpia": 240, "barras": [27, 30], "esp": [50], "vel": 42, "secciones": 7, "fun": ["computadora", "secciones", "picoapico", "recirculacion", "piloto", "agitador", "incorporador", "agua_limpia"]},
 {"id": "stara_imp4000", "nombre": "Stara Imperador 4000", "tipo": "autopropulsada", "tanque": 4000, "agua_limpia": 400, "barras": [30, 36], "esp": [50], "bomba": 803, "fun": ["computadora", "picoapico", "incorporador", "agua_limpia"]},
 {"id": "jd_4630", "nombre": "John Deere 4630", "tipo": "autopropulsada", "tanque": 2770, "agua_limpia": 265, "barras": [24.4, 27.4], "vel": 43, "secciones": 7, "fun": ["computadora", "secciones"]},
 {"id": "jd_m4030", "nombre": "John Deere M4030", "tipo": "autopropulsada", "tanque": 3000, "agua_limpia": 568, "barras": [30, 36], "vel": 30, "secciones": 9, "fun": ["computadora", "secciones", "altura", "piloto", "estacion", "incorporador", "agitador", "agua_limpia"]},
 {"id": "jd_m4040", "nombre": "John Deere M4040", "tipo": "autopropulsada", "tanque": 4000, "agua_limpia": 568, "barras": [36, 30], "esp": [38, 50], "vel": 32, "secciones": 9, "fun": ["computadora", "secciones", "altura", "piloto", "estacion", "incorporador", "agitador", "agua_limpia"]},
 {"id": "jd_r4038", "nombre": "John Deere R4038", "tipo": "autopropulsada", "tanque": 3800, "agua_limpia": 454, "barras": [40], "vel": 40, "secciones": 13, "fun": ["computadora", "secciones", "pwm", "picoapico", "altura", "piloto", "agua_limpia"]},
 {"id": "pla_125j", "nombre": "PLA 125J", "tipo": "autopropulsada", "tanque": 2500, "barras": [27], "fun": ["computadora", "secciones", "suspension"]},
 {"id": "case_patriot350", "nombre": "Case IH Patriot 350", "tipo": "autopropulsada", "tanque": 3500, "agua_limpia": 350, "barras": [30, 36], "esp": [50.8, 35], "secciones": 9, "fun": ["computadora", "secciones", "altura", "piloto", "suspension"]},
 {"id": "nh_def3500", "nombre": "New Holland Defensor 3500 HC", "tipo": "autopropulsada", "tanque": 3500, "agua_limpia": 350, "barras": [30, 36], "esp": [50.8, 35], "vel": 50, "bomba": 549, "secciones": 9, "fun": ["computadora", "secciones"]},
 {"id": "nh_def4000", "nombre": "New Holland Defensor 4000", "tipo": "autopropulsada", "tanque": 4000, "agua_limpia": 400, "barras": [30, 36], "esp": [50.8, 35], "vel": 50, "bomba": 746, "fun": ["computadora", "picoapico", "altura", "suspension"]},
 {"id": "metalfor_fm2500", "nombre": "Metalfor FM2500", "tipo": "autopropulsada", "tanque": 2500, "barras": [20], "fun": ["suspension"]},
 {"id": "jacto_columbia", "nombre": "Jacto Columbia (Cross)", "tipo": "arrastre", "tanque": 2000, "barras": [18], "esp": [35, 50], "bomba": 150, "fun": ["agitador", "suspension"]},
 {"id": "jacto_adv3000", "nombre": "Jacto Advance 3000", "tipo": "arrastre", "tanque": 3000, "agua_limpia": 200, "barras": [20], "esp": [50], "secciones": 4, "fun": ["computadora", "secciones", "agitador", "incorporador", "agua_limpia"]},
 {"id": "metalfor_futur3000", "nombre": "Metalfor Futur 3000S", "tipo": "arrastre", "tanque": 3000, "barras": [20], "esp": [35, 52], "bomba": 110, "secciones": 3, "fun": ["secciones", "suspension"]},
]
MODELOS_MOCHILA = [
 {"id": "jacto_pjh", "nombre": "Jacto PJH (20 L)", "tanque": 20, "pmax": 6.8, "fun": []},
 {"id": "jacto_djb20", "nombre": "Jacto DJB-20 (batería)", "tanque": 20, "fun": ["bateria"]},
 {"id": "stihl_sr450", "nombre": "Stihl SR 450 (atomizador)", "tanque": 14, "fun": ["motor"]},
]
# Funciones de los drones del catálogo
FUN_DRONE = {
 "dji_t10": ["rtk", "radar", "terreno", "caudalimetro", "rutas", "esparcidor"],
 "dji_t20p": ["rtk", "radar", "terreno", "centrifugo", "caudalimetro", "rutas", "esparcidor"],
 "dji_t25": ["rtk", "radar", "terreno", "centrifugo", "caudalimetro", "rutas", "esparcidor"],
 "dji_t30": ["rtk", "radar", "terreno", "caudalimetro", "rutas", "esparcidor"],
 "dji_t40": ["rtk", "radar", "terreno", "centrifugo", "caudalimetro", "rutas", "esparcidor"],
 "dji_t50": ["rtk", "radar", "terreno", "centrifugo", "caudalimetro", "rutas", "esparcidor"],
 "dji_t70p": ["rtk", "radar", "terreno", "centrifugo", "caudalimetro", "rutas", "esparcidor"],
 "dji_t100": ["rtk", "radar", "terreno", "centrifugo", "caudalimetro", "rutas", "esparcidor"],
 "xag_p100": ["rtk", "radar", "terreno", "centrifugo", "caudalimetro", "rutas", "esparcidor"],
}
MODELOS_DRONE.insert(6, {"id": "dji_t70p", "nombre": "DJI Agras T70P", "tanque": 70, "caudal": 30, "faja": [4, 11], "vel": 7, "atom": "centrifugo", "n": 2, "gota": [50, 500]})
BATERIAS_DRONE = {
 "dji_t25": "DB800: carga rápida 9–12 min", "dji_t50": "DB1560: 1.500 ciclos; carga rápida 9–12 min o 2 h normal",
 "dji_t100": "41 Ah: carga 30→95 % en 8–9 min", "xag_p100": "962 Wh: carga con refrigeración por agua en 11 min",
}
