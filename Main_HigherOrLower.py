import pygame
import pygwidgets

# Creating variables for the display windows
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30

# Creating the display windows
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Buttons and the display images
background = pygwidgets.Image(window, (0, 0), 'images/background.png')

newGameButton = pygwidgets.TextButton(window, (20, 530), 'New Game', width=100, height=45)
higherButton = pygwidgets.TextButton(window, (540, 520), 'Higher', width=120, height=55)
lowerButton = pygwidgets.TextButton(window, (340, 520), 'Lower', width=120, height=55)
quitButton = pygwidgets.TextButton(window, (880, 530), 'Quit', width=100, height=45)

img = pygwidgets.Image(window, (40, 30), 'images/BackOfCard.png')

# Flag to track whether the card should be displayed
show_card = False

# Main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else:
            # Clear the window before drawing it again
            window.fill((0, 0, 0))
            background.draw()

            # Draw the window elements
            newGameButton.draw()
            higherButton.draw()
            lowerButton.draw()
            quitButton.draw()

            # Handle button clicks on the interface.
            if newGameButton.handleEvent(event):
                show_card = True
            elif quitButton.handleEvent(event):
                run = False


            # Draw the card if the flag is set
            if show_card:
                img.draw()

            # Update the window
            pygame.display.update()

            # Slow things down a bit
            clock.tick(FRAMES_PER_SECOND)

pygame.quit()