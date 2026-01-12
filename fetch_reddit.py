# scripts/fetch_reddit.py
import praw, random, os

SUBS = [
    "AskReddit",
    "nosleep",
    "tifu",
    "relationship_advice",
    "AmItheAsshole"
]

USED_PATH = "data/used_ids.txt"

def already_used(post_id):
    if not os.path.exists(USED_PATH):
        return False
    with open(USED_PATH) as f:
        return post_id in f.read().splitlines()

def mark_used(post_id):
    with open(USED_PATH, "a") as f:
        f.write(post_id + "\n")

def get_stories(limit=30):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_ID"),
        client_secret=os.getenv("REDDIT_SECRET"),
        user_agent="AutoShortsBot"
    )

    posts = []
    for sub in SUBS:
        for p in reddit.subreddit(sub).hot(limit=limit):
            if not p.stickied and len(p.selftext) > 200 and not already_used(p.id):
                posts.append({"id": p.id, "title": p.title, "text": p.selftext})

    random.shuffle(posts)
    picks = posts[:3]
    for p in picks:
        mark_used(p["id"])
    return picks
