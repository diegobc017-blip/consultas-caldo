# Tratamiento de semillas antes de la siembra: datos de referencia por cultivo, orden de carga,
# inoculantes y empresas, chequeos y registro.
#
# Fuentes:
#  - Embrapa Soja, Circular Técnica 181 (2021): inoculación y coinoculación de soja (≥ 1,2 millones de
#    células por semilla, inoculante como última operación antes de sembrar y nunca mezclado con los
#    curasemillas químicos, surco con 2,5 a 3 dosis/ha, Azospirillum 1 dosis/ha en semilla o 2 en surco,
#    preinoculación con 80 000 a 100 000 células por semilla a la siembra, CoMo 2–3 g Co y 12–25 g Mo/ha,
#    preferentemente foliar en V3–V5 cuando se inocula en la semilla).
#    https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/1144304/1/CIRCULAR-TECNICA-181-online.pdf
#  - Embrapa (Alice), volumen de caldo en semillas de soja: 600 mL por 100 kg como volumen máximo tolerado
#    de solución acuosa. https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/993523/1/
#  - SENAVE, Resolución 564/10: control de fertilizantes, biofertilizantes, inoculantes y enmiendas
#    (los inoculantes tienen su propio registro, no están en el listado de fitosanitarios).
#  - Páginas de las empresas en Paraguay (consultadas en octubre de 2026): Rizobacter del Paraguay,
#    Agrotec, Simbiose Paraguay (Campo Agropecuario), Glymax.
#  - Reglas para análisis de semillas (ISTA): prueba de germinación en rollos de papel, 4 × 100 semillas.

