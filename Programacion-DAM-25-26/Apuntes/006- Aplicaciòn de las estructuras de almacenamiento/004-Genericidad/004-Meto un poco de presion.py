numeros = [
	1,
	2,
	"3",
	4,
	"cinco"
]

print(numeros)

def calculaDoble():
	for numero in numeros:
		numero = int(numero)  ## CONVIERTO EN ENTERO ##
		print(numero*2)
	
calculaDoble()
