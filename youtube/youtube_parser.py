"""Module Containg Functions to Download & Process Audio/Video"""

from pytube import YouTube
from pytube.cli import on_progress
import re
from ffmpy import FFmpeg
import os


def initializing_feed(url):
    return(YouTube(url))


def get_title(feed):
    """Function Returning Feed Title."""
    title = feed.title
    return(re.sub(r'[^\w\s-]', '', title))


def get_quality(stream):
    stream = str(stream)

    if 'audio' in stream:
        return(re.search(r'abr=\"(\d*kbps)\"', stream).group(1))
    else:
        return(re.search(r'res=\"(\d*p)\"', stream).group(1))


def download_audio(url, content, extension):
    # Initizlizing YouTube Feed to be Downloaded
    audio = YouTube(url, on_progress_callback=on_progress)

    try:
        # Getting Audio Stream Data
        audio_feed = audio.streams\
                .filter(progressive=False,
                        only_audio=True,
                        file_extension=extension)\
                .order_by('abr')\
                .desc()\
                .first()

        # Print Info Message
        print(f"Audio in {get_quality(audio_feed)} downloading...\n")

        # Downloading Audio
        audio_feed.download(filename='audio')

    except EOFError as err:
        print(err)

    else:
        print("\n"*2 + "Audio was successfully downloaded!\n")
        print('-' * 54)


def download_video(url, content, extension):
    # Initizlizing YouTube Feed to be Downloaded
    video = YouTube(url, on_progress_callback=on_progress)

    try:
        # Getting Video Stream Data
        video_feed = video.streams\
                     .filter(progressive=False,
                             only_video=True,
                             file_extension=extension)\
                     .order_by('resolution')\
                     .desc()\
                     .first()

        # Print Info Message
        print(f"Video in {get_quality(video_feed)} downloading...\n")

        # Downloading Audio
        video_feed.download(filename='video')

    except EOFError as err:
        print(err)

    else:
        print("\n"*2 + "Video was successfully downloaded!\n")
        print('-' * 54)


def get_audio(url, type, extension, title):

    # Downloading Audio
    download_audio(url, type, extension)

    # Converting MP4/WEBM Audio to MP3 Format
    output = FFmpeg(
                    inputs={f"audio.{extension}": None},
                    outputs={f"{title}.mp3": None}
                    # TODO Ниже присваивается статическое имя "audio", которое
                    # подавляет ошибку
                    # outputs={f"audio.mp3": None}
                    )
    output.run()

    # Removing Temporary Audio File
    os.remove(f"audio.{extension}")

    # Print Output Text
    print('\n' + '*' * 54)
    print("\n" + "Audio was converted to .mp3!\n")
    print('*' * 54)


def get_video(url, type, extension, title):
    # Downloading Audio & Video
    download_audio(url, type, extension)
    download_video(url, type, extension)

    # Merge MP4/WEBM Audio & Video and Convert them to MP4 Format
    output = FFmpeg(
                    inputs={f"audio.{extension}": None,
                            f"video.{extension}": None
                            },
                    outputs={f"{title}.mp4": None}
                    )
    output.run()

    # Removing Temporary Audio & Video Files
    os.remove(f"audio.{extension}")
    os.remove(f"video.{extension}")

    # Print Output Text
    print("\n" + '*' * 54)
    print("\n" + "Audio and Video had been merged and saved as .mp4!\n")
    print('*' * 54)
