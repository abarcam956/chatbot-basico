import json
from datetime import datetime
from pathlib import Path

from utils import normalizar, elegir_respuesta, detectar_intencion, lista_ayuda
from respuestas import respuestas as BASE_RESPUESTAS

class ReglaBot:
    def __init__(self, base_respuestas=None):
        self.respuestas = base_respuestas or BASE_RESPUESTAS
        self.ultimo_bot = None
        self.turnos = [] # historial de turnos
        self.intenciones_uso = {} # contador por intención
        self.mensajes_usuario = 0
        self.total_turnos = 0
        self._ultima_intencion = None
        self._inicio_sesion = datetime.now().isoformat(timespec="seconds")
    
    def _sumar_intencion(self, intent):
        self.intenciones_uso[intent] = self.intenciones_uso.get(intent, 0) + 1
        self._ultima_intencion = intent
    
    def responder(self, texto_usuario):
        msg = normalizar(texto_usuario)
        
        # Comandos rápidos
        if msg in ("ayuda", "help"):
            self._ultima_intencion = "ayuda"
            return lista_ayuda(list(self.respuestas.keys()))
        
        if msg in ("salir", "adios", "hasta luego"):
            self._ultima_intencion = "despedida"
            if "despedida" in self.respuestas:
                resp = elegir_respuesta(self.respuestas["despedida"], self.ultimo_bot)
                self.ultimo_bot = resp
                self._sumar_intencion("despedida")
                return resp
            return "Adiós"
 
        # 1) Coincidencia exacta (clave de intención igual al mensaje)
        if msg in self.respuestas:
            self._sumar_intencion(msg)
            resp = elegir_respuesta(self.respuestas[msg], self.ultimo_bot)
            self.ultimo_bot = resp
            return resp
    
        # 2) Coincidencia por palabras clave
        intent = detectar_intencion(msg)
        if intent and intent in self.respuestas:
            self._sumar_intencion(intent)
            resp = elegir_respuesta(self.respuestas[intent], self.ultimo_bot)
            self.ultimo_bot = resp
            return resp
    
        # 3) Desconocida
        self._ultima_intencion = "desconocida"
        return "No entendí ¿Puedes reformular? (escribe 'ayuda' para ver opciones)"
    
    def registrar_turno(self, usuario, bot):
        now = datetime.now().isoformat(timespec="seconds")
        self.turnos.append({
            "timestamp": now,
            "usuario": usuario,
            "bot": bot,
            "intencion": self._ultima_intencion
        })
        self.mensajes_usuario += 1
        self.total_turnos += 1
    def estadisticas(self):
        top = sorted(self.intenciones_uso.items(), key=lambda x: x[1], reverse=True)
        return {
        "mensajes_usuario": self.mensajes_usuario,
        "total_turnos": self.total_turnos,
        "intenciones_mas_usadas": top
        }
    def guardar_historial_sesion(self, ruta=None):
        """
        Guarda un JSON con:
        - 'sesion' (inicio/fin/contadores)
        - 'interacciones' (turnos con timestamp e intención)
        """
        ruta = ruta or Path(f"historial_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        payload = {
            "sesion": {
                "inicio": self._inicio_sesion,
                "fin": datetime.now().isoformat(timespec="seconds"),
                "mensajes_usuario": self.mensajes_usuario,
                "total_turnos": self.total_turnos,
                "intenciones_uso": self.intenciones_uso
            },
            "interacciones": self.turnos
        }
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        return ruta