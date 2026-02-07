import tkinter as tk
from tkinter import ttk
import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    user="Valentin",
    password="Valendg_25",
    database="CRM"
)
cursor = conexion.cursor()
ventana = tk.Tk()
ventana.config(bg='orangered')
arbol = ttk.Treeview(ventana, columns=('dninie', 'nombre', 'apellidos','email'), show = 'headings')
arbol.heading('dninie', text = 'DNI NIE del cliente')
arbol.heading('nombre', text = 'Nombre del cliente')
arbol.heading('apellidos', text = 'Apellidos del cliente')
arbol.heading('email', text = 'Email del cliente')
cursor.execute('''SELECT * FROM clientes;''')
filas = cursor.fetchall()
for fila in filas:
	arbol.insert("","end", values=(fila[1], fila[2], fila[3], fila[4]))

arbol.pack(padx = 20, pady = 20)

ventana.mainloop()
