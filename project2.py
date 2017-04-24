import random

playing = False
chip_pool = 100
bet = 1

suits = {'H', 'D', 'C', 'S'}
ranking = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10' , 'J', 'Q', 'K'}
card_value = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10 , 'J':10, 'Q':10, 'K':10}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def card_string(self):
        print (self.suit + self.rank)
        

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False # Aces can be 1 or 11

    def add_card(self):
        






class Player(object):
    def __init__(self, bankroll = 100):
        self.bankroll = bankroll

    def adjust_bankroll(self, amount):
        self.bankroll += amount


class Game
