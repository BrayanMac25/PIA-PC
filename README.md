# PIA-PC
Producto Integrador De Aprendizaje de Programación Para Ciberseguridad
Instrucciones de uso:
En este proyecto tenemos los siguientes archivos:
1)	api.py: este sirve para poder hacer búsquedas dentro de shodan para facilitar la buqueda de vulnerabilidades en distintos servidores, en este caso lo que hace es hacer una búsqueda con un argumento dado y arroja los resultados.
2)	cifradoCesar.py: encripta o desencripta una frase dada en cifrado de tipo Cesar
3)	correo.py: con este script se pueden mandar correos a distintas personas.
4)	menu.ps1: este archivo sirve para ayudar a entender de una manera mas sencilla y practica los argumentos en este script de powershell se ven ejemplos de argumentos y el resultado de su ejecución.
5)	menu.py: este es el mas importante ya que este es el único que se debe de ejecutar los demás solo sirven para mandarlos a llamar y nos arrojen resultados, este este compuesto por distintos argumentos que dependiendo de lo que se pida será el resultado este mismo script genera un archivo en el cual se guaran los errores y a su vez se ve lo que hace el script.
6)	metadatos_imagenes.py: en este script se puede utilizar para visualizar los metadatos de las imágenes mandando como argumento una ruta de la carpeta de las imágenes y este script nos muestra en pantalla los metadatos.
7)	Scraping.py: hace un web scraping de la pagina dada por los argumentos en el script del menu.py
8)	Hashpia.py: verifica el hash de el archivo que queramos.
9)	infopag.py: para ver la información de el dominio desde donde nos responden. 
Ya sabiendo de que scripts está compuesto este proyecto nos podemos ir a los argumentos de ejecución del script.

Opciones en argumentos:
-script: en este argumento se especifica que script queremos utilizar por ejemplo.
-script metadatos
-script cifrado
-script scraping
-script mail
-script shodan
-script nmap
-script hash
-script socket

Ya especificado el script que queremos ejecutar agregamos los argumentos que vayamos a querer, estos van dependiendo del script.
A continuación, se mostrará la sintaxis dependiendo del script a ejecutar.
Metadatos:
-script metadatos -dato “ruta de la carpeta de imágenes a inspeccionar”
Ejemplo:
Mi carpeta se llama images y esta en mi escritorio, entonces copeo la dirección de el escritorio y agregamos /images
-script metadatos -dato “C:\Users\braya\OneDrive\Escritorio\images”
Se requiere que la ruta sea ingresada dentro de comillas dobles para evitar un tipo de error.
Cifrado:
-script cifrado -dato “se coloca la palabra: encriptar o des” -text “texto a encriptar o desencriptar”
Ejemplo:
Para encriptar:
-script cifrado -dato encriptar -text “Hola mucho gusto como estas”
Para desencriptar:
-script cifrado -dato des -text “LSPE QYGLS KYWXS GSQS IWXEW”
Web Scraping:
-script scraping -dato “pagina elegida para hacer web scraping”
Ejemplo:
-script scraping -dato “https://www.uanl.mx/”
Se requiere colocar la pagina entre comillas para evitar errores en espacios.
Envío de correo:
-script mail -asunto “asunto de el correo” -correo “correo desde el que se envia” -destinatario “destinatario del correo” -contraseña “contraseña de el correo desde el que se envia” -mensaj “mendaje que se quiere enviar”
Ejemplo: 

-script mail -asunto “investigación” -correo brayanreyna@hotmail.com – destinatario maestra@outlook.com -contraseña “contraseña127” -mensaj “Hola que tal todo bien”
Búsqueda en shodan:
-script shodan -buscar “lo que se desea buscar en shodan” -api “api key ”
Ejemplo:
-script shodan -buscar “smtp” -api cJvdCQtllUGxVfy9qbc

Escaneo con nmap:
-script nmap -dato “ip de el objetivo” -inicio “numero de puerto inicial” -final “numero de puerto para finalizar”
Ejemplo:
-script nmap -dato 192.168.0.9 -inicio 78 -final 81
Hash:
-script hash -dato “ruta de archivo”
Ejemplo:
-script hash -dato C:\Users\braya\OneDrive\pia.py
Socket:
-script socket -dato “nombre del domino”
Ejemplo.
-script -dato uanl.mx




Para mayor entendimiento se puede utilizar en archivo menu.ps1 ejecutando desde powershell.

Para su funcionamiento correcto se necesita que todos los archivos estén juntos dentro de una carpeta.
