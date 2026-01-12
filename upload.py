# scripts/upload.py
import json, os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

def load_creds():
    info = json.loads(os.getenv("YT_OAUTH_JSON"))
    return Credentials.from_authorized_user_info(info)

def video_exists(title):
    """Check if video title already exists on channel"""
    yt = build("youtube", "v3", credentials=load_creds())
    request = yt.search().list(part="snippet", q=title, type="video", maxResults=5)
    response = request.execute()
    for item in response.get("items", []):
        if item["snippet"]["title"].strip().lower() == title.strip().lower():
            return True
    return False

def upload(video_file, title, desc, thumbnail=None):
    if video_exists(title):
        print(f"Duplicate detected, skipping upload: {title}")
        return None

    yt = build("youtube", "v3", credentials=load_creds())
    media = MediaFileUpload(video_file)
    body = {
        "snippet": {
            "title": title,
            "description": desc,
            "categoryId": "24",
            "tags": ["reddit","shorts","story","askreddit","aita","tifu"]
        },
        "status": {"privacyStatus":"public"}
    }
    req = yt.videos().insert(part="snippet,status", body=body, media_body=media)
    resp = req.execute()

    if thumbnail:
        yt.thumbnails().set(videoId=resp["id"], media_body=MediaFileUpload(thumbnail)).execute()

    print(f"Uploaded video: {title}")
    with open("data/youtube_uploaded.txt", "a") as f:
        f.write(title + "\n")
    return resp
