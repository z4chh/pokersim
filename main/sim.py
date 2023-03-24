import random
from functions import *
from classes import *

if __name__ == '__main__':

    input_card_1 = input("Please enter your first card: \n")
    input_card_2 = input("Please enter your second card: \n")

    deck = []
    for val in valid_values:
        for suit in valid_suits:
            deck.append(Card(val, suit))

    card_1 = cardmaker(input_card_1)
    card_2 = cardmaker(input_card_2)

    print(f'Your cards are the {card_1} and the {card_2}.')
