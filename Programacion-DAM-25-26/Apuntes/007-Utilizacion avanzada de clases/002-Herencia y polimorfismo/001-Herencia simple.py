class Persona():
	def __init__(self,nombre,apellidos):
		self.nombre = nombre
		self.apellidos = apellidos
	def dameDatos(self):
		return self.nombre+self.apellidos

class Profesor(Persona):
	def __init__(self,nombre,apellidos):
		super().__init__(nombre, apellidos)
  
class Alumno(Persona):
	def __init__(self,nombre,apellidos,email,direccion):
		super().__init__(nombre, apellidos)

alumno1 = Alumno("Valentin","De Gennaro","info@valentindg.com","calle principal 1")
print(alumno1.dameDatos())

profesor1 = Profesor("Jose Vicente","Carratala","info@jocarsa.com","calle principal 2")
print(profesor1.dameDatos())
