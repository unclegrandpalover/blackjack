import random

#this is the start of the game where you and the dealer draw
def black_jack():
   player_draw()
   dealer_draw()
   player_draw()
   print("the dealer has drawn a card facedown")
   print("your cards add up to", player_total)
   normalgame()




#this is setting a number of decks and making them
num_decks = int(input("How many decks would you like to use?"))
player_total = 0
dealer_total = 0
playerace = 0
dealerace = 0
deck = []
for i in range(0, (52 * num_decks)):
    deck.append(i)



#this is supposed to be the card that the player draws. it takes a random number, assigns that to a card and removes the og value from the deck
def player_draw():
    global player_total
    global playerace
    cardnum = random.choice(deck)
    deck.pop(cardnum)
    #so the card assignments go up to 12, because 51 // 4 = 12, which is the highest possible value (list starts at 0). this makes anything higher thn 51 decrease to fit in.
    while cardnum > 51:
        cardnum = cardnum - 51
    #all of this is card assignment. messy but it works
    if cardnum // 4 == 0 and player_total < 11:
        cardvalue = 11
        rank = "ace"
        playerace += 1
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
    #now we shall tackle suits which is very easy using modulus
    if cardnum % 4 == 0:
        suit = "hearts"
    if cardnum % 4 == 1:
        suit = "clubs"
    if cardnum % 4 == 2:
        suit = "diamonds"
    if cardnum % 4 == 3:
        suit = "spades"
    #now it adds the value to your total and prints the draw
    player_total = cardvalue + player_total
    print("you drew the", rank, "of", suit)

def dealer_draw():
    global dealer_total
    global dealerace
    cardnum = random.choice(deck)
    deck.pop(cardnum)
    #just read player_draw to know what all this does
    while cardnum > 51:
        cardnum = cardnum - 51
    #still card assignment
    if cardnum // 4 == 0 and dealer_total < 11:
        cardvalue = 11
        rank = "ace"
        dealerace += 1
    elif cardnum // 4 == 0 and dealer_total >= 12:
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
    #SUITS SUITS
    if cardnum % 4 == 0:
        suit = "hearts"
    if cardnum % 4 == 1:
        suit = "clubs"
    if cardnum % 4 == 2:
        suit = "diamonds"
    if cardnum % 4 == 3:
        suit = "spades"
    #all of these conditionals are just for flavor text
    if dealer_total == 0 or dealer_total > 11:
        dealer_total = cardvalue + dealer_total
        print("the dealer drew the", rank, "of", suit)
    else:
        dealer_total = cardvalue + dealer_total
        print("the dealer reveals his card to be the", rank, "of", suit)


def normalgame():
    finale = 0
    while finale == 0:
        playeraction = input("what would you like to do now? (hit or stand)")
        if playeraction == "hit":
            player_draw()
            print("your cards add up to", player_total)
        elif playeraction == "stand":
            finale = 1
        else:
            print("the dealer does not understand your yammering")
    dealer_draw()
    print("the dealer's cards add up to", dealer_total)
    #this is
    #room for
    #dealer ai
    #just to let you know
    #now after all that should be win conditions
    #for example
    if player_total > dealer_total:#probably add like "and gameend = 1" or something idk how you code
        print("You have bested the dealer!")
    if player_total == 21 and dealer_total != 21:
        print("Blackjack!")
    #feel free to edit any of this and make sure to add all of them




#function of the start of the game
black_jack()




