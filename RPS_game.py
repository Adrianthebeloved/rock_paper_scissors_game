import RPS_utils
import random

print('Starting the Rock Paper Scissors game!')
print('.............')
player_name = input('Please enter your name:')
print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
player_hand = int(input('Please enter a number (0-2):'))
print('..............')

#next we state the control flow that occurs when the hand given has been validated and what next to do
if RPS_utils.validate(player_hand):
    computer_hand = random.randint(0,2)
    RPS_utils.print_hand(player_hand,player_name)
    RPS_utils.print_hand(computer_hand, 'Computer')
    print('.............')
    #next we call the judge function to determine the result
    result = RPS_utils.judge(player_hand,computer_hand)
    print('Result: '+ result)
else:
    print('Please enter a valid number')