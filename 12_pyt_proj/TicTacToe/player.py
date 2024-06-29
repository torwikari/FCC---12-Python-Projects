import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
        
    # we want all players to get their next move given a game
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):           # comment
        square = random.choice(game.available_moves())
        return square
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (1-9):')
            try:
                val = int(square) - 1
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful then all good.
            except ValueError:
                print('Invalid square. Try again.')
                
        return val

