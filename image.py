from PIL import Image, ImageFilter

img = Image.open('./pokedex/signature.png')

img.thumbnail((400, 400))

img.save('thumbnail.png')

print(img.size)
