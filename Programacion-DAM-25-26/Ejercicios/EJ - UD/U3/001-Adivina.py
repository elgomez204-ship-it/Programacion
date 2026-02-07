'''
	Adivina el número
	v0.1 Valentín Antonio De Gennaro
	La app piensa un número y tienes 6 intentos para adivinarlo
'''
## IMPORTO LA LIBRERIA ##
import random

## DEFINO LAS VARIABLES ##
intentos = 0
maximo_intentos = 6
numero_secreto = random.randint(1,50)

## MUESTRO LA INFORMACIÓN DEL JUEGO ##
print("Estoy eligiendo un número entre el 1 y el 50...")
print("...")
print("...")
print("...")
print("...")
print("Listo, ya lo elegí")
print("Debes adivinar el número que elegí")
print("Tienes 6 intentos")

## COMIENZA EL BUCLE ##
while intentos < maximo_intentos:
    numero = input("Introduce el número: ")
## VERIFICO QUE SEA ENTERO ##
    try:
        entero = int(numero)
    except ValueError:
        print("El número no es entero")
## NO GASTA INTENTO ##
        continue  

## VERIFICO QUE EL NUMERO ESTE DENTRO DEL RANGO ##
    if entero < 1 or entero > 50:
        print("Número fuera del rango establecido (1-50).")
## NO GASTA INTENTO ##
        continue 

    intentos += 1
    assert intentos >= 0, "Contador de intentos negativo"

    if entero == numero_secreto:
        print("Número Correcto, ¡has ganado!")
## TERMINA EL BUCLE SI ACIERTA ##
        break
    elif entero > numero_secreto:
        print("El número es demasiado alto")
    else:
        print("El número es demasiado bajo")

## MUESTRO UNA PISTA AL TERCER INTENTO ##
    if intentos == 3:
        if numero_secreto % 2 == 0:
            print("Pista: El número secreto es par")
        else:
            print("Pista: El número secreto es impar")

## SOLO SE EJECUTA SI PIERDE ##
else:
    print("Has superado el número máximo de intentos, el número que elegi es: ",numero_secreto)
		


		
		
		


		
		
		
		
		
		
		
		
		
		
		
		

		


