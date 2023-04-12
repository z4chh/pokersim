import random
from functions import *

if __name__ == '__main__':

    input_card_1 = input("Please enter your first card: \n")
    input_card_2 = input("Please enter your second card: \n")

    deck = deckmaker()
    card_1 = cardmaker(input_card_1)
    card_2 = cardmaker(input_card_2)

    cardchecker(card_1, card_2)

    print(f'Your cards are the {card_1} and the {card_2}.')

    user_hand = [card_1, card_2]
    deck.remove(card_1)
    deck.remove(card_2)

    opp_1 = genhand(deck)
    opp_2 = genhand(deck)
    opp_3 = genhand(deck)
    opp_4 = genhand(deck)
    opp_5 = genhand(deck)

    flop = flopgen(deck)

    user_hand = precedence(user_hand)

    opp_1 = precedence(opp_1)
    opp_2 = precedence(opp_2)
    opp_3 = precedence(opp_3)
    opp_4 = precedence(opp_4)
    opp_5 = precedence(opp_5)

