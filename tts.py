# scripts/tts.py
import asyncio
from edge_tts import Communicate

async def _speak(text, outfile):
    await Communicate(text, voice="en-US-JennyNeural").save(outfile)

def tts(text, outfile):
    asyncio.run(_speak(text, outfile))
