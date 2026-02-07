En este ejercicio vamos a crear un programa en Python que muestre una pantalla de bienvenida, luego un menú con las opciones de gestión de clientes (Crear, Leer, Actualizar y Eliminar) y que tenga una lista donde se guardarán los clientes.

---

Primero creamos la variable de bienvenida y la mostramos por pantalla:
```
	bienvenida = "###### Gestión de clientes v0.1 ######"
	print(bienvenida)
```
Después creamos la lista del menú con las opciones que va a poder elegir el usuario:
```
	opciones_menu = ["Crear","Leer","Actualizar","Eliminar"]
```
También creamos una lista vacía `clientes` para guardar los datos de los clientes:
```
clientes = []
```
Ahora definimos la función para insertar clientes:
```
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
```
Luego hacemos la función para listar los clientes:
```
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
```
Después creamos la función para actualizar un cliente:
```
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
```
Creamos también la función para eliminar un cliente:
```
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
```
Por último hacemos el menú principal con un `while True` para que el programa siga funcionando hasta que el usuario lo cierre y definimos las opciones:
```
---

**NOTAS:**
- Los clientes se guardan en una lista de diccionarios para poder actualizar y eliminar.
- El ID que se muestra es la posición en la lista + 1.
- El menú funciona con `while True` como en los ejercicios de clase.
- Se usan solo funciones, listas y bucles, sin estructuras avanzadas.

