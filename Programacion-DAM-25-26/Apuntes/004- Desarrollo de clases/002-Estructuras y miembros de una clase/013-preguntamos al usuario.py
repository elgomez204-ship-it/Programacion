####### DECLARAMOS LA CLASE ############
class Cliente():
    def __init__(self):
        self.email = None
        self.nombre = None
        self.direccion = None

########## USAMOS LA CLASE INSTANCIANDO EN UN OBJETO ######
cliente1 = Cliente()
cliente1.email = input("Introduce el email del cliente: ")
cliente1.nombre = input("Introduce el nombre del cliente: ")
cliente1.direccion = input("Introduce la dirección del cliente: ")

print(cliente1)
print(cliente1.email)
print(cliente1.nombre)
print(cliente1.direccion)
