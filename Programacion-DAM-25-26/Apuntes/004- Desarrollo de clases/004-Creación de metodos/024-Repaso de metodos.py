class Gato():
	def __init__ (self):
		self.color = ""
		
	def maulla(self):
		return "miau"
		
gato1 = Gato()
gato1.color = "naranja"  ## SETEAMOS UNA PROPIEDAD ##
print(gato1.maulla())   ## AQUI LLAMAMOS A UN METODO ##
