'''
	Información del equipo
	v0.1 Valentin Antonio De Gennaro
	Te muestra información de un equipo y sus jugadores.
'''

class Equipo():
	def __init__(self, nombre, jugadores):
		self.nombre = nombre
		self.jugadores = jugadores

	def mostrar_equipo(self):
		print("Nombre del equipo:", self.nombre)
		print("Lista de jugadores:")
		for jugador in self.jugadores:
			print("-", jugador)


## CREAMOS UN OBJETO DE TIPO EQUIPO ##
equipo1 = Equipo("Los Pumas", ["Valentín", "Franco", "Lucas", "Martín", "Joaquín"])

## MOSTRAMOS LA INFORMACIÓN DEL EQUIPO ##
equipo1.mostrar_equipo()
