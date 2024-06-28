import random

def play():
    
    while True:
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors': \n")
    
        if user == '':
            print('You must input something')
            continue
        if  user not in ['r', 'p', 's']:
            print("Input 'r' or 'p' or 's' :) ")
            continue
    
        break
    
    computer = random.choice(['r', 'p', 's'])
    
    
    if user == computer:
        return 'It\'s a tie'
    elif is_win(user, computer):
        return 'Congrats, you\'ve won!'
    else: 
        return 'You lost!'
    
def is_win(player, opponent):
    # r > s, s > p, p > r
    # return true if player wins
    return  (player == 'r' and opponent == 's') or \
            (player == 's' and opponent == 'p') or \
            (player == 'p' and opponent == 'r')
        
print(play())