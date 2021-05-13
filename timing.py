def timeSync(server=-25000, user1=-25000, user2=-25000, user3=-25000, user4=-25000):

    global user1Synced
    global user2Synced 
    global user3Synced 
    global user4Synced
    
    if (user1 > (server + 5000)) or (user1 < (server - 5000)):
        user1Synced = False
        print("User 1 Not Synced")
    elif (user1 <= (server + 5000)) or (user1 >= (server - 5000)):
        user1Synced = True
        print("User 1 Synced")   
    if (user2 > (server + 5000)) or (user2 < (server - 5000)):
        user2Synced = False
        print("User 2 Not Synced")
    elif (user2 <= (server + 5000)) or (user2 >= (server - 5000)):
        user2Synced = True
        print("User 2 Synced")
    if (user3 > (server + 5000)) or (user3 < (server - 5000)):
        user3Synced = False
        print("User 3 Not Synced")
    elif (user3 <= (server + 5000)) or (user3 >= (server - 5000)):
        user3Synced = True
        print("User 3 Synced")
    if (user4 > (server + 5000)) or (user4 < (server - 5000)):
        user4Synced = False
        print("User 4 Not Synced")
    elif (user4 <= (server + 5000)) or (user4 >= (server - 5000)):
        user4Synced = True
        print("User 4 Synced")
    else:
        print("An Error has occured")

    if (user1 == -25000) and (user1Synced == False):
        print("User 1 Not Connected")
    if (user2 <= -25000) and (user2Synced == False):
        print("User 2 Not Connected")
    if (user3 <= -25000) and (user3Synced == False):
        print("User 3 Not Connected")
    if (user4 <= -25000) and (user4Synced == False):
        print("User 4 Not Connected")