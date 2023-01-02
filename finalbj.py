import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    def __str__(self):
        return f"{self.value} of {self.suit}"
    
    def get_value(self):
        if self.value in ["jack", "queen", "king"]:
            return 10
        if self.value == "ace":
            return 11
        return self.value

class Deck():
    def __init__(self):
        self.deck = []
        ranks = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]
        suits = ["spades", "hearts", "clubs", "diamonds"]
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.deck.append(card)
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)


class Player(): 
    def __init__(self):
        self.playing_cards = []

    def receive_card(self, card):
        self.playing_cards.append(card)

    def show_cards(self):
        print(f"Player's cards: {self.playing_cards}")

    def get_player_value(self):
        sum_of_cards = 0
        for card in self.playing_cards:
            card.get_value()
            sum_of_cards += card.get_value()
        return sum_of_cards

    def bust(self):
        return self.get_player_value() > 21

class Dealer():
    def __init__(self):
        self.playing_cards = []
        self.hidden_card = []

    def receive_card(self, card):
        self.playing_cards.append(card)

    def receive_hidden_card(self, card):
        self.hidden_card.append(card)

    def show_cards(self):
        print(f"Dealer Cards: {self.playing_cards}, Hidden Card")
    
    def reveal_cards(self):
        print(f"Dealers Cards: {self.playing_cards}, {self.hidden_card}")

    def get_value(self):
        sum_of_cards = 0
        for card in self.playing_cards:
            sum_of_cards += card.get_value()

        for card in self.hidden_card:
            sum_of_cards += card.get_value()

        return sum_of_cards

class Game():
    def __init__(self):

        self.deck = Deck()
        self.deck.shuffle()
    
    def start_game(self):
        card1 = self.deck.deal()
        card2 = self.deck.deal()
        self.player = Player()
        self.player.receive_card(card1)
        self.player.receive_card(card2)
        self.player.show_cards()
        self.player.get_player_value()


        card3 = self.deck.deal()
        card4 = self.deck.deal()
        self.dealer = Dealer()
        self.dealer.receive_card(card3)
        self.dealer.receive_hidden_card(card4)
        self.dealer.show_cards()
    
    def hit(self):
        card5 = self.deck.deal()
        self.player.receive_card(card5)
        self.player.show_cards()
        print(self.player.get_player_value())    
    
    def hit_dealer(self):
        card5 = self.deck.deal()
        self.dealer.receive_card(card5)
        self.dealer.reveal_cards()
        print(self.dealer.get_value())  

    def over_17(self):
        return self.dealer.get_value() < 17

    def over_21(self):
        return self.player.get_player_value() < 21
 
    
jen = Game()

def playblackjack():

    print("Welcome to the table. Let's begin")
    jen.start_game()
    if jen.dealer.get_value() == 21 and jen.player.get_player_value() != 21:
        print(f"Dealer wins")
        return 
    elif jen.player.get_player_value() == 21 and jen.dealer.get_value() != 21:
        print(f"Player wins")
        return
    elif jen.player.get_player_value() == 21 and jen.dealer.get_value() == 21:
        print(f"Push")
        return

    while jen.over_21():
        answer = input("Would you like to hit or stay?\n")
        if answer == "hit":
            jen.hit()

        elif answer == "stay":
            break

    if jen.player.bust():
        print("Dealer wins")
        return
   
    jen.dealer.reveal_cards()
    jen.dealer.get_value()

    while jen.over_17():
        jen.hit_dealer()
        
    if jen.dealer.get_value() > 21:
        print(f"Dealer busts, you win")
        return

    if jen.dealer.get_value() > jen.player.get_player_value():
        print(f"Dealer wins")
        return

playblackjack() 
            
  
                

