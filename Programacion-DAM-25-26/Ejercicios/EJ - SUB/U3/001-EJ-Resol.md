En el ejercicio a continuación se visualiza un código que clasifica a un jugador dependiendo de su edad.
Para realizar este ejercicio primero hay que definir la variable, como se puede ver a continuación:
```
edad_jugador = 21
```
Luego mediante las estructuras de control `if`, `elif` y `else` se van a clasificar a los jugadores y mediante la función `print` para mostrar la clasificación como se puede ver a continuación:
```
if edad_jugador < 10:
    print("Eres un niño")
elif edad_jugador > 10 and edad_jugador <= 19:
    print("Eres un adolescente")
elif edad_jugador > 20 and edad_jugador <= 30:
    print("Eres un joven")
else:
    print("Ya no eres un joven")
```
Y a continuación se puede visualizar el código completo:
```
'''
    Clasificador de edades
    v0.1 Valentin Antonio De Gennaro
    Clasifica a un jugador segun se edad
'''

############### DECLARAMOS LA VARIABLE Y LE ASIGNAMOS UN VALOR #############
edad_jugador = 21

############### CLASIFICAMOS POR EDADES ##############################
if edad_jugador < 10:
    print("Eres un niño")
elif edad_jugador > 10 and edad_jugador <= 19:
    print("Eres un adolescente")
elif edad_jugador > 20 and edad_jugador <= 30:
    print("Eres un joven")
else:
    print("Ya no eres un joven")
```

**NOTAS:**
- Las estructuras de control `if`, `elif` y `else` son muy útiles a la hora de decirle al programa que si se cumple lo que le dijiste haga una cosa y si no lo cumple haga otra.
- En un pueblo pequeño con un club de futbol puede ser útil a la hora de definir lo equipos por edades este programa te va a facilitar la clasificación.
