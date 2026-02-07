'''
	Generador de ticket
	v0.1 Valentin Antonio De Gennaro
	A partir de datos solicitados genera un ticket
'''

############### DECLARAMOS LAS VARIABLES ################

nombre_cliente = input("Introduce el nombre del cliente: ")
edad = int(input("Introduce tu edad: "))

if edad <= 0:
	print("Edad invalida")
else:
	base_imponible = float(input("Introduce la base imponible de la factura: "))
	if base_imponible <= 0:
		print("Error")
	else: 

################## DECLARAMOS EL IVA ####################

		IVA = 0.21  # Es el 21%
		if edad < 18:
			print("No disponible para menores de 18")
			
################### CALCULAMOS #########################

		else:
			if base_imponible < 100:
				porcentaje_descuento = 0
				descuento = 0
				importe_descuento = base_imponible * descuento
				base_tras_descuento = base_imponible - importe_descuento
				importe_iva = base_tras_descuento * IVA
				total_factura = base_tras_descuento + importe_iva
			elif base_imponible >= 100 and base_imponible <=199.99:
				porcentaje_descuento = 5
				descuento = 0.05
				importe_descuento = base_imponible * descuento
				base_tras_descuento = base_imponible - importe_descuento
				importe_iva = base_tras_descuento * IVA
				total_factura = base_tras_descuento + importe_iva
			else:
				porcentaje_descuento = 10
				descuento = 0.1
				importe_descuento = base_imponible * descuento
				base_tras_descuento = base_imponible - importe_descuento
				importe_iva = base_tras_descuento * IVA
				total_factura = base_tras_descuento + importe_iva

################# GENERAMOS EL TICKET ###################

			print("--------------------")
			print("Generador de tickets")
			print("Valentin Antonio De Gennaro")
			print("v0.1-(c)-2025")
			print("--------------------")
			print("Nombre: ",nombre_cliente)
			print("Edad: ",edad)
			print("--------------------")
			print("Base imponible: ", base_imponible,"€")
			print("Porcentaje descuento: ",porcentaje_descuento,"%")
			print("Importe descuento: ", importe_descuento,"€")
			print("Base tras descuento: ", base_tras_descuento,"€")
			print("IVA: ", importe_iva,"€")
			print("Total de la factura: ", total_factura,"€")
			print("--------------------")
