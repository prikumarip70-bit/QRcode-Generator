import qrcode
from PIL import Image

data = input("Enter the text or URL to generate QR code: ")

filename=input("Enter the filename : ")

qr= qrcode.QRCode()
qr.add_data(data)
qr.make()

img = qr.make_image(fill_color="blue",
                    back_color="white"
).convert("RGB")

logo=Image.open("logo.png")
logo = logo.resize((100, 100))
pos = (
    (img.width - logo.width) // 2,
    (img.height - logo.height) // 2
)

img.paste(logo, pos)



img.save(filename)
print(f"QRcode save in {filename}")
