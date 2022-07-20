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

comp_pick = Draw()
player_pick = Draw()
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
    time.sleep(2)
    if comp_pick.value > player_pick.value:
        comp_wins += 1
        Results()
        print()
        print("Comp Win!")
        print()
    elif player_pick.value > comp_pick.value:
        player_wins += 1
        Results()
        print()
        print("Player Win!")
        print()

    if Cards != []:
        Re_Draw() 
    else:
        playing = False
        print()
        print(f"Player Wins: {player_wins}\nComp Wins: {comp_wins}")
        if comp_wins > player_wins:
            print("Comp Won The Game Sorry :(\n")
        else:
            print("You Won The Game Congrats!\n")


# TODO: find ways to add player interactivity ex. Replay Button