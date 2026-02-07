En el ejercicio a continuación vamos a utilizar la estructura de control `for` para indicar los patitos que se producen en un año.
Para realizar este ejercicio primero hay que definir el rango de años,definiendo un bucle `for` para recorrer los años desde 2018 hasta 2023, como se puede ver a continuación:
```
for año in range (2018, 2024):
```
Luego dentro de ese bucle hay que crear otro bucle para contar los días del año.
```
for dia in range (1, 366):
```
Y por ultimo imprimimos en pantalla:
```
print(f"Año {año}: Produjo {dia} patitos")
```
A continuación puedes visualizar el código completo:
```
'''
    Contador de patitos producidos
    v0.1 Valentín Antonio De Gennaro
    Te dice la cantidad de patitos que se producen por año
    
'''

for año in range (2018, 2024):
    for dia in range (1, 366):
        print(f"Año {año}: Produjo {dia} patitos")
```

**NOTAS:**
- A la hora de utilizar el bucle `for` dentro del paréntesis el segundo valor tiene que ser un numero mas del que quieres indicar.

En rugby este código puede utilizarse para contar la cantidad de partidos que se juegan por año.