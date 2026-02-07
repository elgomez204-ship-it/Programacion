def raizSegura(numero):
	'''
		Función que calcula la raíz cuadrada de un número dado.
		Entradas: numero (int, float o str) que se espera que sea numérico
		Salidas: resultado de la raíz cuadrada como float (o cero si hay fallo)
		Capturas de error:
		  1.- Si es numérico
		  2.- Si se puede convertir a número
		  3.- Si no es un número positivo
	'''
	from math import sqrt

	if isinstance(numero, (int, float)):
		if numero >= 0:
			raiz = sqrt(numero)
			return raiz
		else:
			return 0
	
	else:
		try:
			numero = float(numero)
			entero_raiz = sqrt(numero)
			return entero_raiz
		except:
			return 0

numero = int(input("Introduce el numero: "))

print(raizSegura(numero))


