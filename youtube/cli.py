import argparse
import sys
import textwrap


def get_args():

    epilog_text = '''
        Supported combination of arguments and flags:
          youtube
            ├── -s URL               - download video
            ├── -s URL --hq          - download video in HQ format
            ├── -s URL --a           - download audio
            ├── -f FILE              - download video from multiple URL's
            ├── -f FILE --hq         - download video in HQ from multiple URL's
            ├── -f FILE --a          - download audio from multiple URL's
            └── -p CHANNEL_URL --n N - parse info and save data into .csv about
                                       latest N videos from channel

        Pytube issues on GitHub: https://github.com/pytube/pytube/issues
            '''

    parser = argparse.ArgumentParser(
        description='YouTube CLI downloader quick help.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(epilog_text))

    parser.add_argument('-s', default=None, metavar='URL',
                        help='download single video or audio from URL')
    parser.add_argument('-f', default=None, metavar='FILE',
                        help='download multiple items from URL\'s specified \
                            in file')
    parser.add_argument('--hq', action='store_true',
                        help='download video in HQ format')
    parser.add_argument('--a', action='store_true',
                        help='download audio and convert to MP3 format')
    parser.add_argument('-p', default=None, type=str, metavar='URL',
                        help='specify the "channel_url" string like: \
                            "https://www.youtube.com/c/topgtru/videos"')
    parser.add_argument('--n', default=None, type=int, metavar='N',
                        help='specify the number of items, information of \
                            which which will be loaded into .csv file')

    # Print '--help' if no arguments were passed
    if len(sys.argv) == 1:
        parser.print_help()
        parser.exit()

    # Parse & return arguments
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    get_args()
