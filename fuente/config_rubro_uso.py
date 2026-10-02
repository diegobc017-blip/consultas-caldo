# Uso de cada principio activo DENTRO de cada rubro (para activos que se usan en más de un rubro).
# Formato: id -> {rubro: (para qué se usa en ese rubro, objetivos en ese rubro, restricción)}
# Restricción del producto comercial para entrar en ese rubro:
#   ""      todos los productos con ese activo
#   "solo"  solo productos de ese único activo (las mezclas formuladas con otros activos
#           se hacen para el rubro principal, p. ej. soja y maíz)
#   "f:GB"  solo esas formulaciones (p. ej. cebos para hormigas)
#   "sec"   uso secundario o dirigido: los productos se hacen para otro rubro (p. ej. glifosato
#           entre filas de frutales). Quedan ocultos en ese rubro salvo que el usuario marque
#           "Incluir productos de uso general" y no cuentan para la rotación del rubro.
#   "pri"   rubro principal además del primero de AI_RUBROS (p. ej. 2,4-D en pasturas): los productos
#           cuentan como "específicos del rubro" y se listan primero.
#   Se pueden combinar: "solo sec".
# Un producto comercial entra en un rubro si TODOS sus activos se usan en ese rubro
# (intersección) y cumple las restricciones. Los curasemillas quedan en Agrícola.
# Orientativo: la etiqueta registrada en el SENAVE define cultivos, plagas y dosis.

