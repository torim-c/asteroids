import sys
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from AsteroidField import AsteroidField
from shot import shot

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)            #always call this BEFORE instancing player. why? because then the Player() instance is not added to the groups! thus no draw or update!

    asteroid_field = AsteroidField()
 
    #player position
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #the two args affect player initial position



    #infinite loop for running
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        #all of these will be updated while the game runs
        updatable.update(dt)                    # player.update(dt) movement legacy BEFORE GROUPING


        #colision detection - iterate over all asteroids in the <asteroids> group. If player co
        for asteroid in asteroids:
            if player.collision_with(asteroid):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if bullet.collision_with(asteroid):
                    asteroid.split()
                    bullet.kill()
                    break #break loop after hit detected - return closes the entire thing lol


        screen.fill((0, 0, 0))                  #black fill of screen #background color

        for drawed in drawable:                 #draw player after screen fill otherwise you can't see him xD #player.draw(screen) legacy BEFORE GROUPING
            drawed.draw(screen)
        
                     

        pygame.display.flip()                   #update screen
        dt = clock.tick(60)/1000                #retuns the amount of time that has passed since last time it was called - DELTA TIME
        


if __name__ == "__main__":
    main()
