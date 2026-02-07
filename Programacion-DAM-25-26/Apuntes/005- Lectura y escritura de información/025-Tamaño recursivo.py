import os

carpeta = input("Indica una carpeta: ")

suma = 0

for directorio, carpetas, archivo in os.walk(carpeta):
	for archivo in archivo:
		ruta = os.path.join(directorio, archivo)
		try:
			suma += os.path.getsize(ruta)
		except:
			pass
		
print("La crapeta ocupa: ")
print(suma/(1024*1024),"MB")
