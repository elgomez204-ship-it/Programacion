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
