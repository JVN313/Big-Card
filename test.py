#working code for player choice
print(f"Here is your hand!\n{player.hand.cards}\n")
player.choice= int(input("Choose a card to play by its number example, to play ONE enter 1\n"))
for i in player.hand.cards:
    if player.choice == i.value:
        player.choice = player.hand.cards.index(i)
        print(player.play())