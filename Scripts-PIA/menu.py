import os
import argparse
from metadatos_imagenes import printMeta
from cifradoCesar import Encriptar
from cifradoCesar import Desencriptar
from correo import sendmail
from Scraping import Scraping
from api import busqueda
from escan import Escaneo
from hashpia import ha
import logging
from infopag import info
logging.basicConfig( level=logging.DEBUG, filename='menu.log')
print("""Si se tiene dudas del uso de este script en la carpeta se encuentra un script de powershell el cual es mas interactivo para ver los argumentos 
	     contine los script de metadatos, cifrado Cesar, Web Scraping, Envio de Correos, 
	     busquda en shodan, escaneo de puertos y extraccion de hash""")
descrip = """ El parametro principal el cual se utiliza para especificar el script los cuales son:
           ++metadatos
           ++cifrado
           ++scraping
           ++mail
           ++shodan
           ++nmap
           ++hash
           ++Socket"""
descrip2 = """Si se elige el script de metadatos este argumento funciona para ingresar la ruta de las imagenes,
              si elige el script de web scraping se usa para dar la url, si se usa el script de  nmap se usa para la ip
              si se elige el script de socket sirve para dar el nombre del dominio"""
descrip3 = """Si se elige para el script cifrado  funciona para especificar
si se quiere encriptar o desencriptar para encriptar se coloca la palabra encriptar y desencriptar la palabra des"""
descrip4 = "Se utiliza  para darle el asunto al correo"
descrip5 = "Especifica el correo desde el cual se envia el mendaje"
descrip6 = "Especifica quien recibe el correo"
descrip7 = "Especifica la contraseña del correo"
descrip8 = "Para ingresar el mendaje"
descrip9 = "Argumento a buscar en shodan"
descrip10 = "Coloque como argumento la key apy"
descrip11 = "Se usa para colocar el puerto de inicio del escaneo"
descrip12 = "Se usa para especificar el puerto final de escaneo"
if __name__ == "__main__":
	try:
		parser = argparse.ArgumentParser()
		parser.add_argument("-script", dest="nombrescript", help=descrip)
		parser.add_argument("-dato", dest="argumento", help=descrip2)
		parser.add_argument("-text", dest="frase", help=descrip3)
		parser.add_argument("-asunto", dest="asunto1", help=descrip4)
		parser.add_argument("-correo", dest="sender1", help=descrip5)
		parser.add_argument("-destinatario", dest="reciver1", help=descrip6)
		parser.add_argument("-contraseña", dest="password1", help=descrip7)
		parser.add_argument("-mensaj", dest="mensaje1", help=descrip8)
		parser.add_argument("-api", dest="apis", help=descrip10)
		parser.add_argument("-buscar", dest="buscarsh", help=descrip9)
		parser.add_argument("-inicio", dest="inicioe", help=descrip11)
		parser.add_argument("-final", dest="finale", help=descrip12)
		params = parser.parse_args()
		opcion = params.nombrescript
		Frase = params.frase
		datos = params.argumento
		asunto = params.asunto1
		sender = params.sender1
		reciver = params.reciver1
		password = params.password1
		mensaje = params.mensaje1
		busquedas = params.buscarsh
		inic = params.inicioe
		fin = params.finale
		apish = params.apis
		if opcion == 'metadatos':
			printMeta(datos)
		elif opcion == 'cifrado':
			datos = params.argumento
			if datos == 'encriptar':
				Encriptar(Frase)
			elif datos == 'des':
				print(Desencriptar(Frase))
		elif opcion == 'scraping':
			scraping = Scraping()
			scraping.scrapingImages(datos)
			scraping.scrapingPDF(datos)
			scraping.scrapingLinks(datos)
		elif opcion == 'mail':
			sendmail(asunto, sender, reciver, password, mensaje)
			print("Correo Enviado")
		elif opcion == 'shodan':
			busqueda(busquedas, apish)
		elif opcion == 'nmap':
			ip=str(datos)
			inicios= int(inic)
			finales= int(fin)
			Escaneo(inicios, finales, ip)
			print("El escaneo se encuentra en txt en la misma carpeta que este programa")
		elif opcion == 'hash':
			ha(datos)
		elif opcion == 'socket':
			info(datos)
	except(RuntimeError, TypeError, NameError):
		print("Ha ocurrido un error vuelva a intentar.")
		print("""Si tiene alguna duda puede verificar el script de powershell o el 
			     pdf de instrucciones de uso ubicado en la carpeta principal""")
		pass