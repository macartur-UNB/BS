from FGAme import Circle
from scene import *


DASH_RADIUS = 3 * SCALE
position_left = [
    (TAM_PEQ_AREA_ESQUERDA_LINHA[0], TAM_PEQ_AREA_ESQUERDA_LINHA[2]),
    (TAM_PEQ_AREA_ESQUERDA_LINHA[0], TAM_PEQ_AREA_ESQUERDA_LINHA[3])
]

position_right = [
    (TAM_PEQ_AREA_DIREITA_LINHA[1], TAM_PEQ_AREA_DIREITA_LINHA[2]),
    (TAM_PEQ_AREA_DIREITA_LINHA[1], TAM_PEQ_AREA_DIREITA_LINHA[3])
]


SIDE_LEFT = "LEFT"
SIDE_RIGHT = "RIGHT"

ltx_min = TAM_PEQ_AREA_ESQUERDA_LINHA[0] - 10
ltx_max = TAM_PEQ_AREA_ESQUERDA_LINHA[0]
rtx_min = TAM_PEQ_AREA_DIREITA_LINHA[1]
rtx_max = TAM_PEQ_AREA_DIREITA_LINHA[1] + 10
y_min = TAM_PEQ_AREA_ESQUERDA_LINHA[2]
y_max = TAM_PEQ_AREA_ESQUERDA_LINHA[3]

class Goal:
    def __init__(self, side):
        self.__side = side

        if SIDE_LEFT == self.__side:
            self.superior_dash = Dash(position_left[1])
            self.inferior_dash = Dash(position_left[0])
            self.test = Test((ltx_min, ltx_max, y_min, y_max))
        else:
            self.superior_dash = Dash(position_right[1])
            self.inferior_dash = Dash(position_right[0])
            self.test = Test((rtx_min, rtx_max, y_min, y_max))


        
    def is_goal(self, pos):
        x_goal = False
        #print(self.__side)
        if self.__side is SIDE_LEFT:
            x_goal = (pos.x <= self.inferior_dash.pos.x)
            #print('x <=', pos.x, self.inferior_dash.pos.x)
        elif self.__side is SIDE_RIGHT:
            x_goal = (pos.x >= self.inferior_dash.pos.x)
            #print('x >=', pos.x, self.inferior_dash.pos.x)

        y_goal = (pos.y < self.superior_dash.pos.y) and \
                 (pos.y > self.inferior_dash.pos.y)
        #print('y',  self.inferior_dash.pos.y, '<', pos.y, '<', self.superior_dash.pos.y)
        #print('-----')
        return x_goal and y_goal

    def elements(self):
        return [self.superior_dash, self.inferior_dash]


class Test(Rectangle):
    def __init__(self, p):
        super(Rectangle, self).__init__(p, color='red')

class Dash(Circle):
    def __init__(self, pos=(0, 0)):
        super(Dash, self).__init__(DASH_RADIUS, color='white')
        self.mass = 'inf'
        self.move(pos)
