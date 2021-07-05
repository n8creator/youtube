from ffmpy import FFmpeg
from termcolor import colored
import subprocess


def convert_audio_to_mp3(audio_file: str, output_filename: str):
    # Convert MP4 audio file to MP3 format
    r = FFmpeg(
        inputs={f"{audio_file}.mp4": None},
        outputs={f"{output_filename}.mp3": None}
    )
    r.run(stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Print output message
    print(colored('MP4 track was converted to MP3...'))


def merge_mp4_audio_and_video(audio_file: str, video_file: str,
                              output_filename: str):
    # Merge mp4 audio and video files into single mp4 file
    r = FFmpeg(
        inputs={f'{audio_file}.mp4': None, f'{video_file}.mp4': None},
        outputs={f"{output_filename}.mp4": '-c:v copy -strict \
                   experimental -c:a copy -strict experimental'}
    )
    r.run(stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Print output message
    print(colored('Audio and video files were merged...'))
