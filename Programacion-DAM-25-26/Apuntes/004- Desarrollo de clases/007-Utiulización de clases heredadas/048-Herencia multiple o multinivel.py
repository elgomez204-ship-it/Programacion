class Entidad():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0
		
class Animal(Entidad): 
	def __init__(self):
		super().__init__()
		self.edad = 0
		self.nombre = ""
		self.raza = ""

class Gato(Animal):
	def __init__(self):
		super().__init__()  ## TRAIGO TODO LO QUE TENGA LA CLASE SUPERIOR ##
		
class Perro(Animal):
	def __init__(self):
		super().__init__()  ## TRAIGO TODO LO QUE TENGA LA CLASE SUPERIOR ##
		
class Roca(Entidad):
	def __init__(self):

gato1 = Gato()
print(gato1.edad)

perro1 = Perro()
print(perro1.edad)

roca1 = Roca()
print(roca.x)
print(roca.y)
print(roca.z)

