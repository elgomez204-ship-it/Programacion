'''
	Gestión de clientes
	v0.1 Valentín Antonio De Gennaro
	Permite guardar clientes en una lista usando getters y setters.
'''

## CREAMOS LA CLASE CLIENTE ##
	class Cliente():
		def __init__(self, email):
			self.__nombrecompleto = ""
			self.__email = email

		def setNombreCompleto(self, nuevonombre):
			self.__nombrecompleto = nuevonombre

		def getEmail(self):
			return self.__email

		def getNombreCompleto(self):
			return self.__nombrecompleto

	## CREAMOS LA LISTA DE CLIENTES ##
	lista_clientes = []

	## CREAMOS CLIENTES Y LOS AÑADIMOS A LA LISTA ##
	cliente1 = Cliente("cliente1@example.com")
	cliente1.setNombreCompleto("Carlos Pérez")
	lista_clientes.append(cliente1)

	cliente2 = Cliente("cliente2@example.com")
	cliente2.setNombreCompleto("María Gómez")
	lista_clientes.append(cliente2)

	cliente3 = Cliente("cliente3@example.com")
	cliente3.setNombreCompleto("Valentín De Gennaro")
	lista_clientes.append(cliente3)

	## MOSTRAMOS LA INFORMACIÓN DE LOS CLIENTES ##
	for cliente in lista_clientes:
		print("")
		print("Nombre:", cliente.getNombreCompleto())
		print("Email:", cliente.getEmail())
		print("-------------------------------------------")

