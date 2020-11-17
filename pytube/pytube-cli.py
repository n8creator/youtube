from pytube import YouTube
import os, re

# Asking user for Youtube URL to download:
message = input('Input YouTube URL: ') or 'https://www.youtube.com/watch?v=NeQM1c-XCDc'
print(f"URL to be parsed: {message}")

# Initialize YouTube feed
feed = YouTube(str(message))

# Get Feed Title
feed_title = feed.title
feed_title = re.sub('[!.?*]', '', feed_title)

# Get Video & Audio Stream Data
video_stream = feed.streams\
            .filter(progressive=False, only_video=True, file_extension='mp4')\
            .order_by('resolution')\
            .asc()\
            .first()\
            .download(filename=feed_title, filename_prefix='video')
os.rename(video_stream, f"video-{feed_title}.mp4")
print('video downloaded')

audio_stream = feed.streams\
            .filter(only_audio=True, file_extension='mp4')\
            .order_by('abr')\
            .asc()\
            .first()\
            .download(filename=feed_title, filename_prefix='audio')
os.rename(audio_stream, f"audio-{feed_title}.mp4")
print('audio downloaded')
