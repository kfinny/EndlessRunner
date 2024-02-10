import random
from globals import *

class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xsize = PLAYER_SIZE
        self.ysize = PLAYER_SIZE
        self.color = random.choice([RED, GREEN, BLUE, PURPLE])
