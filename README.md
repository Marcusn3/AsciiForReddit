# Display images from subreddit as ascii images

[![forthebadge](https://forthebadge.com/images/badges/powered-by-electricity.svg)](http://forthebadge.com/)

## Requirements:
- PRAW ( `$ pip install praw` )
- A reddit.com account
- Client ID & Client Secret:

To quote the official Praw Documentation:
> These two values are needed to access Reddit’s API as a script application (see Authenticating via OAuth for other application   > types). If you don’t already have a client ID and client secret, follow Reddit’s First Steps Guide to create them.
- User Agent:

To quote the official PRAW Documentation:
> A user agent is a unique identifier that helps Reddit determine the source of network > requests. To use Reddit’s API, you need a unique and descriptive user agent. The recommended format is <platform>:<app       >   > ID>:<version string> (by u/<Reddit username>). For example, android:com.example.myredditapp:v1.2.3 (by u/kemitche). Read more about > user agents at Reddit’s API wiki page.

## Usage:
1. Enter your details in praw.ini
2. run `$ python3 reddit.py`
3. Input a subreddit
4. Input the number of Posts to display
