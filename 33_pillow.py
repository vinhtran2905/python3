from PIL import Image

img = Image.open('546.jpg')
print(img.size)
print(img.format)

#display image by the default image editor
img.show()
