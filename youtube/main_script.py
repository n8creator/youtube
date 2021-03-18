from youtube import youtube_parser
from youtube import user_interaction


def process_stream():
    # Ask User To Specify Params for Video to be Downloaded
    params = user_interaction.get_params()

    # Destucturing User-Specified Params
    url, type, extension = params

    # Initializing YouTube Feed
    feed = youtube_parser.initializing_feed(url)

    # Getting Feed Title
    title = youtube_parser.get_title(feed)

    # Downloading Content From YouTube
    if type == 'audio':
        youtube_parser.get_audio(url, type, extension, title)
    if type == 'video':
        youtube_parser.get_video(url, type, extension, title)


if __name__ == "__main__":
    process_stream()
