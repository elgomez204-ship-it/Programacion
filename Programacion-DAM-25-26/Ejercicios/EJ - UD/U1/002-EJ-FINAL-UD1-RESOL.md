En este ejercicio vamos a desarrollar una aplicación para generar facturas con IVA haciendo uso de operadores de comparación y variables booleanas. Son herramientas utiles a la hora de desarrollar un codigo.
Para desarrollar este codigo primero debemos definir las variables y asignarles un literal, el cual se lo vamos a pedir al usuario, como se puede ver a continuación:
```
	nombre_cliente = input("Introduce el nombre del cliente: ")
	precio_bruto = float(input("Introduce el precio bruto del producto: "))
```
Despues para poder calcular el IVA primero tenemos que declararlo:
```
	IVA = 0.21
```
Despues hay que definir el descuento que se va a aplicar con una constante:
```
	DESCUENTO = 10
```
Luego vamos a definir cuando se aplica ese descuento:
```
	aplica_descuento = precio_bruto >= 50
	con_descuento = aplica_descuento
```
Luego mediante variables booleanas aplicamo el descuento en el caso que corresponda:
```
	if con_descuento:
		total = subtotal_con_iva - DESCUENTO
		aplica_descuento == True
		
	else:
		aplica_descuento == False
```
Y por ultimo le mostramos al usuario la factura con el desglose del total:
```
	if aplica_descuento == True:
		print("-------------------------------")
		print("Nombre: ",nombre_cliente)
		print("-------------------------------")
		print("Precio Bruto:                 |", precio_bruto,"€")
		print("IVA:                          |", iva_aplicado,"€")
		print("Descuento:                    |", DESCUENTO,"€")
		print("Total:                        |", total,"€")
		print("-------------------------------")
```
A continuación el codigo completo:
```
	'''
		Generador de facturas con IVA
		v0.1 Valentin Antonio De Gennaro
		Genera una factura con datos que le pide al usuario y desglosa el total
	'''

	#### DEFINO VARIABLES Y LE PIDO LOS DATOS AL USUARIO #####
	nombre_cliente = input("Introduce el nombre del cliente: ")
	precio_bruto = float(input("Introduce el precio bruto del producto: "))
	IVA = 0.21    #21% del iva
	DESCUENTO = 10

	########## DEFINO CUANDO APLICA EL DESCUENTO #######
	aplica_descuento = precio_bruto >= 50
	con_descuento = aplica_descuento

	################# HAGO CALCULOS ####################
	iva_aplicado = precio_bruto * IVA
	subtotal_con_iva = precio_bruto + iva_aplicado

	############### APLICO EL DESCUENTO #################
	if con_descuento:
		total = subtotal_con_iva - DESCUENTO
		aplica_descuento == True
		
	else:
		aplica_descuento == False
		
	####### LE MUESTRO LA INFORMACIÓN AL USUARIO ##########
	if aplica_descuento == True:
		print("-------------------------------")
		print("Nombre: ",nombre_cliente)
		print("-------------------------------")
		print("Precio Bruto:                 |", precio_bruto,"€")
		print("IVA:                          |", iva_aplicado,"€")
		print("Descuento:                    |", DESCUENTO,"€")
		print("Total:                        |", total,"€")
		print("-------------------------------")

	else:
		print("-------------------------------")
		print("Nombre: ",nombre_cliente)
		print("-------------------------------")
		print("Precio Bruto:                 |", precio_bruto,"€")
		print("IVA:                          |", iva_aplicado,"€")
		print("Descuento:                    |", 0,"€")
		print("Total:                        |", subtotal_con_iva,"€")
		print("-------------------------------")
```
**NOTAS:**
- En python no hay constantes pero se escriben en mayusculas igual para definirlas
