import shodan

def busqueda(buscar, x):
	print("Hpola")
	shodans = shodan.Shodan(x)
	resultados = shodans.search(buscar)
	resultados.keys()
	for x,y in resultados['matches'] [0].items():
		print(x, "=", y)
