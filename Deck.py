import random
from Card import *

class Deck:
    SUIT_TUPLE = ('Diamonds', 'Clubs', 'Hearts', 'Spades')
    STANDARD_DICT = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                     '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                     'Jack': 11, 'Queen': 12, 'King': 13}

    def __init__(self, window, rankValueDict=STANDARD_DICT):
        self.window = window
        self.rankValueDict = rankValueDict
        self.decklist = []

        # Create the cards and save them in an array by iterating through the suit, rank, and value
        for suit in self.SUIT_TUPLE:
            for rank, value in self.rankValueDict.items():
                card = Card(self.window, suit, rank, value)
                self.decklist.append(card)

    def shuffle(self):
        # Shuffle the decklist using the random.shuffle() function
        random.shuffle(self.decklist)

    def getCard(self):
        if len(self.decklist) > 0:
            # Pop one card off the decklist and return it
            return self.decklist.pop()
        else:
            print("Error: No cards left in the deck.")