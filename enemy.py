import random
from globals import *
from intersect import *

class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xsize = PLAYER_SIZE
        self.ysize = PLAYER_SIZE
        self.color = random.choice([RED, GREEN, BLUE, PURPLE])

    def points(self):
        return [
            (self.x, self.y),
            (self.x + self.xsize, self.y),
            (self.x + self.xsize, self.y + self.ysize),
            (self.x, self.y + self.ysize)
        ]
    
    def segments(self):
        points = self.points()
        return [
            LineSegment(points[0][0], points[0][1], points[1][0], points[1][1]),
            LineSegment(points[1][0], points[1][1], points[2][0], points[2][1]),
            LineSegment(points[2][0], points[2][1], points[3][0], points[3][1]),
            LineSegment(points[3][0], points[3][1], points[0][0], points[0][1]),
        ]