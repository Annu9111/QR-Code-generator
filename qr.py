import qrcode

img=qrcode.make("https://www.youtube.com/channel/UC4xFnWBlNM1G0vEGVc7Ermg")

img.save("qr.png")

