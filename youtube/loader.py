from pytube import YouTube
from pytube.cli import on_progress
from termcolor import colored
import re
from pprint import pprint

from youtube.files import remove_temp_files
from youtube.mpeg import merge_mp4_audio_and_video, convert_audio_to_mp3


PROFILES = {
    'progressive': {
        'intro_message': 'Progressive video in .mp4 format downloading...',
        'params': {
            'progressive': True,
            'file_extension': 'mp4'
        },
        'order_by': 'resolution',
        'out_message': '\nVideo was sussessfully downloaded!\n'
    },
    'video': {
        'intro_message': '.mp4 video in highest available resolution '
                         'downloading...',
        'params': {
            'progressive': False,
            'only_video': True,
            'file_extension': 'mp4'
        },
        'order_by': 'resolution',
        'out_message': '\n.mp4 video was successfully downloaded!\n'
    },
    'audio': {
        'intro_message': '.mp4 audio in highest available bitrate '
                         'downloading...',
        'params': {
            'progressive': False,
            'only_audio': True,
            'file_extension': 'mp4'
        },
        'order_by': 'abr',
        'out_message': '\n.mp4 audio was successfully downloaded!\n'
    }
}


def get_filename(url: str):
    """Validate if URL is ever exists and return output filename.

    Args:
        url (str): some YouTube URL

    Returns:
        [str]: output filename
    """
    try:
        yt = YouTube(url=url)
        title = re.sub(r'[^\w\s-]', '', yt.title)  # remove all symbols
        title = re.sub(r'\s+', ' ', title)  # remove recurring spaces
        publish_date = yt.publish_date.strftime('%Y-%m-%d')
        slug = yt.video_id
    except Exception:
        print(f'ERROR: Video at requested url "{url}" does not exist.')
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
        print(f'Some error occured: {err}')
    else:
        return list(yt)  # 'list' here required to format output while printing


def download(url: str, settings: dict, filename: str):
    print(colored(settings['intro_message']))
    try:
        YouTube(url=url, on_progress_callback=on_progress).streams.\
            filter(**settings['params']).\
            order_by(settings['order_by']).\
            desc().\
            first().\
            download(filename=filename, skip_existing=False,
                     timeout=10, max_retries=5)
    except Exception as error:
        print(f'Some error occured: {error}')
    else:
        print(colored(settings['out_message'], 'green'))


def load_hq_video(url: str):
    # Get output filename
    filename = get_filename(url=url)

    # Remove old files if exists and download audio and video files
    remove_temp_files('audio', 'video')
    download(url=url, settings=PROFILES['audio'], filename='audio')
    download(url=url, settings=PROFILES['video'], filename='video')

    # Merge output and video files
    merge_mp4_audio_and_video(audio_file='audio', video_file='video',
                              output_filename=filename)

    # Remove temp files
    remove_temp_files('audio', 'video')


def load_hq_audio(url: str):
    # Get output filename
    filename = get_filename(url=url)

    # Remove old file if exist and download mp4 audio file
    remove_temp_files('audio')
    download(url=url, settings=PROFILES['audio'], filename='audio')

    # Convert mp4 file into mp3 file
    convert_audio_to_mp3(audio_file='audio', output_filename=filename)

    # Remove temp file
    remove_temp_files('audio')


def load_progressive(url: str):
    # Get output filename
    filename = get_filename(url=url)

    # Remove old file (not temp!) with the same name if it ever exist,
    # and download video in progressive format
    remove_temp_files(filename)
    download(url=url, settings=PROFILES['progressive'], filename=filename)


url2 = 'https://www.youtube.com/watch?v=IMLwb8DIksk'
url = 'https://www.youtube.com/watch?v=lskdjflsx4Xf4mmbecEM'
url3 = 'https://www.youtube.com/watch?v=RaqSk9S6WY0'


if __name__ == "__main__":
    print(get_filename(url=url))

    pprint(list_streams(url=url2, settings=PROFILES['progressive']))
    pprint(list_streams(url=url2, settings=PROFILES['video']))
    pprint(list_streams(url=url2, settings=PROFILES['audio']))

    download(url=url2, settings=PROFILES['audio'], filename='audio')
    download(url=url2, settings=PROFILES['video'], filename='video')
    download(url=url2, settings=PROFILES['progressive'], filename='progr')
