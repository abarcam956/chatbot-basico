from datetime import datetime

respuestas = {
    "saludo": [
        "¡Hola! Bienvenido a ElectroWord, ¿en qué puedo ayudarte?",
        "¡Buenas! Gracias por contactar con ElectroWord, ¿qué necesitas?",
        "¡Hola! Encantado de atenderte desde ElectroWord."
    ],
    
    "despedida": [
        "¡Adiós! Gracias por visitar ElectroWord.",
        "¡Hasta luego! Esperamos verte pronto en ElectroWord.",
        "Chao, que tengas un excelente día."
    ],
 
    "agradecimiento": [
        "¡Gracias a ti por confiar en ElectroWord! ",
        "¡Muchas gracias! Estamos aquí para ayudarte siempre.",
        "ElectroWord te agradece tu confianza."
    ],
    
    "horario": [
        "Nuestro horario es de lunes a viernes de 9:00 a 18:00.",
        "Abrimos de lunes a viernes de 9:00 a 18:00 horas.",
        "En ElectroWord atendemos de lunes a viernes en ese horario."
    ],
    
    "ubicacion": [
        "Nuestra tienda principal está en Calle Mayor 123, Rota, Cádiz.",
        "Nos puedes encontrar en Calle Mayor 123, Rota.",
        "Estamos en Rota, Cádiz. ¿Quieres que te pase la ubicación en el mapa?"
    ],
    
    "formas_pago": [
        "Aceptamos tarjeta, PayPal, transferencia bancaria y Bizum.",
        "Puedes pagar con tarjeta, PayPal, transferencia o Bizum.",
        "Ofrecemos varias formas de pago seguras: tarjeta, PayPal, transferencia y Bizum."
    ],
    
    "envios": [
        "Realizamos envíos en 24/48 horas en la península.",
        "El plazo de entrega suele ser de 1 a 2 días laborables.",
        "Enviamos tu pedido lo más rápido posible, normalmente en 24/48h."
    ],
    
    "metodos_envio": [
        "Trabajamos con MRW, SEUR y Correos Express.",
        "Enviamos tu pedido mediante mensajería (MRW, SEUR, Correos Express).",
        "Nuestros envíos se realizan con empresas de mensajería reconocidas."
    ],
    
    "seguimiento_pedido": [
        "Puedes seguir tu pedido con el número de seguimiento que enviamos por email.",
        "El estado de tu pedido está disponible en tu área de cliente.",
        "Te facilitamos un número de seguimiento para rastrear tu envío."
    ],
    
    "garantia": [
        "Todos nuestros productos tienen 2 años de garantía.",
        "Ofrecemos garantía legal de 2 años en nuestros productos.",
        "En ElectroWord la garantía estándar es de 2 años."
    ],
    
    "devoluciones": [
        "Tienes 14 días para devolver tu pedido si no estás satisfecho.",
        "Aceptamos devoluciones en un plazo de 14 días naturales.",
        "Puedes solicitar una devolución desde tu área de cliente o contactando con nosotros."
    ],
    
    "productos_destacados": [
        "Nuestros productos más vendidos son portátiles, smartphones y televisores.",
        "Te recomendamos echar un vistazo a nuestros top ventas en la web.",
        "Tenemos destacados: portátiles, tablets y accesorios muy demandados."
    ],
    
    "stock": [
        "Puedes consultar la disponibilidad directamente en la ficha del producto.",
        "Si el producto aparece como disponible en la web, está en stock.",
        "Algunos productos se agotan rápido, revisa siempre el stock online."
    ],
    
    "soporte_tecnico": [
        "Nuestro equipo de soporte técnico está disponible de lunes a viernes.",
        "Puedes contactar con soporte técnico desde tu cuenta de cliente.",
        "Si tienes problemas técnicos, abre un ticket en soporte y te ayudaremos."
    ],
    
    "contacto": [
        "Puedes llamarnos al 955 123 456 o escribirnos a soporte@electroword.com.",
        "Nuestro teléfono es 955 123 456 y el email soporte@electroword.com.",
        "Estamos disponibles en soporte@electroword.com o en el 955 123 456."
    ],
    
    "reparaciones": [
        "Contamos con servicio técnico propio para reparaciones.",
        "Puedes solicitar reparación contactando con soporte técnico.",
        "Reparamos productos comprados en ElectroWord, consulta condiciones."
    ],
    
    "factura": [
        "Emitimos facturas electrónicas que puedes descargar desde tu cuenta.",
        "Tu factura está disponible en el área de cliente una vez confirmado el pedido.",
        "Si necesitas factura, marca la opción al realizar la compra o solicítala por email."
    ],
    
    "cuenta_usuario": [
        "Puedes acceder a tu cuenta desde la sección 'Área de cliente' en nuestra web.",
        "Tu perfil está disponible en el área de cliente de la web.",
        "Entra en 'Mi cuenta' para gestionar tus pedidos y datos."
    ],
    
    "cancelar_pedido": [
        "Puedes cancelar tu pedido desde el área de cliente si aún no ha sido enviado.",
        "Contacta con soporte para cancelar un pedido en preparación.",
        "La cancelación es posible antes de que el pedido salga del almacén."
    ],
    
    "promociones": [
        "Consulta nuestras promociones y descuentos en la web.",
        "Tenemos ofertas activas en portátiles y smartphones este mes.",
        "Revisa la sección de promociones para encontrar descuentos especiales."
    ],
    
    "politica_privacidad": [
        "Cumplimos con la RGPD. Puedes consultar nuestra política de privacidad en la web.",
        "Nuestra política de privacidad está disponible online en ElectroWord.",
        "Protegemos tus datos según la normativa vigente de privacidad."
    ],

    "quejas_reclamaciones": [
        "Puedes presentar una reclamación enviando un correo a soporte@electroword.com.",
        "Disponemos de hojas de reclamaciones en nuestra tienda física.",
        "Para quejas, contacta con soporte o acude a nuestra tienda en Rota."
    ],
    
    "como_te_llamas": [
        "Soy ElectroBot, el asistente virtual de ElectroWord.",
        "Me llamo ElectroBot y estoy aquí para ayudarte.",
        "Soy el bot de asistencia de ElectroWord."
    ],

    "que_hora_es": [
        f"La hora actual es {datetime.now().strftime('%H:%M:%S')}.",
        f"Ahora mismo son las {datetime.now().strftime('%H:%M:%S')}.",
        "Déjame comprobar... ¡ya te digo la hora exacta!"
    ]
}