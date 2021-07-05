import os
from termcolor import colored


def remove_files(*files: str):
    """Remove old or temporary files.
    """
    for file in files:
        if os.path.isfile(file):
            print(colored(f'File "{file}" was deleted'))
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


if __name__ == "__main__":
    pass
