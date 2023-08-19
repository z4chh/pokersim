import random
from functions import *

if __name__ == '__main__':

    input_card_1 = input("Please enter your first card: (<value> of <suit>) \n")
    input_card_2 = input("Please enter your second card: (<value of <suits> \n")

    deck = deckmaker()
    card_1 = cardmaker(input_card_1)
    card_2 = cardmaker(input_card_2)

    cardchecker(card_1, card_2)

    print(f'Your cards are the {card_1} and the {card_2}.\n')

    user_hand = [card_1, card_2]
    deck.remove(card_1)
    deck.remove(card_2)

    opp_1 = genhand(deck)
    opp_2 = genhand(deck)
    opp_3 = genhand(deck)
    opp_4 = genhand(deck)
    opp_5 = genhand(deck)

    flop = flopgen(deck)
    print("----------USER HAND------------")
    print(card_1)
    print(card_2)
    print("----------FLOP-----------------")
    for card in flop:
        print(card)
    print('\n')
    input("PRESS ENTER TO FLIP ANOTHER CARD")
    flop.append(flipone(deck))

    print("----------USER HAND------------")
    print(card_1)
    print(card_2)
    print("----------FLOP-----------------")
    for card in flop:
        print(card)
    print('\n')

    input("PRESS ENTER TO FLIP THE FINAL CARD, GOOD LUCK\n")
    flop.append(flipone(deck))
    print("----------USER HAND------------")
    print(card_1)
    print(card_2)
    print("----------FLOP-----------------")
    for card in flop:
        print(card)
    print('\n')
    print(precedence(user_hand, flop))

