#CRUD
#CREATE
#READ
#UPDATE
#DELETE

print("Programa de gestión de clientes v0.1 Valentin de Gennaro")

##### MUESTRO OPCIONES AL USUARIO #########
print("Selecciona una opción: ")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")

#### LE PERMITO ESCOGER UNA OPCION ####
opcion = input("Escoge una opción: ")
opcion = int(opcion) #CONVIERTO A ENTERO#

clientes = []  #CREO UNA LISTA VACIA#

while True: #ESTO DESATA UN BUCLE INFINITO PERO CONTROLADO#
    if opcion == 1:
        print("Vamos a insertar un cliente")
    elif opcion == 2:
        print("Vamos a ver a los clientes")
    elif opcion == 3:
        print("Vamos a actualizar un cliente")
    elif opcion == 4:
        print("Vamos a eliminar un cliente")
    else:
        break


