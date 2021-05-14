import tkinter as tk
# Requires pip install requests and pip install Pillow (Pillow should already be installed for the vidReceiver and vidSender)
HEIGHT = 720
WIDTH = 1280
global user_message


def messageHandler(text):
    user_message = text
    print("user_message")


def pauseHandler():
    print("PAUSE CLICKED")


def playHandler():
    print("PLAY CLICKED")


root = tk.Tk()

"""
Need image in this directory!
background_image = tk.PhotoImage(file='example.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
"""
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

videoFrame = tk.Frame(root, bg='#a6a6a6')
videoFrame.place(relx=0.1, rely=0.1, relwidth=0.45, relheight=0.45)

controlsDiv = tk.Frame(videoFrame, bg='gray')
controlsDiv.place(relheight=0.1, relwidth=1, rely=0.9, relx=0)

pauseButton = tk.Button(controlsDiv, text='PAUSE',
                        bg='blue', command=pauseHandler())
pauseButton.pack(side='left')
playButton = tk.Button(controlsDiv, text='PLAY',
                       bg='green', command=playHandler())
playButton.pack(side='left')

chatBox = tk.Frame(root, bg='#d9d9d9')
chatBox.place(relx=0.6, rely=0.1, relwidth=0.3, relheight=0.8)

messageDiv = tk.Frame(chatBox, bg='gray')
messageDiv.place(relwidth=1, relheight=0.05, relx=0, rely=0.95)

textEntry = tk.Entry(messageDiv, bg='white')
textEntry.pack(side='left')
sendMessage = tk.Button(messageDiv, bg='red', text='SEND MESSAGE', command=Lambda: messageHandler(textEntry.get()))
sendMessage.pack(side='left')

commandBox = tk.Frame(root, bg='#bfbfbf')
commandBox.place(relx=0.1, rely=0.6, relwidth=0.45, relheight=0.3)


root.mainloop()
