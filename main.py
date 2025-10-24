import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    #infinite loop for running
    while True:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #from constants
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        #all of these will be updated while the game runs

        screen.fill((0, 0, 0)) #black fill of screen #background color
        pygame.display.flip() #update screen



if __name__ == "__main__":
    main()
