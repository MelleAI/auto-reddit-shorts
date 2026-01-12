# scripts/summarize.py
import os
import openai

openai.api_key = os.getenv("OPENAI_KEY")

def summarize_story(text, max_words=100):
    """Summerar Reddit-story till kort text för YouTube Shorts"""
    prompt = f"Summarize this Reddit story in {max_words} words for a YouTube Short:\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    summary = response.choices[0].message.content.strip()
    return summary
