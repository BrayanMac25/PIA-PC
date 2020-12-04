import hashlib
import os

def ha(file):
	name =str(file)
	file_obj = open(file, "rb")
	file = file_obj.read()
	Hash = hashlib.sha512(file)
	print(Hash)
	Hashed = Hash.hexdigest()
	print( name, Hashed)
