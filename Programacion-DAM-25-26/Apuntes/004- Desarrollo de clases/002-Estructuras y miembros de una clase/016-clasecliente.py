#CRUD
#CREATE
#READ
#UPDATE
#DELETE

####### DECLARAMOS LA CLASE ############
class Cliente():
    def __init__(self):
        self.email = None
        self.nombre = None
        self.direccion = None

print("Programa de gestión de clientes v0.1 Valentin de Gennaro")

##### MUESTRO OPCIONES AL USUARIO #########
print("Selecciona una opción: ")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")



clientes = []  #CREO UNA LISTA VACIA#

while True: #ESTO DESATA UN BUCLE INFINITO PERO CONTROLADO#

#### LE PERMITO ESCOGER UNA OPCION ####
    opcion = input("Escoge una opción: ")
    opcion = int(opcion) #CONVIERTO A ENTERO#
    
    if opcion == 1:
        print("Vamos a insertar un cliente")
        nuevocliente = Cliente()
      ## AHORA LE PONEMOS PROPIEDADES ##
      ## A LARGO PLAZO ES INSEGURO ##
        nuevocliente.nombre = input("Introduce el nombre del cliente: ")
        nuevocliente.email = input("Introduce el email del cliente: ")
        nuevocliente.direccion = input("Introduce la direccion del cliente: ")
      ## AÑADIMOS UN CLIENTE A LA LISTA ##
        clientes.append(nuevocliente)
    elif opcion == 2:
        print("Vamos a ver a los clientes")
        print(clientes)
    elif opcion == 3:
        print("Vamos a actualizar un cliente")
    elif opcion == 4:
        print("Vamos a eliminar un cliente")
    else:
        break


