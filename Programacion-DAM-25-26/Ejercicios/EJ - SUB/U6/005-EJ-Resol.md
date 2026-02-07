En este ejercicio vamos a crear una app para validar direcciones postales usando expresiones regulares.

---

Para desarrollar este ejercicio primero vamos a importar la libreria necesaria:
```
	import re
```
Luego vamos a definir el patrón que vamos a usar para validar las direcciones postales:
```
	patron = r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+ \d+[A-Za-z]? \d{5}$'
```
Luego introducimos una dirección mal y una bien:
```
	direccion_mal = "Calle Mayor"
	direccion_bien = "Calle Mayor 10 46005"
```
Y por ultimo usamos la función `re.match()` para verificar si una dirección postal cumple con el patrón definido:
```
	print(re.match(patron, direccion_mal))
	print(re.match(patron, direccion_bien))
```
A continuación el codigo completo:
```
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
```

---

**NOTAS:**
- El patrón usado permite validar calles con acentos y caracteres de las direcciones de España.
- `re.match()` solo valida si la cadena cumple todo el patrón desde el inicio, ideal para este tipo de comprobaciones.
- Si una dirección no cumple el formato exacto, devuelve None, lo cual facilita detectar errores rápidamente.
