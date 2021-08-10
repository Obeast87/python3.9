import random
import time
from random import randint

def game():
    cpu = randint(1,3)
    player = input("Rock, Paper, or Scissors? (r/p/s): ")

    if player != ("r") and player != ("p") and player != ("s"):
        print ("Invalid Input")
        print("")
        game()

    print("")
    print("Rock!")
    time.sleep(0.5)
    print("Paper!")
    time.sleep(0.5)
    print("Scissors!")
    time.sleep(0.5)
    print("SHOOT!")
    print("")
    time.sleep(0.2)

    if cpu == 1:
        print ("CPU CHOOSES ROCK!")
    if cpu == 2:
        print ("CPU CHOOSES PAPER!")
    if cpu == 3:
        print ("CPU CHOOSES SCISSORS!")
    
    time.sleep(0.5)

    #CPU Rock
    if cpu == 1 and player == ("r"):
        print ("Tie!")
    if cpu == 1 and player == ("p"):
        print ("You Win!")
    if cpu == 1 and player == ("s"):
        print ("You Lose!")

    #CPU Paper
    if cpu == 2 and player == ("r"):
        print ("You Lose!")
    if cpu == 2 and player == ("p"):
        print ("Tie!")
    if cpu == 2 and player == ("s"):
        print ("You Win!")

    #CPU Scissors
    if cpu == 3 and player == ("r"):
        print ("You Win!")
    if cpu == 3 and player == ("p"):
        print ("You Lose!")
    if cpu == 3 and player == ("s"):
        print ("Tie!")
        
    again()

def again():
    print("")
    a = input("Play again? (y/n): ")
    if a == ("y"):
        game()
    if a == ("n"):
        exit()
    else:
        print("Invalid Input")
        again()

game()