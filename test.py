import bs4 # allows you to use BS4 (HTML/ XML parser) 
import requests # allows downloading 



def getAmazonPrice(url):
    res = requests.get(url) # gets the url from the input and gets a request for it 
    res.raise_for_status() # checkpoint to make sure that the code is downloading the page correctly 
    soup = bs4.BeautifulSoup(res.text , "html.parser")
    elems = soup.select('#buyNewSection > div > div > span > span')
    print elems[0].text
    
url = raw_input("what product would you like to see the price of")
print url

getAmazonPrice(url)
