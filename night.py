

for x in playerlist:
    if (playerjob[x] == "villager"):
        #villager function
    elif (playerjob[x] == "werewolf"):
        input("who doyou want to kill")
    elif (playerjob[x] == "shaman"):
        shaman(hangedlist, playerjob)
#loopが終わったらprotected とattackedをそれぞれ初期化