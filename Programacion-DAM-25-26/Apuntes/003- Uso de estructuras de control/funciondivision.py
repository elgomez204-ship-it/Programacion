def hazdivision(dividendo,divisor):
    '''
        funcion de division
        entradas: dividendo y divisor que se esperan que sean numericos
        salidas: resultado de la division como numeros (o cero si hay fallo)
        capturas de error:
         1. si es numerico
         2. si se puede convertir a numero
         3. si no es division entre cero
    '''
#comprobamos si son numeros
    print("entramos en la funcion")
    if isinstance(dividendo, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
        print("parece que los parametros son numeros")
#comprobamos que el divisor no es cero
        if divisor != 0:
            print("parece que los puedo dividir")
            resultado = dividendo/divisor
            return resultado
        else:
            print("no puedo dividir porque el divisor es cero")
            resultado = 0
    else:
        print("los parametros no son numeros, pero voy a intentar convertirlos")
        try:
            print("intento convertir a numeros con exito")
            dividendo = float(dividendo)
            divisor = float(divisor)
            resultado = dividendo/divisor
            return resultado
        except:
            print("he intentado convertir a numeros, pero no he podido")
            return 0
