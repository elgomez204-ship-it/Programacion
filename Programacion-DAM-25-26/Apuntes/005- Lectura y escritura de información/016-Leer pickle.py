## pip3 install pickle

import pickle  ##ESCRIBIR EN BINARIO USANDO ESTA LIBRERIA ##


archivo = open("datos.bin","rb")

cadena = pickle.load(archivo)

print(cadena)

archivo.close()
