import os
from termcolor import colored
import csv
import codecs
from youtube.format import shorten_name


def remove_files(*files: str):
    """Remove old or temporary files.
    """
    for file in files:
        if os.path.isfile(file):
            print(colored(f'File "{shorten_name(file)}" was deleted'))
            os.remove(file)


def parse_file(filepath: str) -> list:
    if os.path.isfile(filepath):
        with open(filepath, 'r') as f:
            urls = f.read()
        data = urls.split('\n')  # split data into url's list
        urls_list = list(dict.fromkeys(data))  # remove duplicates
        return list(filter(None, urls_list))  # remove empty
    else:
        exit(
            colored(f'ERROR: Script stopped, file {filepath} does not exist!',
                    'red'))


def create_file(filename: str):
    if os.path.isfile(filename):
        os.remove(filename)
        os.mknod(filename)
        print(colored(f'Old "{filename}" file deleted, new one created.',
                      'red'))
    else:
        os.mknod(filename)
        print(f'Output file "{filename}" created')


def write_csv(data: dict, filename: str):
    # Codecs used to receive Excel file compatible with UTF-8
    with codecs.open(filename, 'a', 'utf-8-sig') as f:
        saver = csv.writer(f, delimiter=';', dialect='excel')
        saver.writerow((data['url'],
                        data['date'],
                        data['title'],
                        data['views']))


def write_data(url: str, filename: str):
    with open(filename, 'a') as f:
        f.write(url + '\n')


if __name__ == "__main__":
    pass
