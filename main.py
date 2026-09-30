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

def calculate_hand(hand):
   total= sum([card_values[card] for card in hand])
   aces=hand.count('A')
   while total>21 and aces>0:
       total-=10
       aces-=1
   return total

def display_game(player_hand,dealer_hand,hole_card=True):
    if hole_card == False: # To reveal the Dealers second Card
        print(f"\nDealer Hand: {dealer_hand} ")
        print(f"\nDealer Hand Total: {calculate_hand(dealer_hand)} ")
    elif hole_card == True: # To Hide the dealer's card
        print(f"\nDealer Hand: {dealer_hand[0]}, ?")
    print(f"\nPlayer Hand: {player_hand}")
    print(f"\nPlayer Hand Total: {calculate_hand(player_hand)} ")
    print("\n===========================================================================")

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

print("Blackjack")
credit = 1000
print(f"\nYour starting credits:{credit}")
again=""
while True:
    bet = int(input("Credits you want to bet: "))
    if bet>credit:
        print("Sorry you cannot bet more than you have")
        continue
    print(f"Your credits: {credit-bet}")
    result=play_blackjack()
    if result=="Tie":
        print(f"You Won:0\nYour Credits: {credit}")
    elif result=="Win":
            print(f"You Won:{2*bet}\nYour credits: { bet + credit}")
            credit=bet + credit
    elif result=="Lost":
        print(f"You Lost:{bet}\nYour credits: {credit - bet}")
        credit=credit - bet
    again = input("\nPlay another round? (Y/N): ")
    if again != 'Y':
        print("Thanks for playing!")
        break
    elif again == 'Y':
        if credit==0:
            print("Sorry no credits left")
            break

