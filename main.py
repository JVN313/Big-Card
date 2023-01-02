import random
import time
from classes import *

Cards = []

def Card_Creator():
    Card_Names= ["ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN"]
    for index, name in enumerate(Card_Names, 1):
        Cards.append(Card(index,name))

Card_Creator()

def Draw():
    return Cards.pop(random.randint(0,len(Cards)-1))

def Computer_Play():
    i = (random.randint(0,len(computer.hand.cards)-1))
    return i

computer = Player("Computer")
player = Player("Jamm")

while Cards != []:
    player.hand.cards.append(Draw())
    computer.hand.cards.append(Draw())

#GameLoop
print(f"Here is your hand!\n{player.hand.cards}\n")
player.choice= int(input("Choose a card to play by its number example, to play ONE enter 1\n"))
for i in player.hand.cards:
    if player.choice == i.value:
        player.choice = player.hand.cards.index(i)
        player.test = i

computer.choice = Computer_Play()
print(f"You PLayed {player.test}")
print(f"The Computer played {computer.hand.cards[computer.choice]}")

if player.play().value > computer.play().value:
    print("You Win!")
else:
    print("computer Win!")

#comp_pick = Draw()
#player_pick = Draw()
#player_wins = 0
#comp_wins = 0
#playing = True

#def Re_Draw():
#    global comp_pick, player_pick
#    comp_pick = Draw()
#    player_pick = Draw()  

#def Results():
#    print(f"Comp: {comp_pick.name}")
#    print(f"Player: {player_pick.name}")



#while playing:
#    time.sleep(2)
#    if comp_pick.value > player_pick.value:
#        comp_wins += 1
#        Results()
#        print()
#        print("Comp Win!")
#        print()
#    elif player_pick.value > comp_pick.value:
#        player_wins += 1
#        Results()
#        print()
#        print("Player Win!")
#        print()

#    if Cards != []:
#        Re_Draw() 
#    else:
#        playing = False
#        print()
#        print(f"Player Wins: {player_wins}\nComp Wins: {comp_wins}")
#        if comp_wins > player_wins:
#            print("Comp Won The Game Sorry :(\n")
#        else:
#            print("You Won The Game Congrats!\n")


# TODO: find ways to add player interactivity ex. Replay Button
#TODO format player hand