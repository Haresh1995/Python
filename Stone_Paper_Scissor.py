
import random

def gameWin(com,player):
    if com == player:
        return None
    if com == 's':
        if player == 'p':
            return True
        elif player == 'c':
            return False
    elif com == 'p':
        if player == 'c':
            return True
        elif player == 's':
            return False
    elif com == 'c':
        if player == 's':
            return True
        elif player == 'p':
            return False

print("Comp : Stone(s),Paper(p) or Scissor(c)?")
rand = random.randint(1,3)
if rand == 1:
    com = 's'
elif rand == 2:
    com = 'p'
elif rand == 3:
    com = 'c'

player = (input("Player : Stone(s),Paper(p) or Scissor(c)?"))
a = gameWin(com, player)

print(f'Computer choose {com}')
print(f'Player choose {player}')

if player == com:
    print("There is a tie")
if a:
    print("You are a winner")
else:
    print("You loose")



