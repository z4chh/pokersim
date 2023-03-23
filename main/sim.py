import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return f'{self.value} of {self.suit}'

if __name__ == '__main__':
    valid_values = ['Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    valid_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    input_card_1 = input("Please enter your first card: \n")
    input_card_2 = input("Please enter your second card: \n")


    card_1_val = ''
    card_1_suit = ''

    card_2_val = ''
    card_2_suit = ''

    i = 0
    for val in valid_values:
        if i == 1:
            continue
        if val.lower() in input_card_1.lower():
            card_1_val = val
            i = 1
    for suit in valid_suits:
        if suit.lower() in input_card_1.lower():
            card_1_suit = suit

    i = 0
    for val in valid_values:
        if i == 1:
            continue
        if val.lower() in input_card_2.lower():
            card_2_val = val
    for suit in valid_suits:
        if suit.lower() in input_card_2.lower():
            card_2_suit = suit

    card_1 = Card(card_1_val, card_1_suit)
    card_2 = Card(card_2_val, card_2_suit)

    deck = []
    for val in valid_values:
        for suit in valid_suits:
            deck.append(Card(val, suit))

    print(f'Your cards are the {card_1.__str__()} and the {card_2.__str__()}.')
