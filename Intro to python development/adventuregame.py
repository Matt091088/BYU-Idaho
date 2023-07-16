answer = input ("Would yoy like to play an adventure game? [YES/NO] ")

if answer.lower() == "YES":
        print ("That is great, Lets play!")
        print() 
else:
    print ("Are you sure it is a funny game!")  
answer = input ("Do you want to explore a beach or a mountain? [BEACH/MOUNTAIN]" )
if answer.lower() == "BEACH":
        print()
        print ("You are in the middle of the sea in a boat and it is broken and it is sinking, What would you do, would you SWIM to an island or REPAIR the hole? [SWIM/REPAIR]")
if answer.lower() == "repair":
        print ("You don't have any tools to fix the broken hole! You lost the game!" )
if answer.lower() == "swim":
        print()
answer = input ("You arrived on the island and found a PINEAPPLE and next to it a FISH. which one would you eat? PINEAPPLE/FISH")
if answer.lower() == "pineapple":
        print()
        print ("Awesome! You managed to have more energy to wait for someone to rescue you, You have won the game!")
elif answer.lower() == "fish":
        print ("the fish was dead and the heat spoiled it, therefore you died and lost the game")     
if answer.lower() == "mountain":
    answer = input ("You are at the top of the mountain, it is very cold and you see a CAVE to refuge and a MATCH to make a fire. Which one would you choose? CAVE/MATCH")
if answer.lower() == "cave":
        print ("fantastic! You were able to get more heat and survive, you have won the game")
elif answer.lower() == "match":
        print ("the match was wet and did not light therefore you lost the game!")

else:
    print ("Invalid option try again!")



