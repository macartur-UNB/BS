# -*- coding utf-8 -*-
from FGAme import listen, World
from button import Button
from ball import Ball
from mathtools import Vec2
from scene import Scene, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_MIDDLE
import random

TEAM_SIZE = 4
TEAM_A_POSITIONS = ((SCREEN_MIDDLE[0] - 100, SCREEN_MIDDLE[1] + 200),
                    (SCREEN_MIDDLE[0] - 100, SCREEN_MIDDLE[1] - 200),
                    (SCREEN_MIDDLE[0] - 230, SCREEN_MIDDLE[1] + 70),
                    (SCREEN_MIDDLE[0] - 230, SCREEN_MIDDLE[1] - 70),)

TEAM_B_POSITIONS = ((SCREEN_MIDDLE[0] + 100, SCREEN_MIDDLE[1] + 200),
                    (SCREEN_MIDDLE[0] + 100, SCREEN_MIDDLE[1] - 200),
                    (SCREEN_MIDDLE[0] + 230, SCREEN_MIDDLE[1] + 70),
                    (SCREEN_MIDDLE[0] + 230, SCREEN_MIDDLE[1] - 70),)


class ButtonSoccer(World):

    def __init__(self):
        World.__init__(self)
        self.add(Scene())
        self.force = Vec2(0, 0)
        self.add_bounds(width=10)
        self.button_list = []
        self.create_buttons()
        self.ball = Ball()
        self.add(self.ball)

    def create_buttons(self):
        self.create_team('blue', TEAM_A_POSITIONS)
        self.create_team('red', TEAM_B_POSITIONS)

    def create_team(self, color, team_positions):
        for position in team_positions:
            button = Button(color)
            button.pos = position
            self.button_list.append(button)
            self.add(button)

    @listen('frame-enter')
    def force_bounds(self):
        self.ball.update_forces()
        for button in self.button_list:
            button.update_forces()

    def distance(self, a, b):
        return (a - b).norm()

if __name__ == '__main__':
    game = ButtonSoccer()
    game.run()
