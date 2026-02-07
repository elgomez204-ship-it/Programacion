'''
	Gestión de clientes
	v0.1 Valentin Antonio De Gennaro
'''

## PANTALLA DE BIENVENIDA ##
bienvenida = "###### Gestión de clientes v0.1 ######"
print(bienvenida)

## LISTA DEL MENÚ ##
opciones_menu = ["Crear","Leer","Actualizar","Eliminar"]

## LISTA DONDE GUARDAREMOS LOS CLIENTES ##
clientes = []

## FUNCIONES ##

def insertar_cliente():
	nombre = input("Introduce el nombre: ")
	apellidos = input("Introduce los apellidos: ")
	email = input("Introduce el email: ")
	cliente = {
		"nombre": nombre,
		"apellidos": apellidos,
		"email": email
	}
	clientes.append(cliente)
	print("Cliente añadido correctamente.")

def listar_clientes():
	if clientes == []:
		print("No hay clientes todavía.")
	else:
		identificador = 1
		for cliente in clientes:
			print("ID:", identificador)
			print("Nombre:", cliente["nombre"])
			print("Apellidos:", cliente["apellidos"])
			print("Email:", cliente["email"])
			print("---------------------")
			identificador = identificador + 1

def actualizar_cliente():
	listar_clientes()
	id_cliente = int(input("Introduce el ID del cliente a actualizar: "))
	posicion = id_cliente - 1
	if posicion >= 0 and posicion < len(clientes):
		nombre = input("Nuevo nombre: ")
		apellidos = input("Nuevos apellidos: ")
		email = input("Nuevo email: ")
		clientes[posicion]["nombre"] = nombre
		clientes[posicion]["apellidos"] = apellidos
		clientes[posicion]["email"] = email
		print("Cliente actualizado.")
	else:
		print("ID no válido.")

def eliminar_cliente():
	listar_clientes()
	id_cliente = int(input("Introduce el ID del cliente a eliminar: "))
	posicion = id_cliente - 1
	if posicion >= 0 and posicion < len(clientes):
		confirmacion = input("¿Seguro que quieres eliminarlo? (s/n): ")
		if confirmacion == "s":
			del clientes[posicion]
			print("Cliente eliminado.")
		else:
			print("Operación cancelada.")
	else:
		print("ID no válido.")

## MENÚ PRINCIPAL ##
while True:
	print("---- MENÚ PRINCIPAL ----")
	identificador = 1
	for opcion in opciones_menu:
		print(str(identificador)+".-"+opcion)
		identificador = identificador + 1

	opcion_seleccionada = input("Selecciona una opción (1-4) o 'salir': ")
	
## DEFINIMOS LAS OPCIONES ##
	if opcion_seleccionada == "1":
		insertar_cliente()
	elif opcion_seleccionada == "2":
		listar_clientes()
	elif opcion_seleccionada == "3":
		actualizar_cliente()
	elif opcion_seleccionada == "4":
		eliminar_cliente()
	elif opcion_seleccionada.lower() == "salir":
		print("Saliendo del programa...")
		break
	else:
		print("Opción no válida.")

