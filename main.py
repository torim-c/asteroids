import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    pygame.init()
    clock = pygame.time.Clock()                 #FPS control
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #the two args affect player initial position

    #infinite loop for running
    while True:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #from constants
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        #all of these will be updated while the game runs      
        screen.fill((0, 0, 0))                  #black fill of screen #background color
        player.draw(screen)                     #draw player after screen fill otherwise you can't see him xD

        pygame.display.flip()                   #update screen
        dt = clock.tick(60)/1000                #retuns the amount of time that has passed since last time it was called - DELTA TIME
        


if __name__ == "__main__":
    main()
