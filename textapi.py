import requests
import json
import praw
import apikey
"""Summarises the Top n posts of "Stories" subreddit using The Text API"""
# Sending text to The Text API to summarise it.
def get_content(content):
    try:
        url = "https://app.thetextapi.com/text/summarize"
        headers = {
            "Content-Type": "application/json",
            "apikey": ""
        }
        body = {
            "text": content
        }
        response = requests.post(url, headers=headers, json= body)
        summary = json.loads(response.text)
        dict_summary[next(i)] = summary["summary"]

    except:
        print("Out of credits.")


#Creating a Reddit instance
r = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret= "CLIENT_SECRET",
    password="password",
    username="username",
    user_agent= "name of the bot etc."
)

current_subreddit = r.subreddit("stories").top()
i = (x for x in range(10))
dict_summary={}



#getting the Submission ID of a reddit post.

submission = (x for x in current_subreddit if not x.stickied)
get_content(next(submission).selftext)

for a in dict_summary:
    print(dict_summary[a])