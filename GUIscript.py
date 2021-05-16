from vidstream import AudioSender, AudioReceiver, ScreenShareClient, CameraClient, StreamingServer
from tkinter import scrolledtext
import tkinter as tk
import os
import socket
import threading
import requests
from linking import *
import time
import platform
import vlc
from tkinter.constants import *
from main import *

# Requires pip install requests and pip install Pillow (Pillow should already be installed for the vidReceiver and vidSender)
# The GUI operates similar to div's in JS, order determines parents and child. (root is base window, any other child can be defined
#  such as videoFrame is a child of root and controlsDiv is a child of videoFrame)
HEIGHT = 720
WIDTH = 1280
chat_history = "\n"
c = 0


def chatHandler(msg1="init", outside_msg="init"):
    global chat_history
    message = msg1
    if "" in message or " " in message or "   " in message:
        message = "init"
    else:
        pass

    if (message == "init") and (outside_msg != "init"):
        chat_history += ("other: " + outside_msg + "\n")
        chatHistoryNEW.insert(INSERT, "%s" % chat_history)
        #chatHistory['text'] = str(chat_history)
    elif (message != "init") and (outside_msg == "init"):
        chat_history += ("u1: " + message + "\n")
        chatHistoryNEW.insert(INSERT, )
        #chatHistory['text'] = str(chat_history)
    elif (message != "init") and (outside_msg != "init"):
        print("Invalid text")


def messageHandler(text):
    chatHandler(text)
    print(text)


def pauseHandler():
    global c
    c += 1
    if (c % 2 == 0):
        print("Content Resumed")
        startVideo()
    elif (c % 2 != 0):
        print("PAUSE CLICKED")
        pauseVideo()


def playHandler(url):
    # ADD call to play video playback
    print(url)
    MediaLink(url)
    print("PLAY CLICKED")
    startVideo()


root = tk.Tk()

"""
Need image in this directory!
background_image = tk.PhotoImage(file='example.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
"""
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Video Parent
videoFrame = tk.Frame(root, bg='#a6a6a6')
videoFrame.place(relx=0.05, rely=0.1, relwidth=0.7, relheight=0.65)


controlsDiv = tk.Frame(videoFrame, bg='gray')
controlsDiv.place(relheight=0.1, relwidth=1, rely=0.9, relx=0)

url_entry = tk.Entry(controlsDiv)
url_entry.pack(side="left")

pauseButton = tk.Button(controlsDiv, text='PAUSE',
                        bg='blue', command=lambda: pauseHandler())
pauseButton.pack(side='left')
playButton = tk.Button(controlsDiv, text='PLAY',
                       bg='green', command=lambda: playHandler(url_entry.get()))
playButton.pack(side='left')


# Chat parent
chatBox = tk.Frame(root, bg='#d9d9d9')
chatBox.place(relx=0.8, rely=0.1, relwidth=0.2, relheight=0.8)

# chatHistory = tk.Label(chatBox, bg='#d9d9d9', font='40',bd='100')
#chatHistory.place(relwidth=1, relheight=.9,rely=.02, anchor=tk.CENTER)

# TEST

chatHistoryNEW = scrolledtext.ScrolledText(chatBox)
chatHistoryNEW.pack()
chatHistoryNEW.insert('insert', "BEGIN MESSAGE HISTORY:")

chatHistoryNEW.config(state=DISABLED)


messageDiv = tk.Frame(chatBox, bg='gray')
messageDiv.place(relwidth=2, relheight=0.05, relx=0, rely=0.95)

textEntry = tk.Entry(messageDiv, bg='white')
textEntry.pack(side='left')
sendMessage = tk.Button(messageDiv, bg='red', text='SEND MESSAGE',
                        command=lambda: messageHandler(textEntry.get()))
sendMessage.pack(side='left')

# Command parent
commandBox = tk.Frame(root, bg='#bfbfbf')
commandBox.place(relx=0.05, rely=0.8, relwidth=0.7, relheight=0.1)

# GUI
##window = tk.Tk()
#window.title("EE-551 Project")
# window.geometry('300x300')
ip_target = tk.Frame(root)
ip_target.place(rely=0.1, relx=0.05, relwidth=0.7, relheight=0.05)

label_target_ip = tk.Label(ip_target, text="Target IP:")
label_target_ip.pack(side='left')

text_target_ip = tk.Text(ip_target, height=1, width=100)
text_target_ip.pack(side='left')

btn_listen = tk.Button(commandBox, text="Start Listening",
                       width=25, command=start_listening)
btn_listen.pack(side='left')

btn_camera = tk.Button(commandBox, text="Start Camera Stream",
                       width=25, command=start_camera_stream)
btn_camera.pack(side='left')

btn_screen = tk.Button(commandBox, text="Start Screen Sharing",
                       width=25, command=start_screen_sharing)
btn_screen.pack(side='left')

btn_audio = tk.Button(commandBox, text="Start Audio Stream",
                      width=25, command=start_audio_stream)
btn_audio.pack(side='left')

btn_text = tk.Button(commandBox, text="Start Text Stream",
                     width=25, command=start_text_message)
btn_text.pack(side='left')

root.mainloop()
