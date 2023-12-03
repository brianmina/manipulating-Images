import segno
from PIL import Image

filename = "SOAR.png"
im = Image.open(filename)
width, height = im.size

# check if the image need to be resized.
#
# if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
#     # calculate the new width and height to resize to.
#     if width > height:
#         height = int((SQUARE_FIT_SIZE/width) * height)
#         width = SQUARE_FIT_SIZE
#     else:
#         width = int((SQUARE_FIT_SIZE/height) * width)
#         height = SQUARE_FIT_SIZE

print('Resizing %s...' % filename)  # resize the image.
#im = im.resize((width, width))

print('adding logo to %s...' % filename)
#im.save('soarLogoSquare.png')

squareBackground = Image.new("RGBA", (width,width),(62,90,145,))
start_position = (width - height) // 2
squareBackground.paste(im, (0,start_position))
# )

squareBackground.save(f"edited_{filename}")

qr_code = "https://form.jotform.com/233364476993167"
student_qr = segno.make_qr(qr_code)
student_qr.to_artistic(background='edited_SOAR.png', target='dragonboat_festival_team_signup.png', scale=10)
# student_qr.save(
#     f"dragonboat_festival_logo.png",
#     border=2, scale=10, dark='darkred', light='lightblue'
