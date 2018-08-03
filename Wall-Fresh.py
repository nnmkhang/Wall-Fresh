import os.path
import praw
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
        #print picName
        urllib.request.urlretrieve(picUrl, picName)
    else:
        if(picUrl.split('/')[2] == "imgur.com"): # its a link to an non i.imgur link

            if(picUrl.split('/')[-2] =="a"): # this indicates an imgur album
                picName = "Error, This is an album, not downloading"

                print (picName)

            else:
                
                picUrl = "https://i.imgur.com/" + picName +".jpg"
                picName = directory+picName+".jpg"
                #print picUrl 
                urllib.request.urlretrieve(picUrl, picName)
        else: # at this point we have hpyer linked stuff
            print ("Error, this is a text post, not downloading" )


total =0
count =0 
#directory = "C:\\Users\\nnmkh\\Desktop\\Wallpapers\\"
numOfSub = int(input("How many diffrent subreddits will you be taking photos from? "))
directory = input("Download location?(copy paste directory path and add a '\\' at the end) ex: C:\\Users\\nnmkh\\Desktop\\Wallpapers\\")
#numOfSub = 1 # the number of subreddits
subreddits = []

for i in range(numOfSub):
    #subreddits[i] = sub(tempName,tempNum,tempTop)
    tempName = str(input("What subreddit do you want? (ex: earthporn) "))
    tempNum = int(input("how many entries do you want? (ex: 50) "))
    tempTop = input("do you want hot or top? ").lower()
    temp = sub(tempName,tempNum,tempTop) 
    subreddits.append(temp)



reddit = praw.Reddit(client_id ="UB3VMr-CTHOaHQ",
                     client_secret= "zPMe43C4JPelOMb_fwJYhG20mus",
                     username ="Wall-Fresh",
                     password = "123456",
                     user_agent = "Wall-Fresh-Scraper")
for x in range(numOfSub):
    total += subreddits[x].getPostNum()


for x in range (numOfSub):
    if(subreddits[x].getTop() == "top"):
        lim = subreddits[x].getPostNum()
        s = reddit.subreddit(subreddits[x].getName()).top(limit = lim)
        for submissions in s:
        #print submissions.url
            if (submissions.stickied!= True): # dosnt go through the sitcked content 
                downloadUrl(submissions.url)
                count += 1
               # print("Downloading in progress, %d/%d") %(count,total)
        
    elif(subreddits[x].getTop() == "hot"):
        s = reddit.subreddit(subreddits[x].getName()).hot(limit = subreddits[x].getPostNum())
        for submissions in s:
        #print submissions.url
            if (submissions.stickied!= True): # dosnt go through the sitcked content 
                downloadUrl(submissions.url)
                count += 1
               # print("Downloading in progress, %d/%d")%(count,total)

    

print("Download Complete!")
input("Press Enter to close") 

