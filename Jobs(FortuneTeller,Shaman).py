#占い師のfunction
playerlist = {}

#実験用にプレーヤーのdictionary 作った
while True:
    print("Select a player's name.")
    name = input()
    if name == "":
        break
    print("Type the job for that player.")
    job = input()
    if job == "":
        break
    playerlist[name] = job

for i in playerlist.items():
    print(i)

#playerlist1 の中に playerlist を入れる
def fortuneteller(playerlist1, playerjob1):
    #playerlistを表示。（誰を選択するか決めやすくする）
    print(playerlist1)
    #誰を占うか選択(choice)
    choice = input("Who would you like to fortune tell?: ")
    #選択したプレーヤーの役職(choice_job)をdictionaryから引っ張ってきてそれを判定元にする。
    choice_job = playerjob1.get(choice)
    #人狼だった時結果が人狼と出るようにする
    if choice_job == "werewolf":
        print(choice + " is a 'werewolf'. ")
    #人狼以外の役職だった場合、人間と出るようにする。
    else:
        print(choice + " is a 'human'. ")

#hangedlist を入れる
def shaman(hangedlist1, playerjob1):
    #playerlistを表示。（誰を選択するか決めやすくする）
    print(hangedlist1)
    #誰を占うか選択(choice)
    choice = input("Who would you like to fortune tell?: ")
    #選択したプレーヤーの役職(choice_job)をplayerjob1 から引っ張ってきてそれを判定元にする。
    choice_job = playerjob1.get(choice)
    #人狼だった時結果が人狼と出るようにする
    if choice_job == "werewolf":
        print(choice + " is a 'werewolf'. ")
    #人狼以外の役職だった場合、人間と出るようにする。
    else:
        print(choice + " is a 'human'. ") 