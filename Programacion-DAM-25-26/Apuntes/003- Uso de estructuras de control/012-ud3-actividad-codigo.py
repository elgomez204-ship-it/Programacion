#docstring
'''
    Programa clasificador de baloncesto
    v0.1 Valentín de Gennaro
    Este programa clasifica categorías por edades
'''
#importaciones
#este programa no requiere importaciones

#declaraciones variables globales
#inicializamos las variables con valores vacíos

#funciones/clases
#en este programa no hay funciones o clases

#función principal

edad = int(input("Introduce tu edad"))
if edad < 8:
    categoria = "pre-mini"
elif edad >=8 and edad < 12:
    categoria = "mini"
elif edad >=12 and edad < 16:
    categoria = "infantil"
elif edad >=16 and edad < 18:
    categoria = "cadete"
elif edad >=18 and edad < 21:
    categoria = "junior"
else:
    categoria = "senior"
 
print("Tu edad es de",edad,"años y tu categoría es",categoria)

if edad > 40:
    print("Eres un veterano en la cancha")
