# Rubros (sectores) por principio activo / biológico.
# AG = Agrícola (cultivos extensivos y tratamiento de semillas)
# HO = Hortícola y frutícola
# FO = Forestal (plantaciones, viveros, hormigas cortadoras)
# PA = Pasturas y ganadería (potreros, malezas leñosas, salivazo, langosta)
# AL = Granos almacenados y postcosecha
# Asignación orientativa según los usos registrados habituales en Paraguay y la región;
# la etiqueta de cada producto define los cultivos autorizados.

RUBROS = {
    "AG": {"nombre": "Agrícola", "detalle": "Soja, maíz, trigo, arroz, algodón, caña, girasol, canola, sésamo y tratamiento de semillas"},
    "HO": {"nombre": "Hortícola y frutícola", "detalle": "Hortalizas, frutales, cítricos, viveros de plantines"},
    "FO": {"nombre": "Forestal", "detalle": "Eucalipto, pino, viveros forestales, hormigas cortadoras y termitas"},
    "PA": {"nombre": "Pasturas", "detalle": "Potreros, malezas leñosas y de hoja ancha, salivazo, langosta, hormigas"},
    "AL": {"nombre": "Granos almacenados", "detalle": "Silos, depósitos y postcosecha: fumigantes, gorgojicidas, roedores"},
}

