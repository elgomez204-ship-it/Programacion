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
	aplica_descuento = True
	
else:
	aplica_descuento = False
	
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

	

	
	
