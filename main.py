import random
from classes import *

Cards = []

def Card_Creator():
    Card_Names= ["ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN"]
    for index, name in enumerate(Card_Names, 1):
        Cards.append(Card(index,name))

Card_Creator()

def Draw():
    return Cards.pop(random.randint(0,len(Cards)-1))

comp_pick = Draw()
player_pick = Draw()
test = len(Cards)
player_wins = 0
comp_wins = 0
playing = True

def Re_Draw():
    global comp_pick, player_pick
    comp_pick = Draw()
    player_pick = Draw()

def Results():
    print(f"Comp: {comp_pick.name}")
    print(f"Player: {player_pick.name}")

while playing:
    if comp_pick.value > player_pick.value:
        comp_wins += 1
        Results()
        print()
        print("Comp Win")
        print()
    elif player_pick.value > comp_pick.value:
        player_wins += 1
        Results()
        print()
        print("Player Win")
        print()

    if Cards != []:
        Re_Draw() 
    else:
        playing = False
        print()
        print(f"Player Wins: {player_wins}\nComp Wins: {comp_wins}")


# TODO: Fix Draw() on line 16, so the random number generated will always be in range for indexing.