#Making a new Scraper using PRAW (reddits API ) instead of webscraping
#to dodge the 429 errors and the none-type errors, will still use urllib to download
#secret : 	3vO4C9_g9-YhBinGvlh0Yj7Tjlk
#client_id = hYrt1SKHkaf3iw
#lol this is so much easier than using the parser
import praw


#setting up reddit instance

reddit = praw.Reddit(client_id="hYrt1SKHkaf3iw",
                     client_secret = "3vO4C9_g9-YhBinGvlh0Yj7Tjlk",
                     username="username",
                     password="password",
                     user_agent ="prawexample")

subreddit = reddit.subreddit("EarthPorn")
hot_python = subreddit.hot(limit = 2) # will return the "hottest" python content changing limit will change
# how many come
for submission in hot_python: 
    print submission.url# use dir() to get the all of the elements of the thing
    
