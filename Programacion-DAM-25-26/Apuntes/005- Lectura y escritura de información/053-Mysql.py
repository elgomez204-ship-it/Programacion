import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()
cursor.execute('''
  INSERT INTO clientes
  VALUES(
    NULL,
    "11111111H",
    "Daniel",
    "tonto",
    "tonto@daniel.com"
  );
''')
conexion.commit()

cursor.close()
conexion.close()
