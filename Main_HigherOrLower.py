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


# 4 - Load assets: image(s), sounds,  etc.
background = pygwidgets.Image(window, (0, 0),
                            'images/background.png')
newGameButton = pygwidgets.TextButton(window, (20, 530),
                            'New Game', width=100, height=45)
higherButton = pygwidgets.TextButton(window, (540, 520),
                            'Higher', width=120, height=55)
lowerButton = pygwidgets.TextButton(window, (340, 520),
                            'Lower', width=120, height=55)
quitButton = pygwidgets.TextButton(window, (880, 530),
                            'Quit', width=100, height=45)

# Initialize variables
oGame = Game(window)

#  Loop forever
while True:

    # to-do Check for and handle events being sent from the front end


    #  Do any "per frame" actions

    #  Clear the window before drawing it again
    background.draw()

    #  Draw the window elements
    # Tell the game to draw itself
    oGame.draw()
    # Draw remaining user interface components
    newGameButton.draw()
    higherButton.draw()
    lowerButton.draw()
    quitButton.draw()

    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)