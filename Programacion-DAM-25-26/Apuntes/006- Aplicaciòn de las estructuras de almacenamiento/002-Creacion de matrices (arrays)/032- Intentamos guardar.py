'''

	Menú de restaurante
	
'''
import pickle

menu = []

while True:
	print("Opciones: ")
	print("1.-Introducir nueva comida en el menu")
	print("2.-Listar comidas en el menu")
	print("3.-Guardar en archivo")
	opcion = int(input("Elige una opcion: "))
	
	if opcion == 1:
		comida = input("Introduce el nombre de la comida: ")
		menu.append(comida)
		
	elif opcion == 2:
		print("Tu comida hasta el momento es: ")
		for elemento in menu:
			print(elemento)
	
	elif opcion == 3:
		archivo = open("restaurante.txt","w")
		archivo.write(menu)
		archivo.close
