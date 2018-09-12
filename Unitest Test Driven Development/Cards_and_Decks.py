from random import shuffle

class Card:
    
    suits_allowed = ("Hearts", "Diamonds", "Clubs", "Spades") 
    value_list = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q","K")
    
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:

    def __init__(self):
        self.cards = [Card(value, suit) for suit in Card.suits_allowed for value in Card.value_list]
    
    def count(self):
    	return len(self.cards)

    def __repr__(self):
        return f"Deck has {self.count()} cards."

    def _deal(self, num):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        fnum = min([self.count(),num])
        cards = self.cards[-fnum:] # removed cards.
        self.cards = self.cards[:-fnum] #remaining deck.
        return cards

    def shuffle(self):
        shuffle(self.cards)
        
    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, number):
        return self._deal(number)