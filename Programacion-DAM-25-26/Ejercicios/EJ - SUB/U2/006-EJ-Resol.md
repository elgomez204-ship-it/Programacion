En este ejercicio vamos a hacer una aplicación que muestre informacion sobre un partido de rugby, muestra el nombre del equipo, cuando juega y el dia de la semana que juega.

---

Para realizar este ejercicio primero debemos importar la libreria:
```
	from datetime import datetime
```
Luego creamos la clase:
```
	class PartidoRugby():
		def __init__(self, nombre_equipo, fecha_partido):
			self.nombre_equipo = nombre_equipo
			self.fecha_partido = fecha_partido
```
Despues creamos un partido y le agregamos la información:
```
	partido = PartidoRugby("Los Pumas", datetime.now())
```
Y por ultimo mostramos la información:
```
	print("-------------------------------------------")
	print("Nombre del equipo:", partido.nombre_equipo)
	print("Fecha del partido:", partido.fecha_partido.strftime("%Y-%m-%d"))
	print("Día de la semana:", partido.fecha_partido.weekday())
	print("-------------------------------------------")
```

---

A continuación el codigo completo:
```
	'''
		Información de partido de rugby
		v0.1 Valentín Antonio De Gennaro
		Muestra información sobre un partido.
	'''
	## IMPORTAMOS LA LIBRERIA DATETIME ##
	from datetime import datetime				

	## DEFINIMOS LA CLASE PARTIDORUGBY ##
	class PartidoRugby():
		def __init__(self, nombre_equipo, fecha_partido):
			self.nombre_equipo = nombre_equipo
			self.fecha_partido = fecha_partido

	## CREAMOS UN PARTIDO Y LE AGREGAMOS INFORMACIÓN ##
	partido = PartidoRugby("Los Pumas", datetime.now())

	## MOSTRAMOS LA INFORMACIÓN ##
	print("-------------------------------------------")
	print("Nombre del equipo:", partido.nombre_equipo)
	print("Fecha del partido:", partido.fecha_partido.strftime("%Y-%m-%d"))
	print("Día de la semana:", partido.fecha_partido.weekday())
	print("-------------------------------------------")
```

---

**NOTAS:**
- La clase `datetime` permite trabajar con fechas y horas fácilmente en Python. 
- El método `strftime()` se usa para dar formato a la fecha.  
