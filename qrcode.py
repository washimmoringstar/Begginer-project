import qrcode
data = input("enter the text or url to convert into qr code: ").strip()
filename = input("enter the file name to save the qr code: ").strip()
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(f"{filename}.png")
print("QR code is generated")

