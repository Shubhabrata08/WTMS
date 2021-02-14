import qrcode
from PIL import Image
qr = qrcode.QRCode(
    version=8,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=30,
)
qr.add_data('LP02')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("LP02.jpeg")
