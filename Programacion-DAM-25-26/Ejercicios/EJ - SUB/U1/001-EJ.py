'''
	Información de juegos
	v0.1 Valentin Antonio De Gennaro
	
'''

## DEFINO VARIABLES Y LES ASIGNO VALOR ##
jugados_rugby = int(input("Introdcuce el numero de partidos jugados: "))
victorias_rugby = int(input("Introduce el numero de victorias: "))

## CREO UNA LISTA VACIA ##
juegos_movil = []

## PIDO LOS DATOS AL USUARIO Y LOS AÑADO A LA LISTA ##
juego1 = input("Introduce primer juego favorito: ")
juegos_movil.append(juego1)
juego2 = input("Introduce tu segundo juego favorito: ")
juegos_movil.append(juego2)
juego3 = input("Introduce tu tercer juego favorito: ")
juegos_movil.append(juego3)

## MUESTRO INFORMACIÓN AL USUARIO ##
print("#######################################")
print("Jugaste ",jugados_rugby,"partidos en total")
print("Ganaste ",victorias_rugby,"partidos en total")
print("---------------------------------------")

## MUESTRO INFORMACIÓN AL USUARIO ##
for juego in juegos_movil:
	print("Uno de tus juegos favoritos es: ",juego)
	print("---------------------------------------")
