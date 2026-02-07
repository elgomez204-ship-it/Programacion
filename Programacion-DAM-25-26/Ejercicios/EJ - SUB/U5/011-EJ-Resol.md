En este ejercicio vamos a crear una aplicación en Python que gestione un portafolio de piezas y categorías utilizando una base de datos MySQL. El programa permitirá insertar, listar, actualizar y eliminar registros de las tablas `categoria` y `pieza`.

---

Primero importamos la librería necesaria para conectar Python con MySQL:
```
	import mysql.connector
```
Luego nos conectamos con la base de datos:
```
	conexion = mysql.connector.connect(
		host="localhost",
		user="admin",
		password="Portafolio2526@",
		database="portafolio"
	)
	cursor = conexion.cursor()
```

---

Después definimos las funciones para insertar datos.  
Primero creamos la función para insertar una pieza en la tabla `pieza`:
```
	def insertar_pieza(titulo_pieza, descripcion_pieza, imagen, url, id_categoria):
		cursor.execute('''
		  INSERT INTO pieza
		  VALUES(
			NULL,
			"'''+titulo_pieza+'''",
			"'''+descripcion_pieza+'''",
			"'''+imagen+'''",
			"'''+url+'''",
			"'''+id_categoria+'''"
		  );
		''')
		conexion.commit()
```
También creamos la función para insertar una categoría:
```
	def insertar_categoria(titulo_categoria,descripcion_categoria):
		cursor.execute('''
		  INSERT INTO categoria
		  VALUES(
			NULL,
			"'''+titulo_categoria+'''",
			"'''+descripcion_categoria+'''"
		  );
		''')
		conexion.commit()
```

Y la función para actualizar una categoría existente:
```
	def actualizar_categoria(titulo_categoria,descripcion_categoria):
		cursor.execute('''
		  UPDATE categoria SET
			titulo = "'''+titulo_categoria+'''",
			descripcion = "'''+descripcion_categoria+'''"
		''')
		conexion.commit()
```

---

A continuación mostramos una bienvenida al usuario:
```
print("########### Gestión de portafolio ##############")
print("##### v0.1 Valentin Antonio De Gennaro #########")
```

---

