class Cliente():
## ESTE ES EL METODO CONSTRUCTOR ##
	def __init__(self):
		self.nombrecompleto = ""
		self.email = ""
		
## ESTOS SON LOS SETTERS Y LOS GETTERS ##
	def setNombreCompleto(self,nuevonombre):
		self.nombrecompleto = nuevonombre
	def setEmail(self,nuevoemail):
		self.email = nuevoemail
	def getNombreCompleto(self):
		return self.nombrecompleto
	def getEmail(self):
		return self.email
		
clientes = []  ##METO UNA LISTA VACIA##

print("Gestor de clientes v0.1 Valentin Antonio De Gennaro")
while True:
	print("Selecciona una opcion:")
	print("1.-Insertar un nuevo cliente")
	print("2.-Obtener listado de clientes")
	opcion = int(input("Indica tu opcion (1,2): "))

	if opcion == 1:  ## LOS SETTERS SE USAN EN LAS OPERACIONES DE CREACION DE NUEVOS ELEMENTOS
		print("Voy a insertar un cliente")
		nuevocliente = Cliente()
		nombrecliente = input("Introduce el nombre del cliente: ") # TOMO EL DATO #
		nuevocliente.setNombreCompleto(nombrecliente)  ## USO EL METODO SET PARA METER EL DATO EN EL OBJETO ##
		emailcliente = input("Introduce el email de tu cliente: ") # TOMO EL DATO #
		nuevocliente.setEmail(emailcliente)  ## USO EL METODO SET PARA METER EL DATO EN EL OBJETO ##
		
		clientes.append(nuevocliente)
		
	elif opcion == 2:
		print("Saco el listado de clientes")
		for cliente in clientes:
			print("-------------------------")
			print("Nombre: ", cliente.getNombreCompleto())
			print("Email: ", cliente.getEmail())
			print("-------------------------")
