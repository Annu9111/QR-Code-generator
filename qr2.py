import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("https://www.youtube.com/channel/UC4xFnWBlNM1G0vEGVc7Ermg")
qr.make(fit=True)
img=qr.make_image(fill_color="green",back_color="pink")
img.save("qr2.png")