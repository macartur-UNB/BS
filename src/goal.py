from FGAme import Circle
from scene import *


DASH_RADIUS = 3 * SCALE
position1 = [
    (TAM_PEQ_AREA_ESQUERDA_LINHA[0], TAM_PEQ_AREA_ESQUERDA_LINHA[2]),
    (TAM_PEQ_AREA_ESQUERDA_LINHA[0], TAM_PEQ_AREA_ESQUERDA_LINHA[3])
]

position2 = [
    (TAM_PEQ_AREA_DIREITA_LINHA[1], TAM_PEQ_AREA_DIREITA_LINHA[2]),
    (TAM_PEQ_AREA_DIREITA_LINHA[1], TAM_PEQ_AREA_DIREITA_LINHA[3])
]


SIDE_LEFT = "LEFT"
SIDE_RIGHT = "RIGHT"


class Goal:
    def __init__(self, side):
        self.__side = side

        if SIDE_LEFT == self.__side:
            self.superior_dash = Dash(position1[0])
            self.inferior_dash = Dash(position1[1])
        else:
            self.superior_dash = Dash(position2[0])
            self.inferior_dash = Dash(position2[1])

    def is_goal(self, pos):
        x_goal = False
        if self.__side is SIDE_LEFT:
            x_goal = (pos.x <= self.inferior_dash.pos.x)
        elif self.__side is SIDE_RIGHT:
            x_goal = (pos.x >= self.inferior_dash.pos.x)

        y_goal = (pos.y < self.superior_dash.pos.y) and \
                 (pos.y > self.inferior_dash.pos.y)

        return x_goal and y_goal

    def elements(self):
        return [self.superior_dash, self.inferior_dash]


class Dash(Circle):
    def __init__(self, pos=(0, 0)):
        super(Dash, self).__init__(DASH_RADIUS, color='white')
        self.mass = 'inf'
        self.move(pos)
