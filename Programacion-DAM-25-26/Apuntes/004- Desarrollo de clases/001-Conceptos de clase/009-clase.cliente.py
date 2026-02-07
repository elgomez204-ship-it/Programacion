##############Poco estable uso de muchas variables#########

cliente1_email = "info@jocarsa.com"
cliente1_direccion = "la calle de jose vicente"
cliente1_nombre = "Jose vicente"
cliente1_apellidos = "carratala sanchis"

cliente2_email = "info@cliente2.com"
cliente2_direccion = "la calle del cliente2"
cliente2_nombre = "pepe"
cliente2_apellidos = "sanchez"

###############Mucho mejor uso de clases#################

class Cliente:
    def __innit__(self):
        self.email = ""
        self.direccion = ""
        self.nombre = ""
        self.apellidos = ""

cliente1 = Cliente()
cliente1.email = "info@jocarsa.com"
cliente1.direccion = "la calle de jose vicente"
cliente1.nombre = "Jose vicente"
cliente1.apellidos = "carratala sanchis"

cliente2 = Cliente()
cliente2.email = "info@cliente2.com"
cliente2.direccion = "la calle del cliente2"
cliente2.nombre = "pepe"
cliente2.apellidos = "sanchez"

#Las clases nos permiten agrupar datos

