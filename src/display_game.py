from src.game_logic import calculate_hand

def display_game(player_hand, dealer_hand, hole_card=True):
    """Displays the current state of the game board to the console."""
    if hole_card == False:
        print(f"\nDealer Hand: {dealer_hand} ")
        print(f"Dealer Hand Total: {calculate_hand(dealer_hand)} ")
    elif hole_card == True:
        print(f"\nDealer Hand: {dealer_hand[0]}, ?")
    
    print(f"Player Hand: {player_hand}")
    print(f"Player Hand Total: {calculate_hand(player_hand)} ")
    print("\n===========================================================================")
