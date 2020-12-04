import hashlib
import os
archivos = ['api.py', 'cifradoCesar.py', 'correo.py', 'menu.py', 'menu.ps1', 'metadatos_imagenes.py', 'Scraping.py']
for file in archivos:
	name =str(file)
	file_obj = open(file, "rb")
	file = file_obj.read()
	Hash = hashlib.sha512(file)
	print(Hash)
	Hashed = Hash.hexdigest()
	print( name, Hashed)




