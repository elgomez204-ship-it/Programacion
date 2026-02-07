En este ejercicio usando la libreria `math` vamos a relizar dos calculos, la raiz de un numero, y el seno y coseno de los grados de un angulo.
Lo primero que hay que hacer en esta aplicación es importar la libreria, a continuación un ejemplo:
```
	import math
```
Luego vamos a definir la variable y asigarle un valor para calcular la raiz:
```
	numero = 100
```
Despues calculamos la raiz:
```
	raiz = math.sqrt(numero)
```
Luego defino la variable y le asigno un valor para calcular el seno y el coseno:
```
	angulo_grados = 90
```
Y calculamos:
```
seno = math.sin(angulo_radianes)
coseno = math.cos(angulo_radianes)
```
Y por ultimo le mustro la información al usuario:
```
print("La raiz cuadrada de ",numero," es: ",raiz)
print("El seno de ",(angulo_grados)," grados es: ",seno)
print("El coseno de ",(angulo_grados)," grados es: ",coseno)

```
A continuación el codigo completo:
```
	'''
		Calcular la raiz, el seno y el coseno
		v0.1 Valentin Antonio De Gennaro
		Este programa calcula la raiz de un numero, y el coseno y el seno de los grados de un angulo
	'''
	## IMPORTAMOS LA LIBRERIA ##
	import math

	## DEFINO EL NUMERO ##
	numero = 100

	## CALCULO LA RAIZ DE ESE NUMERO##
	raiz = math.sqrt(numero)

	## DEFINO EL ANGULO EN GRADOS ##
	angulo_grados = 90

	## CONVIERTO EL ANGULO DE GRADOS A RADIANES ##
	angulo_radianes = math.radians(angulo_grados)

	## CALCULO EL SENO Y EL COSENO ##
	seno = math.sin(angulo_radianes)
	coseno = math.cos(angulo_radianes)

	## MUESTRO LA INFORMACIÓN AL USUARIO ##
	print("La raiz cuadrada de ",numero," es: ",raiz)
	print("El seno de ",angulo_grados," grados es: ",seno)
	print("El coseno de ",angulo_grados," grados es: ",coseno)
```
**NOTAS:**
- Al momento de usar la libreria math hay que recordar utilizar la funcion usando el math. y la función.

