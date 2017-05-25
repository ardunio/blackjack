import random

def __main__():
    current_roll = roll_craps_dice()
    #This is assuming you bet on the pass line, we will work on making it
    #So other bets are possible
    bet = input('What bet would you like to make? ')
    if bet.lower() == 'pass line' or bet.lower() == 'pass':
        pass_bet(current_roll)
    elif bet.lower() == 'no pass' or bet.lower() == 'not pass':
        not_pass_line(current_roll)
    elif bet.lower() == 'quit':
        pass
    else:
        print ('Not a pass bet or a not pass bet, try pass or pass line or no pass \n',
               'other bets are still being added')

def __init__():
    starting_cash = cash_check()
    print ('Starting cash is ', starting_cash)
    if starting_cash <= 0:
        winnings_add(-starting_cash + 500) #This should set it to zero as -5 + -(-5) = 0 and then adds 500
        print ('You were broke, so we gave you 500 cash')

def cash_check():
     with open ('craps_game.txt', 'r') as textfile:
         cash_file = textfile
         current_cash = int(cash_file.readline().strip())
         return current_cash
     cash_file.close()
     
def winnings_add(winnings):
    current_cash = cash_check()
    with open ('craps_game.txt', 'w') as textfile:
        cash_file = textfile
        new_total = current_cash + winnings
        cash_file.write(str(new_total))
         
def pass_bet(current_roll):
    #How much you bet? Maybe?
    bet_amount = int(input('How much would you like to bet? '))
    #this is a basic pass bet
    if current_roll == 7 or current_roll == 11:
        print ('You win! You rolled', current_roll)
        winnings_add(bet_amount)
    elif current_roll == 2 or current_roll == 3 or current_roll == 12:
        print ('You lose! You rolled', current_roll)
        winnings_add(-bet_amount)
    else:
        #handles the pass line bets after point
        point = current_roll
        print ('The point is', point)
        repeat = True
        while repeat == True:
            new_roll = roll_craps_dice()
            print ('The roll was', new_roll)
            if new_roll == point:
                print ('You win!')
                winnings_add(bet_amount)
                repeat = False
            elif new_roll == 7:
                print ('You lose!')
                winnings_add(-bet_amount)
                repeat = False
            else:
                print ('The roll was', new_roll)

def not_pass_line(current_roll):
    bet_amount = int(input('How much would you like to bet? '))
    if current_roll == 2 or current_roll == 3:
        print ('You win!', current_roll)
        winnings_add(bet_amount)
    elif current_roll == 7 or current_roll == 11:
        print ('You lose!', current_roll)
        winnings_add(-bet_amount)
    elif current_roll == 12:
        print ('You pushed!', current_roll)
    else:
        point = current_roll
        print ('The point is', point)
        repeat = True
        while repeat == True:
            new_roll = roll_craps_dice()
            print ('The roll was', new_roll)
            if new_roll == point:
                print ('You lose!')
                winnings_add(-bet_amount)
                repeat = False
            elif new_roll == 7:
                print ('You win!')
                winnings_add(bet_amount)
                repeat = False
       
def roll_craps_dice():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    total_roll = d1 + d2
    return (total_roll)

__init__()
game_counter = 1
while True:
    __main__()
    cash_on_hand = cash_check()
    print ('You have $', cash_on_hand)
    if cash_on_hand <= 0:
        print ("You have run out of money. Goodbye")
        break
    answer = input ('Play again? ')
    if answer.lower() == 'no':
        break
    else:
        game_counter +=1
        pass
print ('This took {} games'.format(game_counter))
