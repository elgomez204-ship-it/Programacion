'''
	Calculos matematicos
	v0.1 Valentin Antonio De Gennaro
'''

## Importamos la funcion sqrt (raiz) de la libreria math ##

from math import sqrt

## Defino la variable

puntuacion_total = input("Introduce la puntuación total: ")

## Calculo la raiz ##

resultado = sqrt(puntuacion_total)

## Redondeo el resultado ##

redondeo = round(resultado)

## Muestro el resultado ##

print("El resultado redondeado es:",redondeo)

