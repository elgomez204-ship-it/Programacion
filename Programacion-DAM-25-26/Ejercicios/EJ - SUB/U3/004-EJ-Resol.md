Mediante las estructuras de control `try` y `except` se puede hacer que el programa continué ante un error. En este ejercicio calculamos la cantidad total de puntos por partido y en el caso de que el usuario introduzca mal los números y el programa de **ERROR**, este continua con normalidad.
Para realizar este ejercicio primero hay que definir las variables, como se puede ver a continuación:
```
puntos_rugby = 0
partidos_jugados = 0
```
Luego hay que pedirle al usuario que le asigne un valor a esas variables:
```
puntos_rugby = int(input("Introduce tus puntos: "))
partidos_jugados = int(input("Introduce la cantidad de partidos jugados: "))
```
Y luego de asignarles un valor el programa intentara dividir esos valores introducidos, como se puede ver a continuación:
```
try:
    puntosporpartido = puntos_rugby/partidos_jugados
    print("El total de puntos por partido es: ",puntosporpartido)
```
Y en el caso de que el usuario introduzca datos erróneos y el programa no funcione utilizamos un `except` para que el programa continué su funcionamiento, como se puede ver a continuación:
```
except:
    print("ERROR")
    print("El programa continua en funcionamiento")
```
A continuación podemos ver el código completo:
```
'''
    Calculador de puntos por partido
    v0.1 Valentin Antonio De Gennaro
    Divide los puntos entre los partidos jugados
'''

puntos_rugby = 0
partidos_jugados = 0
puntos_rugby = int(input("Introduce tus puntos: "))
partidos_jugados = int(input("Introduce la cantidad de partidos jugados: "))

try:
    puntosporpartido = puntos_rugby/partidos_jugados
    print("El total de puntos por partido es: ",puntosporpartido)
except:
    print("ERROR")
    print("El programa continua en funcionamiento")
```
A la hora de utilizar el `try` y el `except` hay que recordar anidar y no olvidarse de los paréntesis ya que en el caso de no hacerlo el código va a arrojar error y no va a funcionar. 
Es muy útil ya que en el caso de no usarlos y el programa dar error dejaría de funcionar.
