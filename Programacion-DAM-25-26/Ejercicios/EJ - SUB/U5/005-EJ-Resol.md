En este ejercicio vamos a crear una carpeta llamada EquipoRugby, comprimir todos los archivos que haya dentro en un archivo ZIP llamado Partidos.zip, y eliminar la carpeta si está vacía.  

---

Para empezar importamos las librerías necesarias:
```
	import os
	import zipfile
	import shutil
```
Es de buenas practicas agregar un bloque de comentario explicando lo que vamos a hacer:
```
	'''
	  Quiero:
	  1.- Crear una carpeta llamada EquipoRugby
	  2.- Comprimir todos los archivos que haya dentro en un ZIP llamado Partidos.zip
	  3.- Si la carpeta queda vacía, eliminarla
	'''
```
Después iniciamos un bloque `try` para que el programa siga funcionando en el caso de haber un error: 

Primero comprobamos si la carpeta existe y, si no existe, la creamos:
```
	if not os.path.isdir("EquipoRugby"):
		os.mkdir("EquipoRugby")
		print("Se ha creado la carpeta EquipoRugby")
	else:
		print("La carpeta EquipoRugby ya existía")
```
A continuación creamos el archivo ZIP y añadimos dentro todos los archivos que haya en la carpeta:
```
	zip_partidos = zipfile.ZipFile("Partidos.zip", "w", zipfile.ZIP_DEFLATED)

	for directorio, subcarpetas, archivos in os.walk("EquipoRugby"):
		for archivo in archivos:
			ruta_archivo = os.path.join(directorio, archivo)
			ruta_relativa = os.path.relpath(ruta_archivo, "EquipoRugby")
			zip_partidos.write(ruta_archivo, ruta_relativa)

	zip_partidos.close()
	print("Se ha creado el archivo Partidos.zip correctamente")
```

Por último comprobamos si la carpeta está vacía, si no tiene archivos, la eliminamos:
```
	if os.listdir("EquipoRugby") == []:
		os.rmdir("EquipoRugby")
		print("La carpeta EquipoRugby estaba vacía y se eliminó")
	else:
		print("La carpeta EquipoRugby no está vacía y no se eliminó")
```

---

A continuación el código completo:
```
import os
import zipfile
import shutil

'''
  Quiero:
  1.- Crear una carpeta llamada EquipoRugby
  2.- Comprimir todos los archivos que haya dentro en un ZIP llamado Partidos.zip
  3.- Si la carpeta queda vacía, eliminarla
'''

try:
	if not os.path.isdir("EquipoRugby"):
		os.mkdir("EquipoRugby")
		print("Se ha creado la carpeta EquipoRugby")
	else:
		print("La carpeta EquipoRugby ya existía")

	zip_partidos = zipfile.ZipFile("Partidos.zip", "w", zipfile.ZIP_DEFLATED)

	for directorio, subcarpetas, archivos in os.walk("EquipoRugby"):
		for archivo in archivos:
			ruta_archivo = os.path.join(directorio, archivo)
			ruta_relativa = os.path.relpath(ruta_archivo, "EquipoRugby")
			zip_partidos.write(ruta_archivo, ruta_relativa)

	zip_partidos.close()
	print("Se ha creado el archivo Partidos.zip correctamente")

	if os.listdir("EquipoRugby") == []:
		os.rmdir("EquipoRugby")
		print("La carpeta EquipoRugby estaba vacía y se eliminó")
	else:
		print("La carpeta EquipoRugby no está vacía y no se eliminó")

except:
	print("Ha habido un error, continuamos")
```

---

**NOTAS:**
- Usa `os.walk()` para recorrer archivos dentro de subcarpetas.
- El`try/except` evita que el programa se detenga si hay errores.
- `zipfile.ZipFile()` se usa para crear el archivo ZIP.


