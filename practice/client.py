import socket
import threading

nickname = input("choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.0.0.46', 14089))

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
