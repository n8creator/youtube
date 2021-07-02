from pytube import YouTube
from pytube.cli import on_progress
from termcolor import colored


def list_all_streams(url):
    return YouTube(url=url).streams


def list_progressive_streams(url):
    return YouTube(url=url).streams.\
        filter(progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc()


def list_non_progressive_streams(url, type='video'):
    if type == 'audio':
        return YouTube(url=url).streams.\
            filter(progressive=False, only_audio=True).\
            order_by('abr').\
            desc()
    elif type == 'video':
        return YouTube(url=url).streams.\
            filter(progressive=False, only_video=True).\
            order_by('resolution').\
            desc()
    else:
        exit('Only "audio" or "video" are supported!')


def download_it(url: str, settings: dict):
    print(colored(settings['intro_message']))
    try:
        YouTube(url=url, on_progress_callback=on_progress).streams.\
            filter(**settings['params']).\
            order_by(settings['order_by']).\
            desc().\
            first().\
            download(filename=settings['filename'], skip_existing=False)
    except Exception as error:
        print(f'Some error occured: {error}')
    else:
        print(colored(settings['out_message'], 'green'))


PRESETS = {
    'download_progressive_video': {
        'intro_message': 'Progressive video in .mp4 format downloading...',
        'params': {
            'progressive': True,
            'file_extension': 'mp4'
        },
        'order_by': 'resolution',
        'filename': 'video_progressive',
        'out_message': '\nVideo was sussessfully downloaded!\n'
    },
    'download_mp4_video': {
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
    'download_mp4_audio': {
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

url = 'https://www.youtube.com/watch?v=nVliEYIBWFw'


if __name__ == "__main__":
    # download_it(url=url, settings=PRESETS['download_mp4_video'])
    # download_it(url=url, settings=PRESETS['download_mp4_audio'])
    download_it(url=url, settings=PRESETS['download_progressive_video'])
