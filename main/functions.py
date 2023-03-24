
#This file will serve as the location for all of my function definitions
from classes import *

valid_values = ['Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
valid_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

def cardmaker(carddata: str) -> Card:
    card_val = ''
    card_suit = ''
    i = 0
    global valid_suits
    global valid_values
    for val in valid_values:
        if i == 1:
            continue
        if val.lower() in carddata.lower():
            card_val = val
            i += 1
    for suit in valid_suits:
        if suit.lower() in carddata.lower():
            card_suit = suit
    return Card(card_val, card_suit)

