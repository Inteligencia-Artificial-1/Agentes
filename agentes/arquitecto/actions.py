# actions.py
def recibir_solicitud(requisitos):
    """ Recibe los requisitos del cliente para el diseño de la casa. """
    print(f"Requisitos recibidos: {requisitos}")
    return f"Requisitos entendidos: {requisitos}"

def diseñar_plan(requisitos, presupuesto):
    """ Diseña la casa según los requisitos y el presupuesto. Devuelve el tiempo estimado para completar el diseño. """
    print(f"Diseñando casa con los requisitos: {requisitos} y presupuesto: {presupuesto}")
    estimated_time = 20  # Puede cambiarse según el cálculo real
    return f"Plan diseñado con los requisitos: {requisitos} y presupuesto: {presupuesto}. Tiempo estimado: {estimated_time} días."

def colaborar_aprobación(diseño, colaboradores):
    """ Colabora con el cliente (propietario) para aprobar el diseño en el ayuntamiento. """
    print(f"Colaborando con {', '.join(colaboradores)} para aprobar el diseño: {diseño}")
    estado_aprobación = "Diseño aprobado"
    return f"{estado_aprobación} por {', '.join(colaboradores)} para el diseño: {diseño}"

def entregar_diseño(cliente, diseño):
    """ Entrega el diseño finalizado y aprobado al cliente. """
    print(f"Entregando diseño: {diseño} al cliente: {cliente}")
    return f"Diseño {diseño} entregado a {cliente}."
