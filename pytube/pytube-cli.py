from re import sub
import subprocess, sys, re
from subprocess import CompletedProcess, PIPE, STDOUT


# Asking user for Youtube URL to download:
message = input('Input YouTube URL: ') or 'https://www.youtube.com/watch?v=NeQM1c-XCDc'
print(f"URL to be parsed: {message}")

# Calling pytube script & storing output in STDOUT
parsed_itags = subprocess.run(['pytube', message, '--list'], 
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# Converting Byte value to String
parsed_itags = parsed_itags.stdout.decode('utf-8')

# Storing tags to list[]
tag_list = parsed_itags.split('\n')


# Processing lists[] and saving 'itags' and video/audio 'res/abr' into dicts{}
video_formats, audio_formats = {}, {}

for output in tag_list:
    if 'video/mp4' in output and 'res="None"' not in output:
        itag = re.search(r'itag=\"(\d*)\"', output).group(1)
        res = re.search(r'res=\"(\d*)p\"', output).group(1)
        video_formats[int(res)] = int(itag)

    elif 'audio/mp4' in output:
        itag = re.search(r'itag=\"(\d*)\"', output).group(1)
        abr = re.search(r'abr=\"(\d*)kbps\"', output).group(1)
        audio_formats[int(abr)] = int(itag)


# Printing audio/video formats
print(video_formats)
selected = max(video_formats.keys())
print(selected)
video_tag = video_formats[selected]
print(f"--itag={video_tag}")


# Next row used do download video from CLI usin pytube script
# parse_video = subprocess.run(['pytube', message, f"--itag={video_tag}"])
