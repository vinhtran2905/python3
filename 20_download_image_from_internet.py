import urllib.request
import random
def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)


download_web_image("https://image.thanhnien.vn/1600/uploaded/thanhchau/2018_04_21/john-0064_ojmh.jpg")