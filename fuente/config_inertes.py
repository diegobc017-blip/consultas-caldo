# Presentación, inertes (coformulantes) y calidad por tipo de formulación.
# Fuentes: Manual FAO/OMS de especificaciones de plaguicidas (JMPS) y métodos CIPAC (MT);
# guías de formulación CropLife; guías de mezcla de tanque (Purdue PPP-1221, UNL G2350).
# Los límites son los habituales de las especificaciones FAO; cada producto tiene su propia
# especificación. La composición exacta de inertes de cada producto es confidencial: se declara
# al SENAVE en el registro y no figura en el listado público; la hoja de seguridad (SDS) indica
# los solventes y componentes peligrosos.

FAMILIAS = {
 "soluble": {"nombre":"Soluble en agua","corto":"Soluble","como":"Forma una solución verdadera: el activo se disuelve y no hay partículas. Es lo más estable, pero aporta sales que pueden desestabilizar a suspensiones y emulsiones."},
 "solido": {"nombre":"Sólido dispersable","corto":"Sólido disp.","como":"Gránulos o polvo que se deshacen en partículas finas suspendidas en el agua. Necesitan mojarse primero y agitación constante; si les llega aceite antes, forman grumos."},
 "suspension": {"nombre":"Suspensión acuosa","corto":"Suspensión","como":"Partículas sólidas (o microcápsulas) ya dispersas en agua. Sedimentan sin agitación y floculan con exceso de sales."},
 "oleoso": {"nombre":"Emulsionable / oleoso","corto":"Oleoso","como":"Activo en solvente o aceite con emulsionantes: al diluir forma gotitas (emulsión lechosa). Sensibles al agua dura, fría o salina; recubren a los sólidos si entran antes."},
 "no_caldo": {"nombre":"No va en caldo","corto":"No caldo","como":"Cebos, granulados, polvos, fumigantes o semilla en seco: se aplican tal cual."},
}

FORM_FAMILIA = {
 "SL":"soluble","SG":"soluble","SP":"soluble","LS":"soluble","AL":"soluble","TB":"soluble",
 "WG":"solido","WP":"solido","WS":"solido",
 "SC":"suspension","CS":"suspension","ZC":"suspension","FS":"suspension",
 "EC":"oleoso","EW":"oleoso","EO":"oleoso","ME":"oleoso","OD":"oleoso","OP":"oleoso","DC":"oleoso","SE":"oleoso","ES":"oleoso","ME_TS":"oleoso",
 "GR":"no_caldo","GB":"no_caldo","DP":"no_caldo","FUM":"no_caldo","DS":"no_caldo","OTRO":"no_caldo",
}

