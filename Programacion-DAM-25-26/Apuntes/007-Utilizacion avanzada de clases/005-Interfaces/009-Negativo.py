from PIL import Image

imagen = Image.open("jocarsa.png")

anchura,altura = imagen.size					## COJO ALTURA Y ANCHURA

for x in range(0,anchura):						## REPASO LA ANCHURA
	for y in range(0,altura):					## REPASO LA ALTURA
		pixel = imagen.getpixel((x,y))			## COJO CADA PIXEL
## PRIMERO LEO LOS COMPONENTES DE COLOR ##
		rojo = pixel[0]
		verde = pixel[1]
		azul = pixel[2]	
## AHORA LE SUBO EL TONO DE COLOR (ACLARO) ##
		rojo = 255 - rojo
		verde = 255 - verde
		azul = 255 - azul	
## Y SOBREESCRIBO EL COLOR ##
		imagen.putpixel((x, y), (rojo, verde, azul)) # ESTO ES CORRECTO
    
imagen.save("modificado1.png")	

