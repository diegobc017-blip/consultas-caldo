# Pronóstico del tiempo y momento de aplicación.
# Pronóstico: Open-Meteo (https://open-meteo.com, datos CC BY 4.0, uso no comercial sin clave), modelos ECMWF IFS 0,25° y GFS.
# Alertas oficiales: Dirección de Meteorología e Hidrología del Paraguay (https://www.meteorologia.gov.py/), sin API pública.
# Tiempos sin lluvia: UF EDIS AG359, Oklahoma State L-468, TAMU (pasturas), UGA (fungicidas de maíz y algodón),
# OMAFRA, Purdue (activación de preemergentes), Sprayers101, vegcropshotline. La etiqueta del producto manda.
# Calor: Rutgers (volatilidad de dicamba y 2,4-D), etiqueta Cosavet (azufre), UConn (aceites).
# Inversión térmica: GRDC (hazardous inversion), Iowa State.

OPEN_METEO = {
 "url": "https://api.open-meteo.com/v1/forecast",
 "hourly": "temperature_2m,temperature_80m,relative_humidity_2m,precipitation,precipitation_probability,wind_speed_10m,wind_gusts_10m,wind_direction_10m,cloud_cover,is_day",
 "modelos": [["ecmwf_ifs025", "ECMWF (Centro Europeo)"], ["gfs_seamless", "GFS (NOAA, EE. UU.)"]],
 "dias": 4,
 "atribucion": "Pronóstico: Open-Meteo.com (CC BY 4.0), modelos ECMWF y GFS",
 "dmh": "https://www.meteorologia.gov.py/",
}

# Horas sin lluvia que necesita cada activo después de aplicar (valor prudente cuando las fuentes difieren)
LAVADO_H = {
 "glifosato": 6, "24d": 6, "dicamba": 4, "picloram": 2, "triclopir": 6, "fluroxipir": 2, "aminopiralida": 4,
 "paraquat": 0.5, "diquat": 0.5, "glufosinato": 4, "glufosinato_p": 4, "cletodim": 1, "haloxifop": 1,
 "quizalofop": 1, "propaquizafop": 1, "fenoxaprop": 1, "imazetapir": 1, "clorimuron": 4, "metsulfuron": 4,
 "saflufenacil": 1, "fomesafen": 1, "lactofen": 1, "carfentrazona": 1, "flumioxazin": 1, "atrazina": 4,
 "bentazona": 8, "metribuzina": 6,
 "mancozeb": 4, "clorotalonil": 4, "cobre": 4, "azufre": 4, "tiram": 4, "folpet": 4,
}
# Glifosato según la sal (sal potásica de marca: 0,5–1 h; isopropilamina genérica: hasta 6 h)
LAVADO_FORMA = {"glifosato": {"sal_potasica": 1, "sal_amonica": 4, "sal_dimetilamina": 4}}
# Por clase y grupo cuando el activo no está en la lista
LAVADO_CLASE = {"herbicida": 4, "fungicida": 2, "insecticida": 2, "default": 2}
LAVADO_GRUPO = {"FRAC M": 4, "IRAC 4A": 4, "IRAC 1B": 6, "IRAC 28": 1, "IRAC 3A": 2, "IRAC 15": 2}
LAVADO_NOTA = {
 "glifosato": "Sal potásica de marca: 0,5 a 1 h; genéricos de isopropilamina: hasta 6 h.",
 "24d": "Amina: 6 h; algunas etiquetas piden hasta 48 h.",
 "dicamba": "4 h; las formulaciones para soja tolerante piden no aplicar si se espera lluvia en 24 h.",
 "mancozeb": "Necesita secarse sobre la hoja; lo ideal es aplicar unas 24 h antes de la lluvia (25 mm lavan la mitad).",
 "clorotalonil": "Ideal 8 a 24 h antes de la lluvia.",
 "cobre": "Unos 5 mm de lluvia lavan el 80 %.",
}
# Preemergentes: la lluvia los activa (no es un riesgo)
PREEMERGENTES = ["s_metolacloro", "metolacloro", "acetocloro", "piroxasulfona", "trifluralina", "pendimetalina",
                 "clomazona", "isoxaflutol", "sulfentrazona", "diclosulam", "imazapic", "flumetsulam", "diuron", "simazina", "hexazinona", "tebutiuron"]
