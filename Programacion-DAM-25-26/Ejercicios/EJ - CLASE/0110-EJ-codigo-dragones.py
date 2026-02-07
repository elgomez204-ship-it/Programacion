'''
    Duelos de dragones
    v0.2 valentin de gennaro
'''

#En este bloque tomo los datos del usuario #######################

nombre_dragon_a = input("dime el nombre del dragón A: ")
edad_dragon_a = input("dime la edad del dragón A: ")
clasificacion_dragon_a = ""
fuerza_dragon_a = 0
resistencia_dragon_a = 0
print("El nombre del dragon A es:", nombre_dragon_a)
print("La edad del dragon A es:", edad_dragon_a)

nombre_dragon_b = input("dime el nombre del dragón B: ")
edad_dragon_b = input("dime la edad del dragón B: ")
clasificacion_dragon_b = ""
fuerza_dragon_b = 0
resistencia_dragon_b = 0
print("El nombre del dragon B es:", nombre_dragon_b)
print("La edad del dragon B es:", edad_dragon_b)

#En este bloque me aseguro de que son enteros ##################

try:
    edad_dragon_a = int(edad_dragon_a)
    print("He convertido la edad A correctamente")
except:
    edad_dragon_a = 100
    print("No he convertido la edad A correctamente, uso 100 años por defecto")
    
try:
    edad_dragon_b = int(edad_dragon_b)
    print("He convertido la edad B correctamente")
except:
    edad_dragon_b = 100
    print("No he convertido la edad B correctamente, uso 100 años por defecto")
    
#En este bloque clasifico los dragones ########################## 
    
if edad_dragon_a < 50:
    clasificacion_dragon_a = "Joven"
elif edad_dragon_a >= 50 and edad_dragon_a <= 199:
    clasificacion_dragon_a = "Adulto"
elif edad_dragon_a >= 200:
    clasificacion_dragon_a = "Anciano"
print("El dragon A es:", clasificacion_dragon_a)
    
if edad_dragon_b < 50:
    clasificacion_dragon_b = "Joven"
elif edad_dragon_b >= 50 and edad_dragon_b <= 199:
    clasificacion_dragon_b = "Adulto"
elif edad_dragon_b >= 200:
    clasificacion_dragon_b = "Anciano"
print("El dragon B es:", clasificacion_dragon_b)

#En este bloque defino las funciones obligatorias ###############

def calculaFuerzaBase(edad):
    '''
    Calcula una fuerza base segun la edad:
    - Joven (<50): 10 puntos de fuerza
    - Adulto (50-199): 15 puntos de fuerza
    - Anciano (>=200): 12 puntos de fuerza
    '''
    if edad < 50:
        fuerza = 10
    elif edad <= 199:
        fuerza = 15
    else:
        fuerza = 12
    return fuerza


