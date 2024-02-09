# Card class

import pygame
import pygwidgets

class Card():
    Back_Of_Card = pygame.image.load("BackOfCard.png")

    def __init__(self, window, rank, suit, value):
        self.window = window
        self.rank = rank
        self.suit = suit
        self.value = value
        self.cardname = rank + 'of' + suit
        
        fileName = 'images/' + self.cardname + '.png'

        self.images = pygwidgets.ImageCollection(window, (0, 0),{'front': fileName,'back': Card.Back_Of_Card}, 'back')


    def conceal(self):
        self.images.replace('back')

    def reveal(self):
        self.images.replace('front')

    def getName(self):
        return self.cardname

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

    def setLoc(self, loc):  # call the setLoc method of the ImageCollection
        self.images.setLoc(loc)

    def getLoc(self):  # get the location from the ImageCollection
        loc = self.images.getLoc()
        return loc

    def draw(self):
        self.images.draw()



