# Correcciones a la base química (datos/base_quimica_caldo.json) surgidas de la revisión del 02/10/2026.
# La base original no se modifica: estas correcciones se aplican al generar data.js.
# Fuentes: HRAC 2024, IRAC v11.5, FRAC 2025, PPDB (Univ. of Hertfordshire), Ley 3742/09,
# Purdue PPP-122, Sprayers101, etiquetas registradas.

# Campos de principios activos, biológicos y botánicos
ACTIVOS = {
 "flurocloridona": {"grupo_quimico": "N-fenil heterociclos (pirrolidinona)"},
 "isoflualanam": {"grupo_quimico": "Isoxazolinas", "modo_accion": "IRAC 30 – modulador alostérico del canal de cloro GABA"},
 "diatomeas": {"modo_accion": "IRAC UNM – disruptor mecánico no específico"},
 "peptido_flg22": {"modo_accion": "FRAC P09 – inductor de defensas (péptido)"},
 "nano_plata": {"nombre": "Nanopartículas de plata (con o sin cobre)",
                "modo_accion": "Multisitio (la plata no tiene código FRAC; el cobre es FRAC M01)"},
 "feromona": {"nombre": "Feromonas (grandlure del picudo y feromonas de lepidópteros)"},
 # nombres como se escriben en el listado del SENAVE y en las etiquetas de Paraguay
 "lambdacialotrina": {"nombre": "Lambdacialotrina"},
 "betaciflutrina": {"nombre": "Betaciflutrina"},
 "gammacialotrina": {"nombre": "Gammacialotrina"},
 "fluchloraminopyr": {"nombre": "Flucloraminopir-tefuril"},
 "physcion": {"nombre": "Fiscion (extracto de Rheum)"},
 "cartap": {"nombre": "Cartap clorhidrato"},
 "bio_bt": {"modo_accion": "IRAC 11A – disruptor microbiano de la membrana intestinal"},
 "bio_virus": {"modo_accion": "IRAC 31 – baculovirus"},
 "bio_hongo_entomo": {"modo_accion": "IRAC UNF – hongos entomopatógenos (Pochonia y Purpureocillium: nematicidas biológicos)"},
 "dicamba": {"solubilidad_agua_mg_L": 250000, "log_Kow": -1.88},
 "triclopir": {"solubilidad_agua_mg_L": 7.4, "log_Kow": 4.09,
               "_nota": "Valores del éster butotílico, la forma de casi todos los productos (EC); la sal TEA es muy soluble."},
}

# Concentraciones imposibles en el listado (se toma el número del aislamiento como %)
COMPONENTES = {
 # registro: {id_componente: nueva concentración o None}
 "8127": {"bio_hongo_entomo": None},
 "9054": {"bio_bacillus": 15.0},
 # Suma 112 %: el ciproconazol figura con 80 %; la fórmula azoxistrobina 20 % + ciproconazol 8 % es la habitual.
 "7992": {"ciproconazol": 8.0},
}
NOTAS_PRODUCTO = {
 "7992": "El listado del SENAVE indica ciproconazol 80 % (la suma daría 112 %); la app usa 8 %. Verificar en la etiqueta.",
 "8127": "El listado no trae concentración en %; el número del aislamiento (CG 1420) no es una concentración.",
 "9054": "Concentración tomada de 150 g/L (15 %); el número del aislamiento (CNPSO 3602) no es una concentración.",
}

# Reglas de la base: campos que se reemplazan
REGLAS = {
 "A02": {"titulo": "Glifosato + cationes metálicos (micronutrientes, mancozeb)",
         "condiciones": {"presentes": [{"ai": ["glifosato"]}, {"ai": ["mancozeb"], "adyuvante": ["ady_nutriente"]}], "agua": {}, "caldo": {}},
         "recomendacion": "Separar aplicaciones o poner AMS o secuestrante antes del glifosato y hacer prueba de eficacia. Con cobre ver la regla A02b."},
 "A03": {"titulo": "Glifosato + herbicida de contacto rápido (paraquat, diquat, glufosinato)",
         "condiciones": {"presentes": [{"ai": ["glifosato"]}, {"ai": ["paraquat", "diquat", "glufosinato", "glufosinato_p"]}], "agua": {}, "caldo": {}},
         "recomendacion": "Preferir la aplicación secuencial (doble golpe): glifosato primero y el de contacto 7 a 10 días después. Si se mezclan, usar la dosis alta de glifosato."},
 "F01": {"titulo": "Aceites adyuvantes con azufre, folpet o fentin",
         "condiciones": {"presentes": [{"adyuvante": ["ady_mso", "ady_aceite_mineral", "ady_aceite_vegetal", "ady_terpeno"]}, {"ai": ["azufre", "folpet", "fentin"]}], "agua": {}, "caldo": {}}},
 "V02": {"titulo": "Boro con antideriva de goma guar o PVA",
         "mecanismo": "El borato entrecruza la goma guar y el alcohol polivinílico (PVA) formando un gel. Los antiderivas de poliacrilamida no gelifican con boro.",
         "recomendacion": "No combinar boro con antiderivas de goma guar o PVA; si el antideriva es de poliacrilamida, confirmar con prueba de jarra. Disolver completamente las bolsas hidrosolubles antes de agregar boro."},
 "W01": {"recomendacion": "Agregar AMS (fórmula por cationes o 1-2 % p/v) o secuestrante ANTES del producto sensible. Con dicamba usar secuestrante en vez de AMS; con cobre no usar ninguno de los dos."},
}

