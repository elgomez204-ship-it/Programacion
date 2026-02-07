'''
	Registro de cliente
	v0.1 Valentín Antonio De Gennaro
	Programa que guarda y muestra los datos de un cliente.
'''

class Cliente():
	def __init__(self, nombre, apellidos, email, direccion):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
		self.direccion = direccion

## PEDIMOS LOS DATOS AL USUARIO ##
nombre = input("Introduce el nombre del cliente: ")
apellidos = input("Introduce los apellidos del cliente: ")
email = input("Introduce el email del cliente: ")
direccion = input("Introduce la dirección del cliente: ")

## CREAMOS UN CLIENTE ##
cliente1 = Cliente(nombre, apellidos, email, direccion)

## MOSTRAMOS LA INFORMACIÓN ##
print("-------------------------------------------")
print("Nombre:", cliente1.nombre)
print("Apellidos:", cliente1.apellidos)
print("Email:", cliente1.email)
print("Dirección:", cliente1.direccion)
print("-------------------------------------------")

