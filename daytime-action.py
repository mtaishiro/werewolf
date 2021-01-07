from time import sleep

votes = {}
playerlist = ["ryo", "yuuki", "tai", "sam", "haruka", "john", "haruki"]
playerlist2 = {}
hangedlist = []



#definition of time countdown
def timer(max, sectime):

    #maximum time
    max_time = max

    #every second
    sec = sectime

    for i in range (max_time):
        sleep(sec)



def vote():
    #assign 0 (the number of votes) to players for the first vote
    for player in playerlist:
        votes.setdefault(player, 0)
    #print(votes)

    print()

    #start the first vote
    for i in range (len(playerlist)):
        #show player name
        print("Your turn!")
        print()
        
        #vote
        while True:
            suspect = input("choose one player who you hang: ")
            if suspect in playerlist:
                break
            else:
                continue
            
        print()
        print("Your vote ends.")
        print("Give PC to next player!")

        #add each vote
        v = votes[suspect]
        v += 1
        votes[suspect] = v

        print()

    #sort the total votes from larger to smaller
    votes_sorted = dict(sorted (votes.items(), key=lambda x:x[1], reverse=True))
    print("It's time to announce the results of the vote.")
    
    print("Vote results: " + str(votes_sorted))

    print()

    #to output player who gets the largest number of votes
    sorted_keys = list(votes_sorted.keys())

    #to compare the number of votes of players
    numVotes = list(votes_sorted.values())

    #to create the playerlist2 for the second vote
    playerlist2_keys = []

    #when the highest vote and the second one are the same
    if numVotes[0] == numVotes[1]:
        
        #to add player to the playerlist2 for the second vote
        playerlist2_keys.append(sorted_keys[0])
        playerlist2_keys.append(sorted_keys[1])

        #when the third highest vote is smaller than the highest 
        if numVotes[0] > numVotes[2]:
            
            #assign 0 (the number of votes) to players for the second vote
            for player in playerlist2_keys:
                playerlist2.setdefault(player, 0)
            print(playerlist2)

            #start the second vote
            print("start second votes")

            for i in range (len(playerlist)):
                #show player name
                print("Your turn!")
                
                #vote
                while True:
                    suspect2 = input("choose one player who you hang: ")
                    if suspect2 in playerlist2:
                        break
                    else:
                        continue
            
                print()
                print("Your vote ends.")
                print("Give PC to next player!")
                
                #add each vote
                v2 = playerlist2[suspect2]
                v2 += 1
                playerlist2[suspect2] = v2

                print()

            #sort the total votes from larger to smaller    
            hanged = dict(sorted (playerlist2.items(), key=lambda x:x[1], reverse=True))
            print(hanged)

            #to output player who gets the largest number of votes 
            hanged_keys = list(hanged.keys())
            print("Unfortunately, " + hanged_keys[0] + " is killed")

            # to reduce hanged player from the playerlist
            # to create a list that includes only the hanged player
            hangedPlayer = []
            hangedPlayer = sorted_keys[0]
            #print(hangedPlayer)

            # to remove overlapped player
            playerlist.remove(hangedPlayer)
            print(playerlist)

            # to add the hanged player to hangedlist
            hangedlist = sorted_keys[0]

            # to check the job of hanged player
            # if the player is werewolf, decrese the number of werewolf
            # elif the player is Teru Teru Bozu, the game ends
            

        else:
            print("Fortunately, no one is killed")

    # when there is only one player who gets the largest number of votes        
    else:
        print("Unfortunately, " + sorted_keys[0] + " is killed.")


        
        # to reduce hanged player from the playerlist
        # to create a list that includes only the hanged player
        hangedPlayer = []
        hangedPlayer = sorted_keys[0]
        #print(hangedPlayer)

        # to remove overlapped player
        playerlist.remove(hangedPlayer)
        print(playerlist)

        # to add the hanged player to hangedlist
        hangedlist = sorted_keys[0]

    #clear the votes
    votes.clear()
    playerlist2.clear()



print("Daytime action has come.")

print ("Please decide one player to hang in this action.")

print()

print("Players have 5 minutes to discuss.")

print()

print("Please start discussing.")

#5minutes
#timer(300, 1)

print("Time's up!")

print()

print("Then, it's time to vote for deciding who will be hanged")

print()

print("Each player has to choose one player to hang.")

print()

print("Please start voting.")

print()

vote()

print()

print("This is all for the daytime action.")



