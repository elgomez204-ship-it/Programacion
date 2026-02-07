'''
   calculadora de cuadras
   v0.1 (c) valentin
   programa que calcula numero de cuadras a partir de los caballos
'''

import math as matematicas

#datos de inicio
caballos = 0
cuadras = 0
caballos_por_cuadra = 0

#entrada de la información
caballos_por_cuadra =int(input("introduce el numero de caballos por cuadra: "))
caballos = int(input("introduce el numero de caballos: "))

#realización de cálculos
cuadras = caballos / 3
redondeoalza = matematicas.ceil(cuadras)

#salida de resultados
print("si tienes",caballos,"caballos")
print("y te caben",caballos_por_cuadra,"caballos por cuadra")
print("en ese caso necesitas",redondeoalza,"cuadras")


