def play_blackjack():
    deck = create_deck()
    random.shuffle(deck)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    display_game(player_hand,dealer_hand,hole_card=True)

    if calculate_hand(player_hand)==21 and calculate_hand(dealer_hand)==21 :
        display_game(player_hand,dealer_hand,hole_card=False)
        print("Both Have Blackjack! Tie")
        return "Tie"
    elif calculate_hand(player_hand)==21:
        display_game(player_hand,dealer_hand,hole_card=False)
        print("Player Have Blackjack! Player Won")
        return "Win"
    elif calculate_hand(dealer_hand)==21:
        display_game(player_hand,dealer_hand,hole_card=False)
        print("Dealer Have Blackjack! Dealer Won")
        return "Lost"

    while True:

        choice=input("Player wants to 'H' for HIT or 'S' for STAND: ")
        if choice=='H':
            player_hand.append(deck.pop())
            display_game(player_hand, dealer_hand, hole_card=True)
            if calculate_hand(player_hand)>21:
                print("Player Busts Dealer Won")
                return "Lost"
            elif calculate_hand(player_hand)==21:
                print("Player Has Blackjack ! Player Won")
                return "Win"
        elif choice=='S':
            display_game(player_hand, dealer_hand, hole_card=True)
            break
        else:
            print("Invalid choice")


    while calculate_hand(dealer_hand) <17:
        print("Dealer Hits")
        dealer_hand.append(deck.pop())
        display_game(player_hand,dealer_hand,hole_card=False)

    player_total =calculate_hand(player_hand)
    dealer_total =calculate_hand(dealer_hand)

    if dealer_total>21:
        print("Dealer Busts,Player Won")
        return "Win"
    if dealer_total==21:
        print("Dealer Has Blackjack ! Dealer Won")
        return "Lost"
    elif dealer_total>player_total:
        print("Dealer Win")
        return "Lost"
    elif dealer_total<player_total:
        print("Player Win")
        return "Win"
    else:
        print("Tie")
        return "Tie"
