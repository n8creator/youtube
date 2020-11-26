from pytube_cli import youtube_parser
from pytube_cli import user_interaction


def process_stream():
    # Ask User To Specify Params for Video to be Downloaded
    params = user_interaction.get_params()

    # Destucturing User-Specified Params
    url, content, extension = params

    # Initializing YouTube Feed
    feed = youtube_parser.initializing_feed(url)

    # Getting Feed Title
    title = youtube_parser.get_title(feed)

    # Downloading Content From YouTube
    if content == 'audio':
        youtube_parser.get_audio(url, content, extension, title)
    if content == 'video':
        youtube_parser.get_video(url, content, extension, title)


if __name__ == "__main__":
    process_stream()
