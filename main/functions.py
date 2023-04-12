import random
from sim import deck
from classes import *
from typing import List

valid_values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
valid_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
"""these are used to pull info on the deck from"""


def cardmaker(carddata: str) -> Card:
    """this takes the user input and turns it into the user created data type Card"""
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

def cardchecker(first: Card, second: Card) -> None:
    if first == second:
        print("You cannot have two of the same card!")
        exit()

def deckmaker() -> List[Card]:
    """this function is used to generate a deck"""
    list_deck = []
    global valid_suits
    global valid_values
    for value in valid_values:
        for suit in valid_suits:
            list_deck.append(Card(value, suit))
    return list_deck

def genhand(deck: List[Card]) -> List[Card]:
    """this function generates a hand randomly and removes the cards used from the deck"""
    card_1 = random.choice(deck)
    deck.remove(card_1)
    card_2 = random.choice(deck)
    deck.remove(card_2)
    return [card_1, card_2]

def flopgen(deck: List[Card]) -> List[Card]:
    """this function generates a random flop based on the remaining cards in the deck"""
    return_list = []
    for i in range(5):
        choice = random.choice(deck)
        deck.remove(choice)
        return_list.append(choice)
    return return_list

def precedence(hand: List[Card], flop: List[Card]) -> List[Card]:
    total_cards = []
    for card in hand:
        total_cards.append(card)
    for card in flop:
        total_cards.append(card)

def reshuffle():
    global deck
    deck = deckmaker()




