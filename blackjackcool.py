import random




def player_draw():
    cardnum = random.choice(deck)
    deck.remove(cardnum)
    cardnum // 4 = cardnum




def black_jack():
   player_draw()

#this is setting a number of decks and making them
num_decks = int(input("How many decks would you like to use?"))
deck = []
for i in range(1, (52 * num_decks) + 1):
    deck.append(i)


black_jack()
print(deck)




