import bs4 # allows you to use BS4 (HTML/ XML parser) 
import urllib2 # imports pythons native url  downloader library
import urllib
import time # allows the use of the sleep function
# store objects in a hashtable so that you can get constant time when searching for collisions


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


url = "https://www.reddit.com/r/wallpapers/top/"
request = urllib2.Request(url)
#html = urllib2.urlopen(request).read()
html = getUrl(request)

soup = bs4.BeautifulSoup(html, "html.parser")
# everything needed is within the <a> class, which gives links, and title
# to get the subreddit, you have to go to the <a href > part

#table = soup.find('div',attrs={'id':'siteTable'}) # parces the site table from reddit, which excludes the top and side stuff
# the attrs = attirubutes and the id and siteTable is what is defined
#the tag div site table is a list of all of the diffrent links ( each post ) 
table = soup.find('div',class_= "siteTable")# table is an element that has everything
#print table    # use siteTable, using content to test

links = table.find_all("div", class_ = "thing")

for link in links: # after write all of the links to a file 
    picUrl= link.get('data-url') # assigns picUrl to the url of the picture
    print picUrl
    picName = link.get('data-url')
    picName = picName.split('/')[-1] # split turns it into an array, [-1] gets the
    #value without all of the https stuff.
    print picName
    #urllib.urlretrieve(picUrl, picName)
    

# can use urllib.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")

# next step is to use selium to go to the next page, and scrape more. 


 # if u do find_all("a",limit = x) x will be the number of things that you find 


