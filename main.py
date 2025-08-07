import pygame # this allows us to use code from the open-source pygame library throughout this file
import constants # this allows us to use constants defined in the constants.py file
from constants import *
def main():
    pygame.init()  # initialize all imported pygame modules
    pygame.time.Clock()  # create a clock object to manage the frame rate
    clock = pygame.time.Clock()  # create a clock object to manage the frame rate
    dt = 0  # initialize a variable to keep track of the time delta between frames
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # create a window with the specified dimensions
    
    while True:  # game loop
        screen.fill((0, 0, 0))  # fill the screen with black color
        pygame.display.flip()  # update the display to show the changes made to the screen
        for event in pygame.event.get(): # this checks for events like key presses or window close requests
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        clock.tick(60)  # limit the frame rate to 60 frames per second
        dt = clock.tick(60) / 1000.0  # calculate the time delta in seconds

if __name__ == "__main__":
        main()