# Cultivos: plantas objetivo/ha (referencia), peso de mil semillas (g), germinación mínima de referencia (%),
# volumen máximo de caldo por 100 kg (mL; None = seguir la etiqueta), días de primer y último conteo,
# leguminosa (lleva inoculante) y notas.
CULTIVOS_SEM = {
    "soja": {"n": "Soja", "pl": 320000, "pms": 160, "pms_r": [120, 220], "germ": 80, "vmax": 600, "conteo": [5, 8], "leg": "Bradyrhizobium japonicum / elkanii / diazoefficiens", "rub": "AG",
             "n2": "Inoculante en cada siembra (aunque el lote ya tenga soja). Coinoculación con Azospirillum: 1 dosis/ha en la semilla."},
    "maiz": {"n": "Maíz", "pl": 70000, "pms": 320, "pms_r": [250, 400], "germ": 90, "vmax": None, "conteo": [4, 7], "rub": "AG", "unidad": 60000,
             "n2": "Casi siempre viene tratado de la semillera (TSI): revisá la etiqueta de la bolsa antes de agregar otro producto. Bolsa de 60 000 semillas. Azospirillum opcional."},
    "trigo": {"n": "Trigo", "pl": 3000000, "pms": 38, "pms_r": [30, 45], "germ": 80, "vmax": None, "conteo": [4, 8], "rub": "AG",
              "n2": "Curasemillas contra carbones, Fusarium y pulgones de inicio. Azospirillum opcional."},
    "avena": {"n": "Avena / cebada", "pl": 2800000, "pms": 32, "pms_r": [25, 45], "germ": 80, "vmax": None, "conteo": [5, 10], "rub": "AG PA SP", "n2": ""},
    "arroz": {"n": "Arroz", "pl": 2500000, "pms": 27, "pms_r": [22, 32], "germ": 80, "vmax": None, "conteo": [5, 14], "rub": "AG",
              "n2": "Con clomazona en preemergencia se usa semilla con protector (dietholate)."},
    "sorgo": {"n": "Sorgo", "pl": 200000, "pms": 28, "pms_r": [20, 35], "germ": 80, "vmax": None, "conteo": [4, 10], "rub": "AG PA",
              "n2": "Para usar S-metolacloro en preemergencia, la semilla debe venir con protector (fluxofenim)."},
    "girasol": {"n": "Girasol", "pl": 50000, "pms": 60, "pms_r": [45, 80], "germ": 85, "vmax": None, "conteo": [4, 10], "rub": "AG", "unidad": 150000,
                "n2": "Normalmente tratado de fábrica (TSI) contra mildiu y gusanos de suelo."},
    "algodon": {"n": "Algodón", "pl": 110000, "pms": 100, "pms_r": [80, 130], "germ": 75, "vmax": None, "conteo": [4, 12], "rub": "AG",
                "n2": "Semilla deslintada. Curasemillas contra damping-off (Rhizoctonia, Pythium) y trips de inicio."},
    "canola": {"n": "Canola", "pl": 500000, "pms": 4, "pms_r": [3, 6], "germ": 85, "vmax": None, "conteo": [5, 7], "rub": "AG", "n2": "Suele venir tratada de fábrica."},
    "poroto": {"n": "Poroto / frijol", "pl": 220000, "pms": 250, "pms_r": [150, 400], "germ": 80, "vmax": None, "conteo": [5, 9], "leg": "Rhizobium tropici", "rub": "AG HO",
               "n2": "Tegumento frágil: mezclar despacio y con poco volumen."},
    "mani": {"n": "Maní", "pl": 140000, "pms": 500, "pms_r": [350, 900], "germ": 80, "vmax": None, "conteo": [5, 10], "leg": "Bradyrhizobium (cepas de maní)", "rub": "AG",
             "n2": "Semilla sin cáscara muy frágil: tratar a mano o en tambor lento. Inoculante en surco (por ejemplo Rizoliq Surco Maní)."},
    "sesamo": {"n": "Sésamo", "pl": 200000, "pms": 3, "pms_r": [2.5, 4], "germ": 80, "vmax": None, "conteo": [3, 6], "rub": "AG", "n2": ""},
    "chia": {"n": "Chía", "pl": 600000, "pms": 1.3, "pms_r": [1, 1.6], "germ": 80, "vmax": None, "conteo": [4, 7], "rub": "AG", "n2": "Semilla mucilaginosa: con agua forma gel; usar productos en polvo o muy poco volumen."},
    "pastura_gram": {"n": "Pastura gramínea (Brachiaria, Panicum)", "pms": 7, "pms_r": [0.8, 9], "germ": 40, "vmax": None, "conteo": [7, 28], "rub": "PA SP",
                     "spv": 3, "n2": "Se compra por valor cultural (VC = pureza × germinación / 100). La semilla incrustada ya viene tratada; la común se puede tratar con insecticida y fungicida contra hormigas, pulgones de suelo y hongos."},
    "pastura_leg": {"n": "Leguminosa forrajera (leucaena, estilosantes, alfalfa)", "pms": 4, "pms_r": [2, 50], "germ": 60, "vmax": None, "conteo": [4, 14], "leg": "Rizobio específico de cada especie", "rub": "PA SP",
                    "spv": 3, "n2": "Leucaena y estilosantes tienen semilla dura: escarificar (agua caliente o lija) antes de inocular."},
    "hortalizas": {"n": "Hortalizas (almácigo)", "pms": 3, "pms_r": [0.2, 400], "germ": 80, "vmax": None, "conteo": [5, 14], "rub": "HO",
                   "n2": "La semilla hortícola comercial casi siempre viene tratada (tiram, captan o metalaxil). Para semilla propia, tratar con fungicida contra damping-off antes del almácigo."},
    "papa": {"n": "Papa (semilla tubérculo)", "pms": None, "germ": None, "vmax": None, "conteo": None, "rub": "HO",
             "n2": "Se trata el tubérculo-semilla por inmersión o pulverización (fungicida contra Rhizoctonia y sarna, insecticida de inicio) y se deja secar a la sombra antes de plantar."},
    "eucalipto": {"n": "Eucalipto / pino (vivero)", "pms": 1.5, "pms_r": [0.3, 30], "germ": 60, "vmax": None, "conteo": [7, 21], "rub": "FO SP",
                  "n2": "En vivero: fungicida contra damping-off en la semilla o en el sustrato."},
}

# Clases de producto para el tratamiento (orden de carga recomendado)
CLASES_TS = [
    {"id": "fungicida", "n": "Fungicida curasemillas", "orden": 1},
    {"id": "insecticida", "n": "Insecticida / nematicida curasemillas", "orden": 2},
    {"id": "biologico", "n": "Biológico (Bacillus, Trichoderma…)", "orden": 3},
    {"id": "nutriente", "n": "Micronutrientes (cobalto y molibdeno, zinc) o bioestimulante", "orden": 4},
    {"id": "polimero", "n": "Polímero, colorante o secante (talco, grafito)", "orden": 5},
    {"id": "inoculante", "n": "Inoculante (Bradyrhizobium, Azospirillum, rizobio)", "orden": 6},
    {"id": "otro", "n": "Otro", "orden": 4},
]

