'''
	Detectar errores
	v0.1 Valentìn Antonio De Gennaro
'''

edad_jugador = int(input("Introduce la edad del jugador de rugby: "))

try:
	assert edad_jugador == 21, "La edad no es correcta"
except:
	print("La edad del jugador es incorrecta")
	
estado_juego = input("¿Haz terminado tu juego diario?: ")

try:
	assert estado_juego == "si", "Muy mal"
except:
	print("Muy mal no has terminado tu juego diario")
	


