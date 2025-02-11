import socket

LISTEN_IP = "0.0.0.0"
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((LISTEN_IP, PORT))
s.listen(1)
print(f"[*] Esperando conexión en {PORT}...")

conn, addr = s.accept()
print(f"[+] Conexión recibida de {addr}")

while True:
    command = input("$ ")  
    conn.send(command.encode())
    if command.lower() == "exit":
        break
    response = conn.recv(4096).decode()
    print(response)

conn.close()
