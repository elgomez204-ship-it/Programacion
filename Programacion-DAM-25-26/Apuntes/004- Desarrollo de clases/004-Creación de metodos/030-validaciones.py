class CuentaBancaria():
	def __init__(self):
		self.__saldo = 0
		self.__cliente = ""
	
	## DEFINO SETTERS Y GETTERS PARA EL SALDO ##
	
	def setSaldo(self,nuevosaldo):
	## ESTABLEZCO UNA CONDICIÓN DE QUE VALIDA SI EL SALDO NUEVO ES MAYOR DE 1000€ ##
		if nuevosaldo > self.__saldo + 1000:
	## SI SALTA LA ALARMA, AVISA Y *NO* CAMBIA EL SALDO ##
			print("Voy a avisar a la entidad de un ingreso muy grande")
		else:
	## SI PASA EL FILTRO, SOLO ENTONCES SE CAMBIA EL SALDO ##
			self.__saldo = nuevosaldo
			
	def getSaldo(self):
		return self.__saldo
		
cuentacliente1 = CuentaBancaria()
cuentacliente1.setSaldo(1000000000)
print(cuentacliente1.getSaldo())
