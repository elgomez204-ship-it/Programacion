'''
	Estadísticas de Rugby
	v0.1 Valentin Antonio De Gennaro
	Calcula puntos y promedio de puntos en partidos de rugby.
'''

## CREAMOS LA CLASE ##
class RugbyStats:

## CREAMOS UN METODO ESTATICO ##
	@staticmethod
	def calcularPuntosTotales(tesoros, penalizaciones):
		puntosTotales = (tesoros * 5) - (penalizaciones * 2)
		return puntosTotales

## CREAMOS OTRO METODO ESTATICO ##
	@staticmethod
	def calcularPromedioPuntos(listaPuntos):
		total = sum(listaPuntos)
		promedio = total / len(listaPuntos)
		return promedio

## CREMOS LOS PARTIDOS Y CALCULAMOS SUS PUNTOS ##

puntosPartido1 = RugbyStats.calcularPuntosTotales(6, 1)
puntosPartido2 = RugbyStats.calcularPuntosTotales(3, 0)
puntosPartido3 = RugbyStats.calcularPuntosTotales(5, 2)

## GUARDAMOS LOS PUNTOS EN UNA LISTA ##
listaPuntos = [puntosPartido1, puntosPartido2, puntosPartido3]

## CALCULAMOS EL PROMEDIO DE LOS PUNTOS ##
promedio = RugbyStats.calcularPromedioPuntos(listaPuntos)

## MOSTRAMOS RESULTADOS ##
print("Puntos obtenidos en cada partida:", listaPuntos)
print("Promedio de puntos:", promedio)

