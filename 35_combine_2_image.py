from PIL import Image

sister = Image.open('546.jpg')
baby = Image.open('face.jpg')

sister.show()
baby.show()
area = (100,100,200,200)
sister.paste(baby,area)

sister.show()