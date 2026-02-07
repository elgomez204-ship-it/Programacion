print("Agenda deportiva v0.1")
import json 								# Para usar la libreria debo importarlo

agenda_deportiva = []

while True:
	print("Selecciona una opción")
	print("1.-Añadir un evento")
	print("2.-Mostrar los eventos")
	print("3.-Salir")
	opcion = int(input("Tu opción: "))
	
	if opcion == 1:
		print("Añadimos un evento a la agenda")
		deporte = input("Indica el deporte del evento: ")
		nombre = input("Indica el nombre del evento: ")
		fecha = input("Indica la fecha del evento: ")
		descripcion = input("Indica una breve descripción del evento: ")
		agenda_deportiva.append({'deporte':deporte,'nombre':nombre,'fecha':fecha,'descripcion':descripcion})
		archivo = open("agenda.json","w") 				# Abro un archivo
		json.dump(agenda_deportiva,archivo)				# Guardo en Json
		archivo.close()									# Cierro el archivo
		
	elif opcion == 2:
		print("##### Lista de eventos ######")
		for evento in agenda_deportiva:
			print("")
			print("Deporte:",evento['deporte'])
			print("Nombre:",evento['nombre'])
			print("Fecha:",evento['fecha'])
			print("Descripción:",evento['descripcion'])
			print("##############################")
	
	elif opcion == 3:
		print("Saliendo ...")
		break


