'''
Black Jack Program to learn about python!
Anjan Rana Magar
Date:Sep26,2022
'''
import random

# Creating a class Card that makes and return a card!
class Card:
    '''Playing Card'''
    Ranks = list('23456789TJQKA')
    Suits = list("CDHS")
    SuitChar = {"C":chr(9827),"D":chr(9830), "H":chr(9829),"S":chr(9824)}

    def __init__(self,rank, suit):
        ''' Pass rank and suit, it returns you a card. '''

        if rank in Card.Ranks:
            self.rank = rank
        else:
            raise ValueError("Incorrect Rank Given")
        if suit in Card.Suits:
            self.suit = suit
        else:
            raise ValueError("Incorrect Suit Given")

    def __str__(self):
        ''' return the string form of the Card.'''
        return self.rank+Card.SuitChar[self.suit]

# Creating a class Deck that has all the cards from the book:
class Deck:
    ''' A class containing all the cards in the book.'''
    def __init__(self):
        ranklist = Card.Ranks
        suitlist = Card.Suits
        self.mydeck = []
        for i in suitlist:
            for j in ranklist:
                self.mydeck.append(Card(j,i))

    def returndeck(self):
        '''retun the deck but in object form so we need str function to convert to human readable form.'''
        return self.mydeck

    def __str__(self):
        '''passing object through string. We use %13 for thr line break.'''
        decks =''
        count = 1
        for card in range(len(self.mydeck)):
            if count%13==0:
                decks += str(self.mydeck[card])+"\n"
            else:
                decks += str(self.mydeck[card])+ " "
            count += 1
        return decks

    def dealone_Card(self):
        ''' returns one card with pop method:'''
        return self.mydeck.pop()

    def shuffle_Card(self):
        '''shuffle the card:'''
        return random.shuffle(self.mydeck)

class BlackJackHand:
    '''The BlackJackHand is just a hand, it can be of a player or of a dealer, no need to create a separate hand for both.'''
    def __init__(self):
        self.hand = []
        self.hand_str =''

    def getCards(self,deck,n):
        '''get n no of cards from the deck'''
        for i in range(n):
            deck.shuffle_Card()
            pop_card = deck.dealone_Card()
            self.hand.append(pop_card)
            self.hand_str += str(pop_card)+" "

    def reveal_firstcard(self):
        '''return 1st card item'''
        return self.hand[0]

    def __str__(self):
        return self.hand_str

    def handvalue(self):
        ''' Return blackjack value of the hand. '''
        tenpointscard = 'TJQK'
        numbercards = '98765432'
        num_Aces = 0
        value = 0
        for i in self.hand:
            item_o = str(i)
            item = item_o[0]
            if item in tenpointscard:
                value += 10
            elif item in numbercards:
                value += int(item)
            else:
                value+=1
                num_Aces +=1
        if num_Aces>=1:
            if value+10<=21:
                value += 10
        return value

def busted(handvalue):
    if handvalue >= 21:
        return True

def gameplay():
    a_deck = Deck()
    '''Player and Dealer gets the two cards each!'''
    player = BlackJackHand()
    dealer = BlackJackHand()
    player.getCards(a_deck,2)
    dealer.getCards(a_deck, 2)

    player_hand_value = player.handvalue()
    dealer_hand_value = dealer.handvalue()
    print("Player's Card: ",player,
          "\nDealer's Card: ",dealer.reveal_firstcard())


    # display this card as a picture:
    display_aspic(player)
    display_aspic(dealer)

    while not busted(player_hand_value):
        ask_hit = input("Do you want to Hit or Stay? (H/S): ")
        if ask_hit.upper() == 'H':
            player.getCards(a_deck,1)
            print(player)
            player_hand_value = player.handvalue()
            # print("Player Hand Value: ", player_hand_value)

        elif ask_hit.upper()=='S':
            # print("I am exiting out!")
            break
        else:
            continue
    if player_hand_value>21:
        print("Player is Busted!")
    elif player_hand_value == 21:
        print("BlackJack Player")
    else:
        if dealer_hand_value <=17:
            dealer.getCards(a_deck,1)
            dealer_hand_value= dealer.handvalue()
            # print("Dealer Hand Value: ", dealer_hand_value)
            if dealer_hand_value >21:
                print("Dealer is Busted!")


    return player_hand_value, dealer_hand_value

def playone_game():
    ''' We will pass the socre and evalue who win and not!'''
    playerscore, dealerscore = gameplay()
    if playerscore>dealerscore and playerscore<=21:
        print("Player Won!")
    elif playerscore<dealerscore and dealerscore<=21:
        print("Dealer Won!")
    if playerscore == 21:
        print("BlackJack By Player!")
    if dealerscore == 21:
        print("BlackJack By Dealer!")
    if dealerscore ==playerscore:
        print("Draw Games")
    print("Dealervalue:",dealerscore,"Playervalue:",playerscore)


def game():
    rule = "Ten points cards are 'JQKT' where T is a 10. 'A' ace can be either 1 or 11 depending on need."
    rule += "\nOther cards are normal number cards which represent their number itself, '98765432'."
    rule += "\nYou have 2 cards upfront and you have option to hit or stay. Try to get maximum score\nwithout crossing 21.21 is blackjack, winning num."
    print("Welcome to My BlackJack Game via Python. Here are some rules regarding the games: ")
    print(rule)
    play_game = input("\nDo you want to play a game? Type 'Y' for Yes and 'N' for No: ")
    while play_game.upper() == "Y":
        playone_game()
        play_game = input("Do you want to play another game? Type 'Y' for Yes and 'N' for No: ")
        if play_game.upper() == 'N':
            break
game()