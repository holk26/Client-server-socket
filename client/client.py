import socket

def cliente():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(('localhost', 8080))

    telefono = input("Ingrese el número de teléfono a consultar: ")
    cliente_socket.send(telefono.encode())

    respuesta = cliente_socket.recv(1024).decode()
    print(f"Respuesta del servidor: {respuesta}")

    cliente_socket.close()

if __name__ == "__main__":
    cliente()

