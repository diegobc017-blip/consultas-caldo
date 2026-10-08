# Organización de la app por rubro: cultivos, modos de aplicación, tipos de equipo, volúmenes de referencia,
# caldos de ejemplo y casos prácticos, y el módulo de granos almacenados (revisión del 08/10/2026).
# Fuentes de volúmenes: Jacto, Embrapa, INTA, Aapresid (valores de referencia; la etiqueta manda).
# Turboatomizador: método TRV (Tree Row Volume), Fundecitrus (Manual de Tecnologia de Aplicação 2024), IVIA (CitrusVol).
# Granos: etiquetas de Actellic 500 EC (ADAPAR, Brasil) y K-Obiol 2,5 EC (Brasil y México), INTA (insecticidas autorizados
# en granos almacenados), Embrapa (Lorini, Boas práticas de armazenagem), etiquetas de Phostoxin (Brasil y EE. UU.), GRDC.

CULTIVOS_NUEVOS = {"citricos": "Cítricos", "frutales": "Frutales (durazno, mango, uva…)"}
# Cultivos sin datos de selectividad de herbicidas en la app
SIN_SELECT = ["citricos", "frutales"]

CULT_RUBRO = {
 "AG": ["soja", "maiz", "trigo", "arroz", "sorgo", "girasol", "canola", "algodon", "poroto", "sesamo", "chia", "cana", "mandioca"],
 "HO": ["hortalizas", "citricos", "frutales", "mandioca", "poroto"],
 "FO": ["eucalipto"],
 "PA": ["pastura_gram", "pastura_leg"],
 "SP": ["pastura_gram", "pastura_leg", "eucalipto"],
 "AL": [],
}
MODOS_RUBRO = {
 "AG": ["terrestre", "mochila", "drone", "avion"],
 "HO": ["terrestre", "turbo", "mochila", "drone"],
 "FO": ["terrestre", "mochila", "drone", "avion"],
 "PA": ["terrestre", "mochila", "drone", "avion"],
 "SP": ["terrestre", "mochila", "drone"],
 "AL": ["granos", "mochila"],
}
TIPOS_RUBRO = {
 "AG": ["autopropulsada", "arrastre", "montada", "mochila", "drone", "avion"],
 "HO": ["montada", "arrastre", "turbo", "mochila", "pistola", "drone"],
 "FO": ["arrastre", "montada", "mochila", "pistola", "drone", "avion"],
 "PA": ["arrastre", "montada", "autopropulsada", "mochila", "pistola", "drone", "avion"],
 "SP": ["arrastre", "montada", "mochila", "pistola", "drone"],
 "AL": ["cinta", "mochila"],
}
# Volumen de referencia [mín, máx, texto] por rubro y modo (L/ha; en granos, L de caldo por tonelada)
VOL_RUBRO = {
 "AG": {"terrestre": [50, 150, "Herbicidas 50–150 L/ha; fungicidas e insecticidas 80–150 L/ha"],
        "mochila": [150, 300, "Mochila: 150–300 L/ha según la faja y el paso"],
        "drone": [8, 15, "Drone: 8–15 L/ha (más volumen con fungicidas o canopeo cerrado)"],
        "avion": [10, 30, "Avión: 10–30 L/ha"]},
 "HO": {"terrestre": [200, 1000, "Hortalizas: 200–400 L/ha con plantas chicas; 600–1000 L/ha con plena cobertura"],
        "turbo": [300, 3000, "Frutales y cítricos: según el volumen de copa (0,025 a 0,10 L por m³ de copa según el objetivo)"],
        "mochila": [200, 1000, "Mochila: mojar sin chorrear; 200–800 L/ha según el tamaño de las plantas"],
        "drone": [10, 30, "Drone en hortalizas y frutales: 10–30 L/ha, con gota media"]},
 "FO": {"terrestre": [100, 200, "Herbicidas en eucalipto y pino: 100–200 L/ha; después de plantar, dirigido con campana"],
        "mochila": [150, 300, "Mochila con campana: 150–300 L/ha de faja"],
        "drone": [10, 30, "Drone: 10–30 L/ha"], "avion": [20, 50, "Avión: 20–50 L/ha"]},
 "PA": {"terrestre": [100, 200, "Pasturas: 100–200 L/ha con barra; localizado con manguera, mojar bien cada planta"],
        "mochila": [150, 300, "Mochila: 150–300 L/ha o al 1 % para leñosas (localizado)"],
        "drone": [10, 30, "Drone: 10–30 L/ha"], "avion": [20, 50, "Avión: 20–50 L/ha"]},
 "SP": {"terrestre": [150, 200, "Entre filas de árboles: 150–200 L/ha, dirigido y con gota gruesa"],
        "mochila": [150, 300, "Mochila con campana alrededor de los árboles: 150–300 L/ha de faja"],
        "drone": [10, 30, "Drone: solo con radar y lejos de los árboles"]},
 "AL": {"granos": [0.3, 1.5, "Protectores de granos: 0,3 a 1 L de caldo por tonelada (Embrapa: no más de 1–1,5 L/t)"],
        "mochila": [0, 0, "Estructuras vacías: según la etiqueta (por ejemplo 2 a 25 L de caldo cada 100 m²)"]},
}

