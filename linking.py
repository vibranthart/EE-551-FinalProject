# install pafy, python-vlc, and youtube-dl
import vlc
import pafy
import time

# Function to call in other files using [some_variable = MediaLink(your_url)] [some_variable.startVideo, some_variable.stopVideo, some_variable.pauseVideo]
# vlc MediaPlayer commands in vlc.py which is in path C:\Python39\Lib\site-packages


class MediaLink:

    def __init__(self, url):
        self.url = url

        if len(url) < 23:
            print("Your URL is not valid!")
        else:
            global media
            video = pafy.new(url, basic=True)
            # best = video.streams[0]#gets index at 0
            best = video.getbest()  # best quality start from beginning
            media = vlc.MediaPlayer(best.url)
            print("Video Loaded!")

    def stopVideo(self):
        media.stop()

    def startVideo(self):
        media.play()

    def pauseVideo(self):
        media.pause()

    def getTime(self):
        # Get current movie time of player in MILLISECONDS
        media.get_time()

    def getLength(self):
        # Get length of video in ms
        media.get_length()

    def setTime(self, i_time):
        # Set the movie time to desired in MILLISECONDS, here we can sync up instances from peoples players in
        self.i_time = i_time
        media.set_time(i_time)