Creamos un bucle `while True` que mostrará el menú de opciones:
```
	while True:
		print("Escoge una opción:")
		print("1.-Insertar")
		print("2.-Listar")
		print("3.-Actualizar")
		print("4.-Eliminar")
		print("5.-Salir")
		opcion = int(input("Escoge una opcion: "))
```
Y desarrollamos las opciones:
##Opcion 1:
```
	if opcion == 1:
			print("1.-Insertar una categoria")
			print("2.-Insertar una pieza")
			opcion = int(input("Escoge una opcion: "))
			
			if opcion == 1:
				titulo_categoria = input("Ingresa el titulo de la categoria: ")
				descripcion_categoria = input("Introduce la descripcion de la categoria: ")
				insertar_categoria(titulo_categoria, descripcion_categoria)
				
			elif opcion == 2:
				titulo_pieza = input("Ingresa el titulo de la pieza: ")
				descripcion_pieza = input("Introduce la descripcion de la pieza: ")
				imagen = input("Introduce la imagen de la pieza: ")
				url = input("Introduce la url de la pieza: ")
				id_categoria = input("Introduce el id de la categoria: ")
				insertar_pieza(titulo_pieza, descripcion_pieza, imagen, url, id_categoria)
```
##Opcion 2:
```
	elif opcion == 2:
		print("1.-Listar categoria")
		print("2.-Listar pieza")
		print("3.-Ambas")
		opcion = int(input("Escoge una opcion: "))
		
		
		if opcion == 1:
			consulta = "SELECT * FROM categoria;"
			cursor.execute(consulta)
			resultados = cursor.fetchall()
			for fila in resultados:
				print("")
				print("Identificador: ",fila[0])
				print("Titulo: ",fila[1])
				print("descripcion: ",fila[2])
				print("-" * 30)  # línea separadora entre registros
		
		
		elif opcion == 2:
			consulta = "SELECT * FROM pieza;"
			cursor.execute(consulta)
			resultados = cursor.fetchall()
			for fila in resultados:
				print("")
				print("Identificador: ",fila[0])
				print("Titulo: ",fila[1])
				print("descripcion: ",fila[2])
				print("imagen: ",fila[3])
				print("url: ",fila[4])
				print("Id categoria: ",fila[5])
				print("-" * 30)  # línea separadora entre registros
				
		elif opcion == 3:		
			consulta = "SELECT * FROM vista_portafolio;"
			cursor.execute(consulta)
			resultados = cursor.fetchall()
			for fila in resultados:
				print("")
				print("Titulo de la pieza: ",fila[0])
				print("Descripción de la pieza: ",fila[1])
				print("Imagen de la pieza: ",fila[2])
				print("Url de la pieza: ",fila[2])
				print("Titulo de la categoria: ",fila[2])
				print("Descripción de la categoria: ",fila[2])		
				print("-" * 30)  # línea separadora entre registros
```
##Opción 3:
```
	elif opcion == 3:
		print("1.-Modificar una categoria")
		print("2.-Modificar una pieza")
		opcion = int(input("Escoge una opcion: "))
		
		if opcion == 1:
			identificador = input("Introduce el Identificador a actualizar: ")
			titulo = input("Introduce el titulo de la nueva categoria: ")
			descripcion = input("Introduce la descripcion de la nueva categoria: ")
			cursor.execute('''
			  UPDATE categoria 
			  SET
			  titulo = "'''+titulo+'''",
			  descripcion = "'''+descripcion+'''"
			  WHERE Identificador = '''+identificador+'''
			''')
			conexion.commit()
			
		elif opcion == 2:
			identificador = input("Introduce el Identificador a actualizar: ")
			titulo = input("Introduce el titulo de la nueva pieza: ")
			descripcion = input("Introduce la descripcion de la nueva pieza: ")
			fecha = input("Introduce la fecha de la nueva pieza: ")
			imagen = input("Introduce el nombre de la imagen de la nueva pieza: ")
			cursor.execute('''
			  UPDATE piezas 
			  SET
			  titulo = "'''+titulo+'''",
			  descripcion = "'''+descripcion+'''",
			  fecha = "'''+fecha+'''",
			  imagen = "'''+imagen+'''"
			  WHERE Identificador = '''+identificador+'''
			''')
			conexion.commit()
```
##Opción 4:
```
	elif opcion == 4:
		print("1.-Eliminar un elemento de categoria")
		print("2.-Eliminar un elemento de pieza")
		opcion = int(input("Escoge una opcion: "))
		
		if opcion == 1:
			identificador = input("Introduce el Identificador a eliminar: ")
			cursor.execute("DELETE FROM categoria WHERE Identificador = "+identificador+";")
			conexion.commit()
		
		
		elif opcion == 2:
			identificador = input("Introduce el Identificador a eliminar: ")
			cursor.execute("DELETE FROM piezas WHERE Identificador = "+identificador+";")
			conexion.commit()
```
##Opción 5:
```
	elif opcion == 5:
		print("Saliendo...")
		break
```
Y por ultimo cerramos el cursor y la conexión:
```
cursor.close()
conexion.close()
```

---

