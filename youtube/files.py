import os


def remove_temp_files(*files: str):
    for file in files:
        if os.path.isfile(f'{file}.mp4'):
            print(f'Deleteng old file {file}.mp4...\n')
            os.remove(f'{file}.mp4')


def parse_file(filepath: str) -> list:
    if os.path.isfile(filepath):
        with open(filepath, 'r') as f:
            urls = f.read()
        data = urls.split('\n')  # split data into url's list
        urls_list = list(dict.fromkeys(data))  # remove duplicate lines
        return list(filter(None, urls_list))  # remove empty values
    else:
        exit(f'ERROR: Script stopped, file {filepath} does not exist!')


if __name__ == "__main__":
    print(parse_file('input.txt'))
