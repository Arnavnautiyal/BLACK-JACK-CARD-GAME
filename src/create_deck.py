import random

card_values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}

def create_deck():
    symbols=['♦','♣','♥','♠']
    card_number=list(card_values.keys())
    deck=[]
    for _ in symbols:
        for i in card_number:
            deck.append(i)
    return deck
