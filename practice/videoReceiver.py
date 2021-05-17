from vidstream import StreamingServer
import threading

#bond it local ip address - conenct must specify public address
receiver = StreamingServer('10.0.0.46',14089)
t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'STOP':
    continue

#how to stop the server
receiver.stop_server()