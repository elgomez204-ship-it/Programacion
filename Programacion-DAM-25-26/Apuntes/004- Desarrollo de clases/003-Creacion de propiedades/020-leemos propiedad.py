## LAS PROPIEDADES SON COMO LAS VARIABLES PERO DENTRO DE UNA CLASE ##
## GUARDAN INFO DENTRO DE UNA CLASE ##

class cliente():
    def __init__ (self):
        self.nombre = ""
        self.edad = 0
        self.telefonos = ["543534","5345345"]

##AHORA INSTANCIO UN NUEVO OBJETO ##

cliente1 = cliente()

## AHORA LE ESCRIBO UNA PROPIEDAD ##

cliente1.nombre = "José Vicente"

print("El nombre del cliente es:",cliente1.nombre)
        
        
        
