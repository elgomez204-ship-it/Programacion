'''
	Gestión de clientes
	v0.1 Valentín Antonio De Gennaro
	Programa que permite insertar y listar clientes usando clases y listas.
'''

## DEFINIMOS LA CLASE CLIENTE ##
class Cliente:
	def __init__(self):
		self.email = ""
		self.nombre = ""
		self.direccion = ""

## MÉTODO PARA INSERTAR DATOS ##
	def insertar_datos(self):
		self.email = input("Introduce el email del cliente: ")
		self.nombre = input("Introduce el nombre del cliente: ")
		self.direccion = input("Introduce la dirección del cliente: ")

## CREAMOS UNA LISTA VACÍA PARA GUARDAR LOS CLIENTES ##
clientes = []

## MENÚ PRINCIPAL ##
while True:
	print("-------------------------------------------")
	print("Elige una opción")
	print("1. Insertar un cliente")
	print("2. Listar clientes")
	print("3. Salir")
	print("-------------------------------------------")
	opcion = int(input("Selecciona una opción: "))

	if opcion == 1:
		## INSERTAR UN CLIENTE ##
		nuevo_cliente = Cliente()
		nuevo_cliente.insertar_datos()
		clientes.append(nuevo_cliente)
		print("Cliente añadido correctamente.")
	elif opcion == 2:
		## LISTAR CLIENTES ##
		if clientes == []:
			print("No hay clientes registrados.")
		else:
			print("Listado de clientes:")
			for cliente in clientes:
				print("")
				print("Email:", cliente.email)
				print("Nombre:", cliente.nombre)
				print("Dirección:", cliente.direccion)
				print("-------------------------------------------")
	elif opcion == 3:
		print("Saliendo...")
		break
	else:
		print("Opción no válida, intenta de nuevo.")

