import os

carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)

for elemento in elementos:
	ruta = os.path.join(carpeta, elemento)
	print(elemento)
	print(os.path.getsize(elemento))
	print(os.path.getmtime(elemento))

