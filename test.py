from PIL import Image
import bs4
import requests
import urllib
from io import StringIO



im = Image.open("C:\\Code\\Python\\Wall-Fresh\\test.jpg")
width , height = im.size
print(width)
print(height)


url = "https://i.redd.it/kbqxz4jmyzn11.png"
print(url)
res = requests.get(url)
print(res.text)
res.raise_for_status()
file = StringIO(urllib.get(url)).read()
im = Image.open(file)
width , height = im.size
print(width)
print(height)
#print(width)

