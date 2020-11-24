"""Module Containing Pytube Query Functions"""

from pytube import YouTube
import re


def initializing_feed(url):
    return(YouTube(url))


def get_title(feed):
    """Function Returning Feed Title."""
    title = feed.title
    return(re.sub('[!.?*]', '', title))


def parse_stream(feed, order, **kwargs):
    """Function Accepts User Params and Returns YouTube Stream"""
    stream = feed.streams\
                 .filter(**kwargs)\
                 .order_by(order)\
                 .desc()\
                 .first()
    return(stream)


def get_streams_data(feed, content, extension):

    streams_data = {}

    audio_stream = str(parse_stream(feed,
                                    order='abr',
                                    progressive=False,
                                    only_audio=True,
                                    file_extension=extension))

    audio_itag = re.search(r'itag=\"(\d+)\"', audio_stream).group(1)
    audio_quality = re.search(r'abr=\"(\d*kbps)\"', audio_stream).group(1)

    streams_data['audio'] = {}
    streams_data['audio']['itag'] = audio_itag
    streams_data['audio']['quality'] = audio_quality

    if content == 'video':
        video_stream = str(parse_stream(feed,
                                        order='resolution',
                                        progressive=False,
                                        only_video=True,
                                        file_extension=extension))

        video_itag = re.search(r'itag=\"(\d+)\"', video_stream).group(1)
        video_quality = re.search(r'res=\"(\d*p)\"', video_stream).group(1)

        streams_data['video'] = {}
        streams_data['video']['itag'] = video_itag
        streams_data['video']['quality'] = video_quality

    return streams_data



# def get_stream_data(stream_str):
#     itag = re.search(r'itag=\"(\d+)\"', stream_str).group(1)

#     if 'mime_type="video"' in stream_str:
#         quality = re.search(r'res=\"(\d*p)\"', stream_str).group(1)
#     else:
#         quality = re.search(r'abr=\"(\d*kbps)\"', stream_str).group(1)

#     return(itag, quality)


# <Stream: itag="313" mime_type="video/webm" res="2160p" fps="30fps" vcodec="vp9" progressive="False" type="video">
# <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">




