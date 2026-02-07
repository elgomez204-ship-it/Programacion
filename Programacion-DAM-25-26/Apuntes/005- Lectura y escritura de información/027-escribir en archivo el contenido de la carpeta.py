import os

carpeta = input("Indica una carpeta: ")
grande = 1024 * 1024 * 1024 ## 1 GIGA ##

# a crea archivo #
mapa = open("mapa.txt","w") 
# w escribe encima #

for directorio, carpetas, archivos in os.walk(carpeta):
	for archivo in archivos:
		ruta = os.path.join(directorio, archivo)
		mapa.write(ruta+"\n")

mapa.close()

