class Cliente():
## ESTE ES EL METODO CONSTRUCTOR ##
	def __init__(self):
		self.nombrecompleto = ""
		self.email = ""
		
## ESTOS SON LOS SETTERS Y LOS GETTERS ##
	def setNombreCompleto(self,nuevonombre):
		self.nombrecompleto = nuevonombre
	def setEmail(self,nuevoemail):
		self.email = nuevoemail
	def getNombrecompleto(self):
		return self.nombrecompleto
	def getEmail(self):
		return self.email
