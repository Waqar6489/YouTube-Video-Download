import yt_dlp

url = 'https://youtube.com/shorts/U98lKgdbZOE?si=8ofiw50IYZ-RQ8qK'

ydl_opts = {'format': 'best', 'outtmpl': '%(title)s.%(ext)s'}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
