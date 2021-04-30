import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game_1 = CardGame()
        self.card1 = Card('diamonds', 1)
        self.card2 = Card('spades', 10)

    def test_check_is_ace(self):
        self.assertEqual(True, self.card_game_1.check_for_ace(self.card1))
    
    def test_check_is_not_ace(self):
        self.assertEqual(False, self.card_game_1.check_for_ace(self.card2))
    
    def test_check_highest_card(self):
        self.assertEqual(self.card2, self.card_game_1.highest_card(self.card1, self.card2))
    
    def test_check_highest_card_other_way_round(self):
        self.assertEqual(self.card2, self.card_game_1.highest_card(self.card2, self.card1))
    
    def test_card_total(self):
        self.assertEqual("You have a total of 11", self.card_game_1.cards_total([self.card1, self.card2]))