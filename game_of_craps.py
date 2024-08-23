import random 

wallet = 0
your_point = 0
player_name = ''
bet = 0

def game_start():
    global wallet, player_name
    player_name = input('Welcome to the Game of Craps. What is your name?:')
    chips = int(input(f'Hi {player_name}. How many chips would you like to buy?:'))
    wallet += chips
    gameplay()
    
    
def gameplay():
    global wallet, player_name, bet, your_point
    bet = int(input(f'Ready to Play! You have ${wallet} in your wallet {player_name}. Whats your bet?: '))
    while bet > wallet:
        bet = int(input(f'Sorry {player_name}, you only have ${wallet}. Whats your bet?:'))
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    total_point = roll1 + roll2
    if total_point == 7 or total_point == 11:
        wallet += bet
        print(f'Rolled: {roll1}, {roll2} = {total_point}')
        print(f'Winner! You won ${bet}')
        next_round = input('Do you want to play again? (yes/no):')
        if next_round == 'yes':
            gameplay()
        else:
            print('Thanks for Playing')            
    elif total_point == 2 or total_point == 3 or total_point == 12:
        wallet -= bet
        print(f'Rolled: {roll1}, {roll2} = {total_point}')
        print(f'Oops, Sorry {player_name}. You lost ${bet}')
        if wallet == 0:
            print(f'You are BROKE. Sorry {player_name} - come back and play again some time.')
        else:
            next_round = input('Do you want to play again? (yes/no):')
            if next_round == 'yes':
               gameplay()
            else:
               print('Thanks for Playing')                   
    else:
        your_point = total_point
        print(f'Rolled: {roll1}, {roll2} = {total_point}')
        print(f'Your point is {total_point}')
        multiple_rounds()


def multiple_rounds():
    global wallet, player_name, bet, your_point
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    total_point = roll1 + roll2
    if total_point == your_point:
        wallet += bet
        print(f'Rolled: {roll1}, {roll2} = {total_point}')
        print(f'Winner! You won ${bet}')
        next_round = input('Do you want to play again? (yes/no):')
        if next_round == 'yes':
            gameplay()
        else:
            print('Thanks for Playing')
    elif total_point == 7:
        wallet -= bet
        print(f'Rolled: {roll1}, {roll2} = {total_point}')
        print(f'Oops, Sorry {player_name}. You lost ${bet}')
        if wallet == 0:
            print(f'You are BROKE. {player_name} - come back and play again some time.')
        else:
            next_round = input('Do you want to play again? (yes/no):')
            if next_round == 'yes':
               gameplay()
            else:
               print('Thanks for Playing')
    else:
        print(f'Rolled: {roll1}, {roll2} = {total_point}')
        multiple_rounds()               

game_start()