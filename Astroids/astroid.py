from polygon import Polygon
from shape import Shape
from point import Point

class Astroid( Polygon ):

    x = 0
    y = 0
    sizeMultiplier = 1

    def __init__(self, points=[], x=0, y=0, rotation=0, movement = Point(0,0), ang_vel = 0):
        points = [Point(-15*self.sizeMultiplier, 0), Point(-10*self.sizeMultiplier, 10*self.sizeMultiplier), Point(10*self.sizeMultiplier, 0), Point(-10*self.sizeMultiplier, -10*self.sizeMultiplier)]
        super().__init__(points,x,y,rotation)

        self.x = x
        self.y = y

        self.pull = movement
        self.angular_velocity=ang_vel