import bs4 # allows you to use BS4 (HTML/ XML parser) 
import urllib2 # imports pythons native url  downloader library
# store objects in a hashtable so that you can get constant time when searching for collisions


# Refer to code academy to find out which tags are what, u know now so it shouldnt be too bad
# figure out a way to reliably get the url to open, keep getting hit with "error 429 too many requests"
# maybe make a website that runs the code, and gives u a zip file containing all the pictures, In the zip file
# there is a text file that writes all names of the links. WHen you want to get new ones but no duplicates
# go back to the website, paste in the textfile and the program will filter through the images in there and exclude
# the images that are already in the textfile.


url = "https://www.reddit.com/r/all/top/"
request = urllib2.Request(url)
html = urllib2.urlopen(request).read()

soup = bs4.BeautifulSoup(html, "html.parser")
# everything needed is within the <a> class, which gives links, and title
# to get the subreddit, you have to go to the <a href > part

#table = soup.find('div',attrs={'id':'siteTable'}) # parces the site table from reddit, which excludes the top and side stuff
# the attrs = attirubutes and the id and siteTable is what is defined
for table in soup.find('div',attrs={'id':'siteTable'}):
    for table in soup.find('div' ,attrs= {'class'}):
        print(table.get('data-url'))

 # if u do find_all("a",limit = x) x will be the number of things that you find 
    








# make an object which stores: url,title, subreddit
'''
 class pic(object):
     url = ""
     title = ""
     subreddit = ""

     def __init__(self,url,title,subreddit):
         self.url = url
         self.title = title
         self.subreddit = subreddit

'''
