choiceStart = input("choose Apple or Banana: ")

if choiceStart.upper() =="APPLE":
    choiceA = input("choose ONE or TWO: ")
    if choiceA.upper() == "ONE":
        choiceOne = input ("chosee RED, BLUE, or GREEN: ")
        if choiceOne.upper() == "RED":
            print("RED Ending")
        elif choiceOne.upper() == "BLUE":
            print ("Blue ending")
        elif choiceOne.upper() == "GREEN":
            print ("Green ending")
        else:
            print("No valid color choice")
    elif choiceA.upper() =="TWO":
        choiceTwo = input("CIRCLE or SQUARE: ")
        if choiceTwo.upper() == "CIRCLE":
            print ("Circle ending")
        elif choiceTwo.upper() == "SQUARE":
            print ("Square ending")
        else:
            print ("no valid shape choice")
elif choiceStart.upper() == "BANANA":
    choiceB = input("Choose RIGHT or LEFT: ")
    if choiceB.upper() == "RIGHT":
        choiceRight = input("Choose JAM or JELLY: ")
        if choiceRight.upper() == "JAM":
            print ("JAM ending")
        elif choiceRight.upper() == "JELLY":
            print ("Jelly ending")
        else:
            print ("No valid topping found")
    elif choiceB.upper == "LEFT":
        choiceLeft = input("choose NORTH or SOUTH: ")
        if choiceLeft == "NORTH":
            print("north ending") 
        elif choiceLeft == "SOUTH":
            print("South ending")
        else:
            print("no valid cardinal direction found")
    else:
        print("no valid side direction found")
else:
    print("no valid fruit found")

