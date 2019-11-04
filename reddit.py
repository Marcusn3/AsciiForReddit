import ascii
import praw


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
        print("by u/" + author)
        print(divider)
    else:
        print("by u/" + author)
        print(divider)
        continue
