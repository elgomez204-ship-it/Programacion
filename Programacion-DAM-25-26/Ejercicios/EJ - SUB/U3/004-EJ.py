'''
    Calculador de puntos por partido
    v0.1 Valentin Antonio De Gennaro
    Divide los puntos entre los partidos jugados
'''

puntos_rugby = 0
partidos_jugados = 0
puntos_rugby = int(input("Introduce tus puntos: "))
partidos_jugados = int(input("Introduce la cantidad de partidos jugados: "))

try:
    puntosporpartido = puntos_rugby/partidos_jugados
    print("El total de puntos por partido es: ",puntosporpartido)
except:
    print("ERROR")
    print("El programa continua en funcionamiento")

