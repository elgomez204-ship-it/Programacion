'''
	Calculadora de tamaño de carpeta
	v0.1 Valentín Antonio De Gennaro
	Programa que calcula el tamaño total de una carpeta en MB.
'''

import os

ruta = input("Introduce la ruta de la carpeta: ")
tamaño_total = 0

for carpeta, subcarpetas, archivos in os.walk(ruta):
	for archivo in archivos:
		ruta_completa = os.path.join(carpeta, archivo)
		tamaño_total += os.path.getsize(ruta_completa)

print("El tamaño total de la carpeta es:", tamaño_total / 1048576, "MB")

