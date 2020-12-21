import random

#ask for the number of players playing the game
playernum = input("type the number of players. It has to be between 5 and 8: ")

#ask for the job and make a list out of it
joblist = input ("type the jobs you want in the game, separated with a comma and space: ").split(", ")

#ask for player name
playerlist = []
for i in range (int(playernum)):
    playername = input("type the name of Player" + str(i) + " :")
    playerlist.append(playername)

#make random list from 0 to len(playernum)
numlist = list(range(0, int(playernum)))
rannumlist = random.sample(numlist,len(numlist))

#assign player a job and store it in the list
playerjob = {}

for i in range(int(playernum)):
    rannum = rannumlist[i]
    playerjob[playerlist[i]] = joblist[rannum]