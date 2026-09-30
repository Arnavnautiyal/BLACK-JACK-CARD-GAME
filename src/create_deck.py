import random

CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
    '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def create_deck():
    """Generates and returns a shuffled 52-card deck."""
    symbols = ['♦', '♣', '♥', '♠']
    card_numbers = list(CARD_VALUES.keys())
    deck = []
    for _ in symbols:
        for card in card_numbers:
            deck.append(card)
    random.shuffle(deck)
    return deck
