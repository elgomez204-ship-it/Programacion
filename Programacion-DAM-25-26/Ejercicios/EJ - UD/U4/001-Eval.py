'''
	Gestor de clientes
	v0.1 Valentin Antonio De Gennaro
	
'''

## CREAMOS LA CLASE ##

class Cliente():
	def __init__(self,nombre,apellidos,email):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
	
## AÑADIMOS LOS SET ##

	def setNombre(self,nuevonombre):
		self.nombre = nuevonombre
	def setApellidos(self,nuevoapellido):
		self.apellidos = nuevoapellido
	def setEmail(self,nuevoemail):
		self.email = nuevoemail

## AÑADIMOS LOS GET ##
	def getNombre(self):
		return self.nombre
	def getApellidos(self):
		return self.apellidos
	def getEmail(self):
		return self.email

## AGREGO LOS CLIENTES ##
		
cliente1 = Cliente("Juan","perez paz","perez@gmail.com")
cliente2 = Cliente("Roberto","sanchez","rss@gmail.com")
cliente3 = Cliente("Rodrigo","gomez","gomezr@gmail.com")

## AÑADO INFORMACIÓN DENTRO DEL SET ##
cliente1.apellidos = ("perez paz")
cliente1.setApellidos(cliente1.apellidos)

## MUESTRO QUE EL GET Y EL SET FUNCIONAN CORRECTAMENTE ##
print(Cliente.getApellidos)
