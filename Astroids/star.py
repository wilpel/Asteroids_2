from circle import Circle

class Star(Circle):
    def __init__(self, x=0, y=0, r=2, rotation=0):
        super().__init__(x,y,r,rotation)