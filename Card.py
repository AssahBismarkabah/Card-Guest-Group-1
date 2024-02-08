# Card class which is responsible for instantiating the class objects when called

import pygame #importing pygame for implementing the corresponding window and x-y cordinates portioning
import pygwidgets #importing pywidgets for the click and button functionality

class Card():

#  1.load image of back of Card Onces and save it in the class variable BACK_OF_CARD_IMAGE
    def __init__(self, window, rank, suit, value):

#   2.build the window and store its rank,value and suit in a class variable e.g --> self.rank=rank

#   3.build the path to the file in the image folder that contains the image for a specific card (see UML diagram)

#   4. use an image collection object to remember the path of the front and the back of the image

    def conceal(self):
# tells the image collector to set the back of the card as the current image
    def reveal(self):

    def getName(self):

    def getValue(self):

    def getSuit(self):

    def getRank(self):

    def setLoc(self, loc):  # call the setLoc method of the ImageCollection

    def getLoc(self):  # get the location from the ImageCollection

    def draw(self):



