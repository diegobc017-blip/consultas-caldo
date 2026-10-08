# Sistema silvopastoril: árboles + pasturas + ganado.
# Fuentes (revisadas el 05/10/2026):
#  - PNUD/MADES/Green BAAPA (2020), Recomendaciones técnicas para sistema silvopastoril con eucalipto (Paraguay); póster INFONA/ARP/UNICOOP
#  - Embrapa Pecuária Sudeste (2019) implantación del componente arbóreo; Embrapa Mato Grosso (2021)
#  - Etiquetas brasileñas de Tordon HL y Fluroxipir + Picloram Nortox (eucalipto como cultivo sensible, franja de 10 m)
#  - Carvalho et al. 2014 (Rev. Árvore), Tuffi Santos et al. 2006 (UFV): deriva de triclopir, fluroxipir y glifosato en eucalipto
#  - Silva et al. 2004 (imazapir letal para eucalipto); etiqueta Spike 20P (tebutiurón: 1-2 veces la altura de los árboles)
#  - Agostinetto 2010, Tiburcio 2010 (selectividad de isoxaflutol, flumioxazin en eucalipto); Duarte et al. 2004 (Enterolobium)
#  - TAMU ESC-046, Univ. of Arkansas MP44, NDSU (restricciones de pastoreo y heno); Montana State (estiércol y compost)
#  - LSU 2025 (insecticidas en pasturas); etiqueta Fluramim (sulfluramida: animales fuera 24 h)

RUBRO_SP = {"nombre": "Silvopastoril", "detalle": "Árboles (eucalipto, pino o nativas) con pasturas y ganado: malezas sin dañar los árboles, hormigas cortadoras y reingreso de los animales"}

AUXINICOS = ["24d", "dicamba", "picloram", "triclopir", "fluroxipir", "aminopiralida", "clopiralida", "halauxifen"]
RESIDUAL_RAIZ = ["picloram", "tebutiuron", "hexazinona", "imazapir", "aminopiralida", "sulfometuron"]
TOTALES = ["glifosato", "paraquat", "diquat", "glufosinato", "glufosinato_p"]
ESTIERCOL = ["picloram", "clopiralida", "aminopiralida"]

