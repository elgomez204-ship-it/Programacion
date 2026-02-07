'''
	Lista de jugadores de rugby
	v0.1 Valentín Antonio De Gennaro
'''

## CREO UNA LISTA Y LE AÑADO 3 NOMBRES ##
jugadores = ["Antoine Dupont", "Beauden Barrett", "Cheslin Kolbe"]

## AÑADO OTRO NOMBRE A LA LISTA ##
jugadores.append("Maro Itoje")

## MUESTRO LOS JUGADORES DE LA LISTA ##
print("Lista inicial de jugadores:")
for jugador in jugadores:
	print(jugadores)
	
## ELIMINO A UN JUGADOR DE LA LISTA ##
jugador_eliminado = jugadores.pop(1)
print("Jugador eliminado: ",jugador_eliminado)

## MODIFICAMOS EL NOMBRE DE UN JUGADOR ##
indice_a_modificar = 0
jugadores[indice_a_modificar] = "Jonathan Sexton"

## MOSTRAMOS LA LISTA ACTUALIZADA ##
print("Lista actualizada de jugadores:")
for jugador in jugadores:
	print(jugadores)

