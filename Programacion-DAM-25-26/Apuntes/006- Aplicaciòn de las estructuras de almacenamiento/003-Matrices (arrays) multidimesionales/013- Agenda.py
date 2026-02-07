agenda = []

while True:
	nombre = input("Dime tu nombre: ")
	apellidos = input("Dime tus apellidos: ")
	email = input("Dime tu email: ")
	telefono = input("Dime tu telefono: ")
	## AÑADO LOS DATOS A LA AGENDA ##
	agenda.append([nombre,apellidos,email,telefono])
	print(agenda)
