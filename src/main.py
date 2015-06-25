# -*- coding utf-8 -*-
from FGAme import listen, World
from button import Button
from mathtools import Vec2
from scene import Scene, SCREEN_WIDTH, SCREEN_HEIGHT
import random

TEAM_SIZE = 4


class ButtonSoccer(World):

    def __init__(self):
        World.__init__(self)
        self.add(Scene())
        self.force = Vec2(0, 0)
        self.add_bounds(width=10)
        self.button_list = []
        self.create_buttons()

    def create_buttons(self):
        self.create_team('blue', TEAM_SIZE)
        self.create_team('red', TEAM_SIZE)

    def create_team(self, color, team_size):
        for i in range(team_size):
            button = Button(color)
            button.pos = (random.randint(60, SCREEN_WIDTH - 60),
                          random.randint(60, SCREEN_HEIGHT - 60))
            self.button_list.append(button)
            self.add(button)

    @listen('frame-enter')
    def force_bounds(self):
        for button in self.button_list:
            button.update_forces()

    def distance(self, a, b):
        return (a - b).norm()

if __name__ == '__main__':
    game = ButtonSoccer()
    game.run()
