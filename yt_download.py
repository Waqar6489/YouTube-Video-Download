import yt_dlp
url='https://youtube.com/shorts/bOY80Xttrug?si=k1VKzGFxeyDpMQ0Z'
yt_opt={"format":"best",
        "outtmpl": "%(title)s.%(ext)s"}
with yt_dlp.YoutubeDL(yt_opt) as yts:
    yts.download([url])