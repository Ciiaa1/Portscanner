import sys
import socket

objetivo = socket.gethostbyname(input("Inserte la direccion IP: "))

print("Escaneando objetivo: " + objetivo)

try:
    for port in range(1,150):
        s = socket.gethostbyname.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((objetivo, port))
        if resultado == 0:
            print("El puerto {} esta abierto".format(port))
        s.close()
except:
    print("\n Saliemdo...")
    sys.exit(0)