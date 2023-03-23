import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return f'{self.value} of {self.suit}'

if __name__ == '__main__':
    valid_values = ['ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    valid_suits = ['hearts', 'diamonds', 'clubs', 'spades']
    test_card = Card('jack', 'hearts')
    print(test_card)