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

if comp_pick.value > player_pick.value:
    print("Comp Win")
else:
    print("Player Win")
