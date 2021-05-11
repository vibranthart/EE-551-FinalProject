# install pafy, python-vlc, and youtube-dl
import vlc
import pafy
import time

# Function to call in other files using [some_variable = MediaLink(your_url)] [some_variable.startVideo, some_variable.stopVideo, some_variable.pauseVideo]


class MediaLink:

    def __init__(self, url, startPoint, runTime, stopPoint):
        self.url = url
        self.startPoint = startPoint
        self.stopPoint = stopPoint
        self.runTime = runTime
        if len(url) < 23:
            print("Your URL is not valid!")
        else:
            global media
            video = pafy.new(url, basic=True)
            # best = video.streams[0]#gets index at 0
            best = video.getbest()  # best quality start from beginning
            media = vlc.MediaPlayer(best.url)
            print("Video Loaded!")
            # how far in to star playing in seconds
            media.add_option(startPoint)
            # how long to run
            media.add_option(runTime)
            # time to stop
            media.add_option(stopPoint)

    def stopVideo(self):
        media.stop()

    def startVideo(self):
        media.play()

    def pauseVideo(self):
        media.pause()
