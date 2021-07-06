# CLI YouTube downloading utility based on Pybute
## 1. About
This python script allows to download video and audio files from YouTube in different formats:
1. Progressive video in MP4 Mid-quality - fastest download, downloading file contains both  audio and video
2. Video in MP4 HQ quality - slow download, video and audio files downloading separately in highest avaiable quality in MP4 format, and then they are merged together via FFMpeg
3. Audio in MP3 HQ quality - audio file downloading in highest avaiable quality in MP4 format, and then converting from MP4 to MP3 via FFMpeg

Basic commands and interface:
```
usage: youtube [-h] [-s URL] [-f FILE] [--hq] [--a] [-p URL] [--n N]

YouTube CLI downloader quick help.

optional arguments:
  -h, --help  show this help message and exit
  -s URL      download single video or audio from URL
  -f FILE     download multiple items from URL's specified in file
  --hq        download video in HQ format
  --a         download audio and convert to MP3 format
  -p URL      specify the "channel_url" string like: "https://www.youtube.com/c/topgtru/videos"
  --n N       specify the number of items, information of which which will be loaded into .csv file

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
```

Script may be used to download single or multiple files. See, how it works:

# 2. Installation
## 2.1. Install FFMpeg locally
Install `ffmpeg` as a system dependency:
```
$ sudo apt install ffmpeg -y
```

## 2.2. Poetry installation & configuration
This script uses Poetry package manager, so Poetry must be installed and configured properly.

```
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

$ poetry -V
```
Check then `virtualenvs.in-project` setting, and set default value to `true`:
```
$ poetry config virtualenvs.in-project true

$ poetry config --list

# Output
    cache-dir = "..."
    virtualenvs.create = true
    virtualenvs.in-project = true
    virtualenvs.path = "..."
```
## 2.3. Script installation
Execute next steps to install script itself:
```
$ mkdir ~/scripts/ -p && cd ~/scripts/

$ git clone https://github.com/n8creator/youtube && cd youtube/

$ poetry install
```

After execution of `poetry install` command a new folder `.venv` must appear within the root directory of the project.

### 2.4. Add script aliases for quick use Manually add script aliases into ~/.profile file via commands:
```
$ echo "alias youtube='~/scripts/youtube/.venv/bin/youtube'" >> ~/.profile
$ echo "alias youtube_update='cd ~/scripts/youtube/ && poetry update'" >> ~/.profile
$ source ~/.profile
```
