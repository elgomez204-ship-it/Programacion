'''
	Herencia de animales
	v0.1 Valentín Antonio De Gennaro
	Ejemplo de clase madre e hijas usando herencia.
'''

class Animal():
	def __init__(self, edad, nombre, raza):
		self.edad = edad
		self.nombre = nombre
		self.raza = raza

class Gato(Animal):
	def __init__(self, edad, nombre, raza):
		super().__init__(edad, nombre, raza)

class Perro(Animal):
	def __init__(self, edad, nombre, raza):
		super().__init__(edad, nombre, raza)

## CREAMOS OBJETOS ##
gato1 = Gato(3, "Mishi", "Siames")
perro1 = Perro(5, "Rocky", "Labrador")

## MOSTRAMOS LA INFORMACIÓN ##
print("Edad del gato:", gato1.edad)
print("Edad del perro:", perro1.edad)