A continuación el codigo completo:
```
	'''
		Gestion de portafolio
		v0.1 Valentin Antonio De Gennaro
	'''
	import mysql.connector

	conexion = mysql.connector.connect(
		host="localhost",
		user="admin",
		password="Portafolio2526@",
		database="portafolio"
	)
	cursor = conexion.cursor()

	def insertar_pieza(titulo_pieza, descripcion_pieza, imagen, url, id_categoria):
		cursor.execute('''
		  INSERT INTO pieza
		  VALUES(
			NULL,
			"'''+titulo_pieza+'''",
			"'''+descripcion_pieza+'''",
			"'''+imagen.get+'''",
			"'''+url+'''"
			"'''+id_categoria+'''"
		  );
		''')
		conexion.commit()
		
	def insertar_categoria(titulo_categoria,descripcion_categoria):
		cursor.execute('''
		  INSERT INTO categoria
		  VALUES(
			NULL,
			"'''+titulo_categoria+'''",
			"'''+descripcion_categoria+'''"
		  );
		''')
		
	def actualizar_categoria(titulo_categoria,descripcion_categoria):
		cursor.execute('''
		  UPDATE categoria SET
			NULL,
			"'''+titulo_categoria+'''",
			"'''+descripcion_categoria+'''"
		  );
		''')
		conexion.commit()

	print("########### Gestión de portafolio ##############")
	print("##### v0.1 Valentin Antonio De Gennaro #########")

	while True:
		print("Escoge una opción:")
		print("1.-Insertar")
		print("2.-Listar")
		print("3.-Actualizar")
		print("4.-Eliminar")
		print("5.-Salir")
		opcion = int(input("Escoge una opcion: "))
		
		if opcion == 1:
			print("1.-Insertar una categoria")
			print("2.-Insertar una pieza")
			opcion = int(input("Escoge una opcion: "))
			
			if opcion == 1:
				titulo_categoria = input("Ingresa el titulo de la categoria: ")
				descripcion_categoria = input("Introduce la descripcion de la categoria: ")
				insertar_categoria(titulo_categoria, descripcion_categoria)
				
			elif opcion == 2:
				titulo_pieza = input("Ingresa el titulo de la pieza: ")
				descripcion_pieza = input("Introduce la descripcion de la pieza: ")
				imagen = input("Introduce la imagen de la pieza: ")
				url = input("Introduce la url de la pieza: ")
				id_categoria = input("Introduce el id de la categoria: ")
				insertar_pieza(titulo_pieza, descripcion_pieza, imagen, url, id_categoria)
		
		elif opcion == 2:
			print("1.-Listar categoria")
			print("2.-Listar pieza")
			print("3.-Ambas")
			opcion = int(input("Escoge una opcion: "))
			
			
			if opcion == 1:
				consulta = "SELECT * FROM categoria;"
				cursor.execute(consulta)
				resultados = cursor.fetchall()
				for fila in resultados:
					print("")
					print("Identificador: ",fila[0])
					print("Titulo: ",fila[1])
					print("descripcion: ",fila[2])
					print("-" * 30)  # línea separadora entre registros
			
			
			elif opcion == 2:
				consulta = "SELECT * FROM pieza;"
				cursor.execute(consulta)
				resultados = cursor.fetchall()
				for fila in resultados:
					print("")
					print("Identificador: ",fila[0])
					print("Titulo: ",fila[1])
					print("descripcion: ",fila[2])
					print("imagen: ",fila[3])
					print("url: ",fila[4])
					print("Id categoria: ",fila[5])
					print("-" * 30)  # línea separadora entre registros
					
			elif opcion == 3:		
				consulta = "SELECT * FROM vista_portafolio;"
				cursor.execute(consulta)
				resultados = cursor.fetchall()
				for fila in resultados:
					print("")
					print("Titulo de la pieza: ",fila[0])
					print("Descripción de la pieza: ",fila[1])
					print("Imagen de la pieza: ",fila[2])
					print("Url de la pieza: ",fila[2])
					print("Titulo de la categoria: ",fila[2])
					print("Descripción de la categoria: ",fila[2])		
					print("-" * 30)  # línea separadora entre registros
					
					
		elif opcion == 3:
			print("1.-Modificar una categoria")
			print("2.-Modificar una pieza")
			opcion = int(input("Escoge una opcion: "))
			
			if opcion == 1:
				identificador = input("Introduce el Identificador a actualizar: ")
				titulo = input("Introduce el titulo de la nueva categoria: ")
				descripcion = input("Introduce la descripcion de la nueva categoria: ")
				cursor.execute('''
				  UPDATE categoria 
				  SET
				  titulo = "'''+titulo+'''",
				  descripcion = "'''+descripcion+'''"
				  WHERE Identificador = '''+identificador+'''
				''')
				conexion.commit()
				
			elif opcion == 2:
				identificador = input("Introduce el Identificador a actualizar: ")
				titulo = input("Introduce el titulo de la nueva pieza: ")
				descripcion = input("Introduce la descripcion de la nueva pieza: ")
				fecha = input("Introduce la fecha de la nueva pieza: ")
				imagen = input("Introduce el nombre de la imagen de la nueva pieza: ")
				cursor.execute('''
				  UPDATE piezas 
				  SET
				  titulo = "'''+titulo+'''",
				  descripcion = "'''+descripcion+'''",
				  fecha = "'''+fecha+'''",
				  imagen = "'''+imagen+'''"
				  WHERE Identificador = '''+identificador+'''
				''')
				conexion.commit()
		
		elif opcion == 4:
			print("1.-Eliminar un elemento de categoria")
			print("2.-Eliminar un elemento de pieza")
			opcion = int(input("Escoge una opcion: "))
			
			if opcion == 1:
				identificador = input("Introduce el Identificador a eliminar: ")
				cursor.execute("DELETE FROM categoria WHERE Identificador = "+identificador+";")
				conexion.commit()
			
			
			elif opcion == 2:
				identificador = input("Introduce el Identificador a eliminar: ")
				cursor.execute("DELETE FROM piezas WHERE Identificador = "+identificador+";")
				conexion.commit()
		
		elif opcion == 5:
			print("Saliendo...")
			break
		
	cursor.close()
	conexion.close()
```	

---

**NOTAS:**
- El programa se conecta a MySQL usando la librería `mysql.connector`.

	
