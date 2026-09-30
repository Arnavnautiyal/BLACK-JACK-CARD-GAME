# Problem Statement & Project Scope

## Overview
The goal of this project is to build a robust, text-based command-line implementation of the classic casino card game, **Blackjack**, using Python. The application handles standard game rules, card value logic (including dynamic Ace adjustments between 1 and 11), dealer AI behavior, and an integrated credit/betting management loop.

## Functional Requirements
1. **Deck Generation & Shuffling**: Construct a standard 52-card deck consisting of 4 suits and 13 distinct card values, utilizing random shuffling before each round.
2. **Hand Calculation**: Accurately compute the total value of a hand, ensuring Aces dynamically downgrade from 11 to 1 when a hand's total exceeds 21 (bust prevention).
3. **Player Choices**: Allow the user to make interactive decisions during their turn:
   - **Hit ('H')**: Draw another card from the deck.
   - **Stand ('S')**: End turn and pass control to the dealer.
4. **Dealer AI**: Automatically draw cards until the dealer's hand total reaches a minimum of 17.
5. **Betting & Credit Tracking**: Initialize the user with a starting bankroll (credits). Update credits dynamically based on wins, losses, and ties, terminating the game if the balance hits zero.