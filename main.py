import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #initial config
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #do not move under game loop else flicker happens
    clock = pygame.time.Clock()                 #FPS control
    dt = 0


    #groups
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)            #always call this BEFORE instancing player. why? because then the Player() instance is not added to the groups! thus no draw or update!


    #player position
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #the two args affect player initial position



    #infinite loop for running
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        #all of these will be updated while the game runs
        updatable.update(dt)                    # player.update(dt) movement legacy BEFORE GROUPING

        
        screen.fill((0, 0, 0))                  #black fill of screen #background color

        for drawed in drawable:                 #draw player after screen fill otherwise you can't see him xD #player.draw(screen) legacy BEFORE GROUPING
            drawed.draw(screen)
        
                     

        pygame.display.flip()                   #update screen
        dt = clock.tick(60)/1000                #retuns the amount of time that has passed since last time it was called - DELTA TIME
        


if __name__ == "__main__":
    main()
