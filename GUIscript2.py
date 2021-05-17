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
host = '10.0.0.46'
# host = '192.168.1.24'


class MainScript:

    def __init__(self):
        # initializations

        self.nickname = input("choose a nickname: ")
        self.local_ip_address = socket.gethostbyname(socket.gethostname())
        # public_ip_address = requests.get('https//api.ipify.org').text
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, 14089))
        self.server = StreamingServer(self.local_ip_address, 7777)
        self.receiver = AudioReceiver(self.local_ip_address, 5555)

    def start_listening(self):
        self.t1 = threading.Thread(target=self.server.start_server)
        self.t2 = threading.Thread(target=self.receiver.start_server)
        self.t1.start()
        self.t2.start()

    def end_listening(self):
        self.t1 = threading.Thread(target=self.server.stop_server)
        self.t2 = threading.Thread(target=self.receiver.stop_server)
        self.t1.start()
        self.t2.start()

    def start_camera_stream(self):
        self.camera_client = CameraClient(
            inst.text_target_ip.get(1.0, 'end-1c'), 9999)
        self.t3 = threading.Thread(target=self.camera_client.start_stream)
        self.t3.start()

    def end_camera_stream(self):
        self.camera_client = CameraClient(
            inst.text_target_ip.get(1.0, 'end-1c'), 9999)
        self.t3 = threading.Thread(target=self.camera_client.stop_stream)
        self.t3.start()

    def start_screen_sharing(self):
        self.screen_client = ScreenShareClient(
            inst.text_target_ip.get(1.0, 'end-1c'), 9999)
        self.t4 = threading.Thread(target=self.screen_client.start_stream)
        self.t4.start()

    def end_screen_sharing(self):
        # end screen sharing
        self.screen_client = ScreenShareClient(
            inst.text_target_ip.get(1.0, 'end-1c'), 9999)
        self.t4E = threading.Thread(target=self.screen_client.stop_stream)
        self.t4E.start()

    def start_audio_stream(self):
        global audio_count
        audio_count += 1

        self.audio_sender = AudioSender(
            inst.text_target_ip.get(1.0, 'end-1c'), 8888)
        self.t5 = threading.Thread(target=self.audio_sender.start_stream)
        self.t5.start()

    def end_audio_stream(self):
        # end audio stream
        self.audio_sender = AudioSender(
            inst.text_target_ip.get(1.0, 'end-1c'), 8888)
        self.t5E = threading.Thread(target=self.audio_sender.stop_stream)
        self.t5E.start()

    def start_text_message(self, msg="----"):
        def recieve():
            global loopKiller
            loopKiller = 0
            while True:
                try:
                    message = self.client.recv(4096).decode('ascii')
                    if message == 'HART':
                        self.client.send(self.nickname.encode('ascii'))
                    else:
                        print(message)
                        inst.add_to_chat(message)

                except:
                    print("[Error]")
                    self.client.close()
                    break

        def write():
            message = f'{self.nickname}: {msg}'
            self.client.send(message.encode('ascii'))
            # inst.add_to_chat(message) double response?

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

# Main GUI for system startup


class GuiScript:
    def __init__(self, master):
        self.chat_history = "\n"
        self.canvas = tk.Canvas(master, height=HEIGHT, width=WIDTH)
        self.canvas.pack()

        # self.var = tk.StringVar('')
        # Video Parent myFrame Parent
        self.videoFrame = tk.Frame(master, bg='#a6a6a6')
        self.videoFrame.place(relx=0.04, rely=0.1,
                              relwidth=0.6, relheight=0.65)

        self.controlsDiv = tk.Frame(self.videoFrame, bg='gray')
        self.controlsDiv.place(
            relheight=0.1, relwidth=1, rely=0.9, relx=0)

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
        self.chatBox.place(relx=0.65, rely=0.1, relwidth=0.35, relheight=0.8)

        self.dynamicLabel = tk.Scrollbar(self.chatBox, jump=1, )
        self.dynamicLabel.pack(side='right')
        """
        self.chatHistory = tk.Label(
            self.dynamicLabel, font='40', wraplength=0)
        self.chatHistory.place(relwidth=1, relheight=.9, rely=.01)
        """
        self.ChatHistory = tk.Text(
            self.chatBox, wrap=tk.WORD, width=60, state=tk.NORMAL)
        self.ChatHistory.pack(side='left')

        self.ChatHistory['yscroll'] = self.dynamicLabel.set
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
        self.commandBox.place(relx=0.04, rely=0.8,
                              relwidth=0.6, relheight=0.05)

        self.ip_target = tk.Frame(master)
        self.ip_target.place(rely=0.1, relx=0.04, relwidth=0.6, relheight=0.05)

        self.label_target_ip = tk.Label(self.ip_target, text="Target IP:")
        self.label_target_ip.pack(side='left')

        self.text_target_ip = tk.Text(self.ip_target, height=1, width=90)
        self.text_target_ip.pack(side='left')

        self.btn_listen = tk.Button(self.commandBox, text="Start Listening",
                                    width=20, command=lambda: m.start_listening())
        self.btn_listen.pack(side='left')

        self.btn_camera = tk.Button(self.commandBox, text="Start Camera Stream",
                                    width=20, command=lambda: m.start_camera_stream())
        self.btn_camera.pack(side='left')

        self.btn_screen = tk.Button(self.commandBox, text="Start Screen Sharing",
                                    width=20, command=lambda: m.start_screen_sharing())
        self.btn_screen.pack(side='left')

        self.btn_audio = tk.Button(self.commandBox, text="Start Audio Stream",
                                   width=20, command=lambda: m.start_audio_stream())
        self.btn_audio.pack(side='left')

        self.btn_text = tk.Button(self.commandBox, text="Start Text Stream",
                                  width=20, command=lambda: m.start_text_message())
        self.btn_text.pack(side='left')

        # end buttons
        self.endDiv = tk.Frame(master, bg='#bfbfbf')
        self.endDiv.place(relx=0.04, rely=0.85, relwidth=0.6, relheight=0.05)

        self.end_btn_listen = tk.Button(self.endDiv, text="End Listening",
                                        width=20, command=lambda: m.end_listening())
        self.end_btn_listen.pack(side='left')

        self.end_btn_camera = tk.Button(self.endDiv, text="End Camera Stream",
                                        width=20, command=lambda: m.end_camera_stream())
        self.end_btn_camera.pack(side='left')

        self.end_btn_screen = tk.Button(self.endDiv, text="End Screen Sharing",
                                        width=20, command=lambda: m.end_screen_sharing())
        self.end_btn_screen.pack(side='left')

        self.end_btn_audio = tk.Button(self.endDiv, text="End Audio Stream",
                                       width=20, command=lambda: m.end_audio_stream())
        self.end_btn_audio.pack(side='left')
        '''
        self.end_btn_text = tk.Button(self.endDiv, text="End Text Stream",
                                      width=20, command=lambda: m.end_text_message())
        self.end_btn_text.pack(side='left')
        '''

    def messageHandler(self, text):
        if (text == '') or (text == ' ') or (text == '  '):
            print("No text entered")
        else:
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
        self.chat_history = '\n'
        self.chat_history = self.chat_history + '\n' + annc + '\n'
        self.ChatHistory.insert(tk.INSERT, self.chat_history)
        # self.chatHistory['text'] = self.chat_history
        # inst.chatHistoryNEW.insert('end', "%s" % chat_history)
    """
    Need image in this directory!
    background_image = tk.PhotoImage(file='example.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    """


inst = GuiScript(root)
root.mainloop()
