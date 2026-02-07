## pip3 install pickle

import pickle  ##ESCRIBIR EN BINARIO USANDO ESTA LIBRERIA ##


archivo = open("datos.bin","wb")
cadena = 'Valentin'

pickle.dump(cadena,archivo)

archivo.close()
