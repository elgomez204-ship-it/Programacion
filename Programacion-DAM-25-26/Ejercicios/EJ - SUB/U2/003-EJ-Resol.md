En el ejercicio a continuacion vamos a realizar el redondeo para arriba de un numero que le asignemos usando la libreria math.
Para relizar este ejercicio primero debemos importar el metodo `ceil` de la libreria math:
```
	from math import ceil
```
luego definimos la variable y le asignamos un valor literal
```
	numero = 150.8
```
Luego redondemos:
```
	redondeo = ceil(numero)
```
Y por ultimo le mostramos al usuario la informacion:
```
	print(redondeo)
```
A continuación el codigo completo:
```
	'''
		Redondeo de números decimales
		v0.1 Valentin Antonio De Gennaro
		El programa redondea para arriba el numero que se definio
	'''
	## IMPORTAMOS LA LIBRERIA ##
	from math import ceil

	## DEFINIMOS LA VARIABLE Y LE ASIGNAMOS UN VALOR DECIMAL ##
	numero = 150.8

	## REDONDEAMOS EL NUMERO ##
	redondeo = ceil(numero)

	## MOSTRAMOS LA INFORMACION AL USUARIO ##
	print(redondeo)
```
**NOTAS:**
- El uso de las librerias simpre ayuda, en este caso nos ayuda a redondear un numero decimal

