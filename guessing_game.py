"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    # write your code inside this function.
    keep_playing = True
    current_high_score = None
    while keep_playing:
        attempts = 0
        guess = -1
        print("Welcome to the number guessing game!!")
        print("-------------------------------------\n")
        if current_high_score != None:
            print(f'The current HIGH SCORE is {current_high_score}\n')
        random_number = (random.randint(1,10))
        #For debugging purposes
        #print(random_number)
        while guess != random_number:
            try:
                try:
                    guess = int(input("Guess what number I'm thinking of. It's between 1-10\n"))
                except ValueError as err:
                    raise ValueError("Try guessing with an actual number next time!")
                if guess < 1 or guess > 10:
                    raise ValueError("The number should be in range! Remember, it's between 1-10")
            except ValueError as err:
                print(err)
            else:
                attempts += 1
                if guess < random_number:
                    print(f"The number I'm thinking of is HIGHER than {guess}")
                elif guess > random_number:
                    print(f"The number I'm thinking of is LOWER than {guess}")
        print(f'\nGot it!! You guessed the right number! It took {attempts} attempts!\n')
        if current_high_score == None:
            current_high_score = attempts
        if attempts < current_high_score:
            current_high_score = attempts
        #Any answer that is not 'y' considered a No
        keep_playing = input("Would you like to play again? (y)es/(n)o  ").lower() == 'y'
        print('\n')

# Kick off the program by calling the start_game function.
start_game()