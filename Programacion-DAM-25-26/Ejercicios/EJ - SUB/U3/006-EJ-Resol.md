En este ejercicio vamos a introducir reglas dentro de una funcion en este caso, es una funcion de raiz cuadrada y dentro de esa funcion vamos a utilizar el `try` y el `except` para capturar errores.
Para realizar este ejercicio primero debemos definir la función como se puede ver a continuacion:
```
	def raizSegura(numero):
```
Luego debemos importar la libreria:
```
	from math import sqrt
```
Despues de eso comenzamos a introducirle las reglas a la función utilizando `if`, `else` y `return`, como se puede ver a continuacion:
```
	if isinstance(numero, (int, float)):
		if numero >= 0:
			raiz = sqrt(numero)
			return raiz
		else:
			return 0
```
luego debemos pedirle al usuario que introduzca el numero a calcular:
```
	numero = int(input("Introduce el numero: "))
```
Y por ultimo usando un `print` le mostramos al usuario el resultado:
```
	print(raizSegura(numero))
```
A continuación el codigo completo:
```
	def raizSegura(numero):
		'''
			Función que calcula la raíz cuadrada de un número dado.
			Entradas: numero (int, float o str) que se espera que sea numérico
			Salidas: resultado de la raíz cuadrada como float (o cero si hay fallo)
			Capturas de error:
			  1.- Si es numérico
			  2.- Si se puede convertir a número
			  3.- Si no es un número positivo
		'''
		from math import sqrt

		if isinstance(numero, (int, float)):
			if numero >= 0:
				raiz = sqrt(numero)
				return raiz
			else:
				return 0
		
		else:
			try:
				numero = float(numero)
				entero_raiz = sqrt(numero)
				return entero_raiz
			except:
				return 0

	numero = int(input("Introduce el numero: "))

	print(raizSegura(numero))
```
**NOTAS:**
- Si le decimos al programa que devuelva cero cuando se cumple una condición, no podemos agregarle un `assert` ya que de hacerlo arrojaria el error y no el 0
- Es de buenas practicas incluir un docstring detallando que hace el programa

