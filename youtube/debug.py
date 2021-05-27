from pytube import YouTube
from pytube.cli import on_progress
import os

def get_object(url):
    yt = YouTube(url, on_progress_callback=on_progress)
    return yt


def print_streams(obj):
    print(obj.title)
    print(obj.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().last())
    # print(obj.streams)
    # print(obj.streams.filter(file_extension='mp4', only_video=True))
    # print(obj.streams.filter(file_extension='mp4', only_audio=True))


def download_stream(obj, itag):
    yt = obj.streams.get_by_itag(itag)
    # stream.download()
    yt.download(filename='file')
    os.remove(f"file.mp4")


if __name__ == "__main__":
    # yt = get_object('https://www.youtube.com/watch?v=A0L2muGsu-o')
    # yt = get_object('https://www.youtube.com/watch?v=bt1mc-k9uS8')
    # yt = get_object('https://www.youtube.com/watch?v=OuEiUmEMiW0&t=1697s')
    # # yt.streams.last().download(filename='audio')
    print_streams(yt)
    # download_stream(yt, 136)
    yt.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().last().download()


    # YouTube('https://www.youtube.com/watch?v=A0L2muGsu-o&t=402s').streams.fire().download()
    # yt = YouTube('https://www.youtube.com/watch?v=A0L2muGsu-o&t=402s')
    # yt.streams\
    #  .filter(progressive=True, file_extension='mp4')\
    #  .order_by('resolution')\
    #  .asc()\
    #  .first()\
    #  .download()