# Card class which is responsible for instantiating the class objects when called

import pygame #importing pygame for implementing the corresponding window and x-y cordinates portioning
import pygwidgets #importing pywidgets for the click and button functionality

class Card():
    Back_Of_Card = pygame.image.load("BackOfCard.png")

#  1.load image of back of Card Onces and save it in the class variable BACK_OF_CARD_IMAGE
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
#   2.build the window and store its rank,value and suit in a class variable e.g --> self.rank=rank

#   3.build the path to the file in the image folder that contains the image for a specific card (see UML diagram)

#   4. use an image collection object to remember the path of the front and the back of the image

    def conceal(self):
# tells the image collector to set the back of the card as the current image
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



