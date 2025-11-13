'''
Create a simple number guessing game.
The user gets 10 chances to guess it.
If the user guesses the number b4 10 chances, stop asking the number from the user, say Congrats and end the Game.
If the user never guesses the number, ask them 10 times and then end the game.
'''

import random

number = random.randint(1,50)
print("Welcome to the Number Guessing Game! We have a number between 1 and 50. You have 10 chances to guess it.")
guesses = 10

while guesses > 0:
    guess = int(input("Guess a number between 1 and 50: "))
    if guess == number:
        print("Congrats, you guessed it!")
        break
    else:
        if guess < number:
            print("Guess higher!")
        else:
            print("Guess lower!")
        guesses -= 1
        if guesses == 0:
            print("Your chances are over!")
            break
        print("You have {} chances left".format(guesses))

print("The number is:", number)
print("Game ended!! Thank you for playing!")
