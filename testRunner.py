from linking import *
import time

#MUST HAVE VLC MEDIA INSTALLED TO RUN

url = input('enter url')

movie1 = MediaLink(url)
movie1.setTime(120000)
print(movie1.getLength())
movie1.startVideo()