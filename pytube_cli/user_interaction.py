from pytube import YouTube

def greet_user():
    # Asking user for Youtube URL to download:
    message = input('Input YouTube URL: ') or 'https://www.youtube.com/watch?v=NeQM1c-XCDc'
    print(f"URL to be parsed: {message}")
