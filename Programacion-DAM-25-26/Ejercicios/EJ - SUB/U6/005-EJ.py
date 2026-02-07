'''
	Validador de Codigo Postal
	v0.1 Valentín De Gennaro
'''
## IMPORTAMOS LA LIBRERIA NECESARIA ##
import re

## DEFINIMOS EL PATRON PARA VALIDAR EL CODIGO POSTAL ##
patron = r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+ \d+[A-Za-z]? \d{5}$'

## DEFINIMOS LA DIRECCIÓN MAL Y LA BIEN ##
direccion_mal = "Calle Mayor"
direccion_bien = "Calle Mayor 10 46005"

## MOSTRAMOS LA INFORMACIÓN AL USUARIO ##
print(re.match(patron, direccion_mal))
print(re.match(patron, direccion_bien))
