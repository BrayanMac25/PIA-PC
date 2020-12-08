import socket
def info(x):
	ipres = socket.gethostbyname_ex(x)
	ser = socket.getfqdn(x)
	print("Ip donde responde la peticion", ipres[2])
	print("Nombre del servidor donde responde", ser)