# Orden de carga: textos
ORDEN_CARGA = {
 2: "Correctores de agua: secuestrante/quelante o sulfato de amonio (AMS) si hay dureza; buffer/acidificante sólo si la mezcla lo admite (medir y corregir otra vez el pH al final). Antiespumante preventivo si habrá productos espumantes. Si hay bolsas hidrosolubles, cargarlas antes del AMS, en agua limpia.",
 3: "Bolsas hidrosolubles: en agua limpia y sin sales (antes del AMS si es posible); esperar su disolución completa.",
 8: "SL, AL y líquidos solubles (ej. glifosato, glufosinato, 2,4-D sal, reguladores). Los fertilizantes foliares líquidos van con este grupo, salvo indicación de etiqueta.",
 9: "Aceites (MSO/mineral/vegetal), luego tensioactivos, organosiliconados y adherentes. El antideriva va último, después de los fertilizantes.",
 10: "Fertilizantes foliares y micronutrientes que no se cargaron con las soluciones (salvo indicación contraria de etiqueta). Después, el antideriva.",
}

# Medidas: textos
MEDIDAS = {
 "secu": {"detalle": "Quelante/secuestrante (EDTA, fosfonatos, citratos) en el paso 2. Es la alternativa al AMS cuando hay dicamba. No usarlo con cobre: lo precipita o lo libera como Cu²⁺ fitotóxico."},
}

# Reglas nuevas
REGLAS_NUEVAS = [
 {"id": "A02b", "tipo": "antagonismo", "severidad": "alta",
  "titulo": "Glifosato + cobre",
  "condiciones": {"presentes": [{"ai": ["glifosato"]}, {"ai": ["cobre", "nano_plata"]}], "agua": {}, "caldo": {}},
  "mecanismo": "El Cu²⁺ forma complejos con el glifosato y lo inactiva. El AMS y los secuestrantes, que sirven con otros cationes, chocan con el cobre (regla Q06).",
  "recomendacion": "Aplicar por separado.",
  "confianza": "alta", "problemas": ["PR15", "PR22"]},
 {"id": "A03b", "tipo": "antagonismo", "severidad": "media",
  "titulo": "Glifosato + PPO de contacto (carfentrazona, piraflufen, lactofen)",
  "condiciones": {"presentes": [{"ai": ["glifosato"]}, {"ai": ["carfentrazona", "piraflufen", "lactofen"]}], "agua": {}, "caldo": {}},
  "mecanismo": "El daño rápido de los tejidos reduce la translocación del glifosato; con PPO a baja dosis el efecto suele ser menor.",
  "recomendacion": "Usar la dosis plena de glifosato o aplicar en secuencia.",
  "confianza": "media", "problemas": ["PR22"]},
 {"id": "F01b", "tipo": "fitotoxicidad", "severidad": "alta",
  "titulo": "Formulaciones oleosas (EC, OD) con azufre, folpet o fentin",
  "condiciones": {"presentes": [{"formulacion": ["EC", "OD"]}, {"ai": ["azufre", "folpet", "fentin"]}], "agua": {}, "caldo": {}},
  "mecanismo": "Los solventes de EC/OD aumentan la penetración y pueden quemar con azufre o folpet, aunque muchas mezclas de azufre mojable con insecticidas EC se usan sin problema.",
  "recomendacion": "Revisar la etiqueta de ambos productos y hacer prueba en pocas plantas; evitar con calor.",
  "confianza": "media", "problemas": ["PR23"]},
 {"id": "EV03", "tipo": "deriva", "severidad": "media",
  "titulo": "Delta T menor a 2: aire muy húmedo, posible inversión",
  "condiciones": {"presentes": [], "agua": {}, "caldo": {"delta_T": {"<": 2}}},
  "mecanismo": "Con Delta T menor a 2 el aire está casi saturado: las gotas finas no se evaporan y pueden quedar suspendidas, sobre todo con calma o al amanecer (inversión térmica).",
  "recomendacion": "Usar gota media a gruesa, verificar que haya viento constante de 3 a 10 km/h y evitar aplicar con niebla o rocío abundante.",
  "confianza": "media", "problemas": ["PR32"]},
]
SEMAFORO_NUEVAS = {
 "A02b": [2, 2, {}],
 "A03b": [None, 0, {"dosisplena": 1}],
 "F01b": [2, 1, {"jarra": 1}],
 "EV03": [None, 0, {"pastillas": 1}],
}
# Cambios en reglas existentes del semáforo: [nivel_base, piso, medidas]
SEMAFORO_MOD = {
 "A03": [None, 1, {"dosisplena": 1}],
 "V02": [2, 1, {"jarra": 1}],
}
