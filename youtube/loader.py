from pytube import YouTube
from pytube.cli import on_progress
from termcolor import colored


DELIMITER = f'{"*"*80}'  # Delimiter used to format output text


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


def download_progressive_video(url, filename='video'):
    print(colored('Progressive video in .mp4 format downloading...'))
    try:
        YouTube(url=url, on_progress_callback=on_progress).streams.\
            filter(progressive=True, file_extension='mp4').\
            order_by('resolution').\
            desc().\
            first().\
            download(filename=filename, skip_existing=False)
    except Exception as error:
        print(f'Some error occured: {error}')
    else:
        print(colored('\nVideo was successfully downloaded!\n', 'green'))


def download_mp4_video(url, filename='video'):
    print(colored('Video in highest available resolution in .mp4 format '
                  'downloading...'))
    try:
        YouTube(url=url, on_progress_callback=on_progress).streams.\
            filter(progressive=False, only_video=True, file_extension='mp4').\
            order_by('resolution').\
            desc().\
            first().\
            download(filename=filename, skip_existing=False)
    except Exception as error:
        print(f'Some error occured: {error}')
    else:
        print(colored('\nVideo in .mp4 format was successfully downloaded!\n',
                      'green'))


def download_mp4_audio(url, filename='audio'):
    print(colored('Audio in highest available bitrate in .mp4 format '
                  'downloading...'))
    try:
        YouTube(url=url, on_progress_callback=on_progress).streams.\
            filter(progressive=False, only_audio=True, file_extension='mp4').\
            order_by('abr').\
            desc().\
            first().\
            download(filename=filename, skip_existing=False)
    except Exception as error:
        print(f'Some error occured: {error}')
    else:
        print(colored("\nAudio in .mp4 format was successfully downloaded!\n",
                      'green'))


url = 'https://www.youtube.com/watch?v=dAiuiU6VWNc'


if __name__ == "__main__":
    # download_mp4_video(url)
    # download_mp4_audio(url)
    download_progressive_video(url)
