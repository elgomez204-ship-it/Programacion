import os
import zipfile
import shutil

'''
  Quiero:
  1.- Crear una carpeta llamada EquipoRugby
  2.- Comprimir todos los archivos que haya dentro en un ZIP llamado Partidos.zip
  3.- Si la carpeta queda vacía, eliminarla
'''

try:
	if not os.path.isdir("EquipoRugby"):
		os.mkdir("EquipoRugby")
		print("Se ha creado la carpeta EquipoRugby")
	else:
		print("La carpeta EquipoRugby ya existía")

	zip_partidos = zipfile.ZipFile("Partidos.zip", "w", zipfile.ZIP_DEFLATED)

	for directorio, subcarpetas, archivos in os.walk("EquipoRugby"):
		for archivo in archivos:
			ruta_archivo = os.path.join(directorio, archivo)
			ruta_relativa = os.path.relpath(ruta_archivo, "EquipoRugby")
			zip_partidos.write(ruta_archivo, ruta_relativa)

	zip_partidos.close()
	print("Se ha creado el archivo Partidos.zip correctamente")

	if os.listdir("EquipoRugby") == []:
		os.rmdir("EquipoRugby")
		print("La carpeta EquipoRugby estaba vacía y se eliminó")
	else:
		print("La carpeta EquipoRugby no está vacía y no se eliminó")

except:
	print("Ha habido un error, continuamos")

