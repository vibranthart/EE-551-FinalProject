from linking import *
from timing import timeSync
import time

#MUST HAVE VLC MEDIA INSTALLED TO RUN

#TESTS linking.py class MediaLink
#Gets URL
url = input('enter url')
MediaLink(url)


#Will display video length (may not work)
#print(movie1.getLength())
#Starts the Video
startVideo()

"""
movie2 = MediaLink(url)
time.sleep(10)
movie2.startVideo()

"""

#TESTS SERVER USER SYNC IN timing.py 
#syntax: timeSync(server, user1, user2, user3, user4) in milliseconds only accepts 4 users
#timeSync(int(server1), int(user1))



