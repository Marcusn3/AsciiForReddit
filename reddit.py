from time import sleep
from os import system
import praw
import logging
import ascii

reddit = praw.Reddit("bot1")
auth_status = str(reddit.read_only)
divider = "======================================="
EXTENSIONS = [".jpg", ".jpeg", ".png"]
subreddit = reddit.subreddit(
    input("Which Subreddit should be Scraped? (without /r/)\n")
)
postlimit = int(input("Number of Posts to Scrape?\n"))
print(divider)
for submission in subreddit.hot(limit=postlimit):
    author = str(submission.author)
    url = submission.url
    print(submission.title)
    if any(extension in submission.url for extension in EXTENSIONS):
        output = ascii.loadFromUrl(url)
        print(output)
    else:
        continue
    output = ascii.loadFromUrl(url)
    print("by u/" + author)
    print(divider)


# for submission in reddit.subreddit('all').top('all'):
#    print(submission.title)
# submission.reply(reply_text)
#
# for submission in subreddit.stream.submissions():
#     do something with submission
