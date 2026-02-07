class Profesor():
	def __init__(self,nombre,apellidos,email)
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
	def dameDatos(self):
		return self.nombre+self.apellidos

class Alumno():
	def __init__(self,nombre,apellidos,email)
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
	def dameDatos(self):
		return self.nombre+self.apellidos
	
alumno1 = Alumno("Valentin","De Gennaro","info@valentindg.com")
print(alumno1.dameDatos())

profesor1 = Profesor("Jose Vicente","Carratala","info@jocarsa.com")
print(profesor1.dameDatos())
