# install pafy, python-vlc, and youtube-dl
import vlc
import pafy


# Function to call in other files using [some_variable = MediaLink(your_url)] [some_variable.startVideo, some_variable.stopVideo, some_variable.pauseVideo]
# vlc MediaPlayer commands in vlc.py which is in path C:\Python39\Lib\site-packages

def MediaLink(url):
    global media
    if len(url) < 23:
        print("Your URL is not valid!")
    else:
        
        video = pafy.new(url, basic=True)
        # best = video.streams[0]#gets index at 0
        best = video.getbest()  # best quality start from beginning
        media = vlc.MediaPlayer(best.url)
        print("Video Loaded!")   

def stopVideo():
    media.stop()
    print(media.get_time())

def startVideo():
    media.play()
    print(media.get_time())

def pauseVideo():
    media.pause()

def getCurrent():
    # Get current movie time of player in MILLISECONDS 
    x = media.get_time()
    return x
    

def getLength():
    # Get length of video in ms
    media.get_length()

def setCurrentTime( i_time):
    # Set the movie time to desired in MILLISECONDS, here we can sync up instances from peoples players in
    i_time = i_time
    media.set_time( i_time)

