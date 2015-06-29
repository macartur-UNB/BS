from FGAme import Circle
from scene import SCREEN_WIDTH


DASH_RADIUS = 15

position1 = [(40, 380), (40, 230)]
position2 = [(SCREEN_WIDTH - 40, 380), (SCREEN_WIDTH - 40, 230)]

area1 = (40, 60, 380, 230)
area2 = (SCREEN_WIDTH - 60, SCREEN_WIDTH - 40, 380, 230)


SIDE_LEFT = "LEFT"
SIDE_RIGHT = "RIGHT"


class Goal:
    def __init__(self, side):
        self.__side = side

        if SIDE_LEFT in self.__side:
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
