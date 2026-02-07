En este ejercicio vamos a crear una pequeña aplicación donde varios NPC se mueven por la pantalla. Para ello usaremos Python, Flask y un archivo HTML que recibe los datos desde una API.

---

Primero definimos la clase `Npc`, que tendrá la posición, el radio, la dirección y la velocidad. También creamos un método para convertir cada NPC en diccionario:

```
class Npc():
	def __init__(self, x, y, radio, direccion, velocidad):
		self.posx = x
		self.posy = y
		self.radio = radio
		self.direccion = direccion
		self.velocidad = velocidad

	def to_dict(self):
		return {
		"posx": self.posx,
		"posy": self.posy,
		"radio": self.radio,
		"direccion": self.direccion
		}
```
Luego hacemos que cada NPC pueda moverse. Para ello usamos `math.cos` y `math.sin` y actualizamos sus coordenadas:

```
	def mover(self):
		self.direccion += self.direccion*(random.random()-0.5)*0.2
		if self.posx > 500 or self.posx < 0 or self.posy > 500 or self.posy < 0:
			self.direccion += math.pi
		self.posx += math.cos(self.direccion)*self.velocidad
		self.posy += math.sin(self.direccion)*self.velocidad
```
Después generamos 50 NPC con valores aleatorios para que cada uno se mueva de forma distinta:
```
personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
	xaleatoria = random.randint(0, 500)
	yaleatoria = random.randint(0, 500)
	radioaleatorio = random.randint(10, 30)
	direccionaleatoria = random.random()*math.pi*2
	velocidadaleatoria = random.random()*5
	personajes.append(Npc(xaleatoria, yaleatoria, radioaleatorio, direccionaleatoria, velocidadaleatoria))
```
Ahora creamos la aplicación Flask:
```
app = Flask(__name__)

@app.route("/")
def inicio():
	return render_template("juego.html")

@app.route("/api")
def api():
	for personaje in personajes:
		personaje.mover()
	personajes_json = [p.to_dict() for p in personajes]
	return json.dumps(personajes_json, indent=2)
```
En el archivo HTML usamos `fetch` para pedir los datos a la API y dibujar cada NPC usando `div`:
```
fetch("http://127.0.0.1:5000/api")
.then(function(respuesta){return respuesta.json();})
.then(function(datos){
	escenario.innerHTML = ""
	datos.forEach(function(npc){
		let personaje = document.createElement("div")
		personaje.classList.add("npc")
		personaje.style.left = npc.posx+"px"
		personaje.style.top = npc.posy+"px"
		personaje.style.width = npc.radio+"px"
		personaje.style.height = npc.radio+"px"
		escenario.appendChild(personaje)
	})
})
```
A continuación el código completo:
**Python:**
```
	import random
	import json
	from flask import Flask,render_template
	import math

	class Npc():
		def __init__(self, x, y,radio,direccion,velocidad):
			self.posx = x
			self.posy = y
			self.radio = radio
			self.direccion = direccion
			self.velocidad = velocidad
	# Método para convertir el objeto en diccionario
		
		def to_dict(self):
			return {
			"posx": self.posx,
			"posy": self.posy,
			"radio":self.radio,
			"direccion":self.direccion
			}
		def mover(self):
			self.direccion += self.direccion*(random.random()-0.5)*0.2
			if self.posx > 500 or self.posx < 0 or self.posy > 500 or self.posy < 0:
				self.direccion += math.pi
			self.posx += math.cos(self.direccion)*self.velocidad
			self.posy += math.sin(self.direccion)*self.velocidad
			
	# Preparo los personajes

	personajes = []
	numero_personajes = 50

	for i in range(0, numero_personajes):
		xaleatoria = random.randint(0, 500)
		yaleatoria = random.randint(0, 500)
		radioaleatorio = random.randint(10, 30)
		direccionaleatoria = random.random()*math.pi*2
		velocidadaleatoria = random.random()*5
		personajes.append(Npc(xaleatoria, yaleatoria,radioaleatorio,direccionaleatoria,velocidadaleatoria))


	# Lanzo una web

	app = Flask(__name__)

	@app.route("/")
	def inicio():
		return render_template("juego.html")

	@app.route("/api")
	def api():
		for personaje in personajes:
			personaje.mover()
		personajes_json = [p.to_dict() for p in personajes]
		return json.dumps(personajes_json, indent=2)
	  
	if __name__ == "__main__":
		app.run(debug=True)
```
**HTML:**
```
	<!doctype html>
	<html>
		<head>
		    <style>
		        .npc{
		            background:peru;
		            border-radius:50px;
		            position:absolute;
		        }
		    </style>
		</head>
	 	<body>	
		    <main>
		    </main>
		    <script>
		    // Cojo el contenedor
		    let escenario = document.querySelector("main")
		    let temporizador = setTimeout("bucle()",1000)
		    function bucle(){
		            // Me conecto a una api, pido datos, los convierto a json, y los lanzo
		        fetch("http://127.0.0.1:5000/api")
		        .then(function(respuesta){return respuesta.json();})
		        .then(function(datos){
		            console.log(datos)
		            // VACIO EL ESCENARIO SOLO CUANDO RECIBO DATOS
		            escenario.innerHTML = ""
		            // Para cada npc:
		            datos.forEach(function(npc){
		            // Creo un nuevo elemento en HTML
		                let personaje = document.createElement("div")
		            // Le añado una clase css
		            personaje.classList.add("npc")
		            // La posicion x en HTML sera la posicion x que viene de Python
		            personaje.style.left = npc.posx+"px"
		            // La posicion y en HTML será la posición y que viene de Python
		            personaje.style.top = npc.posy+"px"
		            // Pongo la anchura sobre el dato que llega de Python
		            personaje.style.width = npc.radio+"px"
		            // Pongo la altura sobre el dato que llega de Python
		            personaje.style.height = npc.radio+"px"
		            escenario.appendChild(personaje)
		            })
		        })
		        // PRIMERO BORRO EL TEMPORIZADOR ANTERIOR
		        clearTimeout(temporizador)
		        // Y AHORA VUELVO A LANZAR EL TEMPORIZADOR
		        temporizador = setTimeout("bucle()",100)
		    }
		    </script>
	  </body>
	</html>
```

---

**NOTAS:**

- Este ejercicio sirve para entender cómo un backend puede enviar datos en tiempo real a un frontend.
- Los NPC se mueven solos gracias al cálculo de dirección y velocidad.
- Este tipo de práctica es útil para juegos, animaciones o simulaciones visuales.

