# scripts/main.py
from fetch_reddit import get_stories
from process import clean, gen_desc, gen_tags
from summarize import summarize_story
from tts import tts
from make_video import make_video
from upload import upload
from thumbnail import create_thumbnail

def run():
    stories = get_stories()
    for i, s in enumerate(stories):
        print("Processing:", s["title"])

        summary = summarize_story(s["text"])
        text = clean(summary)
        audio_file = f"audio{i}.mp3"
        video_file = f"video{i}.mp4"
        thumb_file = f"thumb{i}.png"

        tts(text, audio_file)
        make_video(text, audio_file, video_file)

        create_thumbnail(s["title"], thumb_file)
        hashtags = " ".join(gen_tags(s["text"]))
        title = s["title"]
        desc = f"{summary}\n#reddit #shorts {hashtags}"

        upload(video_file, title, desc, thumb_file)

if __name__ == "__main__":
    run()
