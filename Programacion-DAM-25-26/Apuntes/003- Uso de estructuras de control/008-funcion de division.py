def hazdivision(dividendo,divisor):
    resultado = dividendo/divisor
    return resultado
    
print(hazdivision(4,3))

for i in range(-100,100):
    for j in range(-100,100):
        hazdivision(i,j)
        
print("todo ha sido correcto")