def turnoDeAtaque(fuerza, resistencia_enemigo):
    '''
    Calcula el daño de un ataque en base a la fuerza del atacante
    y la resistencia del enemigo.
    La formula que uso es:
    daño = fuerza - (resistencia_enemigo // 3), minimo 0.
    No hace prints, solo devuelve el daño.
    '''
    daño = fuerza - (resistencia_enemigo // 3)
    if daño < 0:
        daño = 0

    # Aserciones sobre el daño
    assert isinstance(daño, (int, float)), "El daño debe ser numerico"
    assert daño >= 0, "El daño no puede ser negativo"

    return daño

#En este bloque calculo fuerza y resistencia base ################

fuerza_dragon_a = calculaFuerzaBase(edad_dragon_a)
resistencia_dragon_a = fuerza_dragon_a // 2 + 5

fuerza_dragon_b = calculaFuerzaBase(edad_dragon_b)
resistencia_dragon_b = fuerza_dragon_b // 2 + 5

print("Fuerza base del dragon A:", fuerza_dragon_a, "Resistencia base del dragon A:", resistencia_dragon_a)
print("Fuerza base del dragon B:", fuerza_dragon_b, "Resistencia base del dragon B:", resistencia_dragon_b)

################# Ahora los vamos a entrenar ###################################

for dia in range(1, 4):

###################### como entrenar a tu dragon A##############################
    
    if clasificacion_dragon_a == "Joven":
        fuerza_dragon_a += 2
        resistencia_dragon_a += 2
    elif clasificacion_dragon_a == "Adulto":
        fuerza_dragon_a += 1
        resistencia_dragon_a += 1
    elif clasificacion_dragon_a == "Anciano":
        fuerza_dragon_a += 1
        resistencia_dragon_a += 1
    print("Final del dia" , dia)
    print("El dragon A ahora tiene ", fuerza_dragon_a,"de fuerza y ", resistencia_dragon_a, " de resistencia")
    
###################### como entrenar a tu dragon B###############################
    
    if clasificacion_dragon_b == "Joven":
        fuerza_dragon_b += 2
        resistencia_dragon_b += 2
    elif clasificacion_dragon_b == "Adulto":
        fuerza_dragon_b += 1
        resistencia_dragon_b += 1
    elif clasificacion_dragon_b == "Anciano":
        fuerza_dragon_b += 1
        resistencia_dragon_b += 1
    print("Final del dia" , dia)
    print("El dragon B ahora tiene ", fuerza_dragon_b,"de fuerza y ", resistencia_dragon_b, " de resistencia")

##################### En este bloque preparo el duelo ###############################

salud_dragon_a = 40
salud_dragon_b = 40

print("\nComienza el duelo entre", nombre_dragon_a, "y", nombre_dragon_b)
print("Salud inicial A:", salud_dragon_a, "- Salud inicial B:", salud_dragon_b)

turno = 1

#################### Duelo por turnos hasta que uno llegue a 0 #####################

while salud_dragon_a > 0 and salud_dragon_b > 0:
    print("\n--- Turno", turno, "---")

##################### Turno de ataque del dragon A a B ##############################
    print("\nAtaca", nombre_dragon_a)
    for intento in range(1, 3):  # 2 mordiscos por turno
        daño = turnoDeAtaque(fuerza_dragon_a, resistencia_dragon_b)
        salud_dragon_b -= daño
        if salud_dragon_b < 0:
            salud_dragon_b = 0
############### Asercion para asegurarnos de que la salud no sea negativa ############
        assert salud_dragon_b >= 0, "La salud del dragon B no puede ser negativa"
        print("Mordisco", intento, "->", nombre_dragon_a, "hace", daño, "puntos de daño. Salud de", nombre_dragon_b, ":", salud_dragon_b)
        if salud_dragon_b == 0:
            break

    if salud_dragon_b == 0:
        print("\n", nombre_dragon_b, "no puede continuar el combate.")
        break

######################### Turno de ataque del dragon B a A ###########################
    print("\nAtaca", nombre_dragon_b)
    for intento in range(1, 3):  # 2 mordiscos por turno
        daño = turnoDeAtaque(fuerza_dragon_b, resistencia_dragon_a)
        salud_dragon_a -= daño
        if salud_dragon_a < 0:
            salud_dragon_a = 0
################# Asercion para asegurarnos de que la salud no sea negativa ###########
        assert salud_dragon_a >= 0, "La salud del dragon A no puede ser negativa"
        print("Mordisco", intento, "->", nombre_dragon_b, "hace", daño, "puntos de daño. Salud de", nombre_dragon_a, ":", salud_dragon_a)
        if salud_dragon_a == 0:
            break

    if salud_dragon_a == 0:
        print("\n", nombre_dragon_a, "no puede continuar el combate.")
        break

    turno += 1

###################### En este bloque muestro el resumen final ########################

print("\n===== RESUMEN DEL DUELO =====")
print("Dragón A:", nombre_dragon_a)
print("  Edad:", edad_dragon_a, "- Clasificación:", clasificacion_dragon_a)
print("  Fuerza final:", fuerza_dragon_a, "- Resistencia final:", resistencia_dragon_a)
print("  Salud final:", salud_dragon_a)

print("Dragón B:", nombre_dragon_b)
print("  Edad:", edad_dragon_b, "- Clasificación:", clasificacion_dragon_b)
print("  Fuerza final:", fuerza_dragon_b, "- Resistencia final:", resistencia_dragon_b)
print("  Salud final:", salud_dragon_b)

if salud_dragon_a > salud_dragon_b:
    print("\nEl ganador del duelo es:", nombre_dragon_a)
elif salud_dragon_b > salud_dragon_a:
    print("\nEl ganador del duelo es:", nombre_dragon_b)
else:
    print("\nEl duelo termina en empate.")

