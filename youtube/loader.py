#!/usr/bin/env python3

from pytubefix import YouTube
from pytubefix.cli import on_progress
from termcolor import colored
import re
from youtube.files import remove_files
from youtube.mpeg import merge_mp4_audio_and_video, convert_audio_to_mp3
from youtube.format import shorten_name

from urllib.error import HTTPError
from random import randrange
from time import sleep


PROFILES = {
    'progressive': {
        'intro_message': 'file in highest available progressive resolution...',
        'params': {
            'progressive': True,
            'file_extension': 'mp4'
        },
        'order_by': 'resolution',
        'out_message': 'Progressive MP4 file successfully downloaded!'
    },
    'video': {
        'intro_message': '.mp4 video file in highest available resolution...',
        'params': {
            'progressive': False,
            'only_video': True,
            'file_extension': 'mp4'
        },
        'order_by': 'resolution',
        'out_message': '.mp4 video file was successfully downloaded!'
    },
    'audio': {
        'intro_message': 'audio file in highest available bitrate...',
        'params': {
            'progressive': False,
            'only_audio': True,
            'file_extension': 'mp4'
        },
        'order_by': 'abr',
        'out_message': 'Audio track successfully downloaded...'
    }
}


def get_filename(url: str):
    """Validate if URL is ever exists and return output filename.

    Args:
        url (str): some YouTube URL

    Returns:
        [str] or [None]: output filename or None if URL is not correct
    """
    try:
        yt = YouTube(url=url)
        title = re.sub(r'[^\w\s-]', '', yt.title)  # remove all symbols
        title = re.sub(r'\s+', ' ', title)  # remove recurring spaces
        publish_date = yt.publish_date.strftime('%Y-%m-%d')
        slug = yt.video_id
    except HTTPError:
        print(colored(f'HTTP Error 404: url "{url}" not found!\n', 'red'))
        return None
    except Exception as e:
        print(colored(f'Error: some unexpected error occured - "{e}"', 'red'))
        return None
    else:
        return f'{publish_date} - {title} [{slug}]'


def list_all_streams(url):
    return YouTube(url=url).streams


def list_streams(url: str, settings: dict):
    try:
        yt = YouTube(url=url).streams.\
            filter(**settings['params']).\
            order_by(settings['order_by']).\
            desc()
    except Exception as err:
        print(f'Some error occured while listing streams: {err}')
    else:
        return list(yt)  # 'list' here required to format output while print


def download(url: str, settings: dict, filename: str):
    try:
        yt = YouTube(url=url, on_progress_callback=on_progress).streams.\
            filter(**settings['params']).\
            order_by(settings['order_by']).\
            desc().\
            first()
    except Exception as error:
        print(f'Some error occured while downloading: {error}')
    else:
        print(
            colored(f'Downloading "{shorten_name(yt.title)}" '
                    f'{settings["intro_message"]}'))
        yt.download(filename=f'{filename}.mp4', skip_existing=False,
                    timeout=10, max_retries=5)
        print(colored(f'\n{settings["out_message"]}', 'blue'))


def load_hq_video(url: str):
    # Get output filename
    filename = get_filename(url=url)

    # Break execution if 'filename' return None
    if filename is None:
        return

    # Remove old and temp files if exists, then download audio and video files
    remove_files('audio.mp4', 'video.mp4', f'{filename}.mp4')
    download(url=url, settings=PROFILES['audio'], filename='audio')
    download(url=url, settings=PROFILES['video'], filename='video')

    # Merge output and video files
    merge_mp4_audio_and_video(audio_file='audio', video_file='video',
                              output_filename=filename)

    # Print summary message
    print(colored(f'Video was saved as "{shorten_name(filename)}.mp4"!',
                  'green'))

    # Remove temp files
    remove_files('audio.mp4', 'video.mp4')

    # Print empty line
    print()


def load_hq_audio(url: str):
    # Get output filename
    filename = get_filename(url=url)

    # Break execution if 'filename' return None
    if filename is None:
        return

    # Remove old and temp files if exists, then download mp4 audio file
    remove_files('audio.mp4', f'{filename}.mp3')
    download(url=url, settings=PROFILES['audio'], filename='audio')

    # Convert mp4 file into mp3 file
    convert_audio_to_mp3(audio_file='audio', output_filename=filename)

    # Print summary message
    print(colored(f'MP3 track was saved as "{shorten_name(filename)}.mp3"!',
                  'green'))

    # Remove temp file
    remove_files('audio.mp4')

    # Print empty line
    print()


def load_progressive(url: str):
    # Get output filename
    filename = get_filename(url=url)

    # Break execution if 'filename' return None
    if filename is None:
        return

    # Remove old file (not temp!) with the same name if it ever exist,
    # and download video in progressive format
    remove_files(f'{filename}.mp4')
    download(url=url, settings=PROFILES['progressive'], filename=filename)

    # Print summary message
    print(colored(f'Video was saved as "{shorten_name(filename)}.mp4"!',
                  'green'))

    # Print empty line
    print()


def make_pause(min: int, max: int):
    timeout = randrange(min, max)
    print(f'Making pause between requests for {timeout} seconds...\n')
    sleep(timeout)


if __name__ == "__main__":
    pass
