import json  ## Libreria para usar un json ##

archivo = open("blog.json","r")

contenido = json.load(archivo)

for linea in contenido:
	print('########################')
	print(linea['titulo'])
	print(linea['fecha'])
	print(linea['autor'])
	print(linea['contenido'])
	print('########################')
	print("")

