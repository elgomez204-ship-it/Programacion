'''
	Información de partidos
	v0.1 Valentin Antonio De Gennaro
	Te da información acerca de jugadores.
'''

class Jugador():
	def __init__(self,nombre,edad,equipo):
		self.nombre = nombre
		self.edad = edad
		self.equipo = equipo
	def jugar_rugby (self):
		print(self.nombre, "del equipo",self.equipo, "esta jugando al rugby")


jugador1 = Jugador("Messi",38,"Inter de Miami")

jugador1.jugar_rugby()
