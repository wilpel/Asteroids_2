from circle import Circle
import pygame
class Bullet(Circle):
    x = 0
    y = 0
    sizeMultiplier = 1

    def __init__(self, x=0, y=0, r=2, rotation=0, timer = 0):
        super().__init__(x,y,r,rotation)
        self.accelerate(2)


        self.x = x
        self.y = y


