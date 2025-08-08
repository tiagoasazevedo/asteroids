import pygame # this allows us to use code from the open-source pygame library throughout this file

from player import Player  # import the Player class from the player module
from constants import * # import all constants from the constants module

# Main function to run the game
def main():
    pygame.init()  # initialize all imported pygame modules
    clock = pygame.time.Clock()  # create a clock object to manage the frame rate
    dt = 0  # initialize a variable to keep track of the time delta between frames
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # create a window with the specified dimensions

    updatable = pygame.sprite.Group()  # create a group to hold all updatable objects
    drawable = pygame.sprite.Group()  # create a group to hold all drawable objects
    Player.containers = updatable, drawable  # set the containers for the Player class

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # create a Player object at the center of the screen

    running = True
    while running:
        for event in pygame.event.get():  # this checks for events like key presses or window close requests
            if event.type == pygame.QUIT: # if the window close button is pressed
                running = False # stop the game loop
        dt = clock.tick(60) / 1000.0  # calculate the time delta in seconds
        updatable.update(dt)  # update all updatable objects with the time delta
        screen.fill((0, 0, 0))  # fill the screen with black color
        for sprite in drawable:  # iterate through all drawable objects
            sprite.draw(screen)  # draw each object on the screen
        pygame.display.flip()  # update the display

    pygame.quit() # clean up and close the game window

if __name__ == "__main__":
    main()