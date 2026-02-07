En el ejercicio a continuación vamos a realizar una suma de dos números creando una función `funcionSuma`.
Para realizar este ejercicio primero hay que definir la función, usando camelCase, como se puede ver a continuación:
```
def calculaSuma(operando1, operando2):
```
Luego hay que indicar que hace esa función:
```
    resultado = operando1 + operando2
    return resultado
```
Y por ultimo le indicamos los valores a sumar y lo mostramos por pantalla: 
```
print(calculaSuma(4, 3))
```
A continuación esta el código entero: 
```
'''
    Suma de números
    v0.1 Valentin Antonio De Gennaro
    Definiendo una funcion te realiza una suma
    
'''

def calculaSuma(operando1, operando2):
    resultado = operando1 + operando2
    return resultado
    
print(calculaSuma(4, 3))

```
**NOTA:**
- No hay que olvidarse de indicar los valores en el `print` ya que de no hacerlo no va a indicar nada o va a arrojar error.

Este código puede utilizarse en el rugby para sumar los puntos por partido.