# De suelo y de hoja: aplicados en preemergencia del cultivo (malezas sin emerger) la lluvia los activa;
# en barbecho o sobre el cultivo emergido actúan también por hoja y cuentan las horas sin lluvia.
PRE_SEGUN_MOMENTO = ["atrazina", "metribuzina", "flumioxazin", "saflufenacil", "imazetapir", "clorimuron"]
LLUVIA_ACTIVACION = "Los preemergentes necesitan lluvia para activarse: unos 12 a 25 mm en los días siguientes (según el suelo y la etiqueta)."

# Calor
AUXINICOS_VOLATILES = ["24d", "dicamba", "triclopir"]
T_VOLATILIDAD = 29     # desde aquí aumenta la volatilidad de dicamba y 2,4-D
T_ACEITE_AZUFRE = 30   # aceites y azufre: fitotoxicidad (las etiquetas fijan 32 °C)

# Inversión térmica (desde datos horarios).
# GRDC: no aplicar con menos de 5 km/h medidos a 2 m; el pronóstico da el viento a 10 m, que con aire estable es bastante mayor: se usa 8 km/h.
# Señal directa: aire más caliente a 80 m que a 2 m (solo el modelo GFS publica temperature_80m; ECMWF devuelve vacío).
INVERSION = {"viento_max": 8, "nubes_max": 25, "dif_80m": 1, "viento_max_80m": 12}
RAFAGA_ALTA = 20

# Reglas del semáforo que dependen del pronóstico o de las condiciones cargadas
REGLAS_CLIMA = [
 {"id": "LL02", "tipo": "manejo", "severidad": "alta",
  "titulo": "Lluvia antes del tiempo que necesita el producto",
  "condiciones": {"presentes": [], "agua": {}, "caldo": {"lluvia_margen_h": {"<": 0}}},
  "mecanismo": "Cada producto necesita unas horas sin lluvia para absorberse o secarse sobre la hoja (glifosato y 2,4-D amina hasta 6 h; contacto como mancozeb unas 4 h; paraquat 30 min). Si llueve antes, se lava y pierde eficacia.",
  "recomendacion": "Elegir un horario con más horas sin lluvia por delante o postergar; un adherente o aceite según etiqueta ayuda poco y no reemplaza el tiempo sin lluvia.",
  "confianza": "media", "problemas": ["PR33"]},
 {"id": "CA01", "tipo": "deriva", "severidad": "media",
  "titulo": "Calor con herbicidas hormonales: volatilización",
  "condiciones": {"presentes": [{"ai": AUXINICOS_VOLATILES}], "agua": {}, "caldo": {"temperatura_ambiente_C": {">=": T_VOLATILIDAD}}},
  "mecanismo": "Desde unos 29 °C el dicamba y el 2,4-D (sobre todo éster) pasan a vapor y se mueven horas después de aplicados; la etiqueta de dicamba sobre soja prohíbe aplicar si se esperan 35 °C ese día o el siguiente.",
  "recomendacion": "Aplicar en las horas frescas, preferir sal colina o amina y revisar el pronóstico del día siguiente.",
  "confianza": "alta", "problemas": ["PR17", "PR32"]},
 {"id": "CA02", "tipo": "fitotoxicidad", "severidad": "alta",
  "titulo": "Calor con aceites o azufre: quemado de hojas",
  "condiciones": {"presentes": [{"adyuvante": ["ady_mso", "ady_aceite_mineral", "ady_aceite_vegetal"], "ai": ["azufre"]}], "agua": {}, "caldo": {"temperatura_ambiente_C": {">": T_ACEITE_AZUFRE}}},
  "mecanismo": "Con más de 30 °C los aceites y el azufre aumentan la penetración y queman tejidos; las etiquetas de azufre piden no aplicar si se esperan más de 32 °C en los 3 días siguientes.",
  "recomendacion": "Aplicar temprano o al atardecer, usar la dosis mínima de aceite y no aplicar azufre con calor pronosticado.",
  "confianza": "alta", "problemas": ["PR23"]},
]
SEMAFORO_CLIMA = {
 "LL02": [None, 1, {"adherente": 1}],
 "CA01": [None, 0, {"horario": 1}],
 "CA02": [None, 0, {"horario": 1, "dosismin": 1}],
}
