numeros = [
	1,
	2,
	"3",
	4,
	"cinco",
	"cerveza"
]

print(numeros)
numeros_etiquetas = ['cero','uno','dos','tres','cuatro','cinco']
def calculaDoble():
	for numero in numeros:
		try:
			numero = int(numero)
			print(numero*2)
		except:
			centinela = False
			for i in range(0,len(numeros_etiquetas)):
				if numero == numeros_etiquetas[i]:
					print(i*2)
					centienla = True
			if centinela == False:
				print("No se puede")
	
calculaDoble()
