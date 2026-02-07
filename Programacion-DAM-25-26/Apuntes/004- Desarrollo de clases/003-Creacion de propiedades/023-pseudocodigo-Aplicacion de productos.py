'''
    Aplicación de gestión de productos
    v0.1 2025 Valentín Antonio De Gennaro
    Esta aplicación gestiona productos
'''

## LIBRERÍAS NO ##

## DEFINIMOS CLASES Y FUNCIONES ##

class Producto():
    def __init__(self):
        self.nombre = ""
        self.precio = 0
        
## CREAMOS LAS VARIABLES GLOBALES ##

productos = []

# primero lanzamos un mensaje de bienvenida
print("Gestor de productos v0.1 Valentín Antonio De Gennaro")
# metemos al usuario en un bucle infinito
while True:
# le mostramos al usuario las opciones que tiene
    print("Selecciona una opción:")
    print("1.-Crear un nuevo producto")
    print("2.-Listar productos")
    print("3.-Actualizar productos")
    print("4.-Eliminar productos")
    opcion = int(input("Escoge tu opción: "))
# en función de la opción que coja el usuario
    if opcion == 1:
#o bien creamos un nuevo producto
        print("Creamos un nuevo producto")
        producto = Producto()  #creo una instancia de la clase#
        producto.nombre = input("Introduce el nombre del producto: ") # escribo la propiedad #
        producto.precio = input("Introduce el precio del producto: ") # escribo la propiedad #
        productos.append(producto)          # Y a la lista de productos le añado el producto #
    elif opcion == 2:
#o bien listamos los productos
        print("Vamos a listar productos")
    elif opcion == 3:
#o bien actualizamos los productos
        print("Vamos a actualizar productos")
    elif opcion == 4:
#o bien eliminamos los productos
        print("Vamos a eliminar productos")
# y volvemos a repetir
