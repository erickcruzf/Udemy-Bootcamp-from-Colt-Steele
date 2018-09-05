from random import shuffle

class Card:
    
    suits_allowed = ("Hearts", "Diamonds", "Clubs", "Spades") 
    value_list = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q","K")
    
    def __init__(self, value, suit):
        if suit not in Card.suits_allowed:
            raise ValueError(f"Card suit must be in {Card.suits_allowed}!")
        if value not in Card.value_list:
            raise ValueError(f"Card value must be in {Card.value_list}!")
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
        return f"Deck has {self.count()} cards"

    def _deal(self, num):
        fnum = min([self.count(),num])
        cards = self.cards[-fnum:]
        self.cards = self.cards[:-fnum]
        return cards

    def shuffle(self):
        shuffle(self.cards)
        
    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, number):
        return self._deal(number)


Deck1 = Deck()
Deck1.shuffle()
print(Deck1.deal_card())
print(Deck1.deal_hand(55))