AI_RUBROS = {
 # Herbicidas
 "24d":"AG PA FO", "acetocloro":"AG", "ametrina":"AG HO", "amicarbazona":"AG", "aminopiralida":"PA",
 "atrazina":"AG", "benazolin":"AG", "bentazona":"AG", "bispiribac":"AG", "carfentrazona":"AG",
 "cihalofop":"AG", "cletodim":"AG HO", "clodinafop":"AG", "clomazona":"AG", "clopiralida":"AG PA",
 "cloransulam":"AG", "clorimuron":"AG", "clorsulfuron":"AG", "dicamba":"AG PA", "diclosulam":"AG",
 "diquat":"AG HO", "diuron":"AG HO", "epyrifenacil":"AG", "fenoxaprop":"AG", "florpirauxifen":"AG",
 "flucarbazona":"AG", "fluchloraminopyr":"AG", "flufenoximacil":"AG", "flumetsulam":"AG",
 "flumioxazin":"AG FO", "fluometuron":"AG", "flurocloridona":"AG HO", "fluroxipir":"AG PA",
 "fomesafen":"AG", "glifosato":"AG PA FO HO", "glufosinato":"AG HO", "glufosinato_p":"AG HO",
 "halauxifen":"AG", "haloxifop":"AG FO", "hexazinona":"AG FO", "imazapic":"AG", "imazapir":"AG FO",
 "imazaquin":"AG", "imazetapir":"AG", "iodosulfuron":"AG", "isoxaflutol":"AG FO", "lactofen":"AG",
 "linuron":"AG HO", "mesotriona":"AG", "metamifop":"AG", "metolacloro":"AG", "metribuzina":"AG HO",
 "metsulfuron":"AG PA", "msma":"AG", "nicosulfuron":"AG", "oxifluorfen":"HO FO AG", "paraquat":"AG HO",
 "pendimetalina":"AG HO", "penoxsulam":"AG", "picloram":"PA AG", "pinoxaden":"AG", "piraflufen":"AG",
 "pirazosulfuron":"AG", "piribenzoxim":"AG", "piroxasulfona":"AG", "prometrina":"AG", "propanil":"AG",
 "propaquizafop":"AG HO", "quinclorac":"AG", "quizalofop":"AG HO", "s_metolacloro":"AG HO",
 "saflufenacil":"AG HO", "simazina":"AG HO FO", "sulfentrazona":"AG FO", "sulfometuron":"FO AG",
 "tebutiuron":"AG PA", "tembotriona":"AG", "terbutilazina":"AG", "tiobencarb":"AG", "tolpiralato":"AG",
 "topramezona":"AG", "triclopir":"PA FO AG", "trifloxisulfuron":"AG", "trifludimoxazin":"AG",
 "trifluralina":"AG HO",
 # Fungicidas
 "azoxistrobina":"AG HO", "azufre":"HO AG", "benomil":"HO AG", "benzovindiflupir":"AG HO", "bixafen":"AG",
 "carbendazim":"AG HO", "carboxina":"AG", "ciclobutrifluram":"AG", "cimoxanil":"HO", "ciproconazol":"AG",
 "cloro_activo":"HO", "clorotalonil":"AG HO", "cobre":"HO AG", "cuaternario_amonio":"HO AG",
 "difenoconazol":"AG HO", "diniconazol":"AG HO", "epoxiconazol":"AG", "estreptomicina":"HO AG",
 "fenpropidina":"AG", "fenpropimorf":"AG", "fentin":"AG HO", "fluazinam":"HO AG", "fludioxonil":"AG HO",
 "fluindapir":"AG", "fluopiram":"AG HO", "flutriafol":"AG", "fluxapiroxad":"AG HO", "folpet":"HO",
 "glucano":"AG HO", "hexaconazol":"AG", "inpyrfluxam":"AG", "ipconazol":"AG", "isopirazam":"AG",
 "isoprotiolano":"AG", "kasugamicina":"HO AG", "kresoxim":"HO AG", "mancozeb":"AG HO",
 "mefentrifluconazol":"AG", "metalaxil":"AG HO", "metalaxil_m":"AG HO", "metarilpicoxamida":"AG",
 "metconazol":"AG", "metiltetraprol":"AG", "metominostrobina":"AG", "nano_plata":"HO AG",
 "oxatiapiprolina":"HO", "oxitetraciclina":"HO", "penflufen":"AG", "peptido_flg22":"AG HO",
 "percarbonato":"HO AG", "physcion":"HO AG", "picoxistrobina":"AG", "pidiflumetofen":"AG",
 "piraclostrobina":"AG HO", "propiconazol":"AG HO", "protioconazol":"AG", "reynoutria":"HO AG",
 "sedaxano":"AG", "tebuconazol":"AG HO FO", "tetraconazol":"AG", "tiabendazol":"AG HO", "tiofanato":"AG HO",
 "tiram":"AG HO", "triadimefon":"AG HO", "triadimenol":"AG", "triciclazol":"AG", "trifloxistrobina":"AG HO",
 # Insecticidas / acaricidas
 "abamectina":"HO AG", "acefato":"AG HO", "acetamiprid":"AG HO", "alfacipermetrina":"AG",
 "azadiractina":"HO AG", "benfuracarb":"AG", "betaciflutrina":"AG", "bifentrina":"AG HO FO",
 "buprofezina":"HO AG", "cadusafos":"HO", "carbaril":"HO AG", "carbosulfan":"AG", "cartap":"HO AG",
 "ciantraniliprol":"AG HO", "cihalodiamida":"AG", "cipermetrina":"AG HO", "ciproflanilida":"AG",
 "clorantraniliprol":"AG HO", "clorfenapir":"AG HO", "clorpirifos":"AG HO", "clotianidina":"AG HO", "clorpirifos_metil":"AL",
 "deltametrina":"AG HO AL", "diafentiuron":"HO AG", "diatomeas":"AL", "diclorvos":"AL",
 "dicofol":"HO", "diflubenzuron":"AG FO PA", "dimetoato":"AG HO", "dinotefuran":"AG", "emamectina":"AG HO",
 "esfenvalerato":"AG HO", "espidoxamato":"AG", "espinetoram":"AG HO", "espinosad":"HO AG AL",
 "espirotetramato":"HO AG", "etiprol":"AG", "fenpropatrina":"HO AG", "fipronil":"AG FO PA",
 "flubendiamida":"AG HO", "flufenoxuron":"HO", "fluxametamida":"AG HO", "fosfuros":"AL",
 "gammacialotrina":"AG", "hexitiazox":"HO", "imidacloprid":"AG HO FO", "indoxacarb":"AG HO",
 "isocycloseram":"AG", "isoflualanam":"AG", "lambdacialotrina":"AG HO PA", "lufenuron":"AG HO",
 "malation":"HO AL AG", "matrina":"HO", "metomil":"AG HO", "metoxifenozida":"AG HO", "novaluron":"AG",
 "permetrina":"AL HO", "pimetrozina":"HO", "pirimicarb":"HO AG", "pirimifos_metil":"AL",
 "piriproxifen":"AG HO", "profenofos":"AG", "propargita":"HO", "rotenona":"HO", "spirodiclofen":"HO",
 "spiromesifen":"HO AG", "spiropidion":"AG", "sulfluramida":"FO PA AG", "sulfoxaflor":"AG HO",
 "teflubenzuron":"AG FO", "tetradifon":"HO", "tiametoxam":"AG HO", "tiodicarb":"AG", "triflumuron":"AG FO",
 "zetacipermetrina":"AG",
 # Otros
 "metaldehido":"HO AG", "cloquintocet":"AG", "dietholate":"AG", "fluxofenim":"AG", "aba":"HO",
 "auxinas_reg":"HO AG", "brasinoesteroide":"AG HO", "citocininas":"AG HO", "clormequat":"AG",
 "etefon":"AG HO", "flumetralin":"AG", "giberelico":"HO AG", "mepiquat":"AG", "tidiazuron":"AG HO",
 "trinexapac":"AG", "flocoumafen":"AL", "pbo":"AG AL", "feromona":"HO AG",
 # Biológicos y botánicos
 "bio_bt":"AG HO FO", "bio_bacillus":"AG HO", "bio_pseudomonas":"AG HO", "bio_trichoderma":"AG HO FO",
 "bio_hongo_entomo":"AG HO PA FO", "bio_virus":"AG HO", "bio_consorcio":"AG HO", "bio_macro":"HO AG",
 "bot_extractos":"HO AG",
}
