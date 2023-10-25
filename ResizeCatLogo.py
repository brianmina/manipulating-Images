
from PIL import Image

catIm = Image.open('catlogo.png')
width, height = catIm.size

logoIm = catIm.resize((int(width * 0 + 150), (height * 0 + 150)))
logoIm.save('catlogosized.png')