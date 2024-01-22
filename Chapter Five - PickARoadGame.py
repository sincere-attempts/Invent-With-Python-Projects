# Pick a road game

import random
import time

def displayIntro():
    print('''You are standing at a fork between two roads. One way leads to even more sophisticated civilization, one way returns to monke. Which way, modern man?''')
    print()

def chooseRoad():
    road = '' # variable within a function will evaporate when function returns/closes
    while road != '1' and road != '2':
        print('Which road will you go down? (1 or 2)')
        road = input()

    return road # this assigns the value of road to the chooseRoad function iself and close this function block. IE if "road" now equals 1, based on the user inputing 1, then chooseRoad() will now = 1, and close the program. 

def checkRoad(chosenRoad):
    print('You begin down the road...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('You see a light in the distance...')
    print()
    time.sleep(2)

    friendlyRoad = random.randint(1,2)

    if chosenRoad == str(friendlyRoad): # "If this condition is true, execute this If block"
        print('Wow! I think you\'ve discovered a better way of life!')
    else: #If the If condition wasn't true, execute this block
        print('Wow! It\'s even worse this way!')

playAgain = 'yes' #All the other blocks above have been defined, but not run yet. This is actually the first line of the program that runs.
while playAgain == 'yes' or playAgain == 'y': #Sets up a loop that contains the rest of the game code.
    displayIntro() #Calls the displayIntro() function
    roadNumber = chooseRoad() #Will execute the chooseRoad() function to determine a value to then assign to roadNumber
    checkRoad(roadNumber) #Will run the checkRoad function with the value it finds at roadNumber

    print('Do you want to play again? (yes or no)')
    playAgain = input()
     
