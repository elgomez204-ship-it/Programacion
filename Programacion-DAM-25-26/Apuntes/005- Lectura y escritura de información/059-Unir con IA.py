import sys
import tkinter as tk
from tkinter import messagebox

# Intentar cargar ttkbootstrap; si falta ImageTk/Tk, avisar y salir
try:
    import ttkbootstrap as tb
    from ttkbootstrap.constants import BOTH, YES, LEFT, RIGHT, X, Y, W
except Exception as e:
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "Dependencias faltantes",
        "ttkbootstrap requiere Pillow (ImageTk) y tkinter.\n\n"
        "En Ubuntu/Debian:\n"
        "  sudo apt update && sudo apt install -y python3-pil.imagetk python3-tk\n\n"
        "En entorno virtual:\n"
        "  pip install pillow ttkbootstrap\n\n"
        f"Detalle del error: {e}"
    )
    sys.exit(1)

import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "empresadam",
    "password": "Empresadam123$",
    "database": "empresadam",
}

# Conexión
try:
    conexion = mysql.connector.connect(**DB_CONFIG)
    cursor = conexion.cursor()
except Error as e:
    r = tk.Tk()
    r.withdraw()
    messagebox.showerror("Error de base de datos", f"No se pudo conectar a MySQL:\n{e}")
    sys.exit(1)

# Ventana principal con ttkbootstrap
root = tb.Window(themename="darkly")
root.title("Gestión de clientes - Empresadam")
root.geometry("980x650")

status_var = tk.StringVar(value="Listo.")

# Notebook
notebook = tb.Notebook(root, bootstyle="info")
frame_insertar = tb.Frame(notebook, padding=20)
frame_listado = tb.Frame(notebook, padding=20)
notebook.add(frame_insertar, text="Insertar")
notebook.add(frame_listado, text="Clientes")
notebook.pack(fill=BOTH, expand=YES, padx=12, pady=12)

# -------- Pestaña: Insertar --------
form = tb.Labelframe(frame_insertar, text="Nuevo cliente", bootstyle="primary", padding=20)
form.pack(fill=X, padx=10, pady=10)

lbl_dni = tb.Label(form, text="DNI/NIE", anchor=W)
lbl_nombre = tb.Label(form, text="Nombre", anchor=W)
lbl_apellidos = tb.Label(form, text="Apellidos", anchor=W)
lbl_email = tb.Label(form, text="Email", anchor=W)

ent_dni = tb.Entry(form, width=30)
ent_nombre = tb.Entry(form, width=30)
ent_apellidos = tb.Entry(form, width=30)
ent_email = tb.Entry(form, width=30)

lbl_dni.grid(row=0, column=0, sticky=W, padx=6, pady=6)
ent_dni.grid(row=0, column=1, sticky=W, padx=6, pady=6)
lbl_nombre.grid(row=1, column=0, sticky=W, padx=6, pady=6)
ent_nombre.grid(row=1, column=1, sticky=W, padx=6, pady=6)
lbl_apellidos.grid(row=2, column=0, sticky=W, padx=6, pady=6)
ent_apellidos.grid(row=2, column=1, sticky=W, padx=6, pady=6)
lbl_email.grid(row=3, column=0, sticky=W, padx=6, pady=6)
ent_email.grid(row=3, column=1, sticky=W, padx=6, pady=6)

btns_row = tb.Frame(form)
btns_row.grid(row=4, column=0, columnspan=2, sticky=W, pady=(12, 0))

def limpiar_campos():
    ent_dni.delete(0, tk.END)
    ent_nombre.delete(0, tk.END)
    ent_apellidos.delete(0, tk.END)
    ent_email.delete(0, tk.END)

def insertar_cliente():
    dninie = ent_dni.get().strip()
    nombre = ent_nombre.get().strip()
    apellidos = ent_apellidos.get().strip()
    email = ent_email.get().strip()

    if not (dninie and nombre and apellidos and email):
        status_var.set("Completa todos los campos antes de insertar.")
        return

    try:
        cursor.execute(
            "INSERT INTO clientes (dninie, nombre, apellidos, email) VALUES (%s, %s, %s, %s);",
            (dninie, nombre, apellidos, email),
        )
        conexion.commit()
        status_var.set("Cliente insertado correctamente.")
        limpiar_campos()
        cargar_clientes()
        notebook.select(frame_listado)
    except Error as e:
        status_var.set(f"Error al insertar: {e}")
        messagebox.showerror("Error al insertar", str(e))

btn_insertar = tb.Button(btns_row, text="Insertar cliente", bootstyle="success", command=insertar_cliente)
btn_limpiar = tb.Button(btns_row, text="Limpiar", bootstyle="secondary", command=limpiar_campos)
btn_insertar.pack(side=LEFT, padx=(0, 8))
btn_limpiar.pack(side=LEFT)

# -------- Pestaña: Listado --------
topbar = tb.Frame(frame_listado)
topbar.pack(fill=X, pady=(0, 8))

tb.Label(topbar, text="Listado de clientes", font=("-size", 12)).pack(side=LEFT)

# Barra de búsqueda por DNI/NIE
busqueda_frame = tb.Frame(frame_listado)
busqueda_frame.pack(fill=X, pady=(0, 8))

tb.Label(busqueda_frame, text="Buscar por DNI/NIE:", anchor=W).pack(side=LEFT, padx=(0, 8))
dni_var = tk.StringVar()
dni_entry = tb.Entry(busqueda_frame, textvariable=dni_var, width=24, bootstyle="info")
dni_entry.pack(side=LEFT, padx=(0, 8))

def accion_buscar():
    patron = dni_var.get().strip()
    cargar_clientes(filtro_dni=patron if patron else None)

def accion_limpiar_busqueda():
    dni_var.set("")
    cargar_clientes(None)

btn_buscar = tb.Button(busqueda_frame, text="Buscar", bootstyle="info", command=accion_buscar)
btn_buscar.pack(side=LEFT, padx=(0, 8))
btn_limpiar_busqueda = tb.Button(busqueda_frame, text="Limpiar", bootstyle="secondary", command=accion_limpiar_busqueda)
btn_limpiar_busqueda.pack(side=LEFT)

# Botón de eliminación
acciones_frame = tb.Frame(frame_listado)
acciones_frame.pack(fill=X, pady=(0, 8))

btn_eliminar = tb.Button(acciones_frame, text="Eliminar seleccionados", bootstyle="danger", state="disabled")
btn_eliminar.pack(side=LEFT)

# Treeview de clientes (multiselección)
cols = ("dninie", "nombre", "apellidos", "email")
arbol = tb.Treeview(
    frame_listado,
    columns=cols,
    show="headings",
    bootstyle="info",
    selectmode="extended",  # permite multiselección
)
for col, text, width in [
    ("dninie", "DNI/NIE", 150),
    ("nombre", "Nombre", 180),
    ("apellidos", "Apellidos", 220),
    ("email", "Email", 220),
]:
    arbol.heading(col, text=text)
    arbol.column(col, width=width, anchor=W)

yscroll = tb.Scrollbar(frame_listado, orient="vertical", command=arbol.yview)
xscroll = tb.Scrollbar(frame_listado, orient="horizontal", command=arbol.xview)
arbol.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

arbol.pack(fill=BOTH, expand=YES, side="left")
yscroll.pack(fill=Y, side="left")
xscroll.pack(fill=X)

def cargar_clientes(filtro_dni=None):
    try:
        for item in arbol.get_children():
            arbol.delete(item)

        if filtro_dni:
            patron = f"%{filtro_dni}%"
            cursor.execute(
                "SELECT dninie, nombre, apellidos, email FROM clientes "
                "WHERE dninie LIKE %s "
                "ORDER BY dninie DESC;",
                (patron,),
            )
        else:
            cursor.execute(
                "SELECT dninie, nombre, apellidos, email FROM clientes "
                "ORDER BY dninie DESC;"
            )

        filas = cursor.fetchall()
        for dninie, nombre, apellidos, email in filas:
            arbol.insert("", "end", values=(dninie, nombre, apellidos, email))
        status_var.set(f"Clientes cargados: {len(filas)}")
        actualizar_estado_boton()
    except Error as e:
        status_var.set(f"Error al cargar: {e}")
        messagebox.showerror("Error de consulta", str(e))

def actualizar_estado_boton(event=None):
    seleccion = arbol.selection()
    btn_eliminar.config(state="normal" if seleccion else "disabled")

arbol.bind("<<TreeviewSelect>>", actualizar_estado_boton)

def eliminar_clientes():
    seleccion = arbol.selection()
    if not seleccion:
        status_var.set("No hay clientes seleccionados para eliminar.")
        return

    # Recoger DNIs/NIEs únicos de la selección
    dnis = []
    for iid in seleccion:
        vals = arbol.item(iid, "values")
        if vals and vals[0] not in dnis:
            dnis.append(vals[0])

    if not dnis:
        status_var.set("No se pudieron leer los DNI/NIE seleccionados.")
        return

    if not messagebox.askyesno(
        "Confirmar eliminación",
        f"Se eliminarán {len(dnis)} cliente(s) por DNI/NIE.\n¿Deseas continuar?",
    ):
        return

    try:
        # Generar placeholders para IN (%s, %s, ...)
        placeholders = ", ".join(["%s"] * len(dnis))
        query = f"DELETE FROM clientes WHERE dninie IN ({placeholders});"
        cursor.execute(query, tuple(dnis))
        afectados = cursor.rowcount
        conexion.commit()
        status_var.set(f"Eliminados {afectados} cliente(s).")
        cargar_clientes()
    except Error as e:
        status_var.set(f"Error al eliminar: {e}")
        messagebox.showerror("Error al eliminar", str(e))

btn_eliminar.config(command=eliminar_clientes)

# Carga inicial
cargar_clientes()

# Barra de estado
status_bar = tb.Label(root, textvariable=status_var, anchor=W, bootstyle="inverse-secondary")
status_bar.pack(fill=X, side="bottom")

def on_close():
    try:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()
    finally:
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()

