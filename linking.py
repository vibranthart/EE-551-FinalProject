# Here I will be creating a link service that takes a link and opens up a video player for co-op watching
# install pafy, python-vlc, and youtube-dl
import vlc
import pafy


def StopVideoPlayback():
    media.stop()
def StartVideoPlayback():
    media.play()

#url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
user_url = input("Please paste a url here: ")

video = pafy.new(user_url)

#best = video.streams[0]#gets index at 0
best = video.getbest() #best quality start from beginning

media = vlc.MediaPlayer(best.url)

print("Video Loaded!")

start_playback = input("Would you like to end playback? (Y/N)")
if ((start_playback == 'Y') or (start_playback == 'y')):
    StartVideoPlayback()


stop_playback = input("Would you like to end playback? (Y/N)")
if ((stop_playback == 'Y') or (stop_playback == 'y')):
    StopVideoPlayback()
