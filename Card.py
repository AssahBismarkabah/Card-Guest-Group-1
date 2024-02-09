# Card class which is responsible for instantiating the class objects when called

import pygame
#importing pygame for implementing the corresponding window and x-y coordinates portioning
import pygwidgets

#importing pywidgets for the click and button functionality


class Card():
    BACK_OF_CARD_IMAGE = pygame.image.load('images/BackOfCard.png')
#  1.load image of back of Card once and save it in the class variable BACK_OF_CARD_IMAGE
    def __init__(self, window, rank, suit, value):
        #   2.build the window and store its rank,value and suit in a class variable e.g --> self.rank=rank
        self.window = window
        self.rank = rank
        self.suit = suit
        self.cardName = rank + ' of ' + suit
        self.value = value

        #   3.build the path to the file in the image folder that contains the image for a specific card (see UML diagram)
        fileName = 'images/' + self.cardName + '.png'
        # Set some starting location; use setLoc below to change
        #   4. use an image collection object to remember the path of the front and the back of the image

        self.images = pygwidgets.ImageCollection(window, (0, 0),
                                                 {'front': fileName,
                                                  'back': Card.BACK_OF_CARD_IMAGE}, 'back')



    def conceal(self):
        self.images.replace('back')
# tells the image collector to set the back of the card as the current image
    def reveal(self):
        self.images.replace('front')

    def getName(self):
        return self.cardName

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
