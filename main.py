from threading import Thread
import time
from agentes.albañil import Albañil, REGLAS, ORDEN_ETAPAS

albañiles = []  # Lista global de albañiles
estado_etapas = {etapa: False for etapa in ORDEN_ETAPAS}  # Estado de cada etapa


def registrar_albañiles():
    global albañiles
    while True:
        print("\nRegistro de Albañiles")
        nombre = input("Ingrese el nombre del albañil: ").strip()
        tipo = input("¿Es un albañil experimentado? (s/n): ").strip().lower()
        tipo = "experimentado" if tipo == "s" else "ayudante"

        albañil = Albañil(nombre, tipo)
        print("Selecciona las habilidades para este albañil:")
        habilidades = list(REGLAS.keys())
        for i, habilidad in enumerate(habilidades, start=1):
            print(f"{i}. {habilidad}")
        seleccionadas = input("Selecciona habilidades separadas por coma (ej: 1,3): ").strip()
        indices = [int(i) - 1 for i in seleccionadas.split(",") if i.isdigit()]
        for idx in indices:
            if 0 <= idx < len(habilidades):
                albañil.entrenar(habilidades[idx])

        albañiles.append(albañil)
        print(f"{nombre} registrado como {tipo}.")

        continuar = input("¿Desea registrar otro albañil? (s/n): ").strip().lower()
        if continuar != "s":
            break


def ejecutar_construccion():
    global albañiles, estado_etapas

    for i, etapa in enumerate(ORDEN_ETAPAS):
        print(f"\nIniciando la etapa: {etapa}")

        # Verifica si la etapa anterior está completada
        if i > 0 and not estado_etapas[ORDEN_ETAPAS[i - 1]]:
            print(f"No se puede realizar '{etapa}' antes de completar '{ORDEN_ETAPAS[i - 1]}'.")
            continue

        etapa_threads = []
        for albañil in albañiles:
            thread = Thread(target=ejecutar_tarea_albañil, args=(albañil, etapa))
            etapa_threads.append(thread)
            thread.start()
        for thread in etapa_threads:
            thread.join()

        # Marcar etapa como completada si al menos un albañil la completó
        estado_etapas[etapa] = True

    # Verifica si todas las etapas fueron completadas
    if all(estado_etapas.values()):
        print("\n¡La casa ya fue construida exitosamente! Todas las etapas han concluido.")
    else:
        print("\nNo todas las etapas fueron completadas. La casa no está terminada.")


def ejecutar_tarea_albañil(albañil, tarea):
    if tarea in albañil.habilidades:
        albañil.trabajar(tarea)
    else:
        print(f"{albañil.nombre} no puede realizar '{tarea}'. Está en espera mientras otros trabajan.")
        time.sleep(5)  # Simula un tiempo de espera para el albañil sin habilidades.


# Registro de albañiles
registrar_albañiles()

# Ejecución de la construcción
ejecutar_construccion()
