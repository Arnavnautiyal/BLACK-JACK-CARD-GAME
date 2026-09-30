def calculate_hand(hand):
    total = sum([CARD_VALUES[card] for card in hand])
    aces = hand.count('A')
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total
