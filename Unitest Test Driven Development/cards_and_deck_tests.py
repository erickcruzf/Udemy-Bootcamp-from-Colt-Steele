#run $ python3 cards_and_deck_tests.py -v
import unittest
from Cards_and_Decks import Card, Deck

class Decks_tests(unittest.TestCase):
    
    def setUp(self):
        self.deck = Deck()

    def test__init__(self):
    	"""decks should have a cards attribute, which is a list of cards for value and suit"""
    	self.assertTrue(isinstance(self.deck.cards, list))
    	self.assertEqual(len(self.deck.cards), 52)

    def test_count(self):
    	"""count should return a count of cards remains in the deck"""
    	self.assertEqual(self.deck.count(), 52)
    	self.deck.cards.pop()
    	self.assertEqual(self.deck.count(), 51)

    def test__repr__(self):
    	"""__repr__ should return a string with the format 'Deck of x cards.'"""
    	self.assertEqual(repr(self.deck), "Deck has 52 cards.")

    def test_deal_sufficient_cards(self):
    	"""deal should deal the number of cards left in the deck"""
    	cards = self.deck._deal(10)
    	self.assertEqual(len(cards), 10)
    	self.assertEqual(self.deck.count(), 42)

    def test_deal_insufficient_cards(self):
    	"""deal should deal the number of cards specified"""
    	cards = self.deck._deal(999)
    	self.assertEqual(len(cards), 52)
    	self.assertEqual(self.deck.count(), 0)

    def test_deal_no_cards(self):
    	"""deal should throw a ValueError if the deck is empty"""
    	self.deck._deal(self.deck.count())
    	with self.assertRaises(ValueError):
    	    self.deck._deal(1)
    		
    def test_shuffle(self):
        self.deck.shuffle()
        self.assertEqual(self.deck.count(),52)

    def test_deal_card(self):
    	card = self.deck.cards[-1]
    	dealt_card = self.deck.deal_card()
    	self.assertEqual([card], dealt_card)
    	self.assertEqual(self.deck.count(),51)

    def test_deal_hand(self):
        self.deck.deal_hand(10)
        self.assertEqual(self.deck.count(),42)

class Card_tests(unittest.TestCase):

    def setUp(self):
        self.card = Card("A","Diamonds")

    def test__init__(self):
    	"""Cards should have a suit and a value"""
    	self.assertEqual(self.card.suit, "Diamonds")
    	self.assertEqual(self.card.value, "A")

    def test__repr__(self):
    	"""repr should return a string of the form 'Value of Suit'"""
    	self.assertEqual(self.card.__repr__(), f"{self.card.value} of {self.card.suit}")

if __name__ == "__main__":
    unittest.main()
