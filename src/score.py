from FGAme import *
from scene import *

XCOORDS = (40, SCREEN_WIDTH - 40)

SRADIUS = 15

class Score(RenderTree):
    def __init__(self, side, color):
        RenderTree.__init__(self)
        self.y_height = SCREEN_HEIGHT - 100
        self.x_coord = XCOORDS[0] if side == 'left' else XCOORDS[1]
        self.color = color
        
        #self.add(Rectangle(pos(self.x_coord, SCREEN_HEIGHT - 50), color = self.color))
    
    def submit(self):
        self.y_height -= 40
        point = Circle(SRADIUS, pos = (self.x_coord, self.y_height), color = self.color)
        self.add(point)
    
    def reset(self):
        self.y_height = SCREEN_HEIGHT - 100
        for element in self.walk():
            self.remove(element)
