#  Game class

import pygwidgets
from Constants import *
from Deck import *
from Card import *


class Game():
    CARD_OFFSET = 110
    CARDS_TOP = 300
    CARDS_LEFT = 75
    NCARDS = 8
    POINTS_CORRECT = 15
    POINTS_INCORRECT = 10
    POINTS_EQUAL = 25
    POINTS_UNEQUAL = 20

    def __init__(self, window):
        self.window = window
        self.oDeck = Deck(self.window)
        self.score = 100
        self.compare = 200
        self.scoreText = pygwidgets.DisplayText(window, (300, 164),
                                                'Score: ' + str(self.score),
                                                fontSize=36, textColor=WHITE,
                                                justified='right')

        self.messageText = pygwidgets.DisplayText(window, (50, 460),
                                                  '', width=900, justified='center',
                                                  fontSize=36, textColor=WHITE)

        self.compareText = pygwidgets.DisplayText(window, (500, 164),
                                                  'target: ' + str(self.compare),
                                                  fontSize=36, textColor=WHITE,
                                                  justified='left')
        # loading congratulation sound
        self.congratulation = pygame.mixer.Sound("sounds/Congratulations.wav")
        self.loserSound = pygame.mixer.Sound("sounds/loser.wav")
        self.winnerSound = pygame.mixer.Sound("sounds/ding.wav")
        self.cardShuffleSound = pygame.mixer.Sound("sounds/cardShuffle.wav")
        self.atmosphereSound = pygame.mixer.Sound("sounds/Atmospheric-ambient-music.wav")

        self.cardXPositionsList = []
        thisLeft = Game.CARDS_LEFT
        # Calculate the x positions of all cards, once
        for cardNum in range(Game.NCARDS):
            self.cardXPositionsList.append(thisLeft)
            thisLeft = thisLeft + Game.CARD_OFFSET

        self.reset()  # start a round of the game

    def reset(self):  # this method is called when a new round starts
        self.cardShuffleSound.play()
        self.atmosphereSound.play()

        self.cardList = []
        self.oDeck.shuffle()
        for cardIndex in range(0, Game.NCARDS):  # deal out cards
            oCard = self.oDeck.getCard()
            self.cardList.append(oCard)
            thisXPosition = self.cardXPositionsList[cardIndex]
            oCard.setLoc((thisXPosition, Game.CARDS_TOP))

        self.showCard(0)
        self.cardNumber = 0
        self.compare = 200
        self.currentCardName, self.currentCardValue = \
            self.getCardNameAndValue(self.cardNumber)

        self.messageText.setValue('Starting card is ' + self.currentCardName +
                                  '. Will the next card be higher or lower?')

        self.compareText.setValue(f"TargetPoint: {self.compare}")

    def getCardNameAndValue(self, index):
        oCard = self.cardList[index]
        theName = oCard.getName()
        theValue = oCard.getValue()
        return theName, theValue

    def showCard(self, index):
        oCard = self.cardList[index]
        oCard.reveal()

    def hitHigherOrLower(self, higherOrLower):
        self.cardNumber = self.cardNumber + 1
        self.showCard(self.cardNumber)
        nextCardName, nextCardValue = self.getCardNameAndValue(self.cardNumber)

        if higherOrLower == HIGHER:
            if nextCardValue > self.currentCardValue:
                self.score = self.score + Game.POINTS_CORRECT
                self.messageText.setValue('Yes, the ' + nextCardName + ' was higher')
                self.winnerSound.play()
            else:
                self.score = self.score - Game.POINTS_INCORRECT
                self.messageText.setValue('No, the ' + nextCardName + ' was not higher')
                self.loserSound.play()
        # user hit the EQUAL Button

        elif higherOrLower == EQUAL:

            if nextCardValue == self.currentCardValue:
                self.score = self.score + Game.POINTS_EQUAL
                self.messageText.setValue('Yes, the ' + nextCardName + ' was equal')
                self.winnerSound.play()

            else:
                self.score = self.score - Game.POINTS_UNEQUAL
                self.messageText.setValue('No, the ' + nextCardName + ' was not equal')
                self.loserSound.play()


        elif higherOrLower == LOWER:  # user hit the Lower button

            if nextCardValue < self.currentCardValue:
                nextCardValue < self.currentCardValue
                self.score = self.score + Game.POINTS_CORRECT
                self.messageText.setValue('Yes, the ' + nextCardName + ' was lower')
                self.winnerSound.play()
            else:
                self.score = self.score - Game.POINTS_INCORRECT
                self.messageText.setValue('No, the ' + nextCardName + ' was not lower')
                self.loserSound.play()

        self.scoreText.setValue('Score: ' + str(self.score))

        self.currentCardValue = nextCardValue  # set up for the next card 

        done = (self.cardNumber == (Game.NCARDS - 1))  # did we reach the last card?
        return done

    def draw(self):
        # Tell each card to draw itself
        for oCard in self.cardList:
            oCard.draw()

        self.scoreText.draw()
        self.messageText.draw()
        self.compareText.draw()
