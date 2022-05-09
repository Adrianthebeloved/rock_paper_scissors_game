#now we define the function that executes according to the name and hand given
def print_hand(hand,name='Guest'):
    hands = ['Rock', 'Paper', 'Scissors']
    print(name + ' picked: '+ hands[hand])

#next we define the function that validates whether the hand given is legit, and then what next to do
def validate(hand):
    if hand<0 or hand>2:
        return False
    else:
        return True 

#next we define a function for the RockPaperScissors game
def judge(player, computer):
    if player == computer:
        return 'Draw'
    elif player == 0 and computer == 1:
        return 'Lose'
    elif player == 1 and computer == 2:
        return 'Lose'
    elif player == 2 and computer == 0:
        return 'Lose'
    else:
        return 'Win'
