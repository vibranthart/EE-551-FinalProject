from vidstream import AudioSender, AudioReceiver, ScreenShareClient, CameraClient, StreamingServer
import socket
import threading
import requests
from vlc import libvlc_audio_get_track_count
from tkinter import scrolledtext
import tkinter as tk
from linking import *
from tkinter.constants import *

# Requires pip install requests and pip install Pillow (Pillow should already be installed for the vidReceiver and vidSender)

# Included main.py in this file since scope was confusing me
listen_count = 0
camera_count = 0
screen_count = 0
audio_count = 0
loopKiller = 0
#host = '10.0.0.46'
host = '192.168.1.24'


class MainScript:

    def __init__(self):
        # initializations

        self.nickname = input("choose a nickname: ")
        self.local_ip_address = socket.gethostbyname(socket.gethostname())
        #public_ip_address = requests.get('https//api.ipify.org').text
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, 14089))
        self.server = StreamingServer(self.local_ip_address, 9999)
        self.receiver = AudioReceiver(self.local_ip_address, 8888)

    def start_listening(self):
        global listen_count
        listen_count += 1
        if listen_count % 2 == 0:
            print(listen_count)
            self.t1 = threading.Thread(target=self.server.start_server)
            self.t2 = threading.Thread(target=self.receiver.start_server)
            self.t1.start()
            self.t2.start()
        elif listen_count % 2 != 0:
            print(listen_count)
            self.t1 = threading.Thread(target=self.server.stop_server)
            self.t2 = threading.Thread(target=self.receiver.stop_server)
            self.t1.start()
            self.t2.start()

    def start_camera_stream(self):
        global camera_count
        camera_count += 1
        if camera_count % 2 == 0:
            self.camera_client = CameraClient(
                inst.text_target_ip.get(1.0, 'end-1c'), 7777)
            self.t3 = threading.Thread(target=self.camera_client.start_stream)
            self.t3.start()
        elif camera_count % 2 != 0:
            # end camera stream
            self.camera_client = CameraClient(
                inst.text_target_ip.get(1.0, 'end-1c'), 7777)
            self.t3 = threading.Thread(target=self.camera_client.stop_stream)
            self.t3.start()

    def start_screen_sharing(self):
        global screen_count
        screen_count += 1
        if screen_count % 2 == 0:
            self.screen_client = ScreenShareClient(
                inst.text_target_ip.get(1.0, 'end-1c'), 7777)
            self.t4 = threading.Thread(target=self.screen_client.start_stream)
            self.t4.start()
        elif screen_count % 2 != 0:
            # end screen sharing
            self.screen_client = ScreenShareClient(
                inst.text_target_ip.get(1.0, 'end-1c'), 7777)
            self.t4E = threading.Thread(target=self.screen_client.stop_stream)
            self.t4E.start()

    def start_audio_stream(self):
        global audio_count
        audio_count += 1
        if audio_count % 2 == 0:
            self.audio_sender = AudioSender(
                inst.text_target_ip.get(1.0, 'end-1c'), 5555)
            self.t5 = threading.Thread(target=self.audio_sender.start_stream)
            self.t5.start()
        elif audio_count % 2 != 0:
            # end audio stream
            self.audio_sender = AudioSender(
                inst.text_target_ip.get(1.0, 'end-1c'), 5555)
            self.t5E = threading.Thread(target=self.audio_sender.stop_stream)
            self.t5E.start()

    def start_text_message(self, msg="Initialized"):
        def recieve():
            while True:
                try:
                    message = self.client.recv(4096).decode('ascii')
                    if message == 'HART':
                        self.client.send(self.nickname.encode('ascii'))
                        inst.add_to_chat(message)
                        #inst.chatHistoryNEW.insert('end', message)
                    else:
                        print(message)
                except:
                    print("[Error]")
                    self.client.close()
                    break

        def write():
            global loopKiller
            loopKiller = 0
            while True:
                message = f'{self.nickname}: {msg}'
                self.client.send(message.encode('ascii'))

                if loopKiller < 0:
                    inst.add_to_chat(message)
                    loopKiller += 1
                else:
                    break
                #inst.chatHistoryNEW.insert('end', message)

        self.recieve_thread = threading.Thread(target=recieve)
        self.recieve_thread.start()
        write_thread = threading.Thread(target=write)
        write_thread.start()


HEIGHT = 720
WIDTH = 1280
c = 0
m = MainScript()

root = tk.Tk()
root.title('The Awesome Group - EE-551 Final Project')


