En este ejercicio vamos a crear una agenda de contactos, que permita guardarlos en un archivo `.txt` y luego puedas listarlos.

---

Para realizar este ejercicio primero debemos comenzar el bucle:
```
	while True:
```
Luego le damos las opciones al usuario para que elija que hacer:
```
  print("Dime lo que quieres hacer: ")
  print("1.-Introduce un nuevo contacto")
  print("2.-Leer todos los contactos")
  opcion = int(input("Escoge tu opción: "))
```
Y luego comenzamos a desarrollar las opciones:
##Opción 1:
```
  if opcion == 1:
    nombre = input("Introduce el nombre de la persona: ")
    email = input("Introduce el email de la persona: ")
    archivo = open("agenda.txt",'a') 
    archivo.write(nombre+","+email+"\n")
    archivo.close()
```
##Opcion 2:
```
  elif opcion == 2:
    archivo = open("agenda.txt",'r')
    lineas = archivo.readlines()
    for linea in lineas:
      print(linea)
    archivo.close()
```

---

A continuación el codigo completo:
```
	'''
		Agenda de contactos
		v0.1 Valentin Antonio De Gennaro
		Permite guardar datos en un archivo txt y permite leerlos
	'''

	print("######Agenda de contactos#######")
	print("v0.1 Valentin Antonio De Gennaro")

	while True:
	  print("Dime lo que quieres hacer: ")
	  print("1.-Introduce un nuevo contacto")
	  print("2.-Leer todos los contactos")
	  opcion = int(input("Escoge tu opción: "))
	  if opcion == 1:
		nombre = input("Introduce el nombre de la persona: ")
		email = input("Introduce el email de la persona: ")
		archivo = open("agenda.txt",'a') 
		archivo.write(nombre+","+email+"\n")
		archivo.close()
	  elif opcion == 2:
		archivo = open("agenda.txt",'r')
		lineas = archivo.readlines()
		for linea in lineas:
		  print(linea)
		archivo.close()
```

---

**NOTAS:**
- Es importante cerrar el archivo con `close()` después de usarlo.
