import tkinter as tk
# Requires pip install requests and pip install Pillow (Pillow should already be installed for the vidReceiver and vidSender)
#The GUI operates similar to div's in JS, order determines parents and child. (root is base window, any other child can be defined
#  such as videoFrame is a child of root and controlsDiv is a child of videoFrame)
HEIGHT = 720
WIDTH = 1280
global user_message
chat_history = "\n"

def chatHandler(message="init", outside_msg ="init"):
    global chat_history
    if (message=="init") and (outside_msg!= "init"):
        chat_history += ("other: " + outside_msg + "\n")
        chatHistory['text'] = str(chat_history)
    elif (message!="init") and (outside_msg== "init"):
        chat_history += ("u1: " + message + "\n")
        chatHistory['text'] = str(chat_history)
    elif ():
        chat_history += ("u1: " + message + "\n")
        chatHistory['text'] = str(chat_history)
        chat_history += ("other: " + outside_msg + "\n")
    
    

def messageHandler(text):
    #HART, we can chat using this variable
    user_message = text
    chatHandler(user_message)
    print(user_message)


def pauseHandler():
    #ADD call to pause video playback
    print("PAUSE CLICKED")


def playHandler():
    #ADD call to play video playback
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

#Video Parent
videoFrame = tk.Frame(root, bg='#a6a6a6')
videoFrame.place(relx=0.1, rely=0.1, relwidth=0.45, relheight=0.45)

controlsDiv = tk.Frame(videoFrame, bg='gray')
controlsDiv.place(relheight=0.1, relwidth=1, rely=0.9, relx=0)

pauseButton = tk.Button(controlsDiv, text='PAUSE',
                        bg='blue', command=lambda: pauseHandler())
pauseButton.pack(side='left')
playButton = tk.Button(controlsDiv, text='PLAY',
                       bg='green', command=lambda: playHandler())
playButton.pack(side='left')

#Chat parent
chatBox = tk.Frame(root, bg='#d9d9d9')
chatBox.place(relx=0.8, rely=0.1, relwidth=0.2, relheight=0.6)

chatHistory = tk.Label(chatBox, bg='#d9d9d9', font='40')
chatHistory.place(relwidth=1, relheight=0.95)

messageDiv = tk.Frame(chatBox, bg='gray')
messageDiv.place(relwidth=1, relheight=0.05, relx=0, rely=0.95)

textEntry = tk.Entry(messageDiv, bg='white')
textEntry.pack(side='left')
sendMessage = tk.Button(messageDiv, bg='red', text='SEND MESSAGE', command=lambda: messageHandler(textEntry.get()))
sendMessage.pack(side='left')

#Command parent
commandBox = tk.Frame(root, bg='#bfbfbf')
commandBox.place(relx=0.1, rely=0.6, relwidth=0.45, relheight=0.3)

#GUI
#window = tk.Tk()
#window.title("EE-551 Project")
#window.geometry('300x300')

#label_target_ip = tk.Label(window, text="Target IP:")
#label_target_ip.pack()

'''text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text="Start Listening",width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start Camera Stream",width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Start Screen Sharing",width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Start Audio Stream",width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

btn_text = tk.Button(window, text="Start Text Stream",width=50, command=start_text_message)
btn_text.pack(anchor=tk.CENTER, expand=True)'''

root.mainloop()

