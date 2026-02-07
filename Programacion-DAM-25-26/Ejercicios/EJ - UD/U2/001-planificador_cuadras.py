'''
	Calculador de cuadras
	v0.1 Valentin Antonio De Gennaro
	Calcula los caballos que entran por cuadra y la fecha
'''

from math import ceil
import datetime as fechas

########## ENTRADA DE LA INFORMACIÓN ##########
caballos = int(input("Introduce el número de caballos: "))
if caballos >= 0:
	capacidad_de_cuadra = int(input("Introduce el numero de caballos por cuadra: "))
	if capacidad_de_cuadra >= 0:
		anio = int(input("Introduce el año: "))
		mes = int(input("Introduce el mes: "))
		dia = int(input("Introduce el día: "))
		hoy = fechas.date(anio, mes, dia)
		semana = hoy.weekday()
		diadelasemana = hoy.isoweekday()

########## CALCULAMOS ##########
		cuadras_necesarias = ceil(caballos / capacidad_de_cuadra)

########## MOSTRAMOS LA INFORMACIÓN ##########
		print("----------------------------------------------------")
		print("Tienes",caballos,"caballos")
		print("Te caben",capacidad_de_cuadra,"caballos por cuadra")
		print("Necesitas",cuadras_necesarias,"cuadras")
		print("-----------------Datos de la fecha------------------")
		print(hoy)
		print(hoy.year)
		print(hoy.month)
		print(hoy.day)
		print(semana)
		print(diadelasemana)
		print("----------------------------------------------------")
		
	else:
		print("ERROR - El valor no puede ser menor a cero")


else:
		print("ERROR - El valor no puede ser menor a cero")
