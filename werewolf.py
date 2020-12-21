import random

#the list of jobs according to the number of players
fourplayer = ["villager", "werewolf", "knight", "fortune teller"]
fiveplayer = ["villager", "villager", "werewolf", "knight", "fortune teller"]
sixplayer = ["villager", "villager", "villager", "werewolf", "knight", "fortune teller"]

#ask for the number of players playing the game
playernum = input("type the number of players. It has to be between 4 and 6: ")


#ask for player name
playerlist = []
for i in range (int(playernum)):
    playername = input("type the name of Player" + str(i) + " :")
    playerlist.append(playername)

#make random list from 0 to len(playernum)
numlist = list(range(0, int(playernum)))
rannumlist = random.sample(numlist,len(numlist))

