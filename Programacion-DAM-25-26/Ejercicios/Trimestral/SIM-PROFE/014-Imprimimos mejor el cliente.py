class Cliente():
	def __init__(self,nombre, apellidos,email):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
		
	
print("#######Gestion de clientes v0.1######")
print("#####Valentin Antonio De Gennaro#####")

clientes = []

while True:
	print("Escoge una opción:")
	print("1.-Insertar un cliente")
	print("2.-Listar clientes")
	print("3.-Actualizar un cliente")
	print("4.-Eliminar un cliente")
	opcion = int(input("Escoge una opcion: "))
	
	if opcion == 1:
		nombre = input("Introduce el nombre del cliente: ")
		apellidos = input("Introduce los apellidos del cliente: ")
		email = input("Introduce el email del cliente: ")
		clientes.append(Cliente(nombre, apellidos, email))
		
	elif opcion == 2:
		for cliente in clientes:
			print(cliente.nombre, cliente.apellidos, cliente.email)
	elif opcion == 3:
		pass
	elif opcion == 4:
		pass
	
		
