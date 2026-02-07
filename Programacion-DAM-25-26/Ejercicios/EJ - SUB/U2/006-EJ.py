'''
	Información de partido de rugby
	v0.1 Valentín Antonio De Gennaro
	Muestra información sobre un partido.
'''
## IMPORTAMOS LA LIBRERIA DATETIME ##
from datetime import datetime				

## DEFINIMOS LA CLASE PARTIDORUGBY ##
class PartidoRugby():
	def __init__(self, nombre_equipo, fecha_partido):
		self.nombre_equipo = nombre_equipo
		self.fecha_partido = fecha_partido

## CREAMOS UN PARTIDO Y LE AGREGAMOS INFORMACIÓN ##
partido = PartidoRugby("Los Pumas", datetime.now())

## MOSTRAMOS LA INFORMACIÓN ##
print("-------------------------------------------")
print("Nombre del equipo:", partido.nombre_equipo)
print("Fecha del partido:", partido.fecha_partido.strftime("%Y-%m-%d"))
print("Día de la semana:", partido.fecha_partido.weekday())
print("-------------------------------------------")
