# Hangman is a word guessing game. The computer will choose a random word from the pre-defined list in the file words.txt.
# User has to guess the word. The user has the same amount of 'lives' as the amount of letters in the word.

import random
import ast

def main_word():

    with open ('words.txt', 'r') as file:
        content = file.read()
    words = ast.literal_eval(content)
    random_word = random.choice(words)
    print(random_word)


main_word()

