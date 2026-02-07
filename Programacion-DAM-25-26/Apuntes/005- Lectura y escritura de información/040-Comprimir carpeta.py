import zipfile
import os

origen = "archivos"
destino = "archivo.zip"

archivozip = zipfile.ZipFile(destino, "w", compression=zipfile.ZIP_DEFLATED)

for directorio, carpetas, archivos in os.walk(origen):
	for archivo in archivos:
		rutaarchivo = os.path.join(directorio,archivo)
		rutarelativa = os.path.relpath(rutaarchivo, origen)
		archivozip.write(rutaarchivo, rutarelativa)

archivozip.close()
		
