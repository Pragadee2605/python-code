import qrcode
import image
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
data="https://www.linkedin.com/in/pragadeeswaran-p-0669a9234/"#you can give any link  address
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",black_colour="white")
img.save("project.png")
