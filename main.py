import pygame # this allows us to use code from the open-source pygame library throughout this file
from player import Player  # import the Player class from the player module
from constants import * # import all constants from the constants module
def main():
    pygame.init()  # initialize all imported pygame modules
    pygame.time.Clock()  # create a clock object to manage the frame rate
    clock = pygame.time.Clock()  # create a clock object to manage the frame rate
    dt = 0  # initialize a variable to keep track of the time delta between frames
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # create a window with the specified dimensions
    Player.__init__(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # create a Player object at the center of the screen

    running = True
    while running:
        screen.fill((0, 0, 0))  # fill the screen with black color
        Player.draw(screen)  # draw the player on the screen
        pygame.display.flip()  # update the display to show the changes made to the screen
        for event in pygame.event.get():  # this checks for events like key presses or window close requests
            if event.type == pygame.QUIT:
                running = False
        dt = clock.tick(60) / 1000.0  # calculate the time delta in seconds

    pygame.quit()

if __name__ == "__main__":
    main()