"""Module containing functions to interact with user."""
import re


def get_valid_url():
    """Function asking user for a valid YouTube URL (until he press 'quit' or
    enters valid URL)."""

    # Asking user for Youtube URL to download
    url = input('Input YouTube URL to download or press \'quit\': ')

    # Checking if input URL match YouTube slug
    while not re.search('youtube.com/watch?|youtu.be/', url):

        # Quitting application in case when user entered 'quit'
        if url == 'quit':
            print('-' * 54)
            print('>>> Application quitting...\n')
            quit()

        # Otherwise asking user to input correct url again in while loop
        url = input('URL you have entered is not valid, try again '
                    'or enter \'quit\': ')

    # Printing info message if user entered correct URL to be parsed
    else:
        print('-' * 54)
        print(f">>> URL to be downloaded: {url}\n")
        return(url)


def get_content_type():
    """Function asking user to specify type of content to be downloaded (until
    he press 'quit' or enters 'audio' or 'video')."""

    # Asking user for type of content to be downloaded
    content = input('Input content to be downloaded: "audio" or "video" '
                    '(or press \'quit\'): ')

    # Checking if entered string equals to 'audio' or 'video'
    while not re.search('audio|video', content):

        # Quitting application in case when user entered 'quit'
        if content == 'quit':
            print('-' * 54)
            print('>>> Application quitting...\n')
            quit()

        # Otherwise asking user to input 'audio' or 'video' or quit application
        content = input('String you have entered is not valid. Enter '
                        '"video" or "audio" (or enter \'quit\'): ')

    # Printing info message if user entered 'audio' or 'video' type
    else:
        print('-' * 54)
        print(f">>> {content.title()} was selected.\n")
        return(content)


def get_format():
    """Function asking user to specify format of audio/video to be
    downloaded (until he press 'quit' or enters 'mp3' or 'webm' strings)."""

    # Asking user for format of content to be downloaded
    format = input('Input format of content to be downloaded: "mp4" or '
                   '"webm" (or press \'quit\'): ')

    # Checking if entered string equals to 'mp4' or 'webm'
    while not re.search('mp4|webm', format):

        # Quitting application in case when user entered 'quit'
        if format == 'quit':
            print('-' * 54)
            print('>>> Application quitting...\n')
            quit()

        # Otherwise asking user to enter 'mp4' or 'webm' or quit application
        format = input('String you have entered is not valid. Enter '
                       '"mp4" or "webm format" (or enter \'quit\'): ')

    # Printing info message if user entered 'mp4' or 'webm' format
    else:
        print('-' * 54)
        print(f">>> .{format} format was selected.\n")
        print('*' * 54)
        return(format)


def get_params():
    """Function asking user for video/audio preferences to download and
    returning these preferences as a tuple."""

    # Storing params in variables
    url = get_valid_url()
    content = get_content_type()
    extension = get_format()

    # Returning params in tuple
    return(url, content, extension)


if __name__ == "__main__":
    print(get_params())
