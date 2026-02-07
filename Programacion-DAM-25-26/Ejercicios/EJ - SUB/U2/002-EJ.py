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
print("El seno de ",(angulo_grados)," grados es: ",seno)
print("El coseno de ",(angulo_grados)," grados es: ",coseno)



