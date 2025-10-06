import unicodedata
import random
import re

def normalizar(texto):
    # 1. Pasar a minúsculas y quitar espacios al inicio y fin
    t = texto.strip().lower()
    
    # 2. Descomponer caracteres en base + tilde (NFD)
    t = unicodedata.normalize("NFD", t)
    
    # 3. Eliminar los diacríticos (tildes, diéresis, etc.)
    t = t.encode("ascii", "ignore").decode("utf-8")
    
    # 4. Eliminar todo lo que no sea letras, números o espacios
    t = re.sub(r'[^a-z0-9\s]', '', t)
    
    # 5. Colapsar espacios múltiples en uno solo
    t = re.sub(r'\s+', ' ', t).strip()

    return t

def elegir_respuesta(candidatas, ultima):
    opciones = [r for r in candidatas if r != ultima] or candidatas
    return random.choice(opciones)

# Palabras clave (disparadores)

PALABRAS_CLAVE = {
    "saludo": ["hola", "buenas", "buenos dias", "buenas tardes", "buenas noches"],
    "despedida": ["adios", "hasta luego", "chao", "nos vemos"],
    "agradecimiento": ["gracias", "muchas gracias", "mil gracias"],
    "horario": ["horario", "abren", "cierran"],
    "ubicacion": ["ubicacion", "direccion", "donde estan", "donde queda", "tienda"],
    "formas_pago": ["pago", "pagos", "tarjeta", "paypal", "transferencia", "bizum"],
    "envios": ["envio", "envios", "entrega", "plazo", "tarda", "llega"],
    "metodos_envio": ["mensajeria", "mrw", "seur", "correos express"],
    "seguimiento_pedido": ["seguimiento", "tracking", "numero de seguimiento", "estado pedido"],
    "garantia": ["garantia", "garantias"],
    "devoluciones": ["devolucion", "devolver", "devoluciones"],
    "productos_destacados": ["destacados", "recomendados", "top ventas"],
    "stock": ["stock", "disponible", "hay", "queda"],
    "soporte_tecnico": ["soporte", "tecnico", "ayuda tecnica", "asistencia"],
    "contacto": ["contacto", "telefono", "email", "correo"],
    "reparaciones": ["reparacion", "arreglar", "servicio tecnico"],
    "factura": ["factura", "facturacion"],
    "cuenta_usuario": ["cuenta", "perfil", "area cliente", "mi cuenta"],
    "cancelar_pedido": ["cancelar", "cancelacion"],
    "promociones": ["promocion", "promociones", "oferta", "ofertas", "descuento"],
    "politica_privacidad": ["privacidad", "rgpd", "proteccion de datos"],
    "quejas_reclamaciones": ["reclamacion", "queja", "hoja de reclamaciones"],
    "como_te_llamas": ["como te llamas", "tu nombre", "quien eres"],
    "que_hora_es": ["que hora es", "hora exacta"]
}

def detectar_intencion(texto_normalizado):
    for intent, triggers in PALABRAS_CLAVE.items():
        if any(tr in texto_normalizado for tr in triggers):
            return intent
    return None
    
def lista_ayuda(claves):
    return " Intenciones disponibles:\n- " + "\n- ".join(sorted(claves))

