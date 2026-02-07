from PIL import Image

imagen = Image.open("jocarsa.png")

pixel1 = imagen.getpixel((0, 0))

print(pixel1)

