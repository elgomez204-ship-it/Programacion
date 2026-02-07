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

