class Gato():
	def __init__ (self):
		self.color = ""   ## ESTO ES UNA PROPIEDAD ##
		
	def maulla(self):    ## ESTO ES UN METODO ##
		return "miau"
		
	def setColor(self,nuevocolor):  ## DEFINO UN SETTER - EL METODO ES EL RESPONSABLE DE CAMBIAR LA PROPIEDAD ##
		## POR EJEMPLO AQUI PODRIA VALIODAR SI EL COLOR ES UN COLOR VALIDO PARA UN GATO ##
		self.color = nuevocolor     ## Y CAMBIO LA PROPIEDAD ##
		
	def getColor(self):
		## UNA VEZ MAS, AQUI PODRIA PONER VALIDACIONES SI LO QUISIERA ##
		return self.color
		
gato1 = Gato()
gato1.color = "naranja"   ## AQUI SETEAMOS UNA PROPIEDAD DIRECTAMENTE ( NO ES UNA BUENA PRACTICA) ##

gato1.setColor("naranja")  ## ESTO ES UNA PRACTICA MUCHO MEJOR

print(gato1.color)        ## ACCESO DIRECTO, SE PUEDE PERO NO SE RECOMIENDA

print(gato1.getColor())  ## ACCESO MEDIANTE METODO, *SE RECOMIENDA* ##

