#Imported modules
import time
import random
from random import randint 
from colorama import Fore, Style, Back

#Intro input
m = input ("""Spin length in seconds? 
(Each spin length is randomized from 0/instant to whatever you choose) 
(Default: 15 seconds): """)
if m == (""):
    m = 15
else:
    m = m
#print ("m =",m) #Used to make sure m is working between default and user chosen length


#Retry prompt
def ask():
    
    q = input("Hit Enter to spin again, or type in any key and hit Enter to exit: ")

    while q == "":
        wheel(), ask()
    else:
        exit()


#The wheel itself
def wheel():
    
    #Time it takes to spin
    a = round(random.uniform(0, float(m)), 1)

    print("")
    print("Spinning!")
    #print("a =", a) #Used to make sure a is working and giving random numbers each time
    print("")

    time.sleep(a)

    if a == 1:
        print("The wheel spun for approximately", a, "second.")
    else:
        print("The wheel spun for approximately", a, "seconds.")

    #Color/number output
    n = randint(-1,36)

    if n == -1:
        print (Fore.GREEN + "00")
        print (Style.RESET_ALL)
    elif n == 0:
        print (Fore.GREEN + "0")
        print (Style.RESET_ALL)
    elif n == 1 or n == 3 or n == 5 or n == 7 or n == 9 or n == 12 or n == 14 or n == 16 or n == 18 or n == 19 or n == 21 or n == 23 or n == 25 or n == 27 or n == 30 or n == 32 or n == 34 or n == 36:
        print (Fore.RED + Style.BRIGHT + "RED", n)
        print (Style.RESET_ALL)
    elif n == 2 or n == 4 or n == 6 or n == 8 or n == 10 or n == 11 or n == 13 or n == 15 or n == 17 or n == 20 or n == 22 or n == 24 or n == 26 or n == 28 or n == 29 or n == 31 or n == 33 or n == 35:
        print (Fore.WHITE + Style.DIM + "BLACK", n)
        print (Style.RESET_ALL)

wheel(), ask()