#this will be the scipt using praw and urrlib to download.

import praw
import bs4
import urllib

# create an object that stores:
# subreddit, number of submissions from subreddit, hot or top

class sub(object):
    name =""
    postNum =""
    top = None  # note, there will only be top or false, so switching one will
    # switch the other, hot is on default

    #contstructor 
    def __init__(self,name,postNum,top):
        self.name = name
        self.postNum = postNum
        self.top = top

# now i can make objects using like s = sub("earthporn","50","True")
s = sub("earthporn", "50",True)
print sub.name
print sub.postNum
print sub.top
