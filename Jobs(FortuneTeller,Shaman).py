#占い師のfunction
playerjob = {}
playerlist = []
attackedlist = []
victim = 0
protected = 0
villagercount = 0

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
    playerjob[name] = job

for i in playerjob.items():
    print(i)

#playerlist1 の中に playerlist を入れる
def fortuneteller(playerlist1, playerjob1):
    #playerlistを表示。（誰を選択するか決めやすくする）
    print(playerlist1)
    #誰を占うか選択(choice)
    choice = input("Who would you like to fortune tell?: ")
    #選択したプレーヤーの役職(choice_job)をdictionaryから引っ張ってきてそれを判定元にする。
    choice_job = playerjob1.get(choice)
    #人狼だった時、結果が人狼と出るようにする
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

def werewolf(playerlist1, victim1):
    print("Who would you like to atttack tonight?")
    print(playerlist1)
    print()
    victim1 = input("Your choice: ")
    return victim1

def knight(playerlist1, protected1):
    print("Who would you like to protect tonight?")
    print(playerlist1)
    print()
    protected1 = input("Your choice: ")
    return protected1


#騎士の選んだ人と人狼の選んだ人が一致していた場合　→　守られる
if victim == protected:
    #守られたため何も起こらない
    print('The attack form the werewolf failed!')
    print('There is no victim.')
    #初期化
    victim = 0
    protected = 0

#それ以外、つまり人狼の選んだ人と騎士の選んだ人が一致していない場合　→　死亡
else:
    #attackedlistに被害者をアペンド
    print(victim + " got attacked last night from the werewolf.")
    attackedlist.append(victim)
    #playerlist からいなくなるようにremoveする。
    playerlist.remove(victim)
    #村人のカウンターが1つ減る
    villagercount -= 1
    #初期化
    victim = 0
    protected = 0