from os import path

# Color constants
WHITE = (255,255,255)
BLACK = (0,0,0)
DARKGREY = (40,40,40)
LIGHTGREY = (100,100,100)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

# Game settings
WIDTH = 512 # 16*64 or 32*32 or 64*16
HEIGHT = 384 # 16*48 or 32*24 or 64*12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

TILESIZE = 16
GRIDWITH = WIDTH/TILESIZE
GRIDHEIGHT = HEIGHT/TILESIZE

# Directories
GAME_FOLDER = path.dirname(__file__)
MAP_FOLDER = path.join(GAME_FOLDER,"data","maps")

# Player settings
PLAYER_SPEED = 150