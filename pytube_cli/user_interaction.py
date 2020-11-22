"""Module containing functions to interact with user."""
import re


def get_valid_url():
    """Function asks user for for valid YouTube URL until he press 'quit' or
    enters valid URL.

    """

    # Asking user for Youtube URL to download
    parse_url = input('Input YouTube URL to download or press \'quit\': ')

    # Checking if input URL match YouTube slug
    while not re.search('youtube.com/watch?|youtu.be/', parse_url):

        # Quitting application in case when user entered 'quit'
        if parse_url == 'quit':
            print('-' * 54)
            print('>>> Application quitting...\n')
            break

        # Otherwise asking user to input correct url again in while loop
        parse_url = input('URL you have entered is not valid, try again '
                          'or enter \'quit\': ')

    # Printing info message if user entered correct URL to be parsed
    else:
        print('-' * 54)
        print(f">>> URL to be parsed: {parse_url}\n")
        return(parse_url)


if __name__ == "__main__":
    get_valid_url()