INERTES = {
 "SC": {
  "inertes":[
   ["Agua","Medio continuo (40-60 % del producto)."],
   ["Dispersantes","Lignosulfonatos, naftalensulfonatos condensados, policarboxilatos, copolímeros acrílicos: mantienen separadas las partículas."],
   ["Humectantes","Alcoholes etoxilados, copolímeros EO/PO, sulfosuccinatos: mojan las partículas."],
   ["Anticongelante","Propilenglicol, etilenglicol, glicerina o urea."],
   ["Espesante","Goma xantana, arcillas (atapulgita, bentonita), sílice: evitan la sedimentación en el bidón."],
   ["Conservante","Isotiazolinonas (BIT, CMIT/MIT): impiden la fermentación de la goma."],
   ["Antiespumante","Siliconas (polidimetilsiloxano)."],
  ],
  "calidad":[
   ["Suspensibilidad (CIPAC MT 184)","≥ 60 % del activo en suspensión a los 30 min (dilución en agua estándar)."],
   ["Tamizado en húmedo (MT 185)","≤ 0,5-2 % retenido en malla de 75 µm."],
   ["Espuma persistente (MT 47)","≤ 10-60 mL al minuto."],
   ["Vertibilidad (MT 148)","≤ 5 % de residuo en el envase."],
   ["Espontaneidad de dispersión (MT 160)","≥ 60 %."],
   ["Estabilidad a 0 °C (MT 39)","7 días sin cristales ni pérdida de suspensibilidad."],
   ["Almacenamiento acelerado (MT 46)","14 días a 54 °C: activo ≥ 95 % del inicial y propiedades físicas dentro de especificación."],
  ],
  "problemas":[
   ["Sedimento duro (\"torta\") en el bidón","Dispersante o espesante insuficiente, envase viejo o con calor. Si no se resuspende agitando, la dosis queda desigual: no usar."],
   ["Crecimiento de cristales","Activo poco soluble con molienda gruesa o mala estabilidad: tapa filtros y picos."],
   ["Fermentación, olor ácido, bidón hinchado","Conservante insuficiente: la goma se degrada y cambia la viscosidad."],
   ["Floculación en el caldo","Dispersantes débiles frente a sales (glifosato K, AMS, fertilizantes): \"queso\"."],
   ["Congelamiento","Separación irreversible si no tiene anticongelante suficiente."],
  ],
 },
 "EC": {
  "inertes":[
   ["Solventes","Hidrocarburos aromáticos (nafta pesada, alquilbencenos), ciclohexanona, isoforona, N-metilpirrolidona, dimetilamidas de ácidos grasos, ésteres metílicos (en productos más nuevos)."],
   ["Emulsionantes","Dodecilbencensulfonato de calcio (aniónico) combinado con no iónicos: aceite de ricino etoxilado, alcoholes etoxilados, copolímeros EO/PO, nonilfenol etoxilado (en algunos genéricos)."],
   ["Estabilizantes","Epoxidados o antioxidantes para activos sensibles."],
  ],
  "calidad":[
   ["Estabilidad de emulsión (CIPAC MT 36)","Emulsión espontánea completa; a 0,5 h y 2 h crema ≤ 2-4 mL y sin aceite libre; reemulsiona a las 24 h."],
   ["Espuma persistente (MT 47)","≤ 10-60 mL al minuto."],
   ["Estabilidad a 0 °C (MT 39)","Separación de sólidos o aceite ≤ 0,3 mL tras 7 días."],
   ["Punto de inflamación","Declarado en etiqueta y SDS (transporte y almacenamiento)."],
   ["Almacenamiento acelerado (MT 46)","14 días a 54 °C: activo ≥ 95 %."],
  ],
  "problemas":[
   ["Emulsión que \"crema\" o separa aceite","Emulsionantes de baja calidad o mal balanceados para el agua dura o fría de la zona."],
   ["Cristales en el bidón con frío","Solvente con poco poder: el activo precipita bajo 5-10 °C."],
   ["Fitotoxicidad (quemado de bordes)","Solventes aromáticos o cetonas en exceso, sobre todo con calor y aceites."],
   ["Ataque a mangueras, juntas y diafragmas","Solventes aromáticos y cetonas hinchan gomas y algunos plásticos."],
   ["Riesgo para el operario","Volátiles e inflamables; irritación de piel y vías respiratorias."],
  ],
 },
 "WG": {
  "inertes":[
   ["Dispersantes","Lignosulfonatos, naftalensulfonatos condensados."],
   ["Humectantes","Alquilnaftalensulfonatos, laurilsulfato de sodio."],
   ["Cargas","Caolín, sílice, sulfato de amonio o de sodio, lactosa, almidón."],
   ["Desintegrantes y aglutinantes","Hacen que el gránulo se arme en fábrica y se deshaga en el tanque."],
  ],
  "calidad":[
   ["Humectabilidad (CIPAC MT 53)","Se moja completamente en ≤ 1 min sin agitar."],
   ["Dispersibilidad (MT 174)","≥ 60-70 % dispersado al minuto de agitación."],
   ["Suspensibilidad (MT 184)","≥ 60 % a los 30 min."],
   ["Tamizado en húmedo (MT 185)","≤ 0,5-2 % retenido en 75 µm."],
   ["Polvo (MT 171)","Prácticamente sin polvo."],
   ["Resistencia al desgaste (MT 178)","≥ 98 % de gránulos enteros."],
   ["Espuma persistente (MT 47)","≤ 10-60 mL al minuto."],
  ],
  "problemas":[
   ["Gránulos que no se deshacen","Desintegrante pobre o producto que tomó humedad (bolsa abierta): grumos y picos tapados."],
   ["Mucho polvo al abrir","Gránulos frágiles: exposición del operario y dosis irregular."],
   ["Residuo en filtros","Partículas gruesas (tamizado en húmedo fuera de especificación)."],
   ["Dispersión lenta con agua fría","Normal en muchos WG: pre-dispersar en balde con agua templada."],
  ],
 },
 "WP": {
  "inertes":[
   ["Cargas minerales","Caolín, atapulgita, sílice precipitada, talco, tierra de diatomeas (30-70 % del producto)."],
   ["Humectantes","Alquilnaftalensulfonatos, laurilsulfato de sodio."],
   ["Dispersantes","Lignosulfonatos."],
  ],
  "calidad":[
   ["Humectabilidad (CIPAC MT 53)","≤ 1 min sin agitar."],
   ["Suspensibilidad (MT 184)","≥ 60 % a los 30 min."],
   ["Tamizado en húmedo (MT 185)","≤ 2 % retenido en 75 µm."],
   ["Espuma persistente (MT 47)","≤ 10-60 mL al minuto."],
  ],
  "problemas":[
   ["Polvo fino al cargar","Exposición por inhalación: usar protección respiratoria."],
   ["Adsorción de activos","Las arcillas retienen glifosato, paraquat y diquat del caldo: pierden eficacia (reglas A04 y K05)."],
   ["Desgaste de pastillas","Las cargas minerales son abrasivas: revisar caudal de picos."],
   ["Sedimentación rápida","Mala suspensibilidad: agitación continua."],
  ],
 },
 "SL": {
  "inertes":[
   ["Contraión de la sal","Isopropilamina, potasio, dimetilamina, amonio, colina: hacen soluble al activo y aportan electrolitos."],
   ["Tensioactivos","Aminas grasas etoxiladas (tallowamina, POEA), eteraminas, alquilpoliglucósidos."],
   ["Cosolventes y anticongelante","Glicoles, agua."],
   ["Antiespumante y colorante","En muchas formulaciones."],
  ],
  "calidad":[
   ["Estabilidad de la solución diluida (CIPAC MT 41)","Solución clara tras 18 h; cualquier sedimento pasa por malla de 45 µm."],
   ["Espuma persistente (MT 47)","≤ 10-60 mL al minuto."],
   ["Estabilidad a 0 °C (MT 39)","Separación ≤ 0,3 mL tras 7 días."],
  ],
  "problemas":[
   ["Espuma abundante","Tensioactivos tipo POEA o APG: prever antiespumante (regla E01)."],
   ["Desestabiliza otras formulaciones","Las sales concentradas floculan SC/WG y rompen EC a bajo volumen (reglas Q02 y V01)."],
   ["Cristales con frío","Sales concentradas (p. ej. glifosato potásico) cristalizan o se espesan."],
   ["Toxicidad acuática y ocular","Las aminas etoxiladas (POEA) son más tóxicas para peces que el propio glifosato; cuidar derrames y lavado."],
  ],
 },
 "SG": {
  "inertes":[["Cargas solubles","Sulfato de amonio, urea, lactosa, azúcares."],["Humectantes","Tensioactivos aniónicos o no iónicos."],["Antiapelmazante","Sílice."]],
  "calidad":[["Grado de disolución (CIPAC MT 179)","Disolución completa; residuo en 75 µm ≤ 0,1-0,5 %."],["Espuma persistente (MT 47)","≤ 60 mL al minuto."],["Polvo (MT 171)","Sin polvo."]],
  "problemas":[["Apelmazado","Tomó humedad: disuelve lento y deja grumos."],["Disolución lenta en agua fría","Esperar disolución total antes del siguiente producto."]],
 },
 "SP": {
  "inertes":[["Cargas solubles","Sulfato de sodio o de amonio, azúcares."],["Humectantes","Tensioactivos."]],
  "calidad":[["Grado de disolución (CIPAC MT 179)","Disolución completa en el tiempo indicado."],["Espuma persistente (MT 47)","≤ 60 mL al minuto."]],
  "problemas":[["Apelmazado por humedad","Grumos que no se disuelven."],["Polvo","Exposición del operario."]],
 },
 "OD": {
  "inertes":[
   ["Aceite portador","Aceite vegetal, metilado (MSO) o mineral."],
   ["Emulsionantes","Para que el aceite se emulsione al diluir."],
   ["Agentes reológicos","Arcillas organofílicas, sílice pirogénica: evitan la separación en el bidón."],
  ],
  "calidad":[["Estabilidad de dispersión (CIPAC MT 180)","Sin separación de aceite ni sedimento fuera de límite a 0,5 h, 2 h y 24 h."],["Tamizado en húmedo (MT 185)","≤ 0,5-2 % en 75 µm."],["Estabilidad a 0 °C","Fluye y redispersa tras 7 días."]],
  "problemas":[["Aceite separado arriba del bidón","Sinéresis: agitar el bidón hasta homogeneizar antes de medir."],["Sedimento compacto","Agentes reológicos insuficientes o envase viejo."],["\"Queso\" con WG/WP","El aceite recubre los sólidos si entra antes (regla Q01)."],["Muy espeso con frío","Medir con el producto templado."]],
 },
 "CS": {
  "inertes":[["Pared de la cápsula","Poliurea, poliamida o melamina-formaldehído."],["Dispersantes y espesante","Como en SC."],["Anticongelante","Glicoles."]],
  "calidad":[["Activo libre (no encapsulado)","Dentro del máximo de la especificación: define toxicidad y fitotoxicidad."],["Suspensibilidad (MT 184)","≥ 60-70 %."],["Tamizado en húmedo","≤ 0,5-2 %."],["Estabilidad a 0 °C","Sin aglomeración."]],
  "problemas":[["Cápsulas rotas","Congelamiento, calor o bombas de alta presión: el activo sale libre (más fitotoxicidad y menos residualidad)."],["Floculación con sales","Muy sensibles a electrolitos y solventes de EC."]],
 },
 "ZC": {
  "inertes":[["Cápsulas + partículas","Mezcla de CS y SC con sus dispersantes, espesantes y anticongelante."]],
  "calidad":[["Suspensibilidad (MT 184)","≥ 60 %."],["Tamizado en húmedo","≤ 0,5-2 %."]],
  "problemas":[["Doble sensibilidad","Rotura de cápsulas y floculación de las partículas con sales."]],
 },
 "SE": {
  "inertes":[["Sistema doble","Partículas sólidas (como SC) más gotas de aceite o solvente (como EW), con dispersantes y emulsionantes."]],
  "calidad":[["Estabilidad de dispersión (MT 180)","Sin separación fuera de límite."],["Tamizado en húmedo","≤ 0,5-2 %."]],
  "problemas":[["Inestable con sales y bajo volumen","Separa o flocula fácilmente (reglas Q02 y V01)."],["Maduración en el bidón","Con calor el aceite disuelve parte del sólido y crecen cristales."]],
 },
 "EW": {
  "inertes":[["Solvente o aceite","Fase oleosa con el activo."],["Emulsionantes poliméricos","Estabilizan las gotas en agua."],["Espesante y anticongelante","Goma xantana, glicoles."]],
  "calidad":[["Estabilidad de emulsión (MT 36)","Sin crema ni aceite libre fuera de límite."],["Estabilidad a 0 °C","Sin separación."]],
  "problemas":[["Cremado o coalescencia en el bidón","Agitar el bidón; si quedan gotas de aceite libres, no usar."]],
 },
 "EO": {
  "inertes":[["Emulsión inversa","Agua dispersa en aceite con emulsionantes de baja HLB."]],
  "calidad":[["Inversión y estabilidad","Debe invertir a emulsión en agua al diluir con agitación."]],
  "problemas":[["No invierte","Forma \"mayonesa\" si se diluye sin agitación vigorosa."]],
 },
 "ME": {
  "inertes":[["Tensioactivos en alta proporción","Alcoholes etoxilados, sulfonatos."],["Cosolventes","Alcoholes, glicoles, solventes polares."]],
  "calidad":[["Estabilidad de emulsión (MT 36)","Transparente al diluir."],["Espuma persistente","≤ 60 mL al minuto."]],
  "problemas":[["Espuma","Mucho tensioactivo: prever antiespumante."],["Fitotoxicidad","Penetración alta en hojas tiernas o con calor."],["Turbio con frío o calor","Fuera de su rango de estabilidad."]],
 },
 "DC": {
  "inertes":[["Cosolvente miscible en agua","N-metilpirrolidona, glicoles, alcoholes."],["Dispersantes","Mantienen el activo que precipita al diluir."]],
  "calidad":[["Dispersión al diluir","Partículas finas que no crecen en 1-2 h."]],
  "problemas":[["Cristales al diluir","El activo precipita y las partículas crecen si el caldo queda en reposo (regla X03)."]],
 },
 "OP": {"inertes":[["Polvo para aceite","Activo con cargas para dispersar en aceite."]],"calidad":[["Dispersión en aceite","Sin grumos."]],"problemas":[["Grumos","Requiere pre-dispersión."]]},
 "FS": {
  "inertes":[["Dispersantes, espesante, anticongelante","Como en SC."],["Pigmento o colorante","Obligatorio para identificar semilla tratada."],["Polímero adherente (film)","Fija el producto y reduce el polvo de la semilla."]],
  "calidad":[["Suspensibilidad","≥ 60 %."],["Adherencia a la semilla / polvo desprendido","Bajo desprendimiento (dust-off)."],["Tamizado en húmedo","≤ 0,5-2 %."]],
  "problemas":[["Polvo de la semilla","Pérdida de activo y exposición de polinizadores en la siembra."],["Semilla pegajosa","Mala plantabilidad en la sembradora."],["Menor germinación","Exceso de producto o solventes."]],
 },
 "WS": {"inertes":[["Cargas y humectantes","Para formar pasta con poca agua."]],"calidad":[["Humectabilidad","≤ 1 min."],["Tamizado en húmedo","≤ 2 %."]],"problemas":[["Grumos","Mojar despacio."]]},
 "LS": {"inertes":[["Cosolventes y colorante","Solución para semillas."]],"calidad":[["Estabilidad de la solución","Clara al diluir."]],"problemas":[["Cristales con frío","Templar antes de usar."]]},
 "ES": {"inertes":[["Emulsión para semillas","Solvente, emulsionantes, pigmento."]],"calidad":[["Estabilidad de emulsión","Sin separación."]],"problemas":[["Fitotoxicidad en germinación","Solventes en exceso."]]},
 "ME_TS": {"inertes":[["Microemulsión para semillas","Tensioactivos y cosolventes."]],"calidad":[["Estabilidad","Transparente al diluir."]],"problemas":[["Espuma","Prever antiespumante en la tolva/tambor."]]},
 "AL": {"inertes":[["Variable","Líquidos listos para usar o solubles: agua, cosolventes, tensioactivos."]],"calidad":[["Según etiqueta","Verificar homogeneidad y ausencia de sedimento."]],"problemas":[["Composición poco informada","Revisar SDS antes de mezclar."]]},
 "TB": {"inertes":[["Efervescentes o disgregantes","Bicarbonatos y ácidos orgánicos, cargas."]],"calidad":[["Tiempo de desintegración","Completo en el tiempo indicado."]],"problemas":[["Efervescencia con ácidos","Liberan gas: cargar en tanque con agua y sin acidificantes."]]},
 "GB": {"inertes":[["Atrayente","Pulpa de cítricos u otro sustrato que la hormiga acarrea."],["Aglutinante y aceite","Dan forma al pellet."]],"calidad":[["Atractividad y humedad","El cebo húmedo o viejo pierde atracción."]],"problemas":[["Cebo húmedo o mohoso","No lo cargan las hormigas: aplicar con suelo seco y sin lluvia prevista."]]},
 "GR": {"inertes":[["Soporte granular","Arcilla, arena o sílice impregnada."]],"calidad":[["Granulometría y polvo","Uniforme y sin polvo."]],"problemas":[["Polvo","Exposición del operario."]]},
 "DP": {"inertes":[["Cargas","Talco, caolín, sílice."]],"calidad":[["Finura y fluidez","Sin grumos."]],"problemas":[["Deriva y exposición","Usar protección respiratoria."]]},
 "DS": {"inertes":[["Cargas y adherente","Talco, grafito, pigmento."]],"calidad":[["Adherencia a la semilla","Bajo desprendimiento."]],"problemas":[["Polvo en la siembra","Exposición y pérdida de activo."]]},
 "FUM": {"inertes":[["Fosfuro con estabilizantes","Carbamato de amonio, parafina: regulan la liberación del gas."]],"calidad":[["Envase hermético","Sin humedad."]],"problemas":[["Contacto con agua","Libera fosfina (gas muy tóxico e inflamable): nunca en caldo."]]},
 "OTRO": {"inertes":[["Variable","Consultar la hoja de seguridad."]],"calidad":[["Según etiqueta","—"]],"problemas":[["Sin datos","Consultar al registrante."]]},
}

