#Abel Goshu
#1675552

Dict = {}
for i in range(1, 6):
    print("Enter player {}'s jersey number:".format(i))
    jno = int(input())
    print("Enter player {}'s rating:\n".format(i))
    rating = int(input())
    Dict[jno] = rating
print("ROSTER")
for key in sorted(Dict.keys()):
    print("Jersey number: {}, Rating: {}".format(key, Dict[key]))
while (True):
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit\n")
    option = input("Choose an option:\n")
    def add():
        print("Enter new player's Jersey no:")
        jnoo = int(input())
        print("Enter new player's rating:")
        ratingg = int(input())
        Dict[jnoo] = ratingg
        for key in Dict:
            print("Jersey Number: {} , Rating: {} ".format(key, Dict[key]))
    def remove():
        print("Enter player jersey no:")
        deljno = int(input())
        rmv = Dict.pop(deljno)
        for key in Dict:
            print("Jersey Number: {} , Rating: {}\n".format(key, Dict[key]))
    def update():
        print("Enter a jersey no:")
        udtjno = int(input())
        print("Enter new rating for player:")
        udtrating = int(input())
        Dict[udtjno] = udtrating
        for key in Dict:
            print("Jersey Number: {} , Rating: {}\n".format(key, Dict[key]))
    def outputabove():
        print("Enter a rating:")
        rat = int(input())
        print("ABOVE {}".format(rat))
        for i in Dict:
            if Dict[i] > rat:
                print("Jersey no: {} , Rating : {}\n".format(i, Dict[i]))
    def outputroaster():
        for key in Dict:
            print("Jersey Number: {} , Rating: {}\n".format(key, Dict[key]))
    def Quitprog():
        quit()
        print("Exiting...")
    def switcherd(option):
        switcher = {
        'a': add,
        'd': remove,
        'u': update,
        'r': outputabove,
        'o': outputroaster,
        'q': Quitprog
        }
        func = switcher.get(option, lambda: "Invalid Input")
        return func()

    switcherd(option)