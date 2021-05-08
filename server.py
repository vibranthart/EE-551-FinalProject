import threading
import socket


# local host
host = '127.0.0.1' 
port = 14089

#starts a server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
#listens for incoming connections
server.listen() 

clients = []
nicknames = []

#broadcast message to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(4096)
            #print(message)
            #print(message.decode('ascii'))
           
            if '#1' in message.decode('ascii'):
                broadcast('Trying to Sync...'.encode('ascii'))
            elif '#2' in message.decode('ascii'):
                broadcast('Secondary option'.encode('ascii'))
            else:
                broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            #broadcast
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

def recieve():
    while True:
        client, address = server.accept()
        print(f"Connectedd with {str(address)}")

        #send message to client
        client.send('HART'.encode('ascii'))
        nickname = client.recv(4096).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        #broadcast to that client joined the chat
        print(f'Nickname of client is {nickname}')
        broadcast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('[Success] : Connected to the server!'.encode('ascii'))
        #client.send('[Options] : #1 - Sync Video #2 - '.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
recieve()