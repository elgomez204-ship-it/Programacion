import pickle
agenda = []

while True:
	print("Selecciona una opcione: ")
	print("1.-Introducir un registro")
	print("2.-Leer registros")
	print("3.-Guardar registros")
	print("4.-Eliminar un registro")
	print("5.-Salir")
	opcion = int(input("Elige una opcion: "))
	
	if opcion == 1:	
	## INSERTAR ##
		nombre = input("Dime tu nombre: ")
		apellidos = input("Dime tus apellidos: ")
		email = input("Dime tu email: ")
		telefono = input("Dime tu telefono: ")
		## AÑADO LOS DATOS A LA AGENDA ##
		agenda.append([nombre,apellidos,email,telefono])
		
	elif opcion == 2:
	## IMPRIMIR ##
		print(agenda)
	
	elif opcion == 3:
	## GUARDAR ##
		archivo = open("agenda.bin","wb")
		pickle.dump(agenda,archivo)
		archivo.close()
		
	elif opcion == 4:
	## ELIMINAR ##
		eliminar = input("Introduce el nombre del registro a eliminar: ")
		agenda.pop(eliminar)
		print("Eliminado Correctamente")
	
	elif opcion == 5:
	## SALIR ##
		print("Saliendo...")
		break
		
