'''
	Gestión de movimientos bancarios
	v0.1 Valentín Antonio De Gennaro
	Permite añadir y mostrar los movimientos bancarios de un cliente.
'''

class Cliente():
	def __init__(self, nombre, edad, telefonos):
		self.nombre = nombre
		self.edad = edad
		self.telefonos = telefonos
		self.movimientos_bancarios = []   # LISTA VACÍA PARA GUARDAR LOS MOVIMIENTOS

	def añadir_movimiento(self, monto):
		## AÑADIMOS EL MOVIMIENTO A LA LISTA ##
		self.movimientos_bancarios.append(monto)

	def mostrar_movimientos(self):
		## MOSTRAMOS TODOS LOS MOVIMIENTOS ##
		print("Movimientos bancarios de", self.nombre,":")
		for movimiento in self.movimientos_bancarios:
			print(movimiento)


## CREAMOS UN CLIENTE ##
cliente1 = Cliente("Valentín", 21, ["600000000"])

## AÑADIMOS MOVIMIENTOS ##
cliente1.añadir_movimiento(150.50)
cliente1.añadir_movimiento(-20)
cliente1.añadir_movimiento(300)

## MOSTRAMOS LOS MOVIMIENTOS ##
cliente1.mostrar_movimientos()

