En este ejercicio mediante variables vamos a realizar un registro de los puntos que llevas en rugby.
Las variables se utilizan para almacenar la información y como el nombre lo indica esta informacion puede variar.
Este codigo utiliza variables para definir un valor utilizando un operador de asignacion `=` seguido del valor literal que le asignamos a la variable.
Un ejemplo de asignar valor a una variable: 
```
puntos_rugby = 0
```
Y para mostrar mejor esto voy a mostrarte un codigo el cual mediante un `input` se le pide al usuario que me diga los puntos que anotó y la aplicacion va incrementar por 3 ese valor para calcular los puntos totales que tienes.
```
'''
    Registro puntos en rugby
    v0.1 Valentín Antonio de Gennaro
    Lleva el registro de los puntos anotados
'''

######## Declaro variables ########
puntos_rugby = 0

####### Entrada de información #########
puntos_rugby = int(input("Cuantos puntos has anotado: "))

####### Incremento los puntos #####
puntos_rugby *= 3

###### Devuelvo los datos #########
print("tienes:", puntos_rugby, "puntos totales")
```

**Nota:** 
- Tener cuidado con el cierre de parentesis, se deben cerrar todos los que se abran para que todo funcione.

Trabajar con int nos permite convertir el valor introducido en un numero entero haciendo todo mas simplificado.