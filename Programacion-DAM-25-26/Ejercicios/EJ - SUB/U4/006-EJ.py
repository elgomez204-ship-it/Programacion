'''
	Clase Matematicas
	v0.1 Valentín Antonio De Gennaro
	Clase que permite redondear números y calcular su techo y suelo.
'''

class Matematicas():
	def __init__(self):
		self.PI = 3.14159265359

	def redondeo(self, numero):
		entero = int(numero)
		decimal = numero - entero
		if decimal < 0.5:
			return entero
		else:
			return entero + 1

	def techo(self, numero):
		entero = int(numero)
		if numero == entero:
			return entero
		else:
			return entero + 1

	def suelo(self, numero):
		entero = int(numero)
		return entero


calculadora = Matematicas()

numero = input("Introduce el número: ")

print("Número original:", numero)
print("Redondeo:", calculadora.redondeo(numero))
print("Techo:", calculadora.techo(numero))
print("Suelo:", calculadora.suelo(numero))

