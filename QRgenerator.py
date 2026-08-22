import qrcode

data = input("Enter the text or URL to generate QR code: ")
filename = input("Enter the filename: ")
if not filename.endswith(".png"):
    filename += ".png"

qr = qrcode.QRCode()

qr.add_data(data)
qr.make()

img = qr.make_image(
    fill_color="blue",
    back_color="white"
)

img.save(filename)

print(f"QR code saved successfully as {filename}")