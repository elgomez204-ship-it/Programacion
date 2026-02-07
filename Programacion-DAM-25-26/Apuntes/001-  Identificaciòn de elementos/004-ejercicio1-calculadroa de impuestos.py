'''
  Calculadora de Impuestos
  v0.1 por valentin
  funcionamiento : introduce una base imponible y se calcula IVA y total
'''


# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# aqui pondria las funciones/clases

#ahora calculamos

#primero pido una entrada
print("programa calculadora de impuestos")
print("(c) 2025 valentin")
print("introduce una base y te calculo el iva y el total")
base_imponible = float(input("introduce la base imponible de la factura: "))

#luego realizo calculos
total_iva = base_imponible*0.21
total_factura = base_imponible + total_iva

#por ultimo expreso una salida
print(" el IVA de la factura es: ",total_iva)
print(" el total de la factura es: ",total_factura)


