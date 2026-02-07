En este ejercicio vamos a crear un programa que calcule cuantas cuadras necesitas para la cantidad de caballos que le indique el usuario teniendo en cuenta que entran 3 caballos por cada cuadra.

---

Para realizar este ejercicio primero debemos importar la funcion `ceil` de la libreia `math`
```
	from math import ceil
```
Luego definimos las variables y le pedimos al usuario que introduzca los valores:
```
	numero_caballos = int(input("Introduce el número de caballos que tiene Carlos: "))
	jugos_movil = int(input("Introduce el número de juegos de móvil que jugó Carlos: "))
```
Despues realizamos los calculos:
```
	cuadras = numero_caballos / 3
	redondeoalza = ceil(cuadras)
```
Y por ultimo le mostramos al usuario la información:
```
	print("-------------------------------------------")
	print("Carlos tiene", numero_caballos, "caballos.")
	print("Jugó", jugos_movil, "juegos de móvil.")
	print("Necesita", redondeoalza, "cuadras.")
	print("-------------------------------------------")
```

---

A continuación el codigo completo:
```
	'''
	   calculadora de cuadras
	   v0.1 (c) valentin
	   programa que calcula numero de cuadras a partir de los caballos
	'''
	from math import ceil

	## DEFINIMOS LAS VARIABLES Y LE PEDIMOS AL USUARIO QUE LE ASIGNE LOS VALORES ##
	numero_caballos = int(input("Introduce el número de caballos que tiene Carlos: "))
	jugos_movil = int(input("Introduce el número de juegos de móvil que jugó Carlos: "))

	## CÁLCULAMOS ##
	cuadras = numero_caballos / 3
	redondeoalza = matematicas.ceil(cuadras)

	## MOSTRAMOS LA INFORMACIÓN ##
	print("-------------------------------------------")
	print("Carlos tiene", numero_caballos, "caballos.")
	print("Jugó", jugos_movil, "juegos de móvil.")
	print("Necesita", redondeoalza, "cuadras.")
	print("-------------------------------------------")
```

---

**NOTAS:**
- La función `input()` permite obtener datos del usuario.  