# Caldo de ejemplo por rubro (registros SENAVE vigentes; dosis dentro del rango de etiqueta de Brasil o Chile para
# la misma formulación cuando la de Paraguay no está publicada). AG usa el caso práctico original de la app.
EJEMPLOS = {
 "HO": {"items": [["2618", 3.0], ["4266", 0.09]], "vol": 600, "tanque": 600, "modo": "terrestre", "sup": 2,
        "cult": {"actual": "tomate", "momento": "post", "siguiente": None},
        "caldo": {"horas_en_tanque": 1, "temperatura_ambiente_C": 24, "HR": 70, "viento_kmh": 6, "nubosidad": "Parcial"},
        "agua": {"pH": 7.2, "dureza_ppm_CaCO3": 120}},
 "FO": {"items": [["2979", 3.0], ["1501", 0.15]], "vol": 150, "tanque": 2000, "modo": "terrestre", "sup": 40,
        "cult": {"actual": "eucalipto", "momento": "barbecho", "siguiente": None, "siembra_act_dias": 7},
        "caldo": {"horas_en_tanque": 2, "temperatura_ambiente_C": 26, "HR": 65, "viento_kmh": 7, "nubosidad": "Parcial"},
        "agua": {"pH": 6.8, "dureza_ppm_CaCO3": 80}},
 "PA": {"items": [["311", 3.0]], "vol": 200, "tanque": 2000, "modo": "terrestre", "sup": 50,
        "cult": {"actual": "pastura_gram", "momento": "post", "siguiente": None},
        "caldo": {"horas_en_tanque": 2, "temperatura_ambiente_C": 27, "HR": 65, "viento_kmh": 7, "nubosidad": "Parcial"},
        "agua": {"pH": 7.0, "dureza_ppm_CaCO3": 100}},
 "SP": {"items": [["539", 1.5], ["4713", 0.5]], "vol": 150, "tanque": 2000, "modo": "terrestre", "sup": 30,
        "cult": {"actual": "pastura_gram", "momento": "post", "siguiente": None},
        "caldo": {"horas_en_tanque": 1, "temperatura_ambiente_C": 25, "HR": 70, "viento_kmh": 5, "nubosidad": "Parcial"},
        "agua": {"pH": 7.0, "dureza_ppm_CaCO3": 100}, "silvo": {"arbol": "euc", "alt": 4, "animales": True}},
 "AL": {"items": [["422", 0.010], ["214", 0.020]], "vol": 0.6, "tanque": 200, "modo": "granos", "sup": 100,
        "grano": {"tipo": "maiz", "humedad": 13, "temp": 24, "th": 40},
        "caldo": {"horas_en_tanque": 1}, "agua": {"pH": 6.8}},
}
CASOS = {
 "HO": {"titulo": "Tomate en floración: tizón y polilla del tomate",
        "escenario": "Tomate en plena floración y cuaje, con tizón temprano y tardío en la zona y capturas de Tuta absoluta en las trampas. Se arma un fungicida protector con un insecticida para la polilla, a 600 L/ha con pulverizadora montada.",
        "puntos": ["Mancozeb (WP) es protector: hay que repetirlo cada 5 a 7 días y respetar el máximo de aplicaciones de la etiqueta.",
                   "Clorantraniliprol (diamida, IRAC 28): no más de 2 aplicaciones seguidas ni más de la mitad del ciclo, por la resistencia de Tuta.",
                   "La carencia de la mezcla es la mayor de los dos productos (7 días por el mancozeb).",
                   "El polvo mojable va primero en el orden de carga, bien predispersado, y después la suspensión."]},
 "FO": {"titulo": "Eucalipto: limpieza y preemergente antes de plantar",
        "escenario": "Área para plantar eucalipto en 7 días, con pasto y malezas de hoja ancha. Se desecan las malezas con glifosato y se deja un residual de isoxaflutol en la línea de plantación, a 150 L/ha.",
        "puntos": ["Después de plantar, el glifosato va solo dirigido con campana: una gota en las hojas del eucalipto lo daña.",
                   "El isoxaflutol necesita humedad en el suelo para activarse; en suelos arenosos usar la dosis baja porque se mueve.",
                   "No aplicar isoxaflutol sobre las hojas de los plantines."]},
 "PA": {"titulo": "Potrero con malezas de hoja ancha y semileñosas",
        "escenario": "Potrero de brachiaria con malezas de hoja ancha y arbustos jóvenes. Se aplica picloram + 2,4-D en cobertura total con barra, a 200 L/ha, en época de lluvias.",
        "puntos": ["El picloram es muy persistente y móvil: no sembrar cultivos sensibles (soja, hortalizas) en 2 años y dejar 10 m de distancia de cultivos sensibles por la deriva.",
                   "Los árboles (eucalipto y nativos) toman el picloram por la raíz: no aplicar a menos de 1 a 2 veces la altura de los árboles.",
                   "El estiércol de los animales de ese potrero no va a huertas ni cultivos sensibles por 60 días.",
                   "Sin lluvia por 2 a 3 horas y con temperatura de más de 20 °C para que actúe bien."]},
 "SP": {"titulo": "Silvopastoril: hoja ancha entre las filas de eucalipto, con ganado",
        "escenario": "Eucaliptos de 4 m en filas, con pastura y ganado. Se controlan malezas de hoja ancha entre las filas con 2,4-D amina + fluroxipir, dirigido con campana y gota gruesa, a 150 L/ha. Con campana y gota gruesa se puede llegar a 2 a 3 m de la línea de árboles; sin campana, a 10 m o más.",
        "puntos": ["Se eligieron activos que actúan por la hoja y casi no dejan residuo en el suelo: el picloram, la aminopiralida, el imazapir y el tebutiurón dañan los eucaliptos por la raíz, y el triclopir por las hojas y la corteza.",
                   "La deriva de 2,4-D y fluroxipir deforma y frena los eucaliptos: solo amina (nunca éster), antideriva y sin viento hacia los árboles.",
                   "Los árboles nativos y las leguminosas también son de hoja ancha: protegerlos igual.",
                   "Respetar el reingreso de los animales y el corte para heno de la etiqueta."]},
 "AL": {"titulo": "Maíz que entra al silo: protector contra gorgojos y taladrillo",
        "escenario": "100 t de maíz seco (13 % de humedad) que entran al silo. Se trata en la rosca con pirimifos-metil (gorgojos, Sitophilus) + deltametrina (taladrillo de los granos, Rhyzopertha) en 0,6 L de caldo por tonelada.",
        "puntos": ["Los piretroides controlan mejor a Rhyzopertha y los fosforados a Sitophilus: por eso se combinan. En Brasil hay Rhyzopertha resistente a deltametrina.",
                   "El pirimifos-metil no está registrado para soja (etiqueta de Brasil).",
                   "Carencia: 45 días para el pirimifos-metil (etiqueta de Actellic en Brasil); verificar la etiqueta y revisar los límites de residuos si se exporta.",
                   "Si el grano ya está infestado, primero se fumiga con fosfina (en silo hermético) y después se protege."]},
}

