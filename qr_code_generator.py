import pyqrcode
from pyqrcode import QRCode
# string which represent the QR code
s = "https://trista750321.github.io/personal-site/"
# generate QR code
url = pyqrcode.create(s)
# create and save the png file nameing "mysiteqr.png"
url.svg("my_site.svg", scale = 6)
