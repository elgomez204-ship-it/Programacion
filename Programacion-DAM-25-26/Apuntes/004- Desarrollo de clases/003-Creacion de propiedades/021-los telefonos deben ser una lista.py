## LAS PROPIEDADES SON COMO LAS VARIABLES PERO DENTRO DE UNA CLASE ##
## GUARDAN INFO DENTRO DE UNA CLASE ##

class Cliente():
    def __init__ (self):
        self.nombre = ""
        self.edad = 0
        self.telefonos = []

##AHORA INSTANCIO UN NUEVO OBJETO ##

cliente1 = Cliente()

## AHORA LE ESCRIBO UNA PROPIEDAD ##

cliente1.nombre = "José Vicente"

print("El nombre del cliente es:",cliente1.nombre)

cliente1.telefonos.append("6546464")
cliente1.telefonos.append("3546466")

print(cliente1.telefonos)
        
        