# Impurezas relevantes (FAO/OMS): se controlan en el grado técnico y pueden aumentar con mala
# fabricación o mal almacenamiento.
IMPUREZAS = {
 "glifosato":"Formaldehído y N-nitrosoglifosato.",
 "mancozeb":"Etilentiourea (ETU): aumenta con calor y humedad en el depósito; es tóxica y cancerígena.",
 "malation":"Isomalatión: se forma con calor durante el almacenamiento y es mucho más tóxico que el malatión.",
 "dimetoato":"Ometoato e isodimetoato.",
 "acefato":"Metamidofós (prohibido en muchos países).",
 "clorpirifos":"Sulfotep.",
 "24d":"Fenoles libres (2,4-diclorofenol); en fabricación deficiente, dioxinas.",
 "paraquat":"4,4'-bipiridilo libre y terpiridinas.",
 "diquat":"Dibromuro de etileno.",
 "carbendazim":"2,3-diaminofenazina (DAP) y 2-amino-3-hidroxifenazina (HAP).",
 "tiofanato":"2,3-diaminofenazina (DAP) y 2-amino-3-hidroxifenazina (HAP).",
}

SENALES_MAL_ESTADO = [
 ["Sedimento duro que no se resuspende agitando el bidón","SC, SE, CS, OD","Descartar o reclamar: la dosis queda desigual."],
 ["Cristales en el bidón o en el tapón","EC, SL, SC","Templar a 20-25 °C y agitar; si no se redisuelven, no usar."],
 ["Separación en capas o aceite libre","EC, EW, OD, SE","Agitar el bidón; si no se homogeniza, no usar."],
 ["Bidón hinchado, olor ácido o a fermentado","SC, CS","Conservante agotado o reacción interna: no usar."],
 ["Grumos duros o gránulos apelmazados","WG, WP, SG, SP","Tomó humedad: pierde dispersión; probar en jarra antes de usar."],
 ["Cambio de color u olor respecto de otro lote","Todas","Posible degradación o adulteración: pedir certificado de análisis del lote."],
 ["Etiqueta sin número de registro SENAVE, sin lote o con fecha vencida","Todas","No usar. Verificar el registro en el listado del SENAVE."],
]

PRUEBA_CALIDAD_CASERA = [
 "Frasco transparente de 1 L con el agua que se va a usar.",
 "Dosis de un solo producto, proporcional al volumen por hectárea (igual que la prueba de jarra).",
 "Invertir 10 veces y observar al minuto: la espuma debería bajar casi del todo.",
 "A los 30 minutos: no debería haber más que un velo fino en el fondo (suspensiones y sólidos) ni crema o aceite arriba (emulsionables).",
 "Volver a invertir 10 veces: el sedimento debe resuspenderse por completo.",
 "Pasar el caldo por una media de nylon o el filtro de la pulverizadora: no debe quedar arenilla ni grumos.",
 "Si dos marcas del mismo activo se comportan distinto con el mismo agua, la diferencia está en los inertes y la calidad de la formulación.",
]
