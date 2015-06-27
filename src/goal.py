from FGAme import Circle,Rectangle
from scene import SCREEN_WIDTH,SCREEN_HEIGHT


DASH_RADIUS = 15

position1 = [(50,230), (50,380)]
position2 = [(SCREEN_WIDTH - 50,380), (SCREEN_WIDTH - 50,230)]

area1 = (40,60,380,230) 
area2 = (SCREEN_WIDTH - 60, SCREEN_WIDTH -40,380,230) 


SIDE_LEFT = "LEFT"
SIDE_RIGHT = "RIGHT"


class Goal:
    def __init__(self,side):
        self.__elements = []
        self.__side = side

        if SIDE_LEFT in self.__side:
            for pos  in position1:
                self.__elements.append(Dash(pos))
        else:
            for pos in position2:
                self.__elements.append(Dash(pos))

    def goal_area(self):
        self.__goal_area = None
        if self.__side in SIDE_LEFT: 
            self.__goal_area = Rectangle(area1,color='red',mass='inf')
        else:
            self.__goal_area = Rectangle(area2,color='red',mass='inf')

        return self.__goal_area


    def elements(self):
        return self.__elements


class Dash(Circle):
    def __init__(self,pos=(0,0)):
        super(Dash,self).__init__(DASH_RADIUS,color='black')
        self.mass= 'inf'
        self.move(pos)
