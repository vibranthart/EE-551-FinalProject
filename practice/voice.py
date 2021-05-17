from vidstream import AudioSender
from vidstream import AudioReceiver

import threading
import socket

#ip = socket.gethostbyname(socket.gethostbyname())

#recieves audio
receiver = AudioReceiver('10.0.0.46',14089)
receive_thread = threading.Thread(target=receiver.start_server)

#sends audio 
sender = AudioSender('10.0.0.46', 5555)
sender_thread = threading.Thread(target=sender.start_stream)

receive_thread.start()
sender_thread.start()





