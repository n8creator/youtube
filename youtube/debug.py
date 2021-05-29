from pytube import YouTube
from pytube.cli import on_progress

if __name__ == "__main__":
    # Print streams
    # print(YouTube('https://www.youtube.com/watch?v=A0L2muGsu-o')\
    #         .streams\
    #         # .filter(only_video=True, progressive=False, file_extension='mp4')\
    #         # .order_by('resolution')\
    #         .filter(only_audio=True)\
    #         .desc()\
    #         .last())

    # Download `progressive` file [Works fine]
    YouTube('https://www.youtube.com/watch?v=A0L2muGsu-o', on_progress_callback=on_progress)\
        .streams\
        .filter(only_video=True, progressive=False, file_extension='mp4')\
        .order_by('resolution')\
        .desc()\
        .last()\
        .download(timeout=10, max_retries=5)

        # .filter(progressive=True)\

        # .filter(only_audio=True)\

    # YouTube('https://www.youtube.com/watch?v=A0L2muGsu-o', on_progress_callback=on_progress)\
    #     .streams\
    #     .filter(progressive=True)\
    #     .asc()\
    #     .last()\
    #     .download()