ORDEN_TS = [
    ["Fungicida", "Primero, bien distribuido: protege contra hongos de suelo y de la semilla."],
    ["Insecticida o nematicida", "Después del fungicida. Si es un premezclado de fábrica, va en un solo paso."],
    ["Biológicos de control (Bacillus, Trichoderma)", "Solo si la etiqueta los declara compatibles con los químicos; si no, en un paso aparte o en el surco."],
    ["Micronutrientes y bioestimulantes", "Cobalto y molibdeno: Embrapa recomienda preferir la vía foliar en V3–V5 cuando se inocula en la semilla, porque sus sales bajan la supervivencia de la bacteria."],
    ["Polímero y secante", "Cierran la película, bajan el polvo (menos riesgo para abejas) y mejoran el escurrimiento en la sembradora."],
    ["Inoculante", "Siempre al final, a la sombra, como última operación antes de sembrar y sin mezclarlo en el mismo caldo con los curasemillas químicos. Sembrar el mismo día (o en el plazo que diga la etiqueta si es de preinoculación con protector)."],
]

# Chequeos del tratamiento (niveles 0 verde, 1 amarillo, 2 naranja, 3 rojo)
CHEQUEOS_TS = {
    "vol_alto": {"nivel": 2, "t": "Demasiado caldo para la semilla",
                 "d": "El volumen total supera el máximo de referencia: la semilla se moja de más, se despega el tegumento y baja la germinación.",
                 "m": ["Bajar el agua de dilución: los productos ya aportan volumen.", "Inocular aparte, en el surco (2,5 a 3 dosis/ha), o usar un inoculante concentrado.", "Pasar parte del tratamiento a la vía foliar (cobalto y molibdeno en V3–V5).", "Hacer el tratamiento industrial (TSI)."]},
    "inoc_mezcla": {"nivel": 2, "t": "Inoculante en la misma mezcla que los químicos",
                    "d": "Los curasemillas químicos matan parte de las bacterias del inoculante; en contacto directo, en el mismo caldo, el daño es mayor.",
                    "m": ["Aplicar primero los químicos, dejar secar y recién después inocular.", "Inocular en el surco con equipo propio (2,5 a 3 dosis/ha de Bradyrhizobium).", "Sembrar enseguida: no dejar la semilla inoculada más de unas horas."]},
    "inoc_espera": {"nivel": 2, "t": "Mucho tiempo entre inocular y sembrar",
                    "d": "Las bacterias mueren con el paso de las horas sobre la semilla tratada, más rápido con calor y sol.",
                    "m": ["Inocular por tandas: solo lo que se siembra en el día.", "Usar un inoculante con protector o de preinoculación (larga vida) y respetar su plazo.", "Guardar la semilla inoculada a la sombra y fresca (menos de 20 a 25 °C)."]},
    "como_inoc": {"nivel": 1, "t": "Cobalto y molibdeno junto con el inoculante",
                  "d": "Las sales de cobalto y molibdeno sobre la semilla bajan la supervivencia de Bradyrhizobium.",
                  "m": ["Aplicarlos por vía foliar en V3–V5 (2–3 g de Co y 12–25 g de Mo por hectárea).", "Si van en la semilla, usar formulaciones declaradas compatibles con el inoculante y sembrar enseguida."]},
    "germ_baja": {"nivel": 2, "t": "Germinación por debajo de la referencia",
                  "d": "Con germinación baja hay que sembrar más kilos por hectárea y el lote puede tener vigor bajo.",
                  "m": ["Ajustar la densidad con la calculadora de kilos por hectárea.", "Pedir un análisis de vigor (tetrazolio o envejecimiento acelerado).", "Si la germinación es muy baja, cambiar de lote de semilla."]},
    "germ_muy_baja": {"nivel": 3, "t": "Germinación muy baja", "d": "El lote no conviene para sembrar: el stand va a quedar desparejo aunque se suba la densidad.",
                      "m": ["Cambiar de lote de semilla.", "Repetir la prueba con 4 × 100 semillas para confirmar."]},
    "sin_germ": {"nivel": 1, "t": "Falta la germinación del lote", "d": "Sin ese dato no se puede ajustar la densidad ni saber si el lote sirve.",
                 "m": ["Hacer la prueba casera: 4 repeticiones de 100 semillas en papel húmedo, a unos 25 °C, y contar las plántulas normales.", "O pedir el análisis al laboratorio de semillas."]},
    "neonic": {"nivel": 1, "t": "Semilla tratada con insecticida: cuidar a las abejas",
               "d": "El polvo que se desprende de la semilla tratada con neonicotinoides o fipronil, al sembrar, puede caer sobre flores y colmenas cercanas.",
               "m": ["Usar polímero y talco o grafito con bajo polvo.", "No sembrar con viento hacia colmenas o cultivos en flor.", "No vaciar restos de semilla tratada en el campo ni cerca del agua."]},
    "leg_sin_inoc": {"nivel": 1, "t": "Leguminosa sin inoculante", "d": "La soja, el poroto, el maní y las leguminosas forrajeras necesitan su bacteria para fijar nitrógeno; en soja se recomienda inocular en todas las siembras.",
                     "m": ["Agregar el inoculante al final, o inocular en el surco."]},
    "tsi": {"nivel": 1, "t": "La semilla ya viene tratada de fábrica", "d": "Agregar otro producto sobre una semilla con TSI puede pasarse de dosis o de volumen.",
            "m": ["Revisar la etiqueta de la bolsa: qué activos trae y si admite inoculante o algo más."]},
}

