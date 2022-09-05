import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def test_check_for_ace(self):
        first_card = Card("Spades", 1)
        self.assertEqual(True, CardGame.check_for_ace(self, first_card))

    def test_find_highest_card(self):
        first_card = Card("Clubs", 10)
        second_card = Card("Hearts", 5)
        self.assertEqual(first_card, CardGame.highest_card(self, first_card, second_card))

    def test_count_cards_total(self):
        first_card = Card("Diamonds", 7)
        second_card = Card("Spades", 3)
        cards = [first_card, second_card]
        self.assertEqual("You have a total of 10", CardGame.cards_total(self, cards))