'''

	Menú de restaurante
	
'''
## IMPORTAMOS LA LIBRERIA ##
import pickle
## CREAMOS LA LISTA VACIA ##
menu = []
## EMPEZAMOS EL BUCLE ##
while True:
	print("Opciones: ")
	print("1.-Introducir nueva comida en el menu")
	print("2.-Listar comidas en el menu")
	print("3.-Guardar en archivo")
	opcion = int(input("Elige una opcion: "))
## DESARROLLO LA OPCIÓN 1 ##
	if opcion == 1:
		comida = input("Introduce el nombre de la comida: ")
		menu.append(comida)
## DESARROLLO LA OPCIÓN 2 ##	
	elif opcion == 2:
		print("Tu comida hasta el momento es: ")
		for elemento in menu:
			print(elemento)
## DESARROLLO LA OPCIÓN 3 ##
	elif opcion == 3:
		archivo = open("restaurante.bin","wb")  ## WRITE BINARY ##
		pickle.dump(menu,archivo)
		archivo.close()
		print("Información guardada correctamente ✅")
