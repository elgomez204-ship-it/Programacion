En este ejercico vamos a crear un gestor de clientes haciendo uso de las clases, de set y de get, este gestor lo que hace es almacenar la información de los clientes y luego mostrarsela al usuario por pantalla.

---

Para realizar este ejercicio primero creamos la clase, como se puede ver a continuación:
```
	class Cliente():
		def __init__(self,nombre,apellidos,email):
			self.nombre = nombre
			self.apellidos = apellidos
			self.email = email
```
Luego añadimos el set:
```
	def setNombre(self,nuevonombre):
		self.nombre = nuevonombre
```
Luego añadimos el get:
```
	def getNombre(self):
		return self.nombre
```
Despues tenemos que añadir el cliente y sus datos:
```
	cliente1 = Cliente("Juan","perez paz","perez@gmail.com")
```
Y para demostrar que el set funcione metemos un dato dentro del set:
```
	cliente1.apellidos = ("perez paz")
	cliente1.setApellidos(cliente1.apellidos)
```
Y lo mostramos en pantalla para demostra que el get funciona:
```
	print(Cliente.getApellidos)
```

---

A continuación el codigo completo:
```
	'''
		Gestor de clientes
		v0.1 Valentin Antonio De Gennaro
		
	'''

	## CREAMOS LA CLASE ##

	class Cliente():
		def __init__(self,nombre,apellidos,email):
			self.nombre = nombre
			self.apellidos = apellidos
			self.email = email
		
	## AÑADIMOS LOS SET ##

		def setNombre(self,nuevonombre):
			self.nombre = nuevonombre
		def setApellidos(self,nuevoapellido):
			self.apellidos = nuevoapellido
		def setEmail(self,nuevoemail):
			self.email = nuevoemail

	## AÑADIMOS LOS GET ##
		def getNombre(self):
			return self.nombre
		def getApellidos(self):
			return self.apellidos
		def getEmail(self):
			return self.email

	## AGREGO LOS CLIENTES ##
			
	cliente1 = Cliente("Juan","perez paz","perez@gmail.com")
	cliente2 = Cliente("Roberto","sanchez","rss@gmail.com")
	cliente3 = Cliente("Rodrigo","gomez","gomezr@gmail.com")

	## AÑADO INFORMACIÓN DENTRO DEL SET ##
	cliente1.apellidos = ("perez paz")
	cliente1.setApellidos(cliente1.apellidos)

	## MUESTRO QUE EL GET Y EL SET FUNCIONAN CORRECTAMENTE ##
	print(Cliente.getApellidos)
```

---

**NOTAS:**
- Al momento de crear clases hay que prestar atencion a que la primera letra del nombre de la clase sea en mayuscula






