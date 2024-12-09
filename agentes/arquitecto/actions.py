# actions.py

def recibir_solicitud(requisitos):
    """
    Recibe los requisitos del cliente para el diseño de la casa.
    """
    print(f"Requisitos recibidos: {requisitos}")
    # Almacenar o procesar los requisitos si es necesario
    return f"Requisitos entendidos: {requisitos}"

def diseñar_plan(requirements, budget):
    """
    Diseña la casa según los requisitos y el presupuesto.
    Devuelve el tiempo estimado para completar el diseño.
    """
    print(f"Diseñando casa con los requisitos: {requirements} y presupuesto: {budget}")
    # Simulación del proceso de diseño y estimación de tiempo
    estimated_time = 15  # Ejemplo: 15 días para diseñar
    return f"Plan diseñado. Tiempo estimado: {estimated_time} días."


def colaborar_aprobación(diseño, colaboradores):
    """
    Colabora con el cliente (propietario) para aprobar el diseño en el ayuntamiento.
    """
    print(f"Colaborando con {', '.join(colaboradores)} para aprobar el diseño: {diseño}")
    # Simula el proceso de aprobación
    estado_aprobación = "Diseño aprobado."
    return estado_aprobación

def entregar_diseño(cliente, diseño):
    """
    Entrega el diseño finalizado y aprobado al cliente.
    """
    print(f"Entregando diseño: {diseño} al cliente: {cliente}")
    # Simula el proceso de entrega
    return f"Diseño {diseño} entregado a {cliente}."
