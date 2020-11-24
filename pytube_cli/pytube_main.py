from pytube_cli import pytube_parse
from pytube_cli import user_interaction
# import pytube_cli.pytube_parse


def process_stream():
    # Ask User To Specify Params for Video to be Downloaded
    params = user_interaction.get_params()

    # Destucturing User-Specified Params
    url, content, extension = params

    # Initializing YouTube Feed
    feed = pytube_parse.initializing_feed(url)

    # Getting Feed Title
    title = pytube_parse.get_title(feed)

    # Getting YouTube Streams Data Depending From Type of Content
    streams_data = pytube_parse.get_streams_data(feed, content, extension)


    # Getting YouTube Stream Info
    # itag, quality = pytube_parse.get_stream_data(stream)

    # Returning video_processing()
    print(title)
    print(streams_data)
    # print(stream)
    # print(itag)
    # print(quality)


# # Get Video & Audio Stream Data
# video_stream = feed.streams\
#             .filter(progressive=False, only_video=True, file_extension='mp4')\
#             .order_by('resolution')\
#             .asc()\
#             .first()\
#             .download(filename=title, filename_prefix='video')
# os.rename(video_stream, f"video-{title}.mp4")
# print('video downloaded')

# audio_stream = feed.streams\
#             .filter(progressive=False, only_audio=True, file_extension='mp4')\
#             .order_by('abr')\
#             .asc()\
#             .first()\
#             .download(filename=title, filename_prefix='audio')
# os.rename(audio_stream, f"audio-{title}.mp4")
# print('audio downloaded')


# FFMPEG Callout Example
# ffmpeg -i video.mp4 -i audio.mp4 -c copy output.mp4


if __name__ == "__main__":
    process_stream()
