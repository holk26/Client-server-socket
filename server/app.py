import socket
from controllers import buscar_persona_por_telefono, obtener_todas_las_personas


def servidor():
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(('localhost', 8080))
    servidor_socket.listen(5)
    print("Servidor a la espera de conexiones...")

    while True:
        cliente_socket, direccion = servidor_socket.accept()
        print(f"Conexión aceptada de {direccion}")

        # Recibe el mensaje del cliente
        consulta = cliente_socket.recv(1024).decode().strip()
        print(f"Consulta recibida: {consulta}")

        if consulta.lower() == "all":
            # Si se recibe "all", obtener todos los registros
            registros = obtener_todas_las_personas()
            if registros:
                mensaje = "\n".join(
                    [f"Teléfono: {p.dir_tel}, Nombre: {p.dir_nombre}, Dirección: {p.dir_direccion}, Ciudad: {c.ciud_nombre}"
                     for p, c in registros]
                )
            else:
                mensaje = "No se encontraron registros."
        else:
            # Si no es "all", buscar persona por número de teléfono
            persona, ciudad = buscar_persona_por_telefono(consulta)
            if persona and ciudad:
                mensaje = (f"Teléfono: {persona.dir_tel}, Nombre: {persona.dir_nombre}, "
                           f"Dirección: {persona.dir_direccion}, Ciudad: {ciudad.ciud_nombre}")
            else:
                mensaje = "Persona no encontrada para este número telefónico."

        # Enviar la respuesta al cliente
        cliente_socket.send(mensaje.encode())
        cliente_socket.close()


if __name__ == "__main__":
    servidor()
