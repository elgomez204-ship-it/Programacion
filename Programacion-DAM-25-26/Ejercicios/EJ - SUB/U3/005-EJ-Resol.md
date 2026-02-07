En este ejercico vamos a hacer uso de las aserciones que son utiles para detectar errores. E integrado mis hobbies haciendo que el usuario deba introducir la edad del jugador de rugby y el `assert` se encargue de detectar si la edad es incorrecta ya que la correcta es **21**, y luego hice algo similar pero mi juego diario del movil haciendo que el usuario indique si ha finalizado el juego o no.
En este codigo hacemos uso de el `assert` como se puede ver a continuación:
```
assert edad_jugador == 21, "La edad no es correcta"
```
Pero a la hora de usar el `assert` no hay que olvidarse de hacer uso del `try` y el `except` ya que de no usarlo el codigo va a dar error, a continuación se puede ver la forma correcta:
```
try:
	assert edad_jugador == 21, "La edad no es correcta"
except:
	print("La edad del jugador es incorrecta")
```
Ahora se puede ver el codigo completo:
```
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
```
**NOTAS:**
- No hay que olviadar usar el `try` y el `except`.

El uso de `assert` es necesario a la hora de programar ya que es util para detectar errores.

