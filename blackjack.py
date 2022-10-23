'''
Name: ANJAN RANA MAGAR
Date: 16th Sept. 2022
'''
import random
from random import randrange

class Deck:
    cards = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
    suit = [chr(9827),chr(9829),chr(9830),chr(9824)]
    def __init__(self):
        self.deck =[]
        for i in self.suit:
            for j in self.cards:
                self.deck += [j+i]

    def __str__(self):
        return self.deck

    def deal_one_card(self):
        '''we can use the pop method since we don't want the same card reapeating'''
        return self.deck.pop()

    def shuffle_card(self):
        '''shuffle card for the better dealing of the class'''
        # 1. one way to shuffle is to using random.shuffle(__that list__)
        return random.shuffle(self.deck)
        # 2. the other way is to change the index position:
        # return self.deck

    def getone_card(self):
        return self.deck[randrange(0,len(self.deck))]

# 2. The 2 cards are given to dealer and the player.
def playerhand(deck,num=0):
    '''Function that will get two cards from the getcards() and returns the cards to check the value.'''
    total_card = [deck.getone_card(),deck.getone_card()]
    for i in range(num):
        total_card += [deck.getone_card()]
    return total_card

def dealerhand(deck,num =0):
    '''Function that will get two cards from the getcards() and returns the cards to check the value.'''
    total_card = [deck.getone_card(),deck.getone_card()]
    for i in range(num):
        total_card += [deck.getone_card()]
    return total_card

def hand_value(player, dealer):
    player_value = 0
    dealer_value = 0
    tenpoints = ['K','Q','J','10','A']
    other_points = '23456789'
    for i in player:
        if i[:-1] in tenpoints:
            player_value+=10
        if i[:-1] in other_points:
            player_value += int(i[0])
    for i in dealer:
        if i[:-1] in tenpoints:
            dealer_value += 10
        if i[:-1] in other_points:
            dealer_value += int(i[0])
    return player_value,dealer_value

def ask_card():
    '''ask if the user needs the cards!'''
    ask_user = input("Enter(H/S) for Hit Or Stay? ")
    return ask_user

def give_card(deck):   #,player, dealer, playerhand_value,dealerhand_value)
    answer = ask_card()
    if answer.upper() == 'H':
        # give one card to the player:
        new_deck = playerhand(deck,1)
        return new_deck
    if answer.upper()=='S':
        print("Okey! Let's check what Dealer has on his end!")



    #
    # while ask_user == 'H':
    #     print("i am here!")
    #     a = playerhand(deck,1)
    #     print(a)
    #     playerhand_value,dealerhand_value = hand_value(player, dealer)
    #     if playerhand_value >21:
    #         return isbusted(playerhand_value,dealerhand_value)
    #
    # if ask_user=='S':
    #     dealerhand(deck,1)
    # geet = compare_card(playerhand_value,dealerhand_value)
    # if geet == 1:
    #     return "Congratulation! Player Won!"
    # elif geet == -1:
    #     return "Sorry! You didn't Won!"
    # elif geet== 0:
    #     return "You are draw!"

def compare_card(playerhand_value,dealerhand_value):
    if playerhand_value > dealerhand_value:
        return 1
    elif playerhand_value == dealerhand_value:
        return 0
    else:
        return -1

def isbusted(playerhand_value,dealerhand_value):
    if playerhand_value >21:
        return True
    elif dealerhand_value >21:
        return True
    else:
        return False

def main():
    deck = Deck()
    # card in player and dealer
    player,dealer = playerhand(deck), dealerhand(deck)
    print("PlayerHand Card: ", player)
    print("DealerHand Card: ", dealer)

    # show results for the shuffle:
    deck.shuffle_card()
    print(deck)

    # handvalue for the player and dealer.
    playerhand_value,dealerhand_value = hand_value(player, dealer)
    print("PlayerHand: ", playerhand_value)
    print("DealerHand: ", dealerhand_value)

    # gives card if hit or stay condition.
    # give_card(deck,player, dealer,playerhand_value,dealerhand_value)

    # later change this to while:
    # if ask_card().upper() == 'H':
    #     new_hand = give_card(deck)
    #     print(new_hand)
    #     print("i am here")
    #     playerhand_value,dealerhand_value = hand_value(new_hand,dealer)
    #     print(playerhand_value,dealerhand_value)
    # else:
    #     pass

    # while not isbusted(playerhand_value,dealerhand_value):
    #     isbusted(playerhand_value, dealerhand_value)


if __name__ == '__main__':
    main()