USO_RUBRO = {
 # ---------------- HERBICIDAS ----------------
 "24d": {
  "AG": ("Hoja ancha en barbecho (buva, con glifosato), maíz, trigo, arroz y caña.", "hoja", ""),
  "PA": ("Malezas de hoja ancha y arbustivas de potrero, solo o con picloram.", "hoja len", "pri"),
  "FO": ("Hoja ancha en preplantío y entre filas de eucalipto y pino, dirigido.", "hoja", "solo sec")},
 "ametrina": {
  "AG": ("Pre y postemergente de hoja ancha y gramíneas en caña de azúcar.", "hoja gram pre", ""),
  "HO": ("Malezas en piña, banana y cítricos, dirigido al suelo.", "hoja gram pre", "solo sec")},
 "cletodim": {
  "AG": ("Graminicida post en soja, algodón y girasol: capim amargoso, maíz guacho.", "gram", ""),
  "HO": ("Graminicida post en hortalizas de hoja ancha (cebolla, zanahoria, tomate, poroto).", "gram", "solo")},
 "clopiralida": {
  "AG": ("Hoja ancha (compuestas, leguminosas) en trigo, maíz y canola.", "hoja", ""),
  "PA": ("Hoja ancha de potrero (compuestas y leguminosas invasoras).", "hoja", "pri")},
 "dicamba": {
  "AG": ("Hoja ancha y buva en barbecho y en soja o algodón tolerantes; volátil, cuidar deriva.", "hoja", ""),
  "PA": ("Malezas de hoja ancha y arbustivas en potreros.", "hoja len", "")},
 "diquat": {
  "AG": ("Desecación precosecha (soja, trigo) y control total de contacto.", "total", ""),
  "HO": ("Desecación de papa antes de cosechar y malezas entre filas, dirigido.", "total", "solo")},
 "diuron": {
  "AG": ("Pre y postemergente en algodón y caña; desecante en mezcla.", "pre hoja gram", ""),
  "HO": ("Preemergente en cítricos, piña y banana, dirigido al suelo.", "pre hoja gram", "solo sec")},
 "fluchloraminopyr": {
  "AG": ("Hoja ancha en barbecho (auxínico nuevo).", "hoja", ""),
  "PA": ("Hoja ancha y leñosas de potrero.", "hoja len", "")},
 "flumioxazin": {
  "AG": ("Preemergente de hoja ancha y desecación (buva, caruru) en soja.", "pre hoja total", ""),
  "FO": ("Preemergente en plantaciones de eucalipto y pino.", "pre hoja", "solo")},
 "flurocloridona": {
  "AG": ("Preemergente de hoja ancha en girasol.", "pre hoja", ""),
  "HO": ("Preemergente de hoja ancha en papa y zanahoria.", "pre hoja", "")},
 "fluroxipir": {
  "AG": ("Hoja ancha en barbecho (buva), maíz y trigo.", "hoja", ""),
  "PA": ("Hoja ancha y leñosas de potrero, solo o con picloram o triclopir.", "hoja len", "pri")},
 "glifosato": {
  "AG": ("Sistémico total: barbecho, desecación y post en cultivos RR. Hay malezas resistentes (capim amargoso, buva, caruru, pata de gallina).", "total gram hoja", ""),
  "PA": ("Desecación para implantar o renovar pasturas y control de manchones de malezas.", "total gram hoja", "solo sec"),
  "FO": ("Malezas en preplantío y entre filas de eucalipto y pino, dirigido sin mojar las plantas.", "total gram hoja", "solo"),
  "HO": ("Malezas entre filas de frutales y cítricos y en preplantío de hortalizas, siempre dirigido.", "total gram hoja", "solo sec")},
 "glufosinato": {
  "AG": ("Desecación y post en cultivos tolerantes (LL); útil contra resistentes a glifosato.", "total gram hoja", ""),
  "HO": ("Malezas entre filas de frutales y cítricos, dirigido (contacto).", "total gram hoja", "solo sec")},
 "glufosinato_p": {
  "AG": ("Desecación y post en cultivos tolerantes (LL), isómero activo de menor dosis.", "total gram hoja", ""),
  "HO": ("Malezas entre filas de frutales y cítricos, dirigido (contacto).", "total gram hoja", "solo sec")},
 "haloxifop": {
  "AG": ("Graminicida post en soja y algodón (capim amargoso, maíz guacho).", "gram", ""),
  "FO": ("Graminicida en plantaciones forestales jóvenes (pastos entre filas).", "gram", "solo sec")},
 "hexazinona": {
  "AG": ("Pre y postemergente en caña de azúcar.", "pre hoja gram", ""),
  "FO": ("Pre y postemergente en plantaciones de eucalipto y pino.", "pre hoja gram len", "pri")},
 "imazapir": {
  "AG": ("Maíz y girasol tolerantes (Clearfield).", "gram hoja", ""),
  "FO": ("Control total y residual en preplantío forestal y áreas no cultivadas.", "total gram hoja len", "solo pri")},
 "isoxaflutol": {
  "AG": ("Preemergente de hoja ancha y gramíneas en maíz y caña.", "pre hoja gram", ""),
  "FO": ("Preemergente en eucalipto.", "pre hoja gram", "solo pri")},
 "linuron": {
  "AG": ("Pre y postemergente en soja.", "pre hoja", ""),
  "HO": ("Pre y postemergente en zanahoria y papa.", "pre hoja", "")},
 "metribuzina": {
  "AG": ("Pre y post de hoja ancha en soja y trigo.", "pre hoja", ""),
  "HO": ("Pre y post de hoja ancha en papa y tomate.", "pre hoja", "solo")},
 "metsulfuron": {
  "AG": ("Hoja ancha en trigo y barbecho.", "hoja", ""),
  "PA": ("Malezas de hoja ancha y arbustivas de potrero.", "hoja len", "pri")},
 "oxifluorfen": {
  "HO": ("Pre y post de hoja ancha en cebolla, ajo y frutales (dirigido).", "pre hoja", ""),
  "FO": ("Preemergente en eucalipto y pino.", "pre hoja", ""),
  "AG": ("Preemergente en barbecho y algodón, con glifosato.", "pre hoja", "")},
 "paraquat": {
  "AG": ("Desecante de contacto total: barbecho y desecación precosecha.", "total", ""),
  "HO": ("Malezas entre filas de frutales y hortalizas, dirigido (contacto).", "total", "solo sec")},
 "pendimetalina": {
  "AG": ("Preemergente de gramíneas en soja, maíz y algodón.", "pre gram", ""),
  "HO": ("Preemergente en cebolla, ajo, zanahoria y tomate trasplantado.", "pre gram", "solo")},
 "picloram": {
  "PA": ("Leñosas y hoja ancha de potrero, con 2,4-D, fluroxipir o triclopir; muy persistente.", "len hoja", ""),
  "AG": ("Hoja ancha en barbecho largo; respetar el carry-over (muy persistente).", "hoja", "")},
 "propaquizafop": {
  "AG": ("Graminicida post en soja.", "gram", ""),
  "HO": ("Graminicida post en hortalizas de hoja ancha.", "gram", "solo")},
 "quizalofop": {
  "AG": ("Graminicida post en soja.", "gram", ""),
  "HO": ("Graminicida post en hortalizas de hoja ancha.", "gram", "solo")},
 "s_metolacloro": {
  "AG": ("Preemergente de gramíneas en maíz, soja y algodón.", "pre gram", ""),
  "HO": ("Preemergente en tomate, poroto y otras hortalizas.", "pre gram", "solo")},
 "saflufenacil": {
  "AG": ("Desecación de hoja ancha (buva) y preemergente en soja y maíz.", "hoja total pre", ""),
  "HO": ("Malezas entre filas de cítricos y frutales, dirigido.", "hoja", "solo sec")},
 "simazina": {
  "AG": ("Preemergente en maíz y caña.", "pre hoja gram", ""),
  "HO": ("Preemergente en cítricos y frutales.", "pre hoja gram", "solo sec"),
  "FO": ("Preemergente en plantaciones forestales.", "pre hoja gram", "solo sec")},
 "sulfentrazona": {
  "AG": ("Preemergente de hoja ancha y tiririca en soja y caña.", "pre hoja cip", ""),
  "FO": ("Preemergente en eucalipto.", "pre hoja cip", "solo")},
 "sulfometuron": {
  "FO": ("Control total y preemergente en plantaciones forestales y áreas no cultivadas.", "pre total", ""),
  "AG": ("Preemergente en caña de azúcar, con otros herbicidas.", "pre", "")},
 "tebutiuron": {
  "AG": ("Preemergente en caña de azúcar.", "pre hoja", ""),
  "PA": ("Control de leñosas y arbustivas en potreros.", "len hoja", "pri")},
 "triclopir": {
  "PA": ("Leñosas y arbustivas de potrero, solo o con picloram o fluroxipir.", "len hoja", ""),
  "FO": ("Rebrotes y leñosas en preplantío forestal y aceiros.", "len hoja", ""),
  "AG": ("Hoja ancha en arroz y barbecho.", "hoja", "solo sec")},
 "trifluralina": {
  "AG": ("Preemergente de gramíneas en soja y algodón.", "pre gram", ""),
  "HO": ("Preemergente en hortalizas trasplantadas (tomate, pimiento, repollo).", "pre gram", "solo")},

 # ---------------- FUNGICIDAS ----------------
 "azoxistrobina": {
  "AG": ("Roya, manchas y tizones en soja, maíz y trigo; siempre en mezcla.", "roya manch antr", ""),
  "HO": ("Manchas, antracnosis, tizones y mildiu en tomate, papa, cucurbitáceas y frutales.", "manch antr mild", "")},
 "azufre": {
  "HO": ("Oídio y ácaros en frutales, vid y hortalizas.", "oidio acar", ""),
  "AG": ("Oídio en soja y trigo; multisitio.", "oidio", "")},
 "benomil": {
  "HO": ("Manchas, antracnosis y podredumbres en frutales y hortalizas.", "manch antr podr", ""),
  "AG": ("Manchas y tratamiento de semillas.", "manch suelf", "")},
 "benzovindiflupir": {
  "AG": ("Roya asiática y manchas en soja; manchas en maíz.", "roya manch", ""),
  "HO": ("Manchas y oídio en hortalizas y frutales.", "manch oidio", "solo sec")},
 "carbendazim": {
  "AG": ("Manchas, moho blanco y semillas en soja y cereales.", "manch scle suelf", ""),
  "HO": ("Antracnosis, manchas y podredumbres en frutales y hortalizas.", "antr manch podr", "solo")},
 "clorotalonil": {
  "AG": ("Multisitio: roya y manchas; socio antirresistencia.", "roya manch", ""),
  "HO": ("Multisitio: tizones, manchas, mildiu y antracnosis en tomate, papa y cucurbitáceas.", "manch antr mild", "pri")},
 "cobre": {
  "HO": ("Multisitio: bacteriosis, mildiu y manchas en hortalizas, frutales y cítricos.", "bact mild manch", ""),
  "AG": ("Bacteriosis y manchas en soja y otros cultivos; multisitio.", "bact manch", "")},
 "cuaternario_amonio": {
  "HO": ("Desinfección de herramientas, bandejas e invernaderos; algunas bacteriosis.", "bact", ""),
  "AG": ("Desinfección de herramientas y equipos.", "bact", "")},
 "difenoconazol": {
  "AG": ("Manchas y roya en soja y cereales; semillas.", "manch roya suelf", ""),
  "HO": ("Manchas, oídio, sarna y roya en hortalizas y frutales.", "manch oidio roya", "pri")},
 "diniconazol": {
  "AG": ("Manchas y oídio en cereales.", "manch oidio", ""),
  "HO": ("Oídio y manchas en frutales y hortalizas.", "oidio manch", "")},
 "estreptomicina": {
  "HO": ("Bacteriosis en hortalizas y frutales.", "bact", ""),
  "AG": ("Bacteriosis en tabaco y otros cultivos.", "bact", "")},
 "fentin": {
  "AG": ("Manchas en soja.", "manch", ""),
  "HO": ("Tizón tardío y manchas en papa.", "mild manch", "")},
 "fluazinam": {
  "HO": ("Tizón tardío y hongos de suelo en papa; moho blanco en poroto.", "mild suelf scle", ""),
  "AG": ("Moho blanco en soja.", "scle", "")},
 "fludioxonil": {
  "AG": ("Tratamiento de semillas (Fusarium, Rhizoctonia).", "suelf", ""),
  "HO": ("Botrytis y podredumbres en frutales, hortalizas y postcosecha.", "podr", "")},
 "fluopiram": {
  "AG": ("Manchas, moho blanco y nematodos en soja.", "manch scle nema", ""),
  "HO": ("Oídio, Botrytis y manchas en hortalizas y frutales; nematodos.", "oidio podr manch nema", "")},
 "fluxapiroxad": {
  "AG": ("Roya y manchas en soja, maíz y trigo.", "roya manch", ""),
  "HO": ("Manchas y oídio en hortalizas y frutales.", "manch oidio", "")},
 "glucano": {
  "AG": ("Inductor de defensas (bioinsumo).", "manch", ""),
  "HO": ("Inductor de defensas en hortalizas y frutales (bioinsumo).", "manch", "")},
 "kasugamicina": {
  "HO": ("Bacteriosis en hortalizas y frutales.", "bact", ""),
  "AG": ("Brusone del arroz y bacteriosis.", "piri bact", "")},
 "kresoxim": {
  "HO": ("Oídio, sarna y manchas en frutales y hortalizas.", "oidio manch", ""),
  "AG": ("Manchas y oídio en cereales y soja.", "manch oidio", "")},
 "mancozeb": {
  "AG": ("Multisitio: roya asiática y manchas; principal socio antirresistencia.", "roya manch", ""),
  "HO": ("Multisitio: tizones, mildiu, antracnosis y manchas en papa, tomate, cebolla y frutales.", "mild manch antr", "pri")},
 "metalaxil": {
  "AG": ("Semillas: Pythium y Phytophthora.", "suelf", ""),
  "HO": ("Mildiu, tizón tardío y Phytophthora en papa, tomate, cebolla, cucurbitáceas y cítricos.", "mild suelf", "pri")},
 "metalaxil_m": {
  "AG": ("Semillas: Pythium y Phytophthora.", "suelf", ""),
  "HO": ("Mildiu, tizón tardío y Phytophthora en papa, tomate, cebolla, cucurbitáceas y cítricos.", "mild suelf", "pri")},
 "nano_plata": {
  "HO": ("Bacteriosis y hongos (desinfectante).", "bact", ""),
  "AG": ("Bacteriosis y hongos (desinfectante).", "bact", "")},
 "peptido_flg22": {
  "AG": ("Inductor de defensas (bioinsumo).", "manch", ""),
  "HO": ("Inductor de defensas (bioinsumo).", "manch", "")},
 "percarbonato": {
  "HO": ("Desinfectante oxidante de superficies, agua y bacteriosis.", "bact", ""),
  "AG": ("Desinfectante oxidante.", "bact", "")},
 "physcion": {
  "HO": ("Inductor de defensas contra oídio.", "oidio", ""),
  "AG": ("Inductor de defensas contra oídio.", "oidio", "")},
 "piraclostrobina": {
  "AG": ("Roya, manchas y antracnosis en soja y maíz; siempre en mezcla.", "roya manch antr", ""),
  "HO": ("Manchas, antracnosis y mildiu en hortalizas y frutales.", "manch antr mild", "")},
 "propiconazol": {
  "AG": ("Roya y manchas en cereales y soja.", "roya manch", ""),
  "HO": ("Manchas y roya en frutales y banana (sigatoka).", "manch roya", "solo")},
 "reynoutria": {
  "HO": ("Oídio y manchas (extracto vegetal).", "oidio manch", ""),
  "AG": ("Oídio y manchas (extracto vegetal).", "oidio manch", "")},
 "tebuconazol": {
  "AG": ("Roya, manchas y fusariosis en soja y cereales.", "roya manch", ""),
  "HO": ("Manchas, oídio y roya en frutales y hortalizas.", "manch oidio roya", "solo"),
  "FO": ("Roya del eucalipto en viveros y plantaciones jóvenes.", "roya", "solo sec")},
 "tiabendazol": {
  "AG": ("Tratamiento de semillas.", "suelf", ""),
  "HO": ("Podredumbres en postcosecha de frutas y papa.", "podr", "")},
 "tiofanato": {
  "AG": ("Manchas, moho blanco y semillas en soja.", "manch scle suelf", ""),
  "HO": ("Antracnosis, manchas y podredumbres en frutales y hortalizas.", "antr manch podr", "")},
 "tiram": {
  "AG": ("Multisitio para tratamiento de semillas.", "suelf", ""),
  "HO": ("Manchas y hongos de suelo en hortalizas y frutales.", "manch suelf", "")},
 "triadimefon": {
  "AG": ("Oídio y roya en cereales.", "oidio roya", ""),
  "HO": ("Oídio y roya en hortalizas y frutales.", "oidio roya", "")},
 "trifloxistrobina": {
  "AG": ("Roya y manchas en soja y maíz; siempre en mezcla.", "roya manch", ""),
  "HO": ("Oídio, sarna y manchas en frutales y hortalizas.", "oidio manch", "")},

 # ---------------- INSECTICIDAS / ACARICIDAS ----------------
 "abamectina": {
  "HO": ("Ácaros, minadores y trips en hortalizas y frutales.", "acar minad trips", ""),
  "AG": ("Ácaros en soja y algodón; nematodos en tratamiento de semillas.", "acar nema", "")},
 "acefato": {
  "AG": ("Chinches, trips y lagartas en soja y algodón.", "chin trips lag", ""),
  "HO": ("Pulgones, trips y lagartas en hortalizas.", "pulg trips lag", "solo")},
 "acetamiprid": {
  "AG": ("Mosca blanca y chinches en soja y algodón.", "mbla chin", ""),
  "HO": ("Mosca blanca y pulgones en hortalizas y frutales.", "mbla pulg", "solo")},
 "azadiractina": {
  "HO": ("Lagartas, mosca blanca y pulgones (botánico).", "lag mbla pulg", ""),
  "AG": ("Lagartas, mosca blanca y pulgones (botánico).", "lag mbla pulg", "")},
 "bifentrina": {
  "AG": ("Chinches, lagartas, ácaros y plagas de suelo en soja, maíz y algodón.", "chin lag acar suelo", ""),
  "HO": ("Lagartas y ácaros en hortalizas.", "lag acar", "solo"),
  "FO": ("Termitas y hormigas en plantaciones de eucalipto y pino.", "term", "solo sec")},
 "buprofezina": {
  "HO": ("Mosca blanca y cochinillas en hortalizas y cítricos.", "mbla cochi", ""),
  "AG": ("Mosca blanca en soja y algodón.", "mbla", "")},
 "carbaril": {
  "HO": ("Lagartas y coleópteros en hortalizas y frutales.", "lag coleo", ""),
  "AG": ("Lagartas y coleópteros.", "lag coleo", "")},
 "cartap": {
  "HO": ("Lagartas y minadores en hortalizas.", "lag minad", ""),
  "AG": ("Lagartas.", "lag", "")},
 "ciantraniliprol": {
  "AG": ("Lagartas y mosca blanca en soja y algodón; semillas.", "lag mbla", ""),
  "HO": ("Lagartas, mosca blanca y minadores en hortalizas.", "lag mbla minad", "")},
 "cipermetrina": {
  "AG": ("Lagartas y chinches en soja, maíz y algodón.", "lag chin", ""),
  "HO": ("Lagartas en hortalizas.", "lag", "solo")},
 "clorantraniliprol": {
  "AG": ("Lagartas en soja, maíz y algodón.", "lag", ""),
  "HO": ("Lagartas y polilla del tomate.", "lag", "solo")},
 "clorfenapir": {
  "AG": ("Lagartas y ácaros en algodón y soja.", "lag acar", ""),
  "HO": ("Ácaros y lagartas en hortalizas.", "acar lag", "")},
 "clorpirifos": {
  "AG": ("Plagas de suelo, lagartas y chinches.", "suelo lag chin", ""),
  "HO": ("Plagas de suelo y lagartas en hortalizas.", "suelo lag", "solo")},
 "clotianidina": {
  "AG": ("Chinches y plagas iniciales (semillas).", "chin suelo", ""),
  "HO": ("Pulgones y mosca blanca en hortalizas.", "pulg mbla", "solo")},
 "deltametrina": {
  "AG": ("Lagartas y chinches.", "lag chin", ""),
  "HO": ("Lagartas en hortalizas.", "lag", "solo"),
  "AL": ("Protección de granos almacenados (gorgojos, polillas), con o sin butóxido de piperonilo.", "alm", "pri")},
 "diafentiuron": {
  "HO": ("Mosca blanca y ácaros en hortalizas.", "mbla acar", ""),
  "AG": ("Mosca blanca y ácaros en algodón y soja.", "mbla acar", "")},
 "diflubenzuron": {
  "AG": ("Lagartas defoliadoras en soja.", "lag", ""),
  "FO": ("Lagartas defoliadoras del eucalipto.", "lag", "solo"),
  "PA": ("Langostas, tucuras e isocas de pasturas.", "lang lag", "solo")},
 "dimetoato": {
  "AG": ("Pulgones, chinches y trips.", "pulg chin trips", ""),
  "HO": ("Pulgones, trips y mosca de la fruta.", "pulg trips", "")},
 "emamectina": {
  "AG": ("Lagartas (Helicoverpa, Spodoptera).", "lag", ""),
  "HO": ("Lagartas y polilla del tomate.", "lag", "solo")},
 "esfenvalerato": {
  "AG": ("Lagartas y chinches.", "lag chin", ""),
  "HO": ("Lagartas.", "lag", "solo")},
 "espinetoram": {
  "AG": ("Lagartas en soja y maíz.", "lag", ""),
  "HO": ("Trips, minadores y lagartas en hortalizas.", "trips minad lag", "")},
 "espinosad": {
  "HO": ("Trips, lagartas y mosca de la fruta.", "trips lag", "pri"),
  "AG": ("Lagartas.", "lag", ""),
  "AL": ("Protección de granos almacenados.", "alm", "solo")},
 "espirotetramato": {
  "HO": ("Pulgones, mosca blanca y cochinillas en hortalizas y cítricos.", "pulg mbla cochi", ""),
  "AG": ("Mosca blanca en soja y algodón.", "mbla", "")},
 "fenpropatrina": {
  "HO": ("Ácaros y lagartas en hortalizas y frutales.", "acar lag", ""),
  "AG": ("Ácaros y lagartas.", "acar lag", "")},
 "fipronil": {
  "AG": ("Plagas de suelo, picudo del algodón y tratamiento de semillas.", "suelo coleo", ""),
  "FO": ("Hormigas cortadoras (cebo).", "horm", "f:GB pri"),
  "PA": ("Hormigas cortadoras (cebo).", "horm", "f:GB pri")},
 "flubendiamida": {
  "AG": ("Lagartas.", "lag", ""),
  "HO": ("Lagartas en hortalizas.", "lag", "solo")},
 "fluxametamida": {
  "AG": ("Lagartas.", "lag", ""),
  "HO": ("Lagartas y trips en hortalizas.", "lag trips", "")},
 "imidacloprid": {
  "AG": ("Chinches, pulgones y plagas iniciales (semillas).", "chin pulg suelo", ""),
  "HO": ("Pulgones, mosca blanca y psílidos en hortalizas y cítricos.", "pulg mbla", "solo"),
  "FO": ("Psílido y chinche bronceada del eucalipto; termitas en plantines.", "pulg chin term", "solo sec")},
 "indoxacarb": {
  "AG": ("Lagartas.", "lag", ""),
  "HO": ("Lagartas en hortalizas.", "lag", "solo")},
 "lambdacialotrina": {
  "AG": ("Lagartas y chinches en soja, maíz y algodón.", "lag chin", ""),
  "HO": ("Lagartas en hortalizas.", "lag", "solo"),
  "PA": ("Salivazo, langostas e isocas de pasturas.", "chich lang lag", "solo sec")},
 "lufenuron": {
  "AG": ("Lagartas.", "lag", ""),
  "HO": ("Lagartas en hortalizas.", "lag", "solo")},
 "malation": {
  "HO": ("Pulgones y mosca de la fruta (cebo tóxico).", "pulg", ""),
  "AL": ("Protección de granos almacenados y depósitos.", "alm", "pri"),
  "AG": ("Pulgones.", "pulg", "")},
 "metomil": {
  "AG": ("Lagartas.", "lag", ""),
  "HO": ("Lagartas y pulgones en hortalizas.", "lag pulg", "")},
 "metoxifenozida": {
  "AG": ("Lagartas.", "lag", ""),
  "HO": ("Lagartas en hortalizas.", "lag", "solo")},
 "permetrina": {
  "AL": ("Plagas de depósitos y granos almacenados.", "alm", ""),
  "HO": ("Lagartas en hortalizas.", "lag", "")},
 "pirimicarb": {
  "HO": ("Pulgones en hortalizas y frutales.", "pulg", ""),
  "AG": ("Pulgones en cereales.", "pulg", "")},
 "piriproxifen": {
  "AG": ("Mosca blanca en soja y algodón.", "mbla", ""),
  "HO": ("Mosca blanca y cochinillas en hortalizas y cítricos.", "mbla cochi", "")},
 "spiromesifen": {
  "HO": ("Mosca blanca y ácaros en hortalizas.", "mbla acar", ""),
  "AG": ("Mosca blanca y ácaros en soja y algodón.", "mbla acar", "")},
 "sulfluramida": {
  "FO": ("Hormigas cortadoras (cebo).", "horm", ""),
  "PA": ("Hormigas cortadoras (cebo).", "horm", "pri"),
  "AG": ("Hormigas cortadoras (cebo).", "horm", "")},
 "sulfoxaflor": {
  "AG": ("Chinches, pulgones y mosca blanca.", "chin pulg mbla", ""),
  "HO": ("Pulgones y mosca blanca en hortalizas.", "pulg mbla", "solo")},
 "teflubenzuron": {
  "AG": ("Lagartas.", "lag", ""),
  "FO": ("Lagartas defoliadoras del eucalipto.", "lag", "solo sec")},
 "tiametoxam": {
  "AG": ("Chinches, pulgones y plagas iniciales (semillas).", "chin pulg suelo", ""),
  "HO": ("Pulgones y mosca blanca en hortalizas.", "pulg mbla", "solo")},
 "triflumuron": {
  "AG": ("Lagartas.", "lag", ""),
  "FO": ("Lagartas defoliadoras del eucalipto.", "lag", "solo sec")},

 # ---------------- OTROS ----------------
 "metaldehido": {
  "HO": ("Caracoles y babosas en hortalizas (cebo).", "molu", ""),
  "AG": ("Babosas en siembra directa (cebo).", "molu", "")},
 "auxinas_reg": {
  "HO": ("Enraizamiento y cuaje.", "regu", ""),
  "AG": ("Enraizamiento y crecimiento.", "regu", "")},
 "brasinoesteroide": {
  "AG": ("Tolerancia a estrés y crecimiento.", "regu", ""),
  "HO": ("Tolerancia a estrés y crecimiento.", "regu", "")},
 "citocininas": {
  "AG": ("División celular y crecimiento.", "regu", ""),
  "HO": ("División celular, cuaje y tamaño de fruto.", "regu", "")},
 "etefon": {
  "AG": ("Apertura de cápsulas en algodón y maduración.", "regu", ""),
  "HO": ("Maduración y floración (piña, tomate).", "regu", "")},
 "giberelico": {
  "HO": ("Crecimiento, cuaje y tamaño de fruto.", "regu", ""),
  "AG": ("Crecimiento inicial y germinación.", "regu", "")},
 "tidiazuron": {
  "AG": ("Defoliante de algodón.", "regu", ""),
  "HO": ("Cuaje y tamaño de frutos.", "regu", "")},
 "pbo": {
  "AG": ("Sinergista de piretroides.", "sine", ""),
  "AL": ("Sinergista de piretroides para granos almacenados.", "sine", "pri")},
 "feromona": {
  "HO": ("Confusión sexual y monitoreo de plagas en frutales y hortalizas.", "lag", ""),
  "AG": ("Monitoreo y confusión sexual (picudo, lagartas).", "lag", "")},

 # ---------------- BIOLÓGICOS Y BOTÁNICOS ----------------
 "bio_bt": {
  "AG": ("Lagartas (Bacillus thuringiensis).", "lag", ""),
  "HO": ("Lagartas en hortalizas (Bacillus thuringiensis).", "lag", ""),
  "FO": ("Lagartas defoliadoras del eucalipto (Bacillus thuringiensis).", "lag", "pri")},
 "bio_bacillus": {
  "AG": ("Enfermedades foliares y de suelo; nematodos (Bacillus).", "manch suelf nema", ""),
  "HO": ("Enfermedades foliares y de suelo; nematodos (Bacillus).", "manch suelf nema", "")},
 "bio_pseudomonas": {
  "AG": ("Enfermedades de suelo y promotor de crecimiento.", "suelf", ""),
  "HO": ("Enfermedades de suelo en almácigos y promotor de crecimiento.", "suelf", "")},
 "bio_trichoderma": {
  "AG": ("Hongos de suelo y moho blanco (Trichoderma).", "suelf scle", ""),
  "HO": ("Hongos de suelo en almácigos y hortalizas (Trichoderma).", "suelf", "pri"),
  "FO": ("Hongos de suelo en viveros forestales (Trichoderma).", "suelf", "")},
 "bio_hongo_entomo": {
  "AG": ("Mosca blanca, chinches y lagartas (Beauveria, Metarhizium, Cordyceps).", "mbla chin lag", ""),
  "HO": ("Mosca blanca y lagartas en hortalizas (Beauveria, Cordyceps).", "mbla lag", ""),
  "PA": ("Salivazo de las pasturas (Metarhizium).", "chich", ""),
  "FO": ("Chinche bronceada y lagartas del eucalipto (Beauveria).", "chin lag", "")},
 "bio_virus": {
  "AG": ("Lagartas (baculovirus).", "lag", ""),
  "HO": ("Lagartas en hortalizas (baculovirus).", "lag", "")},
 "bio_consorcio": {
  "AG": ("Enfermedades de suelo y nutrición (consorcio microbiano).", "suelf", ""),
  "HO": ("Enfermedades de suelo y nutrición (consorcio microbiano).", "suelf", "")},
 "bio_macro": {
  "HO": ("Control biológico con insectos benéficos.", "lag mbla", ""),
  "AG": ("Control biológico con insectos benéficos.", "lag", "")},
 "bot_extractos": {
  "HO": ("Insectos y enfermedades varias (extractos botánicos).", "pulg manch", ""),
  "AG": ("Insectos y enfermedades varias (extractos botánicos).", "pulg manch", "")},
}