SEGURIDAD_TS = [
    "La semilla tratada es tóxica: nunca usarla para comer ni para dar a los animales. Va teñida para reconocerla.",
    "Tratar con guantes de nitrilo, protector de ojos, mascarilla para polvo y ropa de manga larga; en un lugar ventilado y lejos de pozos de agua.",
    "Etiquetar las bolsas con el producto, la dosis y la fecha del tratamiento.",
    "Los restos de semilla tratada se entierran en el campo (lejos del agua) o se siembran; no se tiran a cauces ni se queman.",
    "Lavar la tratadora y las herramientas con el triple enjuague y descartar el agua en el lote.",
    "Guardar la semilla tratada a la sombra, en lugar fresco y seco, lejos de alimentos y raciones.",
]

GERMINACION = {
    "pasos": [
        "Tomar una muestra representativa del lote (de varias bolsas).",
        "Contar 4 repeticiones de 100 semillas (o 4 de 50 si hay poca semilla).",
        "Ponerlas sobre papel toalla o de germinación húmedo (no encharcado), enrollar y parar los rollos dentro de una bolsa.",
        "Mantener a unos 25 °C (20 a 30 °C), a la sombra.",
        "Contar las plántulas normales (raíz y brote sanos) en el primer y último conteo del cultivo.",
        "Germinación (%) = plántulas normales / semillas puestas × 100. Promediar las repeticiones.",
    ],
    "nota": "La prueba casera orienta; para semilla que se vende o se certifica vale el análisis del laboratorio (reglas ISTA). El vigor (tetrazolio o envejecimiento acelerado) solo se mide en laboratorio.",
}

