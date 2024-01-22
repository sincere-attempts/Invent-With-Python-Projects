# This is a Guess the Number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input ()

number = random.randint (1, 100)
print('Well, ' + myName + ', I am thinking of a number between 1 and 100. I will give you six chances.')

for guessesTaken in range (6) :
    print ('Take a guess.') # Four spaces in front of "print"
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' gueses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')

choice = input('Do you want to play again?')
if (choice == 'yes'):
    print('sorry you cant I dont know how to do that yet nor how to use punctuation')
else:
    print('great I didnt want to play again either!')


