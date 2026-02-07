class Gato():
	def __init__ (self):
		self.color = "naranja"  ## ESTO ES UNA PROPIEDAD PRIVADA (CONTRAPUESTA A PUBLICA) 
		
gato1 = Gato()
##gato1.__color = "naranja"##
print(gato1.__color)

