# Hangman is a word guessing game. The computer will choose a random word from the pre-defined list in the file words.txt.
# User has to guess the word. The user has the same amount of 'lives' as the amount of letters in the word.

import random
from Hangman.word_list import words

def main():
    random_word = random.choice(words)          # Pick a random word. 
    word_list = list(random_word)               # Change the word to a list.
    letters = len(word_list)                    # Count the number of items in the list.
    print(random_word, letters)                 # For debugging purposes
    
    # Welcome message, requires an input. Includes number of lives / letters.
    print(f"Your word has {letters} letters. You have the same amount of lives. Let's start.\n")
    lives = letters
    current_guess = '-' * letters
    
    while lives > 0 and '-' in current_guess:
        print(f"Current word: {current_guess}")
        user_guess = input("Input a letter: ").lower()          # Ask for input:
        if len(user_guess) != 1 or not user_guess.isalpha():    # Check if the input is empty and if it's a single letter.
            print("Please input a single letter")
        elif user_guess in current_guess:
            print("You've already guessed that letter")
        else:
            if user_guess in word_list:           ## Check if the random_word contain the user's input.
                print("Great, You've guessed the letter!")
                current_guess = update_word(random_word, current_guess, user_guess)
            else:
                lives -= 1
                print(f"Try again! You have {lives} lives left! :)")
                
    if '-' not in current_guess:
        print(f"Congratulations! You've guessed the word {current_guess}")
    else:
        print(f"You're out of lives. The word was: {random_word}")



def update_word(word, current_guess, guessed_letter):
    # Convert the current guessed state to a list
    guessed_list = list(current_guess)
    
    # Iterate through the word and update the guessed list with the guessed letter
    for index, letter in enumerate(word):
        if letter == guessed_letter:
            guessed_list[index] = guessed_letter
    
    # Convert the list back to a string
    updated_guess = ''.join(guessed_list)
    return updated_guess

main()

