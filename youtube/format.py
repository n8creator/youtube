from textwrap import shorten


def shorten_name(name: str):
    return shorten(name, width=70, placeholder='***')
