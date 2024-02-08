# Deck class

import random
from Card import *

class Deck():
    #class variable containing the four suits

    SUIT_TUPLE = ('Diamonds', 'Clubs', 'Hearts', 'Spades')

    # This dict maps each card rank to a value for a standard deck of cards

    STANDARD_DICT = {'Ace':1, '2':2, '3':3, '4':4, '5':5,
                                  '6':6, '7':7, '8': 8, '9':9, '10':10,
                                  'Jack':11, 'Queen':12, 'King':13}


    def __init__(self, window, rankValueDict=STANDARD_DICT):

    #create the cards and save in an array using a loop to
    # iterate through the suit, rank and value and append each
    #card object in a list to create a full deck of cards

    def shuffle(self):
    # Copy the starting deck and save it in the playing decklist but before that all
    #cards should be concealed(faced down)

    def getCard(self):

    # Pop one card off the deck and return it since the deck is already shuffled
    #orderwise through an error message

