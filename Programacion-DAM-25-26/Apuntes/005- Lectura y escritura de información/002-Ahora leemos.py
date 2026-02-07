archivo = open("clientes.txt","r") ## R = READ ##

contenido = archivo.readline()
## TAMBIÉN EXISTE ARCHIVO.READLINES() ##

print(contenido)

archivo.close()
