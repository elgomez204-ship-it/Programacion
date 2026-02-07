'''
	Gestor de clientes
	v0.1 Valentin Antonio De Gennaro
	Introducir, Almacenar y Listar clientes 
'''
import pickle

class Cliente():
	def __init__(self,nombre,apellido,email,edad):
		self.nombre = nombre
		self.apellidos = apellido
		self.email = email
		self.edad = edad

print("######### Gestión de clientes v0.1 #######")
print("####### Valentín Antonio De Gennaro  ######")
			
clientes = [] 
try:
	archivo = open("clientes.bin",'rb')
	clientes = pickle.load(archivo)
except:
	print("No existe archivo de datos")
    
while True:
	archivo = open("clientes.bin",'wb')
	pickle.dump(clientes,archivo)
	archivo.close()
	
	print("Selecciona una opcion")
	print("1.-Insertar un nuevo cliente")
	print("2.-Obtener listado de clientes")
	print("3.-Salir")
	opcion = int(input("Indica tu opcion: "))

	if opcion == 1: 
		print("Voy a insertar un cliente")
		nombre = input("Introduce el nombre del cliente: ") 
		apellidos = input("Introduce el apellido del cliente: ")
		email = input("Introduce el email de tu cliente: ")
		edad = input("Introduce la edad del cliente: ")
		clientes.append(Cliente(nombre,apellidos,email,edad))

	elif opcion == 2:
		identificador = 0
		for cliente in clientes:
			print("##########################################")
			print("Este es el cliente con ID:",identificador)
			print("Nombre: ",cliente.nombre)
			print("Apellidos: ",cliente.apellidos)
			print("Edad: ",cliente.edad)
			print("Email: ",cliente.email)
			print("##########################################")
			identificador += 1

	elif opcion == 3:
		print("Adios")
		break
