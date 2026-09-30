def display_game(player_hand,dealer_hand,hole_card=True):
    if hole_card == False: # To reveal the Dealers second Card
        print(f"\nDealer Hand: {dealer_hand} ")
        print(f"\nDealer Hand Total: {calculate_hand(dealer_hand)} ")
    elif hole_card == True: # To Hide the dealer's card
        print(f"\nDealer Hand: {dealer_hand[0]}, ?")
    print(f"\nPlayer Hand: {player_hand}")
    print(f"\nPlayer Hand Total: {calculate_hand(player_hand)} ")
    print("\n===========================================================================")
