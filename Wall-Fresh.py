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


def downloadUrl(url): #this function takes in a url string and downloads it to your pc
    picUrl = url
    picName = url.split("/")[-1]

    if(picName.split(".")[-1] == "jpg" or picName.split(".")[-1] == "png"):
        picName = directory+picName
        print picName
        urllib.urlretrieve(picUrl, picName)
    else:
        if(picUrl.split('/')[2] == "imgur.com"): # its a link to an non i.imgur link

            if(picUrl.split('/')[-2] =="a"): # this indicates an imgur album
                picName = "album error"
                print picName

            else:
                
                picUrl = "https://i.imgur.com/" + picName +".jpg"
                picName = directory+picName+".jpg"
                print picUrl 
                urllib.urlretrieve(picUrl, picName)
        else: # at this point we have hpyer linked stuff
            print "text error" 
#"C:\Users\nnmkh\Downloads\



    #https://www.reddit.com/r/EarthPorn/comments/7eipbx/join_the_battle_for_net_neutrality_dont_let_the/


directory = "C:\\Users\\nnmkh\\Desktop\\Wallpapers\\"
numOfSub = 1 # the number of subreddits
subreddits = []
#subreddits[0]= sub("5","6",True)
#print subreddits[0].getTop()
for i in range(numOfSub):
    #subreddits[i] = sub(tempName,tempNum,tempTop)
    tempName = str(raw_input("What subreddit do you want? (ex: earthporn) "))
    tempNum = int(raw_input("how many entries do you want? (ex: 50) "))
    tempTop = bool(raw_input("do you want top? (defualt is hot, type: True) "))
    temp = sub(tempName,tempNum,tempTop) 
    subreddits.append(temp)



reddit = praw.Reddit(client_id ="UB3VMr-CTHOaHQ",
                     client_secret= "zPMe43C4JPelOMb_fwJYhG20mus",
                     username ="Wall-Fresh",
                     password = "123456",
                     user_agent = "Wall-Fresh-Scraper")


s = reddit.subreddit(subreddits[0].getName()).top(limit = subreddits[0].getPostNum())
for submissions in s:
    #print submissions.url
    if (submissions.stickied!= True): # dosnt go through the sitcked content 
        downloadUrl(submissions.url)
    



