import random

playerIn = True
dealerIn = True

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
player_hand = []
dealer_hand = []

def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)
    
def total(turn):
    total = 0
    aces = 0
    face_cards = ['J', 'Q', 'K']
    for card in turn:
        if isinstance(card, int):
            total += card
        elif card in face_cards:
            total += 10
        else:  # Ace case ('A')
            aces += 1
            total += 11
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def revealDealerHand():
    if len(dealer_hand) == 2:
        return str(dealer_hand[0])
    elif len(dealer_hand) > 2:
        return str(dealer_hand[0]) + " and X"

for _ in range(2):
    dealCard(player_hand)
    dealCard(dealer_hand)

print(dealer_hand)
print(player_hand)

while playerIn or dealerIn:
    print(f"Dealer has {revealDealerHand()}")
    print(f"Player has {player_hand} with a total of {total(player_hand)}")
    
    if playerIn:
        stayOrHit = input("1 to stay, 2 to hit: ")
    
    if total(dealer_hand) > 16:
        dealerIn = False
    else:
        dealCard(dealer_hand)
    
    if stayOrHit == '1':
        playerIn = False
    else:
        dealCard(player_hand)
        
    if total(player_hand) >= 21:
        break
    elif total(dealer_hand) >= 21:
        break

if total(player_hand) == 21:
    print(f"You win, you have {total(player_hand)} and dealer has {total(dealer_hand)}")
    print("Blackjack!!!")
elif total(dealer_hand) == 21:
    print(f"Dealer wins, you have {total(player_hand)} and dealer has {total(dealer_hand)}")
    print("Blackjack!!!, Dealer wins")
elif total(player_hand) > 21:
    print(f"Dealer wins, you have {total(player_hand)} and dealer has {total(dealer_hand)}")
elif total(dealer_hand) > 21:
    print(f"You win, you have {total(player_hand)} and dealer has {total(dealer_hand)}")
elif 21 - total(dealer_hand) < 21 - total(player_hand):
    print(f"Dealer wins, you have {total(player_hand)} and dealer has {total(dealer_hand)}")
elif 21 - total(dealer_hand) > 21 - total(player_hand):
    print(f"You win, you have {total(player_hand)} and dealer has {total(dealer_hand)}")