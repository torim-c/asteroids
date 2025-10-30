# game constants


#screen display
SCREEN_WIDTH = 1280 
SCREEN_HEIGHT = 720


#Asteroid config
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS


#Player config
PLAYER_RADIUS = 20 # size of player ship
PLAYER_TURN_SPEED = 300 #turn speed of ship - adjust here and don't mess with dt!
PLAYER_SPEED = 200 #player forward speed
PLAYER_SHOOT_COOLDOWN = 0.5

#Shot Config
SHOT_RADIUS = 5
SHOT_SPEED = 500