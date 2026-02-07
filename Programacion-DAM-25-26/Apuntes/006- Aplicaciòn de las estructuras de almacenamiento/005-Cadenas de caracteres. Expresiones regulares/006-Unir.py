# CSV = Coma Separated Values

datos = "uno,dos,tres,cuatro,cinco,seis"

# Primero imprimo la cadena
print(datos)

# Ahora la parto
partido = datos.split(",")

# Ahora imoprimo partido
print(partido)

# Ahora quiero unir todo de nuevo
nueva_cadena = "||".join(partido)

# Ahora imprimo los datos
print(nueva_cadena)


