from linking import MediaLink
from timing import timeSync


#MUST HAVE VLC MEDIA INSTALLED TO RUN

#TESTS linking.py class MediaLink
#Gets URL
#url = input('enter url')
#Passes it to MediaLink class
#movie1 = MediaLink(url)
#Seek the video to specified times in milliseconds
#movie1.setTime(120000)
#Will display video length (may not work)
#print(movie1.getLength())
#Starts the Video
#movie1.startVideo()


#TESTS SERVER USER SYNC IN timing.py 
#syntax: timeSync(server, user1, user2, user3, user4) in milliseconds only accepts 4 users
timeSync(10000, 6000, 7000)