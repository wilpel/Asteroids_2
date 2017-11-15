from polygon import Polygon
from shape import Shape
from point import Point

class Ship( Polygon ):
    def __init__(self, points=[], x=320, y=240, rotation=1):
        points = [Point(0, 0), Point(-10, 10), Point(15, 0), Point(-10, -10)]
        super().__init__(points,x,y,rotation)


