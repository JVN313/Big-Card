import random
from classes import *

Cards = []

def Card_Creator():
    Card_Names= ["ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN",]
    Card_Values = 1
    for name in Card_Names:
        Cards.append(Card(Card_Values,name))
        Card_Values += 1

Card_Creator()

def Draw():
    return Cards.pop(random.randint(0,len(Cards)))

comp_pick = Draw()
player_pick = Draw()
player_wins = 0
comp_wins =0
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
    elif player_pick.value > comp_pick.value:
        player_wins += 1
        Results()
        print()
        print("Player Win")

    Re_Draw()

    #elif comp_pick.value == player_pick.value:
    #    comp_pick= Draw()
    
    if len(Cards) == 0:
        playing = False
        print()
        print(f"Player Wins: {player_wins}\nComp Wins: {comp_wins}")

    #replay = input("PLay Again?: ")
    #if replay == "y":
    #    print()
    #    comp_pick= Draw()
    #    player_pick = Draw()
    #else:
    #    playing = False


# TODO: Fix Draw() on line 16, so the random number generated will always be in range for indexing.