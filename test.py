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
    pick = random.choice(Cards)
    return Cards.pop(pick.value)

p1= Draw()
p2= Draw()
print(p1)
print(p2)
print(Cards)
