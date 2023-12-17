import segno
from PIL import Image

filename = "walter_clark.jpg"
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

# print('Resizing %s...' % filename)  # resize the image.
# #im = im.resize((width, width))
#
# print('adding logo to %s...' % filename)
# #im.save('soarLogoSquare.png')
#
# squareBackground = Image.new("RGBA", (width,width),(62,90,145,))
# start_position = (width - height) // 2
# squareBackground.paste(im, (0,start_position))
# # )
#
# squareBackground.save(f"edited_{filename}")

qr_code = "https://www.instagram.com/walterclark5266/"

student_qr = segno.make_qr(qr_code, error="h")
student_qr.to_artistic(background=filename, target=f'QR_{filename}', scale=13)
student_qr.to_artistic(background=filename, target=f'QR_small_{filename}', scale=5)

qrcode = segno.make(qr_code,  error='h')
img = qrcode.to_pil(scale=8).rotate(45, expand=True)
img_2 = qrcode.to_pil(scale=4).rotate(45, expand=True)
img.save('QR_walter_rotated.png')
img_2.save('QR_walter_small_rotated.png')
# student_qr.save(
#     f"dragonboat_festival_logo.png",
#     border=2, scale=10, dark='darkred', light='lightblue'
