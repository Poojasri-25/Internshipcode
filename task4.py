#rock paper scissor

import sys
import random
print("--------------------------------------")
print("🎮 Welcome to Rock-Paper-Scissors Game!")
playerchoice =input(
    "Enter......\n1 for ROCK\n2 for PAPER\n3 for SCISSOR:\n\n"
)
print("--------------------------------------")
print(playerchoice)
player = int(playerchoice)
if player < 1 or player >3:
    print("Enter the Valid Number")
    sys.exit("👎 oohoh! You must enter 1,2 or 3.")

computerchoice = random.choice("123")
computer = int(computerchoice)
print ("You choose :"+  playerchoice +"|" + "Python choose:"+ computerchoice)
if player ==1 and computer == 3:
    print("🎉You win!")
elif player ==2 and computer == 1:
    print("🎉You win!")
elif player ==3 and computer ==2 :
    print("🎉You win!")
elif player == computer:
    print("😯Tie game!")

else:
    print("🐍Python win!")