En este ejercicio vamos a crera un programa que almacene datos de jugadores en un archivo `.txt` y en un `.bin` y te los muestre.

---

Primero creamos el archivo `jugadores.txt` y escribimos la información de un jugador:
```
	archivo = open("jugadores.txt", "w")
	archivo.write("Nombre: Juan Pérez\n")
	archivo.write("Edad: 25\n")
	archivo.write("Posición: Portero\n")
	archivo.write("Equipo: La Furia Roja\n")
	archivo.close()
```
Y luego añadimos otro jugador:
```
	archivo = open("jugadores.txt", "a")
	archivo.write("Nombre: María García\n")
	archivo.write("Edad: 28\n")
	archivo.write("Posición: Lateral derecho\n")
	archivo.write("Equipo: El Águila Negra\n")
	archivo.close()
```
A continuación leemos el archivo `jugadores.txt` y lo mostramos por pantalla:
```
	archivo = open("jugadores.txt", "r")
	contenido = archivo.read()
	print(contenido)
	archivo.close()
```

Finalmente usamos la librería `pickle` para guardar los jugadores en un archivo binario llamado `jugadores.bin`:
```
	import pickle
```
Luego creamos la clase jugador:
```
	class Jugador():
		def __init__(self, nombre, edad, posicion, equipo):
			self.nombre = nombre
			self.edad = edad
			self.posicion = posicion
			self.equipo = equipo
```
Creamos dos variables para almacenar los datos de los jugadores:
```
jugador1 = Jugador("Juan Pérez", 25, "Portero", "La Furia Roja")
jugador2 = Jugador("María García", 28, "Lateral derecho", "El Águila Negra")
```
Y por ultimo guardamos esos datos en el archivo `.bin`:
```
	archivo_binario = open("jugadores.bin", "wb")
	pickle.dump([jugador1, jugador2], archivo_binario)
	archivo_binario.close()
```

---

A continuación el codigo completo:
```
	'''
		Gestión de jugadores
		v0.1 Valentín Antonio De Gennaro
		Programa que guarda información de jugadores de rugby en archivos de texto y binarios.
	'''

	import pickle

	## ESCRIBIMOS EL PRIMER JUGADOR ##
	archivo = open("jugadores.txt", "w")
	archivo.write("Nombre: Juan Pérez\n")
	archivo.write("Edad: 25\n")
	archivo.write("Posición: Portero\n")
	archivo.write("Equipo: La Furia Roja\n")
	archivo.close()

	## AÑADIMOS UN NUEVO JUGADOR ##
	archivo = open("jugadores.txt", "a")
	archivo.write("Nombre: María García\n")
	archivo.write("Edad: 28\n")
	archivo.write("Posición: Lateral derecho\n")
	archivo.write("Equipo: El Águila Negra\n")
	archivo.close()

	## LEEMOS EL CONTENIDO DEL ARCHIVO ##
	archivo = open("jugadores.txt", "r")
	contenido = archivo.read()
	print(contenido)
	archivo.close()

	## CREAMOS LA CLASE JUGADOR ##
	class Jugador():
		def __init__(self, nombre, edad, posicion, equipo):
			self.nombre = nombre
			self.edad = edad
			self.posicion = posicion
			self.equipo = equipo

	## ALMACENAMOS LOS DATOS EN DOS VARIABLES ##
	jugador1 = Jugador("Juan Pérez", 25, "Portero", "La Furia Roja")
	jugador2 = Jugador("María García", 28, "Lateral derecho", "El Águila Negra")

	## GUARDAMOS LOS JUGADORES EN UN ARCHIVO BINARIO ##
	archivo_binario = open("jugadores.bin", "wb")
	pickle.dump([jugador1, jugador2], archivo_binario)
	archivo_binario.close()
```

---

**NOTAS:**
- La librería `pickle` sirve para guardar objetos en formato binario. 
- Es importante cerrar todos los archivos después de usarlos con `close()`.



