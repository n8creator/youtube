from pytube import YouTube
from pytube.cli import on_progress
from termcolor import colored
import re
from pprint import pprint


PROFILES = {
    'progressive': {
        'intro_message': 'Progressive video in .mp4 format downloading...',
        'params': {
            'progressive': True,
            'file_extension': 'mp4'
        },
        'order_by': 'resolution',
        'filename': 'video_progressive',
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
        'filename': 'video',
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
        'filename': 'audio',
        'out_message': '\n.mp4 audio was successfully downloaded!\n'
    }
}


def generate_filename(url):
    yt = YouTube(url=url)
    title = re.sub(r'[^\w\s-]', '', yt.title)  # remove all symbols
    title = re.sub(r'\s+', ' ', title)  # remove recurring spaces
    publish_date = yt.publish_date.strftime('%Y-%m-%d')
    slug = yt.video_id

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
        return list(yt)  # 'list' here needed to format output while printing


def download(url: str, settings: dict):
    print(colored(settings['intro_message']))
    try:
        YouTube(url=url, on_progress_callback=on_progress).streams.\
            filter(**settings['params']).\
            order_by(settings['order_by']).\
            desc().\
            first().\
            download(filename=settings['filename'], skip_existing=False,
                     timeout=10, max_retries=5)
    except Exception as error:
        print(f'Some error occured: {error}')
    else:
        print(colored(settings['out_message'], 'green'))


url = 'https://www.youtube.com/watch?v=IMLwb8DIksk'
url2 = 'https://www.youtube.com/watch?v=x4Xf4mmbecE'
url3 = 'https://www.youtube.com/watch?v=RaqSk9S6WY0'


if __name__ == "__main__":
    print(generate_filename(url=url))

    pprint(list_streams(url=url2, settings=PROFILES['progressive']))
    pprint(list_streams(url=url2, settings=PROFILES['video']))
    pprint(list_streams(url=url2, settings=PROFILES['audio']))

    download(url=url2, settings=PROFILES['audio'])
    download(url=url2, settings=PROFILES['video'])
    download(url=url2, settings=PROFILES['progressive'])
