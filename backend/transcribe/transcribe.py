import yt_dlp
import whisper
import os

def transcribe_video(youtube_url: str) -> str:
    # Download audio from YouTube
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    
    # Transcribe with Whisper
    model = whisper.load_model("base")
    result = model.transcribe("audio.mp3")
    
    # Cleanup
    if os.path.exists("audio.mp3"):
        os.remove("audio.mp3")
    
    return result["text"]