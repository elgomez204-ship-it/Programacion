tupla = ('manzanas','peras', 'platanos')
## NECESITO METER UNA FRUTA MAS ##
print(tupla)

lista = list(tupla)  ## CONVIERTO UNA TUPLA EN UNA LISTA ##
print(lista)
lista.append('fresas')

## AHORA SUPONGAMOS QUE TENGOP QUE VOLVER A LA TUPLA ##
nuvea_tupla = tuple(lista)
print(nuvea_tupla)
