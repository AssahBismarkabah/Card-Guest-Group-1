# Higher or Lower - pygame version
# Main program

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import pygwidgets
from Game import *

# 2 - Define constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Higher Or Lower")

# 4 - Load assets: image(s), sounds,  etc.
background = pygwidgets.Image(window, (0, 0),
                              'images/background.png')
newGameButton = pygwidgets.TextButton(window, (15, 530),
                                      'New Game', width=100, height=45)
higherButton = pygwidgets.TextButton(window, (440, 520),
                                     'Higher', width=120, height=55)
lowerButton = pygwidgets.TextButton(window, (240, 520),
                                    'Lower', width=120, height=55)
quitButton = pygwidgets.TextButton(window, (880, 530),
                                   'Quit', width=100, height=45)
equalButton = pygwidgets.TextButton(window, (650, 520),
                                    'Equal', width=120, height=55)

# 5 - Initialize variables
oGame = Game(window)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events or key being pressed
    for event in pygame.event.get():
        if ((event.type == QUIT) or
                ((event.type == KEYDOWN) and (event.key == K_ESCAPE)) or
                (quitButton.handleEvent(event))):
            pygame.quit()
            sys.exit()

        if newGameButton.handleEvent(event):
            oGame.reset()
            lowerButton.enable()
            higherButton.enable()
            equalButton.enable()

        if higherButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(HIGHER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()
                equalButton.disable()

        if lowerButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(LOWER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()
                equalButton.disable()
            # handle event when user clicks on equal button
        if equalButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(EQUAL)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()
                equalButton.disable()

    # 8 - Do any "per frame" actions

    # 9 - Clear the window before drawing it again
    background.draw()

    # 10 - Draw the window elements
    # Tell the game to draw itself
    oGame.draw()
    # Draw remaining user interface components
    newGameButton.draw()
    higherButton.draw()
    lowerButton.draw()
    quitButton.draw()
    equalButton.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