class GuiScript:
    def __init__(self, master):
        self.chat_history = "\n"
        self.canvas = tk.Canvas(master, height=HEIGHT, width=WIDTH)
        self.canvas.pack()
        #self.var = tk.StringVar('')
        # Video Parent myFrame Parent
        self.videoFrame = tk.Frame(master, bg='#a6a6a6')
        self.videoFrame.place(relx=0.05, rely=0.1,
                              relwidth=0.7, relheight=0.65)

        self.controlsDiv = tk.Frame(self.videoFrame, bg='gray')
        self.controlsDiv.place(relheight=0.1, relwidth=1, rely=0.9, relx=0)

        self.url_entry = tk.Entry(self.controlsDiv)
        self.url_entry.pack(side="left")

        self.pauseButton = tk.Button(self.controlsDiv, text='PAUSE',
                                     bg='blue', command=lambda: self.pauseHandler())
        self.pauseButton.pack(side='left')
        self.playButton = tk.Button(self.controlsDiv, text='PLAY',
                                    bg='green', command=lambda: self.playHandler(self.url_entry.get()))
        self.playButton.pack(side='left')

        # Chat parent
        self.chatBox = tk.Frame(master, bg='#d9d9d9')
        self.chatBox.place(relx=0.8, rely=0.1, relwidth=0.2, relheight=0.8)

        self.chatHistory = tk.Label(self.chatBox, font='40')
        self.chatHistory.place(relwidth=1, relheight=.9, rely=.01)

        """
                # TEST

                self.chatHistoryNEW = scrolledtext.ScrolledText(self.chatBox)
                self.chatHistoryNEW.pack()
                self.chatHistoryNEW.insert('insert', "BEGIN MESSAGE HISTORY:")

                self.chatHistoryNEW.config(state=DISABLED)
        """
        self.messageDiv = tk.Frame(self.chatBox, bg='gray')
        self.messageDiv.place(relwidth=2, relheight=0.05, relx=0, rely=0.95)

        self.textEntry = tk.Entry(self.messageDiv, bg='white')
        self.textEntry.pack(side='left')
        self.sendMessage = tk.Button(self.messageDiv, bg='red', text='SEND MESSAGE',
                                     command=lambda: self.messageHandler(self.textEntry.get()))
        self.sendMessage.pack(side='left')

        # Command parent
        self.commandBox = tk.Frame(master, bg='#bfbfbf')
        self.commandBox.place(relx=0.05, rely=0.8, relwidth=0.7, relheight=0.1)

        # GUI
        ##window = tk.Tk()
        #window.title("EE-551 Project")
        # window.geometry('300x300')
        self.ip_target = tk.Frame(master)
        self.ip_target.place(rely=0.1, relx=0.05, relwidth=0.7, relheight=0.05)

        self.label_target_ip = tk.Label(self.ip_target, text="Target IP:")
        self.label_target_ip.pack(side='left')

        self.text_target_ip = tk.Text(self.ip_target, height=1, width=100)
        self.text_target_ip.pack(side='left')

        self.btn_listen = tk.Button(self.commandBox, text="Start Listening",
                                    width=25, command=lambda: m.start_listening)
        self.btn_listen.pack(side='left')

        self.btn_camera = tk.Button(self.commandBox, text="Start Camera Stream",
                                    width=25, command=lambda: m.start_camera_stream)
        self.btn_camera.pack(side='left')

        self.btn_screen = tk.Button(self.commandBox, text="Start Screen Sharing",
                                    width=25, command=lambda: m.start_screen_sharing)
        self.btn_screen.pack(side='left')

        self.btn_audio = tk.Button(self.commandBox, text="Start Audio Stream",
                                   width=25, command=lambda: m.start_audio_stream)
        self.btn_audio.pack(side='left')

        self.btn_text = tk.Button(self.commandBox, text="Start Text Stream",
                                  width=25, command=lambda: m.start_text_message())
        self.btn_text.pack(side='left')

    def messageHandler(self, text):
        m.start_text_message(text)

    def pauseHandler(self):
        global c
        c += 1
        if (c % 2 == 0):
            print("Content Resumed")
            startVideo()
        elif (c % 2 != 0):
            print("PAUSE CLICKED")
            pauseVideo()

    def playHandler(self, url):
        # ADD call to play video playback
        print(url)
        MediaLink(url)
        print("PLAY CLICKED")
        startVideo()

    def add_to_chat(self, annc):
        self.chat_history = self.chat_history + '\n' + annc + '\n'
        self.chatHistory['text'] = self.chat_history
        #inst.chatHistoryNEW.insert('end', "%s" % chat_history)
    """
    Need image in this directory!
    background_image = tk.PhotoImage(file='example.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    """


inst = GuiScript(root)
root.mainloop()
