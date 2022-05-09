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
    return Cards[random.randint(0,9)]

comp_pick = Draw()
player_pick = Draw()
playing = True

def Results():
    print(f"Comp: {comp_pick.name}")
    print(f"Player: {player_pick.name}")

while playing:
    if comp_pick.value > player_pick.value:
        Results()
        print()
        print("Comp Win")
    elif player_pick.value > comp_pick.value:
        Results()
        print()
        print("Player Win")
    elif comp_pick.value == player_pick.value:
        comp_pick= Draw()

    replay = input("PLay Again?: ")
    if replay == "y":
        print()
        comp_pick= Draw()
        player_pick = Draw()
    else:
        playing = False
