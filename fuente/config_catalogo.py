# Catálogo de productos: clase, origen, forma de uso y función de los coadyuvantes.
# El listado del SENAVE escribe la "clase de uso" de más de 130 formas distintas (INSECTICIDA - ACARICIDA, FUNGUICIDA,
# REGULADOR DE PH, BIOFUNGICIDA...). Acá se normaliza y se cruza con la composición de cada producto.
import re, unicodedata

CLASES = {  # orden en que se muestran
 "herbicida": "Herbicida", "insecticida": "Insecticida", "acaricida": "Acaricida", "fungicida": "Fungicida",
 "bactericida": "Bactericida", "nematicida": "Nematicida", "molusquicida": "Molusquicida", "rodenticida": "Rodenticida",
 "regulador": "Regulador de crecimiento", "coadyuvante": "Coadyuvante", "limpiador": "Limpiador de tanque",
 "desinfectante": "Desinfectante", "repelente": "Repelente", "protector": "Protector (antídoto)", "feromona": "Feromona",
}
ORIGENES = {"quimico": "Químico", "biologico": "Biológico (microorganismos)", "botanico": "Botánico (extractos)", "semioquimico": "Feromona"}
USOS = {"pulverizacion": "Pulverización", "curasemillas": "Tratamiento de semillas", "cebo": "Cebo", "fumigante": "Fumigante (granos y silos)", "otro": "Otra forma de uso"}
FUNCIONES_ADY = {
 "aceite": "Aceite (mineral, vegetal o metilado)", "tensioactivo": "Tensioactivo / humectante", "organosiliconado": "Organosiliconado (superhumectante)",
 "penetrante": "Penetrante (d-limoneno, aceite de naranja)", "corrector": "Corrector de agua (secuestrante, AMS)", "ph": "Regulador de pH (acidificante o alcalinizante)",
 "antiespumante": "Antiespumante", "antideriva": "Antideriva", "adherente": "Adherente", "solvente": "Solvente / humectante", "nutriente": "Nutriente foliar",
 "limpiador": "Limpiador de tanque", "desinfectante": "Desinfectante",
}
ADY_FUNCION = {
 "ady_mso": "aceite", "ady_aceite_mineral": "aceite", "ady_aceite_vegetal": "aceite", "ady_terpeno": "penetrante",
 "ady_no_ionico": "tensioactivo", "ady_anionico": "tensioactivo", "ady_cationico": "tensioactivo", "ady_jabon": "tensioactivo", "ady_lecitina": "tensioactivo",
 "ady_organosiliconado": "organosiliconado", "ady_secuestrante": "corrector", "ady_ams": "corrector", "ady_acidificante": "ph", "ady_alcalinizante": "ph",
 "ady_antiespumante": "antiespumante", "ady_antideriva": "antideriva", "ady_adherente": "adherente", "ady_humectante": "solvente",
 "ady_nutriente": "nutriente", "ady_boro": "nutriente", "ady_silicato": "nutriente",
}
CLASE_ACTIVO = {"herbicida": "herbicida", "insecticida": "insecticida", "fungicida": "fungicida", "regulador_crecimiento": "regulador",
                "protector_semilla": "protector", "protector_herbicida": "protector", "sinergista": "insecticida", "molusquicida": "molusquicida",
                "rodenticida": "rodenticida", "feromona": "feromona"}
# Componentes que no son activos ni coadyuvantes clásicos
COMP_CLASE = {"cuaternario_amonio": "desinfectante", "cloro_activo": "desinfectante", "percarbonato": "limpiador", "nano_plata": "fungicida"}

# Limpiadores de tanque registrados en el SENAVE (06/10/2026). Ninguno publica la etiqueta en internet:
# "nombre" = se identifica como limpiador por su nombre y composición; "posible" = verificar en la etiqueta.
LIMPIADORES = {
 "6532": {"conf": "nombre", "tipo": "detergente", "nota": "Limpiador de tanque con butilglicol (solvente). Dosis según etiqueta."},
 "6771": {"conf": "nombre", "tipo": "detergente", "nota": "Detergente de tanque (lauril éter sulfato de sodio). Dosis según etiqueta."},
 "6082": {"conf": "nombre", "tipo": "alcalino", "nota": "Limpiador alcalino (hidróxido de potasio) con tensioactivo y antiespumante: sube el pH y disuelve restos de hormonales y sulfonilureas."},
 "8806": {"conf": "nombre", "tipo": "amoniacal", "nota": "Limpiador amoniacal (hidróxido de amonio e hidróxido de sodio). Nunca junto con lavandina."},
 "7897": {"conf": "posible", "tipo": "desengrasante", "nota": "d-Limoneno con tensioactivo y antiespumante: sirve para restos oleosos (EC, aceites). Verificar en la etiqueta si es limpiador o coadyuvante."},
 "8737": {"conf": "posible", "tipo": "oxidante", "nota": "Percarbonato de sodio (oxidante a base de peróxido). El listado no trae la clase de uso: verificar en la etiqueta."},
}
DESINFECTANTES = {
 "6011": "Desinfectante clorado: no sirve para sacar restos de herbicidas. Nunca con amoníaco, productos amoniacales ni ácidos.",
 "6121": "Sanitizante contra hongos y bacterias (maquinaria, pediluvios): no saca restos de herbicidas.",
}

def _nk(t):
    t = unicodedata.normalize("NFD", (t or "").upper())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")

def clases_senave(cu):
    """Clases según el texto 'clase de uso' del SENAVE."""
    t = _nk(cu); out = []
    def add(x):
        if x not in out: out.append(x)
    if re.search(r"REGULADOR DE PH|ACONDICIONADOR|ADITIVO|COADYUV|ADYUV|ADHERENTE|EMULSIONANTE|TENS[IO]*ACTIVO|SURFACTANTE|ANTIDERIVA|ACIDIFICANTE|DISOLVENTE", t): add("coadyuvante")
    if "HERBIC" in t or "DEFOLIANTE" in t or "DESECANTE" in t: add("herbicida")
    if re.search(r"INSECTIC|AFIDICIDA|GORGOJ|HORMIGUIC|INSECTICIDA", t): add("insecticida")
    if "ACARIC" in t: add("acaricida")
    if re.search(r"FUNGIC|FUNGUIC|FUNGIST", t): add("fungicida")
    if "BACTERIC" in t: add("bactericida")
    if "NEMATIC" in t: add("nematicida")
    if "MOLUSQ" in t: add("molusquicida")
    if "RODENTIC" in t: add("rodenticida")
    # regulador de crecimiento vegetal (no el regulador de pH ni el regulador de crecimiento de insectos de un insecticida)
    if re.search(r"FITOREG|FITORREG|FITOHORMONA|PROMOTOR DE CRECIMIENTO|LIBERADORES DE CRECIMIENTO|BIOESTIMULANTE|MADURADOR|REGULADOR(?! DEL? ?PH)", t) and "INSECTIC" not in t: add("regulador")
    if "DESINFECT" in t or "SANITIZANTE" in t: add("desinfectante")
    if "LIMPIADOR" in t or "LIMPIA TANQUE" in t: add("limpiador")
    if "FEROMONA" in t: add("feromona")
    if "REPELENTE" in t: add("repelente")
    if re.search(r"PROTECTOR DE (SEMILLA|CULTIVO)", t): add("protector")
    return out

def origen_senave(cu):
    t = _nk(cu)
    if re.search(r"MICROBIOL|BIOLOG|BIOFUNG|BIOINSECT|BIO FUNG", t): return "biologico"
    if re.search(r"BOTANIC|\bORGANICO", t): return "botanico"
    return None
