A test suite using Python's built-in `unittest` framework to test core game logic like hand scoring and Ace reduction.

```python
import unittest
from main import calculate_hand, create_deck

class TestBlackjackGame(unittest.TestCase):
    
    def test_create_deck_length(self):
        deck = create_deck()
        self.assertEqual(len(deck), 52)

    def test_calculate_hand_simple(self):
        hand = ['10', '7']
        self.assertEqual(calculate_hand(hand), 17)

    def test_calculate_hand_with_ace_high(self):
        hand = ['A', '9']
        self.assertEqual(calculate_hand(hand), 20)

    def test_calculate_hand_with_ace_low(self):
        hand = ['A', '9', '5']
        # 11 + 9 + 5 = 25 -> Ace drops to 1 -> 1 + 9 + 5 = 15
        self.assertEqual(calculate_hand(hand), 15)

    def test_calculate_hand_multiple_aces(self):
        hand = ['A', 'A', '9']
        # 11 + 11 + 9 = 31 -> First Ace drops to 1 -> 21 -> Second Ace drops to 1 -> 11
        self.assertEqual(calculate_hand(hand), 11)

if __name__ == '__main__':
    unittest.main()
