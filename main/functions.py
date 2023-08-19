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
        card_counter = 0
    if card_counter >= 5:
        return 1

    # ---------------------------------Straight Flush checker------------------------------------------------
    card_counter = 0
    straight_flushes = [
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
    for straight_flush in straight_flushes:
        for card in total_cards:
            if card in straight_flush:
                card_counter += 1
        if card_counter >= 5:
            return 2
        card_counter = 0

    # ---------------------------------Four of a kind checker-------------------------------------------------
    card_count = {}

    for card in total_cards:
        rank = card.value
        if rank in card_count:
            card_count[rank] += 1
            if card_count[rank] == 4:
                return 3
        else:
            card_count[rank] = 1

    # --------------------------------Full House Checker------------------------------------------------------
    card_count = {}
    for card in total_cards:
        rank = card.value
        if rank in card_count:
            card_count[rank] += 1
        else:
            card_count[rank] = 1
    for card in card_count:
        if card_count[card] >= 3:
            card_count[card] = -3
            for updated_card in card_count:
                if card_count[updated_card] >= 2:
                    return 4

    # -----------------------------Flush---------------------------------------------------------------------
    card_count = {}
    for card in total_cards:
        suit = card.suit
        if suit in card_count:
            card_count[suit] += 1
            if card_count[suit] == 5:
                return 5
        else:
            card_count[suit] = 0

    # -----------------------------Straight Checker----------------------------------------------------------
    ranks = []
    for card in total_cards:
        ranks.append(card.value)
    ranks = sorted(ranks)
    duplicate_count = 0
    for value in ranks:
        duplicate_count = ranks.count(value)
        if duplicate_count == 2:
            ranks.remove(value)
        if duplicate_count == 3:
            ranks.remove(value)
            ranks.remove(value)
    num_of_combinations = 2
    for i in range(num_of_combinations):
        if ranks[i + (len(ranks) - duplicate_count - 3)] - ranks[i] == 4:
            return 6

    # -------------------------------Three of a kind----------------------------------------------------------
    for card in total_cards:
        if total_cards.count(card) == 3:
            return 7

    # -------------------------------Two pair-----------------------------------------------------------------
    two_pair_tally = 0
    current_total_cards = total_cards
    for card in current_total_cards:
        if current_total_cards.count(card) == 2:
            two_pair_tally += 1
            current_total_cards.remove(card)
    if two_pair_tally >= 2:
        return 8

    # -------------------------------pair---------------------------------------------------------------------
    for card in total_cards:
        if total_cards.count(card) == 2:
            return 9

    # -------------------------------high card--------------------------------------------------------------
    return 10

def reshuffle():
    '''this function 'reshuffles' the deck'''
    global deck
    deck = deckmaker()


def translator(place: int) -> None:
    if place == 1:
        print("Royal Flush!! You're gonna win.")
    elif place == 2:
        print("Straight Flush! You've surely won")
    elif place == 3:
        print("Four of a kind!")
    elif place == 4:
        print("Full house!")
    elif place == 5:
        print("Flush, nice")
    elif place == 6:
        print("Straight")
    elif place == 7:
        print("Three of a kind")
    elif place == 8:
        print("Two pair")
    elif place == 9:
        print("Pair..")
    elif place == 10:
        print("Hope for high card...")