GRANOS = {"maiz": "Maíz", "trigo": "Trigo", "arroz": "Arroz", "sorgo": "Sorgo", "soja": "Soja", "otro": "Otro grano"}
HUMEDAD_MAX = 13   # % para almacenar de forma segura (Embrapa)
PROTECTORES = [
 ["Pirimifos-metil 500 EC", "8 a 16 mL/t en hasta 1 L de agua por t, en la cinta o la rosca", "Gorgojos (Sitophilus) y polillas; no está registrado para soja. Carencia de 30 a 45 días según la etiqueta."],
 ["Deltametrina 2,5 EC", "14 a 20 mL/t en 0,6 a 2 L/t (etiqueta de Brasil); la de México llega a 40 mL/t para 12 meses, en 300 mL de agua por t", "Taladrillo (Rhyzopertha) y polillas; hay poblaciones resistentes. Con butóxido de piperonilo, 12 a 20 mL/t. Con deltametrina al 10 % (Granfino), la cuarta parte."],
 ["Diclorvos (DDVP)", "Según la concentración del producto (los registrados van de 10 % a 100 %): ver la etiqueta", "Acción de choque y corta duración."],
 ["Tierra de diatomeas", "1 a 2 kg/t", "Acción física; sirve en granos para semilla y en producción orgánica."],
]
ESTRUCTURAS = [
 ["Pirimifos-metil 500 EC", "100 a 200 mL cada 100 m², en 2 a 25 L de agua según lo poroso de la superficie"],
 ["Deltametrina 2,5 EC", "53 a 80 mL cada 100 m², en 5 a 10 L de agua"],
]
FUMIGACION = {
 "dosis": ["Silo o estructura hermética: 2 a 3 g de fosfina por m³ (2 a 3 tabletas de 3 g por m³; cada tableta libera 1 g)",
           "Granel en silo metálico: 3 a 6 tabletas de 3 g por tonelada (INTA)",
           "Bolsas bajo lona de 150 µm o más: según la etiqueta, por m³ del volumen tapado"],
 "tiempos": [["Menos de 15 °C", "No recomendado"], ["15 a 25 °C", "7 días bajo lona y 12 días en silo (20 % más)"], ["Más de 25 °C", "6 días bajo lona y 10 días en silo"]],
 "tiempos_nota": "Etiqueta de Phostoxin en Brasil (144 h bajo lona y 240 h en silo vertical con más de 25 °C; 20 % más entre 15 y 25 °C). GRDC pide 7 a 10 días y Embrapa 400 ppm por 5 días o más. La etiqueta de EE. UU. permite tiempos más cortos, pero con Rhyzopertha y Tribolium resistentes a la fosfina en la región conviene el tiempo largo. Más dosis no compensa menos tiempo.",
 "seguridad": ["Solo en estructuras herméticas (probar la hermeticidad del silo); nunca en lugares donde viven personas o animales, ni a menos de 50 m de viviendas",
               "Siempre dos personas, carteles de aviso en todas las entradas y máscara con equipo autónomo si no se sabe la concentración",
               "Las tabletas reaccionan con el agua y los ácidos y pueden inflamarse: nunca van al tanque de la pulverizadora",
               "Ventilar antes de entrar: 24 h con ventiladores o unos 5 días sin ellos; entrar solo con menos de 0,23 ppm (etiqueta de Brasil; 0,3 ppm en EE. UU.) medido con un detector. Los alimentos, 48 h de aireación como mínimo",
               "Hay Rhyzopertha y Tribolium resistentes a la fosfina en Brasil: las fumigaciones cortas o con pérdidas la empeoran"],
}
GRANO_CUIDADOS = ["Humedad para guardar: 13 % o menos en soja, maíz, trigo y arroz",
                  "Airear cuando la diferencia entre el grano y el aire es de más de 5 °C; por debajo de 13 °C los insectos casi no se multiplican",
                  "Calar el silo: 5 puntos por metro de profundidad; en bolsas, al menos 10 % de las bolsas",
                  "CO₂ en el silo: de 600 a 1100 ppm indica deterioro inicial; más de 1100 ppm, insectos u hongos activos"]

