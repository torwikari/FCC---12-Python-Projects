# Hangman is a word guessing game. The computer will choose a random word from the pre-defined list in the file words.txt.
# User has to guess the word. The user has the same amount of 'lives' as the amount of letters in the word.

import random
import ast

def word():

    with open ('words.txt', 'r') as file:       # Open the file without the need to close it. 
        content = file.read()                   # Read the file. 
    words = ast.literal_eval(content)           # Parse the data into the list with AST.
    random_word = random.choice(words)          # Pick a random word. 
    letters = len(random_word)                    # Count the number of letters of the word to know the users lives.
    print(random_word, letters)
    
    # Welcome message, requires an input. Includes number of lives / letters.
    user_guess = input(f"Your word has {letters} letters. You have the same amount of lives. Let's start.\nInput a letter: ")
    
    # Check if the input is empty and if it's a single letter.
    while True:
        if len(user_guess) != 1 or not user_guess.isAlpha() or user_guess == '':
            print("Please input a single letter")
    # Check if the random_word contain the user's input.
        lives = letters
        for x in random_word:
            if lives == 0:              ## Check if the user is out of lives.
                print("You're out of lives. Game end.")
            elif x == user_guess:
                print("Great, You've guessed the letter!")
            elif x != user_guess:
                lives -= 1
                print(f"Try again! You have {lives} left! :)")
    
    # Add letter and repeat.

word()

