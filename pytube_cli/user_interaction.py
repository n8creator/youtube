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
        print(f">>> URL to be parsed: {url}\n")
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
        print(f">>> {content.title()} will be downloaded.\n")
        return(content)


def get_extension():
    """Function asking user to specify extension of audio/video to be
    downloaded (until he press 'quit' or enters 'mp3' or 'webm' strings)."""

    # Asking user for extension of content to be downloaded
    extension = input('Input extension of content to be downloaded: "mp4" or '
                      '"webm" (or press \'quit\'): ')

    # Checking if entered string equals to 'mp4' or 'webm'
    while not re.search('mp4|webm', extension):

        # Quitting application in case when user entered 'quit'
        if extension == 'quit':
            print('-' * 54)
            print('>>> Application quitting...\n')
            quit()

        # Otherwise asking user to enter 'mpr' or 'webm' or quit application
        extension = input('String you have entered is not valid. Enter '
                          '"mp4" or "webm" (or enter \'quit\'): ')

    # Printing info message if user entered 'mp4' or 'webm' type
    else:
        print('-' * 54)
        print(f">>> Content in .{extension} format will be "
              "downloaded.\n")
        return(extension)


if __name__ == "__main__":
    get_valid_url()
    get_content_type()
    get_extension()
