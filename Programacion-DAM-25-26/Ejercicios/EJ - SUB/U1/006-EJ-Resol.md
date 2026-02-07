En este ejercicio se realizó una calculadora de impuestos, que puede ser utilizada para calcular el IVA de la venta de entradas de un partido de rugby.
Para realizar este código primero vamos a declarar las variables:
```
base_imponible = 0
total_iva = 0
total_factura = 0
```
Luego en pantalla se va a mostrar la información del programa usando la función `print`:
```
print("programa calculadora de impuestos")
print("(c) 2025 Jose Vicente Carratalá")
print("introduce una base y te calculo el iva y el total")
```
Seguido de eso el programa va a pedirte que introduzcas la base imponible mediante `input`:
```
base_imponible = float(input("introduce la base imponible de la factura: "))
```
Luego de introducir la base imponible el programa lo que va a hacer es calcular el IVA y el total de la factura mediante operadores aritméticos `*`:
```
total_iva = base_imponible*0.21
total_factura = base_imponible + total_iva
```
Y como acción final te va a mostrar por pantalla el total del IVA y el total de la factura usando `print`:
```
print(" El total del IVA es: ",total_iva)
print(" El total de la factura es: ",total_factura)
```
A continuación podemos ver el código completo:
```
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
```
**Nota:**
- He aplicado lo aprendido en clase, ya que en clase vimos los operadores aritméticos, la función `print` y `input`.
