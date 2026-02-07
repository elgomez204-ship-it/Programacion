import pickle

class Cliente():
	def __init__(self,nuevonombre,nuevoemail):
		self.nombre = ""
		self.email = ""
		
clientes = []

clientes.append(Cliente('Valentin De Gennaro','valentindegennaro@gmail.com'))
clientes.append(Cliente('Roberto','roberto@gmail.com'))

print(clientes)

archivo = open("clientes.bin","wb")
pickle.dump(clientes,archivo)
archivo.close()
