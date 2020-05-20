from PIL import Image,ImageDraw
import qrcode
data="https://facebook.com"
img=qrcode.make(data)
img.save("ur qrcode.png")