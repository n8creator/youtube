#!/usr/bin/env python3

from pytube import Channel, YouTube
from youtube.files import create_file, write_csv, write_data,\
    parse_file, remove_files
from time import sleep
from random import random
from termcolor import colored


CSV_FILENAME = 'youtube.csv'
URLS_FILENAME = 'temp_urls.txt'


def parse_links(channel_url: str, output_filename: str, limit: int = None):
    # Create or replace existed temp file to store parsed url's
    create_file(output_filename)

    # Parse url's and save them into file
    print('Started process of parsing URL\'s from specified channel...')

    counter = 0
    ch = Channel(channel_url)

    if limit is None:
        for url in ch.video_urls:
            write_data(url=url, filename=output_filename)
            counter += 1
    else:
        for url in ch.video_urls[:limit]:  # Reduce by 1
            write_data(url=url, filename=output_filename)
            counter += 1

    # Print output message
    print(colored(f'{counter} links were parsed and saved to '
          f'{output_filename} file.\n', 'green'))


def parse_data(urls_file: str, output_csv: str):
    # Create or replace existed temp file to store parsed url's
    create_file(output_csv)

    # Parse urls from file
    urls = parse_file(filepath=urls_file)
    urls_len = len(urls)

    # Parse URL's data and save result into output file
    counter = 1
    for url in urls:
        yt = YouTube(url=url)
        data = {
            'url': url,
            'date': yt.publish_date.strftime('%Y-%m-%d'),
            'title': yt.title
        }
        write_csv(data=data, filename=output_csv)

        print(colored(f'[{counter} of {urls_len}]: Data for "{url}" were '
                      f'parsed and saved into file'))

        sleep(random())
        counter += 1


def parse_channel(channel_url: str, links_limit: int = None):
    parse_links(channel_url=channel_url,
                output_filename=URLS_FILENAME,
                limit=links_limit)

    parse_data(urls_file=URLS_FILENAME, output_csv=CSV_FILENAME)
    remove_files(URLS_FILENAME)


if __name__ == "__main__":
    pass
