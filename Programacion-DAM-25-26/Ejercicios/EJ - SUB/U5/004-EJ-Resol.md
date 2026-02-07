En este ejercicio vamos a crear un programa que calcule el tamaño total de una carpeta que el usuario indique.  

---

Primero importamos la librería `os`, que nos permite trabajar con rutas y archivos del sistema:
```
	import os
```
Luego le pedimos al usuario que nos indique la ruta de la carpeta:
```
	ruta = input("Introduce la ruta de la carpeta: ")
```
Creamos una variable para almacenar el tamaño de la carpeta:
```
	tamaño_total = 0
```

A continuación usamos `os.walk()` para recorrer todos los archivos y subcarpetas dentro de la ruta indicada. Por cada archivo que encontremos, sumamos su tamaño utilizando `os.path.getsize()`: 
```
	for carpeta, subcarpetas, archivos in os.walk(ruta):
		for archivo in archivos:
			ruta_completa = os.path.join(carpeta, archivo)
			tamaño_total += os.path.getsize(ruta_completa)
```
Y por ultimo le mostramos al usuario el tamaño de la carpeta en `MB`:
```
	print("El tamaño total de la carpeta es:", tamaño_total / 1048576, "MB")
```

---

A continuación el codigo completo:
```
	'''
		Calculadora de tamaño de carpeta
		v0.1 Valentín Antonio De Gennaro
		Programa que calcula el tamaño total de una carpeta en MB.
	'''

	import os

	ruta = input("Introduce la ruta de la carpeta: ")
	tamaño_total = 0

	for carpeta, subcarpetas, archivos in os.walk(ruta):
		for archivo in archivos:
			ruta_completa = os.path.join(carpeta, archivo)
			tamaño_total += os.path.getsize(ruta_completa)

	print("El tamaño total de la carpeta es:", tamaño_total / 1048576, "MB")
```

---

**NOTAS:**
- `os.walk()` permite recorrer todas las carpetas y archivos dentro de una ruta.  
- `os.path.getsize()` devuelve el tamaño del archivo en bytes.  
- Para mostrar el tamaño en MB se divide entre `1048576`.  

