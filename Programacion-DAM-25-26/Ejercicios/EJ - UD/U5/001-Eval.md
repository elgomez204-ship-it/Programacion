En este ejercicio vamos a crear una aplicación de gestion de clientes la cual te va permitir introducir los datos de un cliente, la aplicación va a introducir esos datos en un archivo binario, y luego te permite mostrarlos en pantalla.

---

Para realizar este ejercicio primero debemos importar la libreria, a continaución un ejemplo:
```
	import pickle
```
Despues debemos definir la clase:
```
	class Cliente():
		def __init__(self,nombre,apellido,email,edad):
			self.nombre = nombre
			self.apellidos = apellido
			self.email = email
			self.edad = edad
```
Luego usando `try` y `except` vamos a abrir el archivo .bin, se usa el `try` y `except` ya que hay caso de que el archivo no exista:
```
	try:
		archivo = open("clientes.bin",'rb')
		clientes = pickle.load(archivo)
	except:
		print("No existe archivo de datos")
```
Y creamos el bucle:
```
	while True:
```
Y le damos al usuario opciones para que elija:
```
	print("Selecciona una opcion")
	print("1.-Insertar un nuevo cliente")
	print("2.-Obtener listado de clientes")
	print("3.-Salir")
	opcion = int(input("Indica tu opcion: "))
```
Desarrollamos las opciones:
```
	if opcion == 1: 
		print("Voy a insertar un cliente")
		nombre = input("Introduce el nombre del cliente: ") 
		apellidos = input("Introduce el apellido del cliente: ")
```
La opcion2:
```
	elif opcion == 2:
		identificador = 0
		for cliente in clientes:
			print("##########################################")
			print("Este es el cliente con ID:",identificador)
			print("Nombre: ",cliente.nombre)
```
Y por ultimo la opcion 3:
```
	elif opcion == 3:
		print("Adios")
```

---

A continuación el codigo completo:
```
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
```

---

**NOTAS:**
- Al momento de utilizar bucles hay que recordar cerrarlos.
- El uso de la libreria pickle es util, ya que en este caso te permite almacenar los datos del cliente, y aunque el programa se cierre y se vuelva a abrir si el archivo .bin existe los datos tambien.