# Reglas propias de granos almacenados
REGLAS_AL = [
 {"id": "AL01", "tipo": "reaccion_peligrosa", "severidad": "critica",
  "titulo": "Fumigante (fosfuro) en el caldo: no va en el tanque",
  "condiciones": {"presentes": [{"ai": ["fosfuros"]}], "agua": {}, "caldo": {}},
  "mecanismo": "Los fosfuros de aluminio o magnesio liberan fosfina (gas muy tóxico) al contacto con el agua o la humedad, y la reacción con agua o ácidos puede inflamarse.",
  "recomendacion": "Sacarlo del caldo. La fosfina se aplica como tabletas o pellets en silo o bajo lona hermética, con los tiempos y la seguridad de la etiqueta.",
  "confianza": "alta", "problemas": ["PR20", "PR44"]},
 {"id": "AL02", "tipo": "manejo", "severidad": "alta",
  "titulo": "Pirimifos-metil en soja: no registrado",
  "condiciones": {"presentes": [{"ai": ["pirimifos_metil"]}], "agua": {}, "caldo": {"grano": {"==": "soja"}}},
  "mecanismo": "La etiqueta del pirimifos-metil lo registra para cereales (maíz, trigo, arroz, sorgo, cebada, avena), no para soja.",
  "recomendacion": "Usar un producto registrado para soja o confirmar en la etiqueta del producto paraguayo.",
  "confianza": "media", "problemas": ["PR46"]},
 {"id": "AL03", "tipo": "manejo", "severidad": "alta",
  "titulo": "Grano con más de 13 % de humedad",
  "condiciones": {"presentes": [], "agua": {}, "caldo": {"humedad_grano": {">": HUMEDAD_MAX}}},
  "mecanismo": "Con humedad alta el grano respira, se calienta y se forman hongos; los insectos se multiplican más rápido y el protector dura menos.",
  "recomendacion": "Secar a 13 % o menos antes de guardar y tratar; airear para bajar la temperatura.",
  "confianza": "alta", "problemas": ["PR50"]},
 {"id": "AL04", "tipo": "manejo", "severidad": "media",
  "titulo": "Más de 1,5 L de caldo por tonelada",
  "condiciones": {"presentes": [], "agua": {}, "caldo": {"litros_t": {">": 1.5}}},
  "mecanismo": "Mucha agua sobre el grano sube la humedad y favorece hongos.",
  "recomendacion": "Usar 0,3 a 1 L de caldo por tonelada (Embrapa: no más de 1 a 1,5 L/t), salvo que la etiqueta indique hasta 2 L/t.",
  "confianza": "media", "problemas": ["PR50", "PR49"]},
]
SEMAFORO_AL = {"AL01": [3, 3, {}], "AL02": [2, 2, {}], "AL03": [2, 2, {}], "AL04": [None, 0, {}]}
# Reglas que no aplican en granos almacenados (ambiente de campo, volumen por hectárea, cultivo)
CLAVES_CAMPO = ["temperatura_ambiente_C", "HR", "viento_kmh", "rafagas_kmh", "delta_T", "fuera_ley", "lluvia_h", "lluvia_margen_h",
                "hora_inversion", "estado_plantas", "abejas", "momento", "volumen_L_ha", "nubosidad", "rubro"]

# Equipos nuevos
TIPOS_NUEVOS = {"turbo": "Turboatomizador (frutales y cítricos)", "pistola": "Manguera con pistola (localizado)", "cinta": "Aplicador de granos (cinta o rosca)"}
TRV_INDICE = [0.025, 0.10]  # L por m³ de copa: 0,025–0,04 contra psílido (Fundecitrus), 0,08–0,10 aplicación diluida (IVIA)
