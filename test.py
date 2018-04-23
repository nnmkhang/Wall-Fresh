import bs4 # allows you to use BS4 (HTML/ XML parser) 
import urllib2 # imports pythons native url  downloader library
# store objects in a hashtable so that you can get constant time when searching for collisions 
url = "https://www.reddit.com/r/all/top/"
request = urllib2.Request(url)
html = urllib2.urlopen(request).read()

soup = bs4.BeautifulSoup(html, "html.parser")
# everything needed is within the <a> class, which gives links, and title
# to get the subreddit, you have to go to the <a href > part

#table = soup.find('div',attrs={'id':'siteTable'}) # parces the site table from reddit, which excludes the top and side stuff
# the attrs = attirubutes and the id and siteTable is what is defined
for table in soup.find('div',attrs={'id':'siteTable'}):
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
