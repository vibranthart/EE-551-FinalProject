def timeSync(server1=-25000, user1=-25000, user2=-25000, user3=-25000, user4=-25000):

    global user1Synced
    global user2Synced 
    global user3Synced 
    global user4Synced
    
    serverLow = server1 - 5000
    serverHigh = server1 + 5000
    error = -25000

    if (user1 > serverHigh) or (user1 < serverLow):
        user1Synced = False
        print("User 1 Not Synced")
    elif (user1 <= serverHigh) or (user1 >= serverLow):
        user1Synced = True
        print("User 1 Synced")   
    if (user2 > serverHigh) or (user2 < serverLow):
        user2Synced = False
        print("User 2 Not Synced")
    elif (user2 <= serverHigh) or (user2 >= serverLow):
        user2Synced = True
        print("User 2 Synced")
    if (user3 > serverHigh) or (user3 < serverLow):
        user3Synced = False
        print("User 3 Not Synced")
    elif (user3 <= serverHigh) or (user3 >= serverLow):
        user3Synced = True
        print("User 3 Synced")
    if (user4 > serverHigh) or (user4 < serverLow):
        user4Synced = False
        print("User 4 Not Synced")
    elif (user4 <= serverHigh) or (user4 >= serverLow):
        user4Synced = True
        print("User 4 Synced")
    else:
        print("An Error has occured")

    if (user1 == error) and (user1Synced == False):
        print("User 1 Not Connected")
    if (user2 == error) and (user2Synced == False):
        print("User 2 Not Connected")
    if (user3 == error) and (user3Synced == False):
        print("User 3 Not Connected")
    if (user4 == error) and (user4Synced == False):
        print("User 4 Not Connected")