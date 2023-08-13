import random
from classes import *
from typing import List

valid_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
valid_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
"""these are used to pull info on the deck from"""


def cardmaker(card_data: str) -> Card:
    """this takes the user input and turns it into the user created data type Card"""
    card_val = ''
    card_suit = ''
    i = 0
    global valid_suits
    global valid_values
    for val in valid_values:
        if i == 1:
            continue
        try:
            if str(val) in card_data:
                card_val = val
                i += 1
        except:
            pass
        if 'jack' in card_data.lower():
            card_val = 11
        elif 'queen' in card_data.lower():
            card_val = 12
        elif 'king' in card_data.lower():
            card_val = 13
        elif 'ace' in card_data.lower():
            card_val = 1
    for suit in valid_suits:
        if suit.lower() in card_data.lower():
            card_suit = suit
    return Card(card_val, card_suit)


def cardchecker(first: Card, second: Card) -> None:
    """this takes the user inputted cards and makes sure they are not the same"""
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
    for i in range(3):
        choice = random.choice(deck)
        deck.remove(choice)
        return_list.append(choice)
    return return_list


def flipone(deck: List[Card]) -> Card:
    """this function flips the fourth and fifth card"""
    choice = random.choice(deck)
    deck.remove(choice)
    return choice


def precedence(hand: List[Card], flop: List[Card]) -> int:
    """this function determines precedence of each player"""
    total_cards = []  # List[Card]
    for card in hand:
        total_cards.append(card)
    for card in flop:
        total_cards.append(card)

    # ---------------------------------Royal Flush checker---------------------------------------------------
    valid_royal_flush = [
        [Card(10, 'Hearts'), Card(11, 'Hearts'), Card(12, 'Hearts'), Card(13, 'Hearts'), Card(1, 'Hearts')],
        [Card(10, 'Diamonds'), Card(11, 'Diamonds'), Card(12, 'Diamonds'), Card(13, 'Diamonds'), Card(1, 'Diamonds')],
        [Card(10, 'Spades'), Card(11, 'Spades'), Card(12, 'Spades'), Card(13, 'Spades'), Card(1, 'Spades')],
        [Card(10, 'Clubs'), Card(11, 'Clubs'), Card(12, 'Clubs'), Card(13, 'Clubs'), Card(1, 'Clubs')]
    ]
    card_counter = 0
    for vrf in valid_royal_flush:
        for card in total_cards:
            if card in vrf:
                card_counter += 1
    if card_counter >= 5:
        return 1

    # ---------------------------------Straight Flush checker------------------------------------------------
    straights = [
        [Card(10, 'Hearts'), Card(11, 'Hearts'), Card(12, 'Hearts'), Card(13, 'Hearts'), Card(1, 'Hearts')],
        [Card(10, 'Diamonds'), Card(11, 'Diamonds'), Card(12, 'Diamonds'), Card(13, 'Diamonds'), Card(1, 'Diamonds')],
        [Card(10, 'Spades'), Card(11, 'Spades'), Card(12, 'Spades'), Card(13, 'Spades'), Card(1, 'Spades')],
        [Card(10, 'Clubs'), Card(11, 'Clubs'), Card(12, 'Clubs'), Card(13, 'Clubs'), Card(1, 'Clubs')],

        [Card(9, 'Hearts'), Card(10, 'Hearts'), Card(11, 'Hearts'), Card(12, 'Hearts'), Card(13, 'Hearts')],
        [Card(9, 'Diamonds'), Card(10, 'Diamonds'), Card(11, 'Diamonds'), Card(12, 'Diamonds'), Card(13, 'Diamonds')],
        [Card(9, 'Spades'), Card(10, 'Spades'), Card(11, 'Spades'), Card(12, 'Spades'), Card(13, 'Spades')],
        [Card(9, 'Clubs'), Card(10, 'Clubs'), Card(11, 'Clubs'), Card(12, 'Clubs'), Card(13, 'Clubs')],

        [Card(8, 'Hearts'), Card(9, 'Hearts'), Card(10, 'Hearts'), Card(11, 'Hearts'), Card(12, 'Hearts')],
        [Card(8, 'Diamonds'), Card(9, 'Diamonds'), Card(10, 'Diamonds'), Card(11, 'Diamonds'), Card(12, 'Diamonds')],
        [Card(8, 'Spades'), Card(9, 'Spades'), Card(10, 'Spades'), Card(11, 'Spades'), Card(12, 'Spades')],
        [Card(8, 'Clubs'), Card(9, 'Clubs'), Card(10, 'Clubs'), Card(11, 'Clubs'), Card(12, 'Clubs')],

        [Card(7, 'Hearts'), Card(8, 'Hearts'), Card(9, 'Hearts'), Card(10, 'Hearts'), Card(11, 'Hearts')],
        [Card(7, 'Diamonds'), Card(8, 'Diamonds'), Card(9, 'Diamonds'), Card(10, 'Diamonds'), Card(11, 'Diamonds')],
        [Card(7, 'Spades'), Card(8, 'Spades'), Card(9, 'Spades'), Card(10, 'Spades'), Card(11, 'Spades')],
        [Card(7, 'Clubs'), Card(8, 'Clubs'), Card(92, 'Clubs'), Card(10, 'Clubs'), Card(11, 'Clubs')],

        [Card(6, 'Hearts'), Card(7, 'Hearts'), Card(8, 'Hearts'), Card(9, 'Hearts'), Card(10, 'Hearts')],
        [Card(6, 'Diamonds'), Card(7, 'Diamonds'), Card(8, 'Diamonds'), Card(9, 'Diamonds'), Card(10, 'Diamonds')],
        [Card(6, 'Spades'), Card(7, 'Spades'), Card(8, 'Spades'), Card(9, 'Spades'), Card(10, 'Spades')],
        [Card(6, 'Clubs'), Card(7, 'Clubs'), Card(8, 'Clubs'), Card(9, 'Clubs'), Card(10, 'Clubs')],

        [Card(5, 'Hearts'), Card(6, 'Hearts'), Card(7, 'Hearts'), Card(8, 'Hearts'), Card(9, 'Hearts')],
        [Card(5, 'Diamonds'), Card(6, 'Diamonds'), Card(7, 'Diamonds'), Card(8, 'Diamonds'), Card(9, 'Diamonds')],
        [Card(5, 'Spades'), Card(6, 'Spades'), Card(7, 'Spades'), Card(8, 'Spades'), Card(9, 'Spades')],
        [Card(5, 'Clubs'), Card(6, 'Clubs'), Card(7, 'Clubs'), Card(8, 'Clubs'), Card(9, 'Clubs')],

        [Card(4, 'Hearts'), Card(5, 'Hearts'), Card(6, 'Hearts'), Card(7, 'Hearts'), Card(8, 'Hearts')],
        [Card(4, 'Diamonds'), Card(5, 'Diamonds'), Card(6, 'Diamonds'), Card(7, 'Diamonds'), Card(8, 'Diamonds')],
        [Card(4, 'Spades'), Card(5, 'Spades'), Card(6, 'Spades'), Card(7, 'Spades'), Card(8, 'Spades')],
        [Card(4, 'Clubs'), Card(5, 'Clubs'), Card(6, 'Clubs'), Card(7, 'Clubs'), Card(8, 'Clubs')],

        [Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts'), Card(6, 'Hearts'), Card(7, 'Hearts')],
        [Card(3, 'Diamonds'), Card(4, 'Diamonds'), Card(5, 'Diamonds'), Card(6, 'Diamonds'), Card(7, 'Diamonds')],
        [Card(3, 'Spades'), Card(4, 'Spades'), Card(5, 'Spades'), Card(6, 'Spades'), Card(7, 'Spades')],
        [Card(3, 'Clubs'), Card(4, 'Clubs'), Card(5, 'Clubs'), Card(6, 'Clubs'), Card(7, 'Clubs')],

        [Card(2, 'Hearts'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts'), Card(6, 'Hearts')],
        [Card(2, 'Diamonds'), Card(3, 'Diamonds'), Card(4, 'Diamonds'), Card(5, 'Diamonds'), Card(6, 'Diamonds')],
        [Card(2, 'Spades'), Card(3, 'Spades'), Card(4, 'Spades'), Card(5, 'Spades'), Card(6, 'Spades')],
        [Card(2, 'Clubs'), Card(3, 'Clubs'), Card(4, 'Clubs'), Card(5, 'Clubs'), Card(6, 'Clubs')],

        [Card(1, 'Hearts'), Card(2, 'Hearts'), Card(3, 'Hearts'), Card(4, 'Hearts'), Card(5, 'Hearts')],
        [Card(1, 'Diamonds'), Card(2, 'Diamonds'), Card(3, 'Diamonds'), Card(4, 'Diamonds'), Card(5, 'Diamonds')],
        [Card(1, 'Spades'), Card(2, 'Spades'), Card(3, 'Spades'), Card(4, 'Spades'), Card(5, 'Spades')],
        [Card(1, 'Clubs'), Card(2, 'Clubs'), Card(3, 'Clubs'), Card(4, 'Clubs'), Card(5, 'Clubs')]
    ]




def reshuffle():
    '''this function 'reshuffles' the deck'''
    global deck
    deck = deckmaker()