SOLO_FILA = ["isoxaflutol", "sulfentrazona", "flumioxazin", "oxifluorfen", "simazina", "haloxifop"]
REGLAS_SILVO = [
 {"id": "SP06", "tipo": "fitotoxicidad", "severidad": "alta",
  "titulo": "Preemergente forestal o graminicida en silvopastoril: mata la pastura",
  "condiciones": {"presentes": [{"ai": SOLO_FILA}], "agua": {}, "caldo": {"rubro": {"==": "SP"}}},
  "mecanismo": "Los preemergentes de eucalipto (isoxaflutol, sulfentrazona, flumioxazin, oxifluorfen, simazina) y los graminicidas controlan justamente los pastos: en silvopastoril la pastura es el cultivo.",
  "recomendacion": "Usarlos solo en la fila de árboles, en la implantación y antes de sembrar la pastura, dirigidos; nunca en cobertura sobre el potrero.",
  "confianza": "alta", "problemas": ["PR24"]},
 {"id": "SP01", "tipo": "fitotoxicidad", "severidad": "alta",
  "titulo": "Herbicida hormonal en silvopastoril: daña los árboles",
  "condiciones": {"presentes": [{"ai": AUXINICOS}], "agua": {}, "caldo": {"rubro": {"==": "SP"}}},
  "mecanismo": "Los auxínicos de pasturas (2,4-D, picloram, triclopir, fluroxipir, aminopiralida, dicamba) controlan justamente plantas de hoja ancha: el eucalipto y las especies nativas o leguminosas también lo son. Las etiquetas de picloram en Brasil listan al eucalipto como cultivo sensible.",
  "recomendacion": "Aplicación dirigida a las malezas, a más de 10 m de la fila de árboles, con gota gruesa y antideriva; nunca sobre la copa ni con viento hacia los árboles.",
  "confianza": "alta", "problemas": ["PR23", "PR32"]},
 {"id": "SP02", "tipo": "fitotoxicidad", "severidad": "critica",
  "titulo": "Herbicida residual que absorben las raíces de los árboles",
  "condiciones": {"presentes": [{"ai": RESIDUAL_RAIZ}], "agua": {}, "caldo": {"rubro": {"==": "SP"}}},
  "mecanismo": "Picloram, tebutiurón, hexazinona, imazapir y aminopiralida quedan activos en el suelo y las raíces de los árboles los absorben aunque la aplicación no toque las hojas. Las raíces llegan más allá de la copa; el imazapir se usa justamente para matar eucaliptos.",
  "recomendacion": "No aplicar bajo la copa ni en la zona de raíces: dejar una distancia de 1 a 2 veces la altura de los árboles (etiqueta de tebutiurón). Con eucalipto evitar imazapir.",
  "confianza": "alta", "problemas": ["PR23"]},
 {"id": "SP03", "tipo": "deriva", "severidad": "alta",
  "titulo": "Herbicida total cerca de los árboles",
  "condiciones": {"presentes": [{"ai": TOTALES}], "agua": {}, "caldo": {"rubro": {"==": "SP"}}},
  "mecanismo": "La deriva de glifosato daña al eucalipto: por encima de unos 86 g/ha (6 % de una dosis normal) ya reduce altura y diámetro; los de contacto queman hojas y corteza verde.",
  "recomendacion": "Solo dirigido a las malezas, con pantalla o mochila, sin mojar hojas ni tallos verdes; con viento que se aleje de los árboles.",
  "confianza": "alta", "problemas": ["PR23", "PR32"]},
 {"id": "SP04", "tipo": "manejo", "severidad": "media",
  "titulo": "Animales en el potrero: período de reingreso y de carencia",
  "condiciones": {"presentes": [{"clase": ["herbicida", "insecticida", "fungicida"]}], "agua": {}, "caldo": {"rubro": {"en": ["SP", "PA"]}}},
  "mecanismo": "Cada producto tiene en la etiqueta cuánto esperar para volver a pastorear, cortar heno o mandar animales a faena; las vacas lecheras suelen tener plazos más largos.",
  "recomendacion": "Sacar los animales antes de aplicar y respetar el reingreso de la etiqueta del producto registrado en el SENAVE.",
  "confianza": "alta", "problemas": ["PR26"]},
 {"id": "SP05", "tipo": "manejo", "severidad": "media",
  "titulo": "Estiércol de animales que comieron pasto tratado",
  "condiciones": {"presentes": [{"ai": ESTIERCOL}], "agua": {}, "caldo": {"rubro": {"en": ["SP", "PA"]}}},
  "mecanismo": "Picloram, clopiralida y aminopiralida pasan casi intactos por el animal: el estiércol, el compost o el heno de ese potrero dañan hortalizas, leguminosas y árboles sensibles.",
  "recomendacion": "No usar estiércol ni compost de esos animales en cultivos sensibles (las etiquetas brasileñas indican 60 días); no sacar del campo el heno tratado con aminopiralida.",
  "confianza": "alta", "problemas": ["PR23"]},
]
SEMAFORO_SILVO = {
 "SP06": [None, 1, {"solofila": 1}],
 "SP01": [None, 1, {"dirigida": 1, "antideriva": 1}],
 "SP02": [None, 2, {"zonaraiz": 1}],
 "SP03": [None, 0, {"dirigida": 1, "antideriva": 1}],
 "SP04": [None, 0, {"retiro": 1}],
 "SP05": [1, 1, {}],
}
MEDIDAS_SILVO = {
 "solofila": {"tipo": "practica", "nombre": "Solo en la fila de árboles, antes de sembrar la pastura", "detalle": "Dirigido a la línea de plantación en la implantación, cuando todavía no hay pastura sembrada; nunca en cobertura sobre el potrero."},
 "dirigida": {"tipo": "practica", "nombre": "Aplicación dirigida lejos de los árboles", "detalle": "Dirigida a las malezas con pantalla, mochila o barra corta, a más de 10 m de la fila de árboles y sin mojar hojas ni tallos de los árboles."},
 "zonaraiz": {"tipo": "practica", "nombre": "Fuera de la zona de raíces", "detalle": "No aplicar bajo la copa ni a menos de 1 a 2 veces la altura de los árboles."},
 "retiro": {"tipo": "practica", "nombre": "Animales fuera del potrero", "detalle": "Animales retirados antes de aplicar y reingreso según la etiqueta."},
}

