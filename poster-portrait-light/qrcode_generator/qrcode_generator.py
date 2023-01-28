from PIL import Image

import qrcode

Logo_link = "bitmap.png"
logo = Image.open(Logo_link)
basewidth = 175

# adjust image size
wpercent = basewidth / float(logo.size[0])
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    version=2,
    border=0,
    box_size=12,
)

QRcode.add_data("https://youtu.be/ihDTMcn7LWM")

# generating QR code
QRcode.make()

# taking color name from user
QRcolor = "Black"

# adding color to QR code
QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert("RGB")

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)

QRimg.paste(logo, pos)

# save the QR code generated
QRimg.save("posterQR.png")

print("QR code generated!")
