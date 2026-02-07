import os

carpeta = input("Indica una carpeta: ")
grande = 1024 * 1024 * 1024 ## 1 GIGA ##



for directorio, carpetas, archivo in os.walk(carpeta):
	for archivo in archivo:
		ruta = os.path.join(directorio, archivo)
		try:
			if os.path.getsize(ruta) > grande:
				print(ruta, os.path.getsize(ruta)/(1024*1024),"MB")
		except:
			pass
		

