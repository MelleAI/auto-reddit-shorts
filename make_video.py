# scripts/make_video.py
import random
import glob
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, CompositeAudioClip, afx

def make_video(text, audio_file, out_file):
    # Välj slumpmässig gameplay
    bgs = glob.glob("assets/gameplay*.mp4")
    bg_choice = random.choice(bgs)
    bg = VideoFileClip(bg_choice).loop()

    # Ladda TTS
    voice = AudioFileClip(audio_file)

    # Bakgrundsmusik med ducking
    music = AudioFileClip("assets/music.mp3").volumex(0.25)
    music = music.fx(afx.audio_fadein, 1).fx(afx.audio_fadeout, 2)

    mixed_audio = CompositeAudioClip([music, voice.volumex(1.3)])

    # Video subclip matching TTS-duration
    dur = voice.duration
    base = bg.subclip(0, dur).resize((1080,1920))

    # Text-overlay
    txt = (TextClip(text, fontsize=48, color="white",
                    size=(1080,1920), method="caption", align="center")
           .set_duration(dur))

    final = CompositeVideoClip([base, txt]).set_audio(mixed_audio)
    final.write_videofile(out_file, fps=30, codec="libx264", audio_codec="aac")
