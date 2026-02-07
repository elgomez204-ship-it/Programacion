'''
   Calculador de puntuación de videojuegos
   v0.1 Valentin de Gennaro
   Este programa calcula la puntuación de tu juego favorito
'''
   

#Datos del inicio
nombre_del_juego = 0
puntuación = 0

#Entrada de datos
nombre_del_juego = input("Introduce el nombre de tu juego favorito: ")
puntuación = int(input("introduce la puntuación: "))

#Cálculos
doble_de_la_puntuación = puntuación * 2

#Salida de los resultados
print("Tu juego favorito es", nombre_del_juego, "Y el doble de su puntuación es", doble_de_la_puntuación)



