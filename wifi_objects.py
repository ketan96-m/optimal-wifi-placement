
class Router:
    def __init__(self,pos):
        self.pos = pos

class AccessPoints:
    def __init__(self, pos):
        self.pos = pos

class Rooms:
    def __init__(self, pos, width, height):
        self.pos = pos
        self.width = width
        self.height = height
    def GetCorner(self):
        self.top_left = self.pos[0], self.pos[1]
        self.top_right = (self.pos[0]+self.width,self.pos[1])
        self.bottom_left = (self.pos[0], self.pos[1]+self.height)
        self.bottom_right = (self.pos[0]+self.width, self.pos[1] + self.height)
