#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.
SERVER = 'localhost'
PORT = 6001
Metodo = sys.argv[1]
Direccion = sys.argv[2]

Separar = Direccion.split(":")
Login = Separar[0]
Puerto = Separar[1]
print(Login)
print(Puerto)
# Contenido que vamos a enviar
LINE = '¡Hola mundo!'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

#Contenido que enviamos
if not len(sys.argv) != 2:
    sys.exit("Usage: python client.py method receiver@IP:SIPport")
if Metodo == "INVITE":
    USER = Direccion
print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
