import pyqrcode

data = "https://www.youtube.com/channel/UCI7vdRnuzygmhYXlO8Z1GBQ"

img = pyqrcode.create(data)

img.png('youtube.png',scale=10)