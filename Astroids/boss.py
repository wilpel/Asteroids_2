from polygon import Polygon
from shape import Shape
from point import Point

class Boss( Polygon ):

    health = 10

    def __init__(self, points=[], x=320, y=0, rotation=90):
        points = [Point(0, 0), Point(-30, 30), Point(25, 0), Point(-30, -30)]
        super().__init__(points,x,y,rotation)


