####### DECLARAMOS LA CLASE ############
class Cliente():
    def __init__(self):
        self.email = None
        self.nombre = None
        self.direccion = None

########## USAMOS LA CLASE INSTANCIANDO EN UN OBJETO ######
cliente1 = Cliente()
cliente1.email = "test@gmail.com"
cliente1.nombre = "jose"
cliente1.direccion = "la calle de jose"