# Inoculantes y productos para la semilla que figuran en las páginas de las empresas en Paraguay.
# Los inoculantes se registran en el SENAVE como fertilizantes/biofertilizantes (Res. 564/10), no en el
# listado de fitosanitarios, por eso no salen en el buscador de productos.
INOCULANTES = [
    {"e": "Rizobacter del Paraguay S.A.", "n": "Rizoliq Top II", "org": "Bradyrhizobium japonicum + B. diazoefficiens", "cult": "Soja, garbanzo y otras leguminosas", "tipo": "inoculante", "nota": "Líquido concentrado (1 × 10¹⁰ bacterias/mL a la elaboración)."},
    {"e": "Rizobacter del Paraguay S.A.", "n": "Rizoliq Dakar", "org": "Bradyrhizobium sp.", "cult": "Soja", "tipo": "inoculante", "nota": "Formulación para sequía y calor (2 × 10¹⁰ bacterias/mL a la elaboración)."},
    {"e": "Rizobacter del Paraguay S.A.", "n": "Rizoliq Max", "org": "Bradyrhizobium sp.", "cult": "Soja", "tipo": "inoculante", "nota": "Líquido de alta concentración."},
    {"e": "Rizobacter del Paraguay S.A.", "n": "Rizoliq LLI S", "org": "Bradyrhizobium", "cult": "Soja", "tipo": "preinoculante", "nota": "Larga vida: según la empresa, se aplica hasta 60 días antes de sembrar.", "dias": 60},
    {"e": "Rizobacter del Paraguay S.A.", "n": "Rizospirillum", "org": "Azospirillum brasilense", "cult": "Soja (coinoculación) y maíz", "tipo": "inoculante"},
    {"e": "Rizobacter del Paraguay S.A.", "n": "Rizoliq Surco / Surco Maní", "org": "Bradyrhizobium", "cult": "Soja y maní", "tipo": "surco", "nota": "Se aplica en el surco, no sobre la semilla: evita el contacto con los curasemillas."},
    {"e": "Rizobacter del Paraguay S.A.", "n": "Premax", "org": "Protector bacteriano", "cult": "Con inoculantes", "tipo": "protector", "nota": "Prolonga la supervivencia del inoculante sobre la semilla; no es un inoculante."},
    {"e": "Rizobacter del Paraguay S.A.", "n": "Signum", "org": "Bioinductor de nodulación", "cult": "Soja", "tipo": "bioinductor"},
    {"e": "Rizobacter del Paraguay S.A.", "n": "RizofosPlus", "org": "Pseudomonas fluorescens (solubiliza fósforo y zinc)", "cult": "Algodón, maíz, trigo", "tipo": "biofertilizante"},
    {"e": "Rizobacter del Paraguay S.A.", "n": "Rizoderma Max", "org": "Trichoderma harzianum", "cult": "Cebada, garbanzo, maíz", "tipo": "biológico"},
    {"e": "Rizobacter del Paraguay S.A.", "n": "Rizomicro Zn / Vitagrow TS", "org": "Zinc y multinutriente para semilla", "cult": "Cereales, algodón, alfalfa", "tipo": "nutriente"},
    {"e": "Agrotec S.A.", "n": "Masterfix Soja", "org": "Bradyrhizobium japonicum + B. elkanii", "cult": "Soja", "tipo": "inoculante", "nota": "Según la empresa, compatible con el tratamiento profesional de semillas."},
    {"e": "Simbiose Paraguay S.R.L.", "n": "Bioma Brady", "org": "Bradyrhizobium japonicum (cepas 5079 y 5080)", "cult": "Soja", "tipo": "inoculante"},
    {"e": "Simbiose Paraguay S.R.L.", "n": "Bioma Mais", "org": "Azospirillum brasilense (Ab-V5 y Ab-V6)", "cult": "Maíz y coinoculación de soja", "tipo": "inoculante"},
    {"e": "Simbiose Paraguay S.R.L.", "n": "Stimu Control", "org": "Biofungicida (tratamiento de semillas)", "cult": "Soja y maíz", "tipo": "biológico"},
    {"e": "Simbiose Paraguay S.R.L.", "n": "Solubphos", "org": "Bacillus megaterium + B. subtilis (solubilizan fósforo)", "cult": "Varios", "tipo": "biofertilizante"},
]

# Servicios de tratamiento industrial o equipos que ofrecen las empresas (según sus páginas)
SERVICIOS_TS = [
    {"e": "Agrotec S.A.", "n": "CITS (centro de tratamiento industrial de semillas) y Spectrum TS (tratamiento en el campo)", "url": "https://agrotec.com.py/soluciones/tratamiento-de-semillas/"},
    {"e": "Glymax Paraguay S.A.", "n": "Pack para TSI (tratamiento de semillas industrial)", "url": "https://www.glymax.com/productos"},
    {"e": "Rizobacter del Paraguay S.A.", "n": "Inoculantes, biológicos y curasemillas para semilla", "url": "https://www.rizobacter.com/py/es/paraguay"},
    {"e": "Simbiose Paraguay S.R.L.", "n": "Portafolio biológico para semilla", "url": "https://www.campoagropecuario.com.py/notas/innovaciones-biologicas-con-simbiose-paraguay"},
]

FUENTES_TS = [
    ["Embrapa Soja, Circular Técnica 181: inoculación y coinoculación", "https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/1144304/1/CIRCULAR-TECNICA-181-online.pdf"],
    ["Embrapa: volumen de caldo en el tratamiento de semillas de soja", "https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/993523/1/Influenciadovolumedecaldaedacombinacaodeprodutosusadosnotratamentodasementedesojasobreoseudesempenhofisiologico.pdf"],
    ["SENAVE, Resolución 564/10 (fertilizantes, biofertilizantes e inoculantes)", "https://lic-public.wto.org/en/legislations/2548"],
]
