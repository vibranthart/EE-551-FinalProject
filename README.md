# EE-551-FinalProject
Hello! Welcome to our Final Project!

Some Dependencies you need to download:
  For the Screen Share:
    pip install wheel
    pip install pinwin
    pipwin install pyaudio
    pip install Pillow
    pip install vidsteam
    
   For the Video Player:
    Install VLC Media Player
    pip install pafy
    pip install python-vlc
    pip install youtube-dl

  Objective:
  The objective of this project is to create and develop a way for users to watch videos on the web as group while being Online.
  In the recent year, Covid has caused many people to stay at home and watch remotely and interact with friends through social media, 
  such as Instagram, Snapchat, Skype, Discord, Zoom, etc... Our program takes in the basic fundamentals from chat rooms like Zoom 
  and off voice calls, share screen, face time, and direct messaging capabilities. One additional feature is to be able to place 
  a url link of a youtube video where users are then able to watch the video in sync with their peers as a group watch.

  This method is meant to by pass sharing the screen and having host and user delay. By having the videos be run on all clients, 
  and synchronizing the times to allow a cohesive group watch.

  Challenges & Issues:
  The challenges we faced are being to listen and stream between multiple users. The current issue with the state of our program 
  is that only two users are able to connect through voice call, face time, and screen share. However, the direct messaging is able 
  to host multiple users chatting on the stream. Another issue is that the video links can processed and the video can be played, but 
  the functionality to synchronize the videos are still not implemented.

  Future Improvements:
  Currently the only set of communication that is dependent on a server is the direct messaging. Due to direct messaging being hosted
  through a server client type of structure multiple users can enter in. If the server is bolstered to host additional features
  such as voice call, share screen or facetime then multple people can stream and view at the same time. In addition, having the server
  communicate between clients will help in video synchronization to allow time stamps to be easily communicated between all clients.

  Lessons Learned:
  The team learned alot about how to utilize sockets, and threading to allow communication between clients and servers. We learned
  how connections can be made through finding the IP Address and attaching the proper ports to fit the receiving and sending end. Another
  value lesson learned was in port forwarding and understanding how clients can connect in different networks. The team also worked
  on learning how to create a GUI using Python and making an interface that can be easy to use and understand.
