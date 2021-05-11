from vidstream import ScreenShareClient
import threading

#specify host you want to connect to
sender = ScreenShareClient('10.0.0.46',14089)

t = threading.Thread(target=sender.start_stream)
t.start()

while input("") != 'STOP':
    continue

sender.stop_stream() 
