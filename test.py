from PIL import Image, ImageFile
import bs4
import requests
import urllib
from io import StringIO



im = Image.open("C:\\Code\\Python\\Wall-Fresh\\test.jpg")
width , height = im.size
#print(width)
#print(height)

url = "https://i.redd.it/x0n5toj5j1o11.jpg"

def getsizes(uri):
    # get file size *and* image size (None if not known)
    file = urllib.request.urlopen(uri)
    size = file.headers.get("content-length")
    if size: size = int(size)
    p = ImageFile.Parser()
    while 1:
        data = file.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            print(p.image.size)
            width = p.image.size[0]
            height = p.image.size[1]
            #print(width)
            #print(height)
            file.close()
            if(height > width or height < 1080 or width < 1920):
                return False
            return True
            
    



if(getsizes(url)):
    print("gotem")
'''
size,width,height = getsizes(url)
print(size)
print(width)
print(height)
'''




# (10965, (179, 188))
'''
file = StringIO(str(urllib.request.urlopen(url).read()))
im2 = Image.open(file)
width,height = im.size
print(width)
print(height)
'''