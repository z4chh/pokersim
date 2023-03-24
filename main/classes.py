#This will be where the classes for my project go

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f'{self.value} of {self.suit}'

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) != Card:
            return False
        return self.suit == other.suit and self.value == other.value
