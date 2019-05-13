import pyqrcode
from pyqrcode import QRCode

s="http://amritavarshi.github.io"

url=pyqrcode.create(s)

url.svg("pwqr.svg",scale = 8)
