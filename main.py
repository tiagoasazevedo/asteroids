import pygame # this allows us to use code from the open-source pygame library throughout this file

from player import Player  # import the Player class from the player module
from constants import * # import all constants from the constants module
from asteroid import Asteroid  # import the Asteroid class from the asteroid module
from asteroidfield import AsteroidField  # import the AsteroidField class from the asteroidfield module
from shots import Shot  # import the Shot class from the shots module

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

    asteroids = pygame.sprite.Group()  # create a group to hold all asteroid objects
    Asteroid.containers = asteroids, updatable, drawable  # set the containers for the Asteroid class

    asteroid_field = pygame.sprite.Group()  # create a group to hold the asteroid field
    AsteroidField.containers = updatable  # set the containers for the AsteroidField class
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # create a Player object at the center of the screen
    asteroid_field.add(AsteroidField())  # add an instance of AsteroidField to the group

    shots = pygame.sprite.Group()  # create a group to hold all shot objects
    Shot.containers = shots, updatable, drawable  # set the containers for the Shot class

    running = True
    while running:  # main game loop
        for event in pygame.event.get():  # this checks for events like key presses or window close requests
            if event.type == pygame.QUIT: # if the window close button is pressed
                running = False # stop the game loop
        dt = clock.tick(60) / 1000.0  # calculate the time delta in milliseconds since the last frame, limiting to 60 FPS
        updatable.update(dt)  # update all updatable objects with the time delta
        for sprite in asteroids:  # iterate through all asteroid sprites
            sprite.update(dt) # update each asteroid's position based on its velocity and the time delta
            for shot in shots:  # iterate through all shot sprites
                if sprite.collision(shot):  # check for collision between asteroid and shot
                    sprite.kill()  # remove the asteroid
                    shot.kill()  # remove the shot
                    break  # stop checking for more collisions
            if sprite.collision(player): # check for collision with player
                print("Game over!")
                return pygame.quit() # kill game if asteroid collides with player
        screen.fill((0, 0, 0))  # fill the screen with black color
        for sprite in drawable:  # iterate through all drawable objects
            sprite.draw(screen)  # draw each object on the screen
        pygame.display.flip()  # update the display

    pygame.quit() # clean up and close the game window

if __name__ == "__main__":
    main()