# scripts/process.py
import textwrap
import openai, os

openai.api_key = os.getenv("OPENAI_KEY")

def clean(text, limit=700):
    """Rensar och förkortar texten för video captions"""
    t = text.replace("\n", " ").strip()
    return t[:limit] + ("..." if len(t) > limit else "")

def gen_desc(full_text):
    """Genererar beskrivning med preview och hashtags"""
    preview = clean(full_text, 200)
    return textwrap.dedent(f"""
    A wild Reddit story narrated with AI voice.
    Source: Reddit
    Preview: {preview}
    #reddit #story #shorts #askreddit #aita #tifu
    """).strip()

def gen_tags(text):
    """Genererar hashtags baserat på storyn via OpenAI"""
    prompt = f"Suggest 5 relevant hashtags for this story: {text}"
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    tags = resp.choices[0].message.content.strip().split()
    return [t for t in tags if t.startswith("#")]