# Riesgo para los árboles según el grupo: [nivel 0-3, texto]
ARBOLES = {"euc": "Eucalipto", "pino": "Pino", "nat": "Nativas o leguminosas"}
RIESGO_ARBOL = {
 "24d":          {"euc": [2, "Sensible: la deriva deforma hojas y frena el crecimiento"], "pino": [1, "Moderado: evitar mojar los brotes"], "nat": [2, "Sensibles, sobre todo las leguminosas"]},
 "picloram":     {"euc": [3, "Sensible por hoja y por raíz (residual): las etiquetas lo listan como cultivo sensible"], "pino": [2, "Residual absorbido por raíces"], "nat": [3, "Sensibles por hoja y por raíz"]},
 "triclopir":    {"euc": [2, "La deriva daña (síntomas hasta unos 50 días)"], "pino": [1, "Evitar mojar los brotes"], "nat": [2, "Sensibles"]},
 "fluroxipir":   {"euc": [2, "La deriva daña"], "pino": [1, "Evitar mojar los brotes"], "nat": [2, "Sensibles, sobre todo las leguminosas"]},
 "aminopiralida":{"euc": [3, "Sensible por hoja y por raíz (muy residual)"], "pino": [2, "Residual absorbido por raíces"], "nat": [3, "Leguminosas muy sensibles"]},
 "clopiralida":  {"euc": [2, "Sensible a la deriva"], "pino": [1, "Poco sensible"], "nat": [3, "Leguminosas muy sensibles"]},
 "dicamba":      {"euc": [2, "Sensible; además es volátil"], "pino": [1, "Evitar mojar los brotes"], "nat": [2, "Sensibles"]},
 "metsulfuron":  {"euc": [2, "Sin datos de selectividad confirmados: solo dirigido"], "pino": [0, "Los pinos lo toleran (usado sobre el pino en EE. UU.)"], "nat": [2, "Sin datos: solo dirigido"]},
 "tebutiuron":   {"euc": [3, "Lo absorben las raíces: distancia de 1 a 2 veces la altura del árbol"], "pino": [3, "Lo absorben las raíces"], "nat": [3, "Lo absorben las raíces"]},
 "hexazinona":   {"euc": [2, "Residual: solo en preplantío o lejos de la fila"], "pino": [0, "Los pinos lo toleran"], "nat": [3, "Residual absorbido por raíces"]},
 "imazapir":     {"euc": [3, "Letal para el eucalipto (se usa para matar tocones)"], "pino": [0, "Los pinos lo toleran"], "nat": [3, "Muy dañino"]},
 "glifosato":    {"euc": [2, "La deriva reduce altura y diámetro: solo dirigido con pantalla"], "pino": [1, "No mojar brotes en crecimiento"], "nat": [3, "Mata las plantas jóvenes (Enterolobium)"]},
 "paraquat":     {"euc": [2, "Quema hojas y corteza verde: solo dirigido"], "pino": [2, "Quema follaje"], "nat": [2, "Quema follaje"]},
 "diquat":       {"euc": [2, "Quema hojas y corteza verde: solo dirigido"], "pino": [2, "Quema follaje"], "nat": [2, "Quema follaje"]},
 "glufosinato":  {"euc": [2, "Quema el follaje que moja: solo dirigido"], "pino": [2, "Quema follaje"], "nat": [2, "Quema follaje"]},
 "isoxaflutol":  {"euc": [0, "Selectivo para eucalipto (preemergente de plantaciones)"], "pino": [1, "Ver etiqueta"], "nat": [0, "Sin daño en Enterolobium"]},
 "flumioxazin":  {"euc": [0, "Selectivo para eucalipto; daño leve que se recupera"], "pino": [1, "Ver etiqueta"], "nat": [1, "Ver etiqueta"]},
 "sulfentrazona":{"euc": [0, "Usado en plantaciones de eucalipto"], "pino": [1, "Ver etiqueta"], "nat": [0, "Sin daño en Enterolobium"]},
 "oxifluorfen":  {"euc": [1, "Preemergente en plantaciones; no mojar follaje"], "pino": [1, "Ver etiqueta"], "nat": [1, "Daño leve y pasajero"]},
}
RIESGO_GRAMINICIDA = [0, "Solo controla gramíneas: no afecta a los árboles (pero sí a la pastura de gramíneas)"]

# Reingreso de animales y heno: valores de referencia de etiquetas (EE. UU. y Brasil); en Paraguay rige la etiqueta del SENAVE
REINGRESO = {
 "24d": "Ganado de carne sin restricción; lecheras 7–14 días; heno 7–30 días; faena 3–7 días.",
 "picloram": "Ganado de carne sin restricción; lecheras 7–14 días; heno 14–30 días; faena 3 días. Estiércol: no usar en cultivos sensibles por 60 días.",
 "triclopir": "Ganado de carne sin restricción; lecheras 14 días o hasta la temporada siguiente (dosis altas); heno 14 días; faena 3 días.",
 "fluroxipir": "Con triclopir: lecheras hasta la temporada siguiente; heno 14 días; faena 3 días.",
 "aminopiralida": "Sin restricción de pastoreo; el heno tratado no sale del campo por 18 meses; estiércol y compost no van a cultivos sensibles.",
 "clopiralida": "Pocas restricciones de pastoreo; estiércol y compost no van a cultivos sensibles.",
 "dicamba": "Lecheras 7–60 días según la dosis; heno 37–90 días; faena 30 días.",
 "tebutiuron": "Sin restricción de pastoreo; heno 1 año.",
 "lambdacialotrina": "Pastoreo 1 día; heno 7 días (EE. UU.). En Brasil algunos productos no están registrados para pasturas: verificar la etiqueta.",
 "diflubenzuron": "Pastoreo 1 día; heno 1 día.",
 "sulfluramida": "Cebo: animales fuera del área 24 h; aplicar en los orificios activos o en portacebos.",
 "fipronil": "Cebo: aplicar en los orificios activos o en portacebos, lejos de los animales; muy tóxico para abejas.",
}

PRACTICAS_SILVO = [
 "Círculo limpio de unos 2 m alrededor de cada árbol joven, con carpida o glifosato dirigido con pantalla.",
 "Los animales entran cuando los árboles superan 2,5 a 3 m de altura o 6 cm de diámetro a 1,3 m (unos 18 meses); antes, con alambrado que proteja las filas.",
 "Hormigas cortadoras: controlarlas antes de plantar y revisar cada 15 días los primeros años, con cebos en los orificios activos.",
 "Malezas de la pastura: preferir productos selectivos de gramíneas (no afectan árboles) o aplicaciones dirigidas; evitar los residuales de suelo cerca de las filas.",
 "Aplicar con viento que se aleje de las filas de árboles y dejar una franja sin aplicar junto a ellas.",
]
