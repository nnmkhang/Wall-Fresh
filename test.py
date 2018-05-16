import bs4 # allows you to use BS4 (HTML/ XML parser) 
import urllib2 # imports pythons native url  downloader library
import urllib
import time # allows the use of the sleep function
# store objects in a hashtable so that you can get constant time when searching for collisions
#path name: C:\Users\nnmkh\Desktop\Wallpapers

# Refer to code academy to find out which tags are what, u know now so it shouldnt be too bad
# figure out a way to reliably get the url to open, keep getting hit with "error 429 too many requests"
# maybe make a website that runs the code, and gives u a zip file containing all the pictures, In the zip file
# there is a text file that writes all names of the links. WHen you want to get new ones but no duplicates
# go back to the website, paste in the textfile and the program will filter through the images in there and exclude
# the images that are already in the textfile.
#option to remove pictures with watermarks

def getUrl(request):
    
    try:
        return urllib2.urlopen(request).read()
    except urllib2.HTTPError,e:
        if( e.code == 429):
            time.sleep(2)
            print "ERROR 429, too many requests. Retrying."
  
            return getUrl(request)
        elif(e.code == 404):
            print "404 Error. Are you sure the url is correct?"
            return

        
##Main Function starts now ##
directory = "C:\\Users\\nnmkh\\Desktop\\Wallpapers\\" # needed the second \ to close all of them. idk why it does that 
url = "https://www.reddit.com/r/wallpapers/top/?sort=top&t=all"
request = urllib2.Request(url)
#html = urllib2.urlopen(request).read()
html = getUrl(request)

soup = bs4.BeautifulSoup(html, "html.parser")
# everything needed is within the <a> class, which gives links, and title
# to get the subreddit, you have to go to the <a href > part

#table = soup.find('div',attrs={'id':'siteTable'}) # parces the site table from reddit, which excludes the top and side stuff
# the attrs = attirubutes and the id and siteTable is what is defined
#the tag div site table is a list of all of the diffrent links ( ea5ch post ) 
table = soup.find('div', attrs = {'id' : 'siteTable'})
#table = soup.find('div', class_=siteTable)


links = table.find_all("div", class_ = "thing")

for link in links: # after write all of the links to a file 
    picUrl= link.get('data-url') # assigns picUrl to the url of the picture
    #print picUrl
    picName = link.get('data-url')
    picName = picName.split('/')[-1] # split turns it into an array, [-1] gets the
    #value without all of the https stuff.
    # now you need to filter all the shit that cant be downloaded, like text posts, albums etc.
    # to counter text posts, check if the last 3 letters arnt "jpg" or "png" or check if the first letter ir "r" because they are relative links
    # to counter albums, check if the last letters are jpg or png also, check if the string at split('/')[-2] is "a" for album
    # also note, files that are under the i.imgur end with.jgp, but imgur does not have the appended .jgp to counter this, check if the first letter is an r/ since there
    # are relative links, then you can check if the 2nd last split after data-url is an "a" for album and omit those. 

    if(picName.split(".")[-1] == "jpg" or picName.split(".")[-1] == "png"):
        picName = directory+picName
        urllib.urlretrieve(picUrl, picName)
    else:
        if(picUrl.split('/')[1] == "r"): # its a hyper link to a text post
            picName = "text error"
        elif(picUrl.split('/')[-2] =="a"): # this indicates an imgur album
            picName = "album error" 
        else: # at this point we need to download the non i.imgur files
            picUrl = "https://i.imgur.com/" + picName +".jpg"
            picName = directory+picName+".jpg"
            urllib.urlretrieve(picUrl, picName)
             
    print picUrl
    print picName
# everything is working at this point, only error is the sometimes the none-type error occurs 
    



