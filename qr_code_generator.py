import qrcode
from PIL import Image

qr=  qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border= 3)
qr.add_data("https://www.amazon.in/")
qr.make(fit= True)
img= qr.make_image(fill_color="black",back_color="white")
img.save("amazon_shopping.png")