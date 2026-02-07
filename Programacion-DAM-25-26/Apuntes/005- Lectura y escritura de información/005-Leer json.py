import json  ## Libreria para usar un json ##

archivo = open("blog.json","r")

contenido = json.load(archivo)

print(contenido) ## Se importa en lo llamado 'DICCIONARIO'  en python ##


