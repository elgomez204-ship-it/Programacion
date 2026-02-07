from PIL import Image

imagen = Image.open("jocarsa.png")

anchura,altura = imagen.size					## COJO ALTURA Y ANCHURA

for x in range(0,anchura):						## REPASO LA ANCHURA
	for y in range(0,altura):					## REPASO LA ALTURA
		pixel = imagen.getpixel((x,y))			## COJO CADA PIXEL
		print(pixel)							## LO SACO POR PANTALLA

