class Card:

    def __init__(self,value,name):
        self.value= int(value)
        self.name = name

    def __repr__(self):
        return f"Card({self.name}:{self.value})"

