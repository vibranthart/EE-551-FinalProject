from linking import *
import time

url = input('enter url')

movie1 = MediaLink(url)

movie1.startVideo()

time.sleep(10)
movie1.stopVideo()
