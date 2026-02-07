'''
    Aplicación de gestión de productos
    v0.1 2025 Valentín Antonio De Gennaro
    Esta aplicación gestiona productos
'''

class Producto():
    def __init__(self):
        self.nombre = ""
        self.precio = 0
        

productos = []

print("Gestor de productos v0.1 Valentín Antonio De Gennaro")
while True:
    print("Selecciona una opción:")
    print("1.-Crear un nuevo producto")
    print("2.-Listar productos")
    print("3.-Actualizar productos")
    print("4.-Eliminar productos")

    opcion = int(input("Escoge tu opción: "))

    if opcion == 1:
        print("Creamos un nuevo producto")
        producto = Producto()
        producto.nombre = input("Introduce el nombre del producto: ")
        producto.precio = input("Introduce el precio del producto: ")
        productos.append(producto)   
    elif opcion == 2:
        print("Vamos a listar productos")
    elif opcion == 3:
        print("Vamos a actualizar productos")
    elif opcion == 4:
        print("Vamos a eliminar productos")


