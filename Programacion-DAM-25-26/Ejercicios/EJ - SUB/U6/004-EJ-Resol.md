En este ejercicio vamos a crear una aplicación que mediante los datos que hay almacenados en una lista, nos devuelva el doble de su valor, pero esa lista tiene números y etiquetas.

---

Para realizar este ejercicio primero debemos definir la lista y asignarle los números y etiquetas:
```
datos = [
	1,
	2,
	"tres",
	4,
	"cinco",
	6
]
```
Luego vamos a mostrar el contenido de esa lista por pantalla:
```
print(datos)
```
Despues creamos la lista con las etiquetas:
```
numeros_etiquetas = ['cero','uno','dos','tres','cuatro','cinco','seis']
```
Y ahora definimos la función:
```
def calculaDoble():
	for dato in datos:
		try:											## INTENTO CONVERTIR A ENTERO ##
			numero = int(dato)
			print(numero*2)
		except:											## SI NO ES UN NÚMERO, INTENTO BUSCAR EN ETIQUETAS ##
			centinela = False
			for i in range(0,len(numeros_etiquetas)):
				if dato == numeros_etiquetas[i]:
					print(i*2)
					centienla = True
			if centinela == False:
				print("No se puede")
```
Y por ultimo llamamos a la función:
```
calculaDoble()
```

---

A continuación el codigo completo:
```
	'''
		LISTA CON NÚMEROS Y ETIQUETAS
		v0.1 Valentín de Gennaro
	'''

	## CREAMOS UNA LISTA Y EL ASIGAMOS DATOS ##
	datos = [
		1,
		2,
		"3",
		4,
		"cinco",
		6
	]
	## MOSTRAMOS ESOS DATOS AL USUARIO POR PANTALLA ##
	print(datos)

	## CREAMOS UNA LISTA DE ETIQUETAS ##
	numeros_etiquetas = ['cero','uno','dos','tres','cuatro','cinco','seis']

	## DEFINIMOS UNA FUNCIÓN ##
	def calculaDoble():
		for dato in datos:
			try:											## INTENTO CONVERTIR A ENTERO ##
				numero = int(dato)
				print(numero*2)
			except:											## SI NO ES UN NÚMERO, INTENTO BUSCAR EN ETIQUETAS ##
				centinela = False
				for i in range(0,len(numeros_etiquetas)):
					if dato == numeros_etiquetas[i]:
						print(i*2)
						centinela = True
				if centinela == False:
					print("No se puede")
		
	calculaDoble()
```

---

**NOTAS:**
- Si una etiqueta no está en la lista o el dato no es numérico, el programa muestra "No se puede".
- El centinela es necesario para saber si la etiqueta existe realmente en la lista y evitar falsos positivos.
