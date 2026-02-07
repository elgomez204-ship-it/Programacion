def hazdivision(dividendo,divisor):
#comprobamos si son numeros
    if isinstance(dividendo, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
#comprobamos que el divisor no es cero
        if divisor != 0:
            resultado = dividendo/divisor
            return resultado
        else:
            resultado = 0
    else:
        try:
            dividendo = float(dividendo)
            divisor = float(divisor)
            resultado = dividendo/divisor
            return resultado
        except:
            return 0
    
print(hazdivision(4, "3"))
