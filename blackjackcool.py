import random

#this is the start of the game where you and the dealer draw
def black_jack():
   player_draw()
   #dealer_draw()
   player_draw()
   #dealer_draw_hidden()
   print("your cards add up to", player_total)

#this is setting a number of decks and making them
num_decks = int(input("How many decks would you like to use?"))
player_total = 0
deck = []
for i in range(0, (52 * num_decks)):
    deck.append(i)


#this is supposed to be the card that the player draws. it takes a random number, assigns that to a card and removes the og value from the deck
def player_draw():
    global player_total
    cardnum = random.choice(deck)
    deck.remove(cardnum)
    #all of this is card assignment. it might be messy but it works
    if cardnum // 4 == 0 and playertotal < 12:
        cardvalue = 11
        rank = "ace"
    elif cardnum // 4 == 0 and player_total >= 12:
        cardvalue = 1
        rank = "ace"

    if cardnum // 4 == 1:
        cardvalue = 2
        rank = "two"

    if cardnum // 4 == 2:
        cardvalue = 3
        rank = "three"

    if cardnum // 4 == 3:
        cardvalue = 4
        rank = "four"

    if cardnum // 4 == 4:
        cardvalue = 5
        rank = "five"

    if cardnum // 4 == 5:
        cardvalue = 6
        rank = "six"

    if cardnum // 4 == 6:
        cardvalue = 7
        rank = "seven"

    if cardnum // 4 == 7:
        cardvalue = 8
        rank = "eight"

    if cardnum // 4 == 8:
        cardvalue = 9
        rank = "nine"

    if cardnum // 4 == 9:
        cardvalue = 10
        rank = "ten"

    if cardnum // 4 == 10:
        cardvalue = 10
        rank = "jack"

    if cardnum // 4 == 11:
        cardvalue = 10
        rank = "queen"

    if cardnum // 4 == 12:
        cardvalue = 10
        rank = "king"
    #now it adds the value to your total and prints the draw
    player_total = cardvalue + player_total
    print("you drew the", rank, "of suit!")



#function of the start of the game
black_jack()








