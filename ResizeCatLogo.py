
from PIL import Image

#catIm = Image.open('catlogo.png')
#width, height = catIm.size

#logoIm = catIm.resize((int(width * 0 + 150), (height * 0 + 150)))
#logoIm.save('catlogosized.png')

# create a new image
im = Image.new('RGBA',(264, 415), (1,55,164))
im.save('fondo.png')

body = Image.open('Brian nb.jpg')
body = body.resize((100,100))

im.paste(body, (100,100))
im.save("newfondo.png")