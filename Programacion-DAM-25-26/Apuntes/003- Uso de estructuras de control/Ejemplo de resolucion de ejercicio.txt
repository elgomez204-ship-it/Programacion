En este ejercicio vamos a desarrollar un ejemplo de cambio de tipo de datos, el cual nos va a permitir introducir el nombre de un juego y la puntuación del mismo y nos diga el doble de la misma, mediante variables.

Para resolver este ejercicio, primero vamos a declarar una serie de variables que contendrán la información.
'''
nombre_del_juego = 0
puntuación = 0
'''

Luego vamos a pedirle al usuario que nos indique cual es su juego favorito y cual es la puntuación del mismo en formato entero.
```
nombre_del_juego = input("Introduce el nombre de tu juego favorito: ")
puntuación = int(input("introduce la puntuación: "))
```

Luego mediante un operador aritmético se va a multiplicar esa puntuación.
```
doble_de_la_puntuación = puntuación * 2
```

Y por ultimo se va a mostrar en pantalla el nombre del juego y el doble de su puntuación.
```
print("Tu juego favorito es", nombre_del_juego, "Y el doble de su puntuación es", doble_de_la_puntuación)
```

A continuación podemos ver un programa informático completo que trabaja el concepto de cambo de tipo de datos.
```
'''
   Calculador de puntuación de videojuegos
   v0.1 Valentín de Gennaro
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

```

Notas:
-Tener cuidado con el cierre de todos los paréntesis que se abren ya que si no se cierra uno el código no funciona

Trabajar con int nos permite convertir el valor introducido en un numero entero haciendo todo mas simplificado.
