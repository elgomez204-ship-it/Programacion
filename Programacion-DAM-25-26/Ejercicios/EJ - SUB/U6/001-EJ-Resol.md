En este ejercicio vamos a crear una aplicación que gestione jugadores de rugby, esta aplicación puede agregar, eliminar y modificar jugadores de una lista.

---

Para realizar este ejercicio primero debemos definir la lista y agregarle 3 nombres de jugadores de rugby. A continuación un ejemplo:
```
	jugadores = ["Antoine Dupont", "Beauden Barrett", "Cheslin Kolbe"]
```
Luego añadimos un nombre a la lista:
```
	jugadores.append("Maro Itoje")
```
Luego Usando un bucle `for` vamos a recorrer la lista y mostrarla al usuario usando `print`:
```
	print("Lista inicial de jugadores:")
	for jugador in jugadores:
		print(jugadores)
```
Ahora eliminamos a un jugador de la lista usando el metodo `pop()`:
```
	jugador_eliminado = jugadores.pop(1)
	print("Jugador eliminado: ",jugador_eliminado)
```
Luego de eso vamos a modificar el nombre de un jugador:
```
	indice_a_modificar = 0
	jugadores[indice_a_modificar] = "Jonathan Sexton"
```
Y por ultio mostramos la lista actualizada al usuario:
```
	print("Lista actualizada de jugadores:")
	for jugador in jugadores:
		print(jugadores)
```

---

A continuación el codigo completo:
```
	'''
		Lista de jugadores de rugby
		v0.1 Valentín Antonio De Gennaro
	'''

	## CREO UNA LISTA Y LE AÑADO 3 NOMBRES ##
	jugadores = ["Antoine Dupont", "Beauden Barrett", "Cheslin Kolbe"]

	## AÑADO OTRO NOMBRE A LA LISTA ##
	jugadores.append("Maro Itoje")

	## MUESTRO LOS JUGADORES DE LA LISTA ##
	print("Lista inicial de jugadores:")
	for jugador in jugadores:
		print(jugadores)
		
	## ELIMINO A UN JUGADOR DE LA LISTA ##
	jugador_eliminado = jugadores.pop(1)
	print("Jugador eliminado: ",jugador_eliminado)

	## MODIFICAMOS EL NOMBRE DE UN JUGADOR ##
	indice_a_modificar = 0
	jugadores[indice_a_modificar] = "Jonathan Sexton"

	## MOSTRAMOS LA LISTA ACTUALIZADA ##
	print("Lista actualizada de jugadores:")
	for jugador in jugadores:
		print(jugadores)
```

---

**NOTAS:**
- El uso de una lista es util para almacenar información y luego poder mostrarla.
- Usando `append()` podemos agregar información a la lista.
