
def intro():
    print("You are one of the kings knights.")
    print("After years of brutal war and bloodshed, you return home.")
    print("You stand in the middle of the town square.")
    print("Will you: ")
    print("#1: Go to the tavern?")
    print("#2: Go to the mayors house?")
    print("#3: Go to the watchtower?")
    print()
    Firstpath = input("What will you do? (1/2/3): ")

    if Firstpath == '1':
        print()
        path1()

    elif Firstpath == '2':
        print()
        path2()

    elif Firstpath == '3':
        print()
        path3()

def path1():
    print("You enter the bar and order yourself a beer.")
    print("After all, you deserve some rest now, right?")
    print("As you sit down, you notice a strange, hooded figure luring in the shadows")
    print("Your options are: ")
    print("#1: Ignore the stranger and enjoy your cold beer?")
    print("Try to talk to the stranger?")
    print()
    Secondpath = input("Which one will you choose? (1/2): ")
    if Secondpath == '1':
        print()
        path1_1()

    elif Secondpath == '2':
        print()
        path1_2()

def path1_1():
    print("You get back to your drink.")
    print("Sadly, you seem to not fully know your limits...")
    print("The beers keep coming... 2, 3, 4....")
    print("without any of the other guests or the barkeeper noticing, you get literally blackout drunk")
    print("One person, however, notices your drunken state:")
    print("the shadowy figure you noticed earlier.")
    print("What you sadly did not know: That person was not just some random stranger.")
    print("He is an assasin, hired to kill you.")
    print("As soon as you fall asleep on your table, the hooded figure gets up")
    print("From his cloak, he pulls a dagger.")
    print("You never saw the blade coming, that now is buried deep into your body, just beneath the rip cage...")
    print("GAME OVER")

def path1_2():
    print("With a quick gesture, you manage to get the strangers attention,")
    print("prompting him to come over to your table.")
    print()
    print("The stranger turns out to be a traveler, coming from the distant kingdom of NAMENSIDEE")
    print("You have a long, good conversation, so that you don`t even notice the time flying by.")
    print("As the evening approaches and the darkness begins to fall over the village, the stranger gets up.")
    print("He hastily waves you goodbye, telling you of his wife and children waiting for him at home.")
    print()
    print("Now on your own once again, you drink the last bit of beer left in your glass and attempt to get up.")
    print("What you failed to notice: When your drinking buddy got up, he tapped on the ring he wore on his finger.")
    print("A small movement, for sure, but enough to activate a mechanism inside the jewelery, ")
    print("opening a secret compartment, from which came pouring down a few drops of fluid... ")
    print("The realization hits you too late, as the poison begins flowing through your veins,")
    print("stopping your heartbeat in the matter of seconds.")
    print("Your lifeless body hits the floor, before anyone even notices that there might be something wrong.")
    print("GAME OVER")

def path2():
    print()

def path2_1():
    print()


def path2_2():
    print()

def path3():
    print()

def path3_1():
    print()

def path3_2():
    print()




print("     ######################")
print("     #                    #")
print("     #      Name vergeben #")
print("     #                    #")
print("     ######################")
startGame = input("Would you like to start the game? (Y/N)")
if startGame == "N" or startGame == "n":
    print("See you later then")
elif startGame == "Y" or startGame == "y":
    intro()
