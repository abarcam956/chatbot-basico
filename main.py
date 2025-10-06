from bot import ReglaBot

def main():
    bot = ReglaBot()
    print("ElectroWordBot listo.")
    print(" - Escribe 'ayuda' para ver intenciones")
    print(" - Escribe 'salir' para terminar\n")
    
    while True:
        u = input("Tú: ")
        r = bot.responder(u)
        print("Bot:", r)
        bot.registrar_turno(u, r)
        
        # Si la última intención fue despedida, cerramos
        if bot._ultima_intencion == "despedida":
            archivo = bot.guardar_historial_sesion()
            print("\nHistorial guardado en:", archivo)
            print("Estadísticas:", bot.estadisticas())
            break

if __name__ == "__main__":
 main()