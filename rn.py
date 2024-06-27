import random 

## The user is guessing computers number.

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess the number: "))
        if guess > random_number:
            print("Your number is too big!")
        elif guess < random_number:
            print("Your number is too small!")
        
    print(f"Congratulations, you've guessed the number {random_number}! :)")
    
## The computer is guessing users number.
    
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f' is {guess} too high (H), too low (L), or correct (C)?')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
            
    print(f'Yay! the computer guessed your number {guess}, correctly!')
    

computer_guess(1000)
