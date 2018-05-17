#this will be the scipt using praw and urrlib to download.

import praw
import bs4
import urllib

#username: Wall-Fresh
#passwored: 123456
#client id: UB3VMr-CTHOaHQ
#secret: zPMe43C4JPelOMb_fwJYhG20mus



# create an object that stores:
# subreddit, number of submissions from subreddit, hot or top

class sub:
    subNum = 0 # the number of subreddits that have been created, static variable


    #contstructor 
    def __init__(self,name,postNum,top):
        self.name = name
        self.postNum = postNum
        self.top = top
        sub.subNum +=1

    #accessors 
    def getName(self):
        return self.name
    def getPostNum(self):
        return self.postNum
    def getTop(self):
        return self.top



# now i can make objects using like s = sub("earthporn","50","True")
#s = sub("earthporn", "50",True)
#print s.getName() # using acessors for good programming practce,
#print s.getPostNum() # for ex, if the fields were private 
#print s.getTop()


numOfSub = 5 # the number of subreddits
subreddits = []
#subreddits[0]= sub("5","6",True)
#print subreddits[0].getTop()
for i in range(2):
    print i 
    #subreddits[i] = sub(tempName,tempNum,tempTop)
    tempName = str(raw_input("What subreddit do you want? (ex: earthporn) "))
    tempNum = int(raw_input("how many entries do you want? (ex: 50) "))
    tempTop = bool(raw_input("do you want top? (defualt is hot, type: True) "))
    temp = sub(tempName,tempNum,tempTop) 
    subreddits.append(temp)

print subreddits[0].getName()

