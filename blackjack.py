import random
import os

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

cards_scores = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

class Card:
    def __init__(self, suit, value, score):
        self.suit = suit
        self.value = value
        self.score = score

    def show_card(self):
        print(self.value, self.suit)

    # This will check if a card of the same value is present or not, doesn't bother about the suit. 
    # We'll use this functionality to check if we have an ace.
    def __eq__(self, other):
        return self.value == other.value


deck = []
for suit in suits:
    for card in cards:
        deck.append(Card(suits_values[suit], card, cards_scores[card]))

# CODE STRUCTURE AND ORGANIZATION
#TODO: Make a main function and declare all instatiations in the main function.
#TODO: May be make dealer and player into separate classes to prevent copy paste

# GAMEPLAY IMPROVEMENT
#TODO: Using Ace: Should Ace be more convenient usage or, is the first Ace appearance always 11? For now its always 11
#TODO: What happens when dealer and player get blackjack in the first turn?
#TODO: If the player hits and gets to 21, but the dealer already has a blackjack, dealer wins I guess. Need to implement that.


def BlackJack(deck):

    player_cards = []
    dealer_cards = []

    player_score = 0
    dealer_score = 0

    print("Welcome to Blackjack! Press any key to start!")
    input()

    while(len(player_cards) < 2):

        # Deal player cards
        current_player_card = random.choice(deck)
        player_cards.append(current_player_card)
        player_score += current_player_card.score
        deck.remove(current_player_card)

        # Manage two aces
        if( (len(player_cards) == 2) and (player_cards[0].score == 11) and ((player_cards[1].score == 11)) ):
            player_cards[1].score -= 10
            player_score -= 10

        # Print player cards
        if(len(player_cards) == 2):
            print("Player Cards: ")
            player_cards[0].show_card()
            player_cards[1].show_card()
            print("Player Score: ", player_score)
            print("\n")

        
        # Deal dealer cards
        current_dealer_card = random.choice(deck)
        dealer_cards.append(current_dealer_card)
        dealer_score += current_dealer_card.score
        deck.remove(current_dealer_card)

        # Manage two aces
        if( (len(dealer_cards) == 2) and (dealer_cards[0].score == 11) and ((dealer_cards[1].score == 11)) ):
            dealer_cards[1].score -= 10
            dealer_score -= 10

        # Print dealer cards
        if(len(dealer_cards) == 2):
            # Show only the first card for dealer
            print("Dealer Cards: ")
            dealer_cards[0].show_card()
            print("Dealer Score: ", dealer_cards[0].score)
            print("\n")


    # If the player has a blackjack, declare as the winner. 
    # TODO: I wonder what happens when both player and dealer have blackjack in the first turn .. 
    if(player_score == 21):
        print("Blackjack! Player wins!")
        quit()

    while(player_score < 21):
        user_choice = input("Press h to hit and s to stick!") 

        if(user_choice.upper() == 'H'):
            print("User chose to hit!")

            current_player_card = random.choice(deck)

            #This is to handle if Ace is already present in player's hand
            if(current_player_card.score == 11 and current_player_card in player_cards):
                current_player_card.score -= 10
                player_cards.append(current_player_card)
                player_score += 1
            else:
                player_cards.append(current_player_card)
                player_score += current_player_card.score

            deck.remove(current_player_card)

            # Print player and dealer cards and scores after every hit turn
            print("Player Cards: ")
            for aCard in player_cards:
                aCard.show_card()
            print("Player Score: ", player_score)
            print("\n")

            print("Dealer Cards: ")
            dealer_cards[0].show_card()
            print("Dealer Score: ", dealer_cards[0].score)
            print("\n")


        elif(user_choice.upper() == 'S'):
            break

        else:
            print("Wrong input! Press h to hit and s to stick!")


    if(player_score > 21):
        print("Player Busted!")
        quit()

    if(player_score == 21):
        print("Player's got a Blackjack!")

    #Now dealer would reveal the cards and score
    print("Dealer Cards: ")
    for dCard in dealer_cards:
        dCard.show_card()
    print("Dealer Score: ", dealer_score)
    print("\n")

    while(dealer_score < 17):
        current_dealer_card = random.choice(deck)

        #This is to handle if Ace is already present in dealer's hand
        if(current_dealer_card.score == 11 and current_dealer_card in dealer_cards):
            current_dealer_card.score -= 10
            dealer_cards.append(current_dealer_card)
            dealer_score += 1
        else:
            dealer_cards.append(current_dealer_card)
            dealer_score += current_dealer_card.score

        deck.remove(current_dealer_card)

        # Print player and dealer cards and scores after every hit turn
        print("Player Cards: ")
        for aCard in player_cards:
            aCard.show_card()
        print("Player Score: ", player_score)
        print("\n")

        #Now dealer would reveal the cards and score
        print("Dealer Cards: ")
        for dCard in dealer_cards:
            dCard.show_card()
        print("Dealer Score: ", dealer_score)
        print("\n")

    if(dealer_score > 21):
        print("Dealer bust! Player wins")

    if(player_score == dealer_score):
        print("Its a tie!")

    elif(player_score > dealer_score):
        print("Player Wins!")

    elif(player_score < dealer_score):
        print("Dealer Wins!")

    quit()
           


BlackJack(deck)