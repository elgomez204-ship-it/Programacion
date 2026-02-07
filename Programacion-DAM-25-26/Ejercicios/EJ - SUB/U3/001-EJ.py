'''
    Clasificador de edades
    v0.1 Valentin Antonio De Gennaro
    Clasifica a un jugador segun se edad
'''

############### DECLARAMOS LA VARIABLE Y LE ASIGNAMOS UN VALOR #############
edad_jugador = 21

############### CLASIFICAMOS POR EDADES ##############################
if edad_jugador < 10:
    print("Eres un niño")
elif edad_jugador > 10 and edad_jugador <= 19:
    print("Eres un adolescente")
elif edad_jugador > 20 and edad_jugador <= 30:
    print("Eres un joven")
else:
    print("Ya no eres un joven")
    
