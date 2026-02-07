En este ejercicio vamos a crear una aplicación que gestione el menu de un restaurante y lo almacene en un archivo binario y luego lo muestre.

---

Para realizar este ejercicio primero debemos importar la `pickle` la cual usaremos para guardar y leer en el archivo binario:
```
	import pickle
```
Luego usando `try / except` para evitar error cargamos o creamos el archivo binario:
```
	try:
		archivo = open("menu.bin","rb")
		menu = pickle.load(archivo)
		archivo.close()
		print("Menú cargado correctamente:", menu)
		
	except:
		print("No existe archivo previo. Creando un menú nuevo...")
		menu = []
```
Luego creamos un bucle `while` y le pedimos al usuario que indique una opción:
```
	while True:
		print("Selecciona una opcion:")
		print("1.- Añadir una nueva comida")
		print("2.- Mostrar el menu")
		print("3.- Guardar menú en archivo binario")
		print("4.- Cargar menú desde archivo binario")
		print("5.- Salir")
		opcion = int(input("Escoge una opción: "))
```
Luego del menu debemos desarrollar las opciones:

Opción 1:
```
	if opcion == 1:
		comida = input("Dime el nombre de la comida: ")
		menu.append(comida)
		print("Comida añadida:", comida)
```
Opción 2:
```
	elif opcion == 2:
		print("Comidas guardadas:")
		for comida in menu:
			print(comida)
```
Opción 3:
```
	elif opcion == 3:
		archivo = open("menu.bin","wb")
		pickle.dump(menu, archivo)
		archivo.close()
		print("Menú guardado correctamente.")
```
Opción 4:
```
	elif opcion == 4:
		try:
			archivo = open("menu.bin","rb")
			menu = pickle.load(archivo)
			archivo.close()
			print("Menú cargado:", menu)
		except:
			print("No se pudo cargar el archivo binario.")
```
Opción 5:
```
	elif opcion == 5:
		print("Saliendo...")
		break
```

---

A continuación el codigo completo:
```
'''
	Gestión de menú de restaurante
	v0.1 Valentín Antonio De Gennaro
'''

## IMPORTAMOS LA LIBRERIA NECESARIA ##
import pickle

print("### Gestión del menu de un restaurante ###")
print("#### v0.1 Valentin Antonio De Gennaro ####")

## INTENTAMOS CARGAR EL MENÚ ##
try:
	archivo = open("menu.bin","rb")
	menu = pickle.load(archivo)
	archivo.close()
	print("Menú cargado correctamente:", menu)
	
## SI NO EXITE CREAMOS UN MENU NUEVO ##	
except:
	print("No existe archivo previo. Creando un menú nuevo...")
	menu = []

## LE DAMOS LAS OPCIONES AL USUARIO ##
while True:
	print("Selecciona una opcion:")
	print("1.- Añadir una nueva comida")
	print("2.- Mostrar el menu")
	print("3.- Guardar menú en archivo binario")
	print("4.- Cargar menú desde archivo binario")
	print("5.- Salir")
	opcion = int(input("Escoge una opción: "))

## DESARROLLAMOS LAS OPCIONES: ##

	## OPCIÓN 1: AÑADIR COMIDA ##
	if opcion == 1:
		comida = input("Dime el nombre de la comida: ")
		menu.append(comida)
		print("###########################")
		print("Comida añadida:", comida)
		print("###########################")

	## OPCIÓN 2: MOSTRAR LISTA ##
	elif opcion == 2:
		print("###########################")
		print("Comidas guardadas:")
		for comida in menu:
			print("###########################")
			print(comida)
			print("###########################")

	## OPCIÓN 3: GUARDAR EN BINARIO ##
	elif opcion == 3:
		archivo = open("menu.bin","wb")
		pickle.dump(menu, archivo)
		archivo.close()
		print("###########################")
		print("Menú guardado correctamente.")
		print("###########################")

	## OPCIÓN 4: CARGAR DESDE BINARIO ##
	elif opcion == 4:
		try:
			archivo = open("menu.bin","rb")
			menu = pickle.load(archivo)
			archivo.close()
			print("###########################")
			print("Menú cargado:", menu)
			print("###########################")
		except:
			print("###########################")
			print("No se pudo cargar el archivo binario.")
			print("###########################")

	## OPCIÓN 5: SALIR ##
	elif opcion == 5:
		print("Saliendo del programa.")
		break

	else:
		print("###########################")
		print("Opción no válida.")
		print("###########################")

```

---

**NOTAS:**
- Al momento de usar el bucle `while` hay que controlarlo ya que de no hacerlo el programa va a ser un bucle sin fin.
- Usando la libreria `pickle` podemos guardar información en un archivo binario y luego mostrar la información.

