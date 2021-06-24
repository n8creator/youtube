from pytube import YouTube
from pytube.cli import on_progress
from pprint import pprint


def download_progressive(url):
    YouTube(url=url, on_progress_callback=on_progress)\
        .streams\
        .filter(progressive=True)\
        .asc()\
        .last()\
        .download()

urls = [
    'https://www.youtube.com/watch?v=Q4SwkZ5GEzc',
    'https://www.youtube.com/watch?v=vkPLpOPHh1I',
    'https://www.youtube.com/watch?v=WLoNLxwGp4w'
]

if __name__ == "__main__":
    for url in urls:
        download_progressive(url)


    # Print streams
    # print(YouTube('https://www.youtube.com/watch?v=A0L2muGsu-o')\
    #         .streams\
    #         .filter(only_video=True, progressive=False, file_extension='webm')\
    #         # .filter(only_video=True, progressive=False, file_extension='mp4')\
    #         # .filter(progressive=True)\
    #         .order_by('resolution')\
    #         .desc())

    # # print(YouTube('https://www.youtube.com/watch?v=EZQ_RA5KTc8').streams)

    # # # Download `progressive` file [Works fine]
    # url = 'https://www.youtube.com/watch?v=A0L2muGsu-o'
    # YouTube(url, on_progress_callback=on_progress)\
    #     .streams\
    #     .get_by_itag(243)\
    #     .download(timeout=10, max_retries=5)

    # Download `non-progressive` file [Works fine]
    # url ='https://www.youtube.com/watch?v=A0L2muGsu-o'
    # YouTube(url, on_progress_callback=on_progress)\
    #     .streams\
    #     .filter(only_video=True, progressive=False, file_extension='mp4')\
    #     .order_by('resolution')\
    #     .desc()\
    #     .last()\
    #     .download(timeout=10, max_retries=5)

        # .filter(progressive=True)\
        # .filter(only_audio=True)\




