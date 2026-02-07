En el ejercicio a continuación se visualiza una aplicación que puede ser utilizada para calcular la duración de los partidos o torneos, o las calorías quemadas durante ese partido.
Mediante un operador aritmético `*` se puede calcular diferentes valores y luego mediante la función `print`se puede mostrar por pantalla la información. Un ejemplo en código: 
```
'''
    Realizar cálculos matemáticos
    v0.1 Valentín Antonio de Gennaro
'''

################ 1 ########################

dias_torneo = 3

horas = dias_torneo * 24
print("El torneo de rugby duró:", horas, "horas")

########### 2 ############################

horas = 10

minutos = horas * 60
print("10 horas son:",minutos, "minutos")

########### 3 ###########################

hora = 2
calorias = 500

calorias_quemadas = calorias * hora
print("En total quemaste:", calorias_quemadas, "calorías")
```
La forma de hacerlo paso a paso es primero definir la variable
```
dias_torneo = 3
```
Luego mediante el operador aritmético `*` vamos a realizar una multiplicación
```
horas = dias_torneo * 24
```
Y por ultimo mostramos por pantalla el resultado para que el usuario pueda visualizarlo
```
print("El torneo de rugby duró:", horas, "horas")
```
En resumen mediante operadores aritméticos se pueden realizar cálculos matemáticos 
