'''
	Registro de personas
	v0.1 Valentín Antonio De Gennaro
	Almacena datos de personas

'''

## DEFINIMOS LA CLASE ##
class Persona():
	def __init__(self):
		self.nombre = ""
		self.apellido = ""
		self.edad = 0
		self.ocupacion = ""

## DEFINO SETTERS Y GETTERS ##
	def setNombre(self, nuevonombre):
		self.nombre = nuevonombre
		
	def setApellido(self, nuevoapellido):
		self.apellido = nuevoapellido
		
	def setEdad(self, nuevaedad):
		self.edad = nuevaedad
		
	def setOcupacion(self, nuevaocupacion):
		self.ocupacion = nuevaocupacion
		
	def getNombre(self):
		return self.nombre
		
	def getApellido(self):
		return self.apellido
		
	def getEdad(self):
		return self.edad
		
	def getOcupacion(self):
		return self.ocupacion
		
	
listapersonas = [] # CREO UNA LISTA VACIA #

print("Programa de registro de personas v0.1 Valentín Antonio De Gennaro")

## MUESTRO OPCIONES AL USUARIO ##

while True:
	print("Selecciona una opción: ")
	print("1.-Insertar una persona")
	print("2.-Mostrar la lista de personas")
	
## LE PERMITO ESCOGER UNA OPCION ##

	opcion = int(input("Escoge una opción: "))
	
	if opcion == 1:
		print("Vamos a insertar una persona")
## INGRESO DE INFORMACION ##
		nuevo = Persona()
		
		nombrepersona = input("Introduce el nombre de la persona: ")
		nuevo.setNombre(nombrepersona)
		
		apellidopersona = input("Introduce el apellido de la persona: ")
		nuevo.setApellido(apellidopersona)
		
		edadpersona = int(input("Introduce la edad de la persona: "))
		nuevo.setEdad(edadpersona)
		
		ocupacion = input("Introduce la ocupación de la persona: ")
		nuevo.setOcupacion(ocupacion)
		
## AÑADIMOS EL CLIENTE A LA LISTA ##
		listapersonas.append(nuevo)
		print("Cliente insertado correctamente.")
	elif opcion == 2:
		print("Vamos a ver la lista de personas")
		for persona in listapersonas:
			print("-------------------------------------------------")
			print("Nombre:", persona.getNombre())
			print("Apellido:", persona.getApellido())
			print("Edad:", persona.getEdad())
			print("Ocupación:", persona.getOcupacion())
			print("-------------------------------------------------")
