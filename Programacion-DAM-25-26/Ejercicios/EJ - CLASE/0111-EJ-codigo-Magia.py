'''
	Duelo de magos
	v0.1 Valentín Antonio de Gennaro
'''
################### Pedir edad #####################

edad_mago = input("Introduce la edad del mago: ")
clasificacion_mago = 0
poder_base = 0
print("La edad del mago es: ", edad_mago)

##################Convertir a entero#################

try:
    edad_mago = int(edad_mago)
    print("He convertido la edad correctamente")
    
except:
    edad_mago = 100
    print("No he convertido la edad correctamente, uso 100 años por defecto")
    
################### Clasificacion por edad ############

if edad_mago < 30:
    clasificacion_mago = "Aprendiz"
    
elif edad_mago >= 30 and edad_mago <= 99:
    clasificacion_mago = "Hechicero"
    
elif edad_mago >= 100:
    clasificacion_mago = "Archimago"
    
print("El mago es: ", clasificacion_mago)

############ poder ###################
def poderBase(clasificacion_mago):
    '''
        poderBase
        entradas: clasificacion_mago
        salidas: poder_base
    '''
    poder_base = 0

    if clasificacion_mago == "Aprendiz":
        poder_base = 5
        
    elif clasificacion_mago == "Hechicero":
        poder_base = 8
        
    elif clasificacion_mago == "Archimago":
        poder_base = 10

    print("El poder base de tu", clasificacion_mago, "es:", poder_base)
    return poder_base

# Llamo a la función y guardo el resultado en la variable poder_base
poder_base = poderBase(clasificacion_mago)

################### Duelo con el escudo ###################

# escudo empieza con 15pts
energia_escudo = 15
print("La energía inicial del escudo es:", energia_escudo)

# recorre dos turnos con for
for turno in range(1, 3):
    print("\n---------- Turno", turno, "----------")

    # turno 1 fuego daño = poderbase // 2
    if turno == 1:
        print("El mago lanza un hechizo de FUEGO")
        daño = poder_base // 2
    
    # turno 2 hechizo rayo = daño = poderbase // 3
    else:
        print("El mago lanza un hechizo de RAYO")
        daño = poder_base // 3

    # nos aseguramos de que el daño nunca sea negativo
    if daño < 0:
        daño = 0

    # tras cada daño, print de daño y mayor que cero
    print("El daño provocado al escudo es:", daño)

    # resta el daño al escudo
    energia_escudo = energia_escudo - daño

    # tras ajuste de energia, energia no puede ser menor que cero
    if energia_escudo < 0:
        energia_escudo = 0

    print("La energía del escudo tras el ataque es:", energia_escudo)

################### Salida final ###################

print("\n=========== RESUMEN DEL DUELO ===========")
print("Edad del mago:", edad_mago)
print("Rango del mago:", clasificacion_mago)
print("Poder base del mago:", poder_base)
print("Energía final del escudo:", energia_escudo)

# energia es 0
if energia_escudo == 0:
    print("El escudo ha sido destruido. El duelo ha roto la defensa mágica.")

# energia es mayor que 0, escudo resiste duelo
else:
    print("El escudo resiste el duelo. La barrera mágica sigue en pie.")

