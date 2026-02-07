En este ejercicio vamos a crear una aplicación para gestionar una agenda, la cual guarda los datos en un archivo binario.

---

Para realizar este ejercicio primero debemos importar la libreria necesaria:
```
	import pickle
```
Luego creamos una lista vacia:
```
	agenda = []
```
Despues usando el bucle `while` le pedimos al usuario los datos del contacto a agregar:
```
	while True:
			nombre = input("Dime tu nombre: ")
			apellidos = input("Dime tus apellidos: ")
			email = input("Dime tu email: ")
			telefono = input("Dime tu telefono: ")
```
Luego añadimos los datos a la lista:
```
	agenda.append([nombre,apellidos,email,telefono])
```
Despues mostramos por pantalla los datos almacenados en la lista:
```
	print(agenda)
```
Y por ultimo guardamos los datos en un archivo binario:
```
	archivo = open("agenda.bin","wb")
	pickle.dump(agenda, archivo)
	archivo.close()
```

---

A continuación el codigo completo:
```
	'''
		Gestión de agenda
		v0.1 Valentín Antonio De Gennaro
	'''

	## IMPORTAMOS LA LIBRERIA NECESARIA ##
	import pickle

	print("############ Gestión de agenda ###########")
	print("#### v0.1 Valentin Antonio De Gennaro ####")

	## CREAMOS LA LISTA VACIA ##
	agenda = []

	## CREAMOS UN CONTACTO ##
	while True:
			nombre = input("Dime tu nombre: ")
			apellidos = input("Dime tus apellidos: ")
			email = input("Dime tu email: ")
			telefono = input("Dime tu telefono: ")
			
			## AÑADIMOS LOS DATOS A LA AGENDA ##
			agenda.append([nombre,apellidos,email,telefono])
			
			## MOSTRAMOS LOS DATOS DE LA AGENDA ##
			print(agenda)
				
			## GUARDAMOS LOS DATOS EN EL ARCHIVO BINARIO ##
			archivo = open("agenda.bin","wb")
			pickle.dump(agenda, archivo)
			archivo.close()
```

---

**NOTAS:**
- Esta agenda se podría usar para guardar contactos del equipo, de clase o de cualquier actividad.
- El archivo agenda.bin permite mantener los datos aunque cerremos el programa.
