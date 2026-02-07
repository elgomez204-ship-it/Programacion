En este ejercicio vamos a crear un objeto llamado `Equipo` que almacenará información acerca de un equipo y los nombres de sus jugadores.  

---

Primero debemos crear la clase `Equipo`:
```
	class Equipo():
		def __init__(self, nombre, jugadores):
			self.nombre = nombre
			self.jugadores = jugadores
```
Luego creamos un método llamado `mostrar_equipo()` que se encargará de mostrar por pantalla el nombre del equipo y los jugadores:
```
	def mostrar_equipo(self):
		print("Nombre del equipo:", self.nombre)
		print("Lista de jugadores:")
		for jugador in self.jugadores:
			print("-", jugador)
```

Luego creamos un equipo y le agregamos un nombre y jugadores:
```
	equipo1 = Equipo("Los Pumas", ["Valentín", "Franco", "Lucas", "Martín", "Joaquín"])
```
Por último llamamos al método `mostrar_equipo()` para mostrar toda la información en pantalla:
```
	equipo1.mostrar_equipo()
```

---

A continuación el codigo completo:
```
	'''
		Información del equipo
		v0.1 Valentin Antonio De Gennaro
		Te muestra información de un equipo y sus jugadores.
	'''
	## CREAMOS LA CLASE ##
	class Equipo():
		def __init__(self, nombre, jugadores):
			self.nombre = nombre
			self.jugadores = jugadores

		def mostrar_equipo(self):
			print("Nombre del equipo:", self.nombre)
			print("Lista de jugadores:")
			for jugador in self.jugadores:
				print("-", jugador)

	## CREAMOS UN EQUIPO ##
	equipo1 = Equipo("Los Pumas", ["Valentín", "Franco", "Lucas", "Martín", "Joaquín"])

	## MOSTRAMOS LA INFORMACIÓN DEL EQUIPO ##
	equipo1.mostrar_equipo()

```

---

**NOTAS:**
- Los bucles `for` son muy útiles para recorrer listas y mostrar información.

