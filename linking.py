# Here I will be creating a link service that takes a link and opens up a video player for co-op watching
# install pafy, python-vlc, and youtube-dl
import vlc
import pafy


def StopVideoPlayback():
    media.stop()


url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
video = pafy.new(url)

best = video.streams[1]#gets index at 0
#best = video.getbest() best quality start from beginning

media = vlc.MediaPlayer(best.url)

print("Video Playing...")

# Starts video
media.play()


stop = input("Would you like to end playback? (Y/N)")
if ((stop == 'Y') or (stop == 'y')):
    StopVideoPlayback()
