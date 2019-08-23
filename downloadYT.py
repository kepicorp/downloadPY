from __future__ import unicode_literals
import youtube_dl
import sys

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


if (len(sys.argv) != 2):
    print('Invalidate parameters, usage: downloadYT.py http://myyoutubelink')
else:
    print('About to extract '+sys.argv[1])
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([sys.argv[1]])
