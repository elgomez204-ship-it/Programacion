En este ejercicio vamos a calcular la raiz de un numero, y luego lo vamos a redondear. En el rugby se puede usar para calcular los puntos totales de un torneo
En este ejercicio vamos a utilizar la funciòn `sqrt` de la libreria `math`, se importa de la siguiente manera:
```
from math import sqrt
```
luego de eso tenemos que definir la varaible y asiganrle un literal, que va a ser el nùmero que usaremos para calcular la raiz.
```
puntuacion_total = 1569
```
ahora empieza la parte de calcular, empezamos por la raiz
```
resultado = sqrt(puntuacion_total)
```
luego tenemos que redondear ese resultado
```
redondeo = round(resultado)
```
y como parte final hay que mostrarle al usuario el resultado final
```
print("El resultado final es:",redondeo)
```
A continuación el codigo completo:
```
	'''
		Calculos matematicos
		v0.1 Valentin Antonio De Gennaro
	'''

	## Importamos la funcion sqrt (raiz) de la libreria math ##

	from math import sqrt

	## Defino la variable

	puntuacion_total = input("Introduce la puntuación total: ")

	## Calculo la raiz ##

	resultado = sqrt(puntuacion_total)

	## Redondeo el resultado ##

	redondeo = round(resultado)

	## Muestro el resultado ##

	print("El resultado redondeado es:",redondeo)
```
**NOTAS:**
- El uso de la libreria `math` es necesario para poder realizar calculo de raiz cuadrada, que en este caso se hace haciendo uso de la función `sqrt`

