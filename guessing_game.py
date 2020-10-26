"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    keep_playing = True
    while keep_playing:
        attempts = 0
        guess = -1
        print("Welcome to the number guessing game")
        random_number = (random.randint(1,10))
        print(random_number)
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
        print(f'Got it!! You guessed the right number! It took {attempts} attempts!')
        
        keep_playing = input("Would you like to play again? (y)es/(n)o  ").lower() == 'y'


# Kick off the program by calling the start_game function.
start_game()