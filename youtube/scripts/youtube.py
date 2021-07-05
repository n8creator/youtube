#!/usr/bin/env python3

from youtube.cli import get_args
from youtube.loader import load_hq_video, load_hq_audio, load_progressive
from youtube.parser import parse_channel
from youtube.files import parse_file


def main():
    args = get_args()

    # Process single URL
    if args.s:
        url = args.s
        if args.hq:
            load_hq_video(url=url)
        elif args.a:
            load_hq_audio(url=url)
        else:
            load_progressive(url=url)

    # Process multiple URL's loaded from file
    elif args.f:
        urls_list = parse_file(args.f)
        for url in urls_list:
            if args.hq:
                load_hq_video(url=url)
            elif args.a:
                load_hq_audio(url=url)
            else:
                load_progressive(url=url)

    # Parse info about videos into .csv file
    elif args.p:
        if args.n:
            parse_channel(channel_url=args.p, links_limit=args.n)
        else:
            parse_channel(channel_url=args.p)


if __name__ == "__main__":
    main()
