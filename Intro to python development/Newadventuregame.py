answer = input ("Let's play a funny game! Press enter to start the game and enjoy it!")


QuestionOne = input("Do you want to explore a beach or a mountain? [BEACH/MOUNTAIN]")

if QuestionOne.upper() =="BEACH":
    choiceBeach = input("You are in the middle of the sea in a boat and it is broken and it is sinking, What would you do, would you SWIM to an island or REPAIR the hole? [SWIM/REPAIR]")
    if choiceBeach.upper() == "SWIM":
        answerOne = input ("What would you choose to take from the broken boot, a FLOAT, an emergency FLARE or a BACKPACK with food? ")
        if answerOne.upper() == "FLOAT":
            print("Thas is a good choice, You will reach the Island")
        elif answerOne.upper() == "FLARE":
            print ("It would not be a good idea because it would get wet and it would not work ")
        elif answerOne.upper() == "BACKPACK":
            print ("Good choice it would help you calm your hunger for a few days! ")
        else:
            print("No valid option")
    elif choiceBeach.upper() =="REPAIR":
        choiceRepair = input("You have a HAMMER and a BUCKET in the boat, which one would you choose?" )
        if choiceRepair.upper() == "HAMMER":
            print ("With a hammer you will not be able to fix the boat and it will sink, you lost the game!" )
        elif choiceRepair.upper() == "BUCKET":
            print ("Good choice since it will allow you to remove the water!" )
        else:
            print ("No valid answer")
elif QuestionOne.upper() == "MOUNTAIN":
    choiceMountain = input("You are at the top of the mountain, it is very cold and you see a CAVE and a MATCH. Which one would you choose? CAVE/MATCH")
    if choiceMountain.upper() == "CAVE":
        choiceCave = input("You meet with a wolf inside the cave. would you choose a STONE or RUN?")
        if choiceCave.upper() == "STONE":
            print ("You would probably scare the wolf out of the cave!" )
        elif choiceCave.upper() == "RUN":
            print ("The wolf would reach you since it runs faster, You have lost the game!")
        else:
            print ("Wrong option")
    elif choiceMountain.upper() == "MATCH":
        choiceMatch = input("You have some matches and you want to light firewood. What would you choose, PAPER or ALCOHOL?")
        if choiceMatch.upper() == "PAPER":
            print("The snow dampened the paper so it wouldn't light. you have lost the game!") 
        elif choiceMatch.upper() == "ALCOHOL":
            print("Excellent choice, alcohol will help ignite the fire faster" )
        else:
            print("No valid choice")
    else:
        print("No valid option try again")
else:
    print("Try again, you wrote it wrong")