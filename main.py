from vidstream import AudioSender, AudioReceiver, ScreenShareClient, CameraClient, StreamingServer
# from vidstream import *
import tkinter as tk
import socket
import threading
import requests

nickname = input("choose a nickname: ")

local_ip_address = socket.gethostbyname(socket.gethostname())
# public_ip_address = requests.get('https//api.ipify.org').text
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.0.0.46', 14089))


server = StreamingServer(local_ip_address, 9999)
receiver = AudioReceiver(local_ip_address, 8888)


def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()

# end start listening


def end_listening():
    t1E = threading.Thread(target=server.stop_server)
    t2E = threading.Thread(target=receiver.stop_server)
    t1E.start()
    t2E.start()


def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0, 'end-1c'), 7777)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()

# end camera stream


def end_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0, 'end-1c'), 7777)
    t3E = threading.Thread(target=camera_client.stop_stream)
    t3E.start()


def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0, 'end-1c'), 7777)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()

# end screen sharing


def end_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0, 'end-1c'), 7777)
    t4E = threading.Thread(target=screen_client.stop_stream)
    t4E.start()


def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0, 'end-1c'), 5555)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()

# end audio stream


def end_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0, 'end-1c'), 5555)
    t5E = threading.Thread(target=audio_sender.stop_stream)
    t5E.start()


def start_text_message():
    def recieve():
        while True:
            try:
                message = client.recv(4096).decode('ascii')
                if message == 'HART':
                    client.send(nickname.encode('ascii'))
                else:
                    print(message)
            except:
                print("[Error]")
                client.close()
                break

    def write():
        while True:
            message = f'{nickname}: {input("")}'
            client.send(message.encode('ascii'))

    recieve_thread = threading.Thread(target=recieve)
    recieve_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()


'''
# GUI
window = tk.Tk()
window.title("EE-551 Project")
window.geometry('300x3')

label_target_ip = tk.Label(window, text="Target IP:")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text="Start Listening",
                       width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start Camera Stream",
                       width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Start Screen Sharing",
                       width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Start Audio Stream",
                      width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

btn_text = tk.Button(window, text="Start Text Stream",
                     width=50, command=start_text_message)
btn_text.pack(anchor=tk.CENTER, expand=True)

# end functions
btn_listen_end = tk.Button(
    window, text="End Listening", width=50, command=end_listening)
btn_listen_end.pack(anchor=tk.CENTER, expand=True)

btn_camera_end = tk.Button(
    window, text="End Camera Stream", width=50, command=end_camera_stream)
btn_camera_end.pack(anchor=tk.CENTER, expand=True)

btn_screen_end = tk.Button(
    window, text="End Screen Sharing", width=50, command=end_screen_sharing)
btn_screen_end.pack(anchor=tk.CENTER, expand=True)

btn_audio_end = tk.Button(window, text="End Audio Stream",
                          width=50, command=end_audio_stream)
btn_audio_end.pack(anchor=tk.CENTER, expand=True)

window.mainloop()
'''
