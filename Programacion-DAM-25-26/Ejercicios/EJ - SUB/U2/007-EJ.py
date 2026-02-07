'''
   calculadora de cuadras
   v0.1 (c) valentin
   programa que calcula numero de cuadras a partir de los caballos
'''
from math import ceil

## DEFINIMOS LAS VARIABLES Y LE PEDIMOS AL USUARIO QUE LE ASIGNE LOS VALORES ##
numero_caballos = int(input("Introduce el número de caballos que tiene Carlos: "))
jugos_movil = int(input("Introduce el número de juegos de móvil que jugó Carlos: "))

## CÁLCULAMOS ##
cuadras = numero_caballos / 3
redondeoalza = ceil(cuadras)

## MOSTRAMOS LA INFORMACIÓN ##
print("-------------------------------------------")
print("Carlos tiene", numero_caballos, "caballos.")
print("Jugó", jugos_movil, "juegos de móvil.")
print("Necesita", redondeoalza, "cuadras.")
print("-------------------------------------------")
