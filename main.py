from agentes.albañil import Albañil, ACCIONES, ORDEN_ETAPAS

albañiles = []

def registrar_albañiles():
    global albañiles
    while True:
        print("\nRegistro de Albañiles")
        nombre = input("Ingrese el nombre del albañil: ").strip()
        tipo = input("¿Es un albañil experimentado? (s/n): ").strip().lower()
        tipo = "experimentado" if tipo == "s" else "ayudante"

        albañil = Albañil(nombre, tipo)
        print("Selecciona las habilidades para este albañil:")
        habilidades = list(ACCIONES.keys())
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

def asignar_tareas():
    global albañiles
    for albañil in albañiles:
        print(f"\nAsignando tareas para {albañil.nombre} ({albañil.tipo}):")
        for tarea in ORDEN_ETAPAS:
            if tarea in albañil.habilidades:
                albañil.trabajar(tarea)
            else:
                print(f"{albañil.nombre} no puede realizar '{tarea}' por falta de habilidad.")
                break

registrar_albañiles()

asignar_tareas()
