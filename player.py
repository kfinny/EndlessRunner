import random
from globals import *
from enemy import Enemy
from intersect import *

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = PLAYER_SIZE
        self.color = WHITE

    def points(self):
        return [(self.x, self.y), (self.right_boundary(), self.y + self.size), (self.left_boundary(), self.y + self.size) ]
    
    def segments(self):
        points = self.points()
        return [
            LineSegment(points[0][0], points[0][1], points[1][0], points[1][1]),
            LineSegment(points[1][0], points[1][1], points[2][0], points[2][1]),
            LineSegment(points[2][0], points[2][1], points[0][0], points[0][1])
        ]

    def left_boundary(self):
        return self.x - (self.size / 2)

    def right_boundary(self):
        return self.x + (self.size / 2)
    
    def draw(self):
        pass

    def collision(self, enemy: Enemy) -> bool:
        for seg1 in self.segments():
            for seg2 in enemy.segments():
                if test_intersection(seg1, seg2):
                    print(seg1)
                    for s in enemy.segments():
                        print(f'\t{s}')
                    return True
        return False
