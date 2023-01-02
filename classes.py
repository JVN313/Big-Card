class Card:

    def __init__(self,value,name):
        self.value= int(value)
        self.name = name

    def __repr__(self):
        return f"Card({self.name}:{self.value})"

class Hand:
    
    def __init__(self):
        self.cards = []

    def __repr__(self) -> str:
        f"{self.cards}"


class Player:

    def __init__(self,name):
        self.name = name
        self.hand = Hand()
        self.choice = " "

    def play(self):
        return self.hand.cards.pop(int(self.choice))