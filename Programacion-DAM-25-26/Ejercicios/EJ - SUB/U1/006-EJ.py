'''
  Calculadora de Impuestos
  v0.1 por Valentìn Antonio De Gennaro
  funcionamiento : introduce una base imponible y se calcula IVA y total
'''
             
############# VARIABLES ########################
base_imponible = 0
total_iva = 0
total_factura = 0

############## ENTRADA DE DATOS ################
print("programa calculadora de impuestos")
print("(c) 2025 Jose Vicente Carratalá")
print("introduce una base y te calculo el iva y el total")
base_imponible = float(input("introduce la base imponible de la factura: "))

############# CALCULOS #########################
total_iva = base_imponible*0.21
total_factura = base_imponible + total_iva

############## SALIDA ##########################
print(" El total del IVA es: ",total_iva)
print(" El total de la factura es: ",total_factura)
