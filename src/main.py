# -*- coding utf-8 -*-
from FGAme import listen, World
from button import Button
from mathtools import Vec2
from scene import Scene, SCREEN_WIDTH, SCREEN_HEIGHT
import random

coef_friction = 15 ** 5

STATE = ["ACTIVE", "WAITING_FORCE", "COMPUTING_FORCE", "APPLYING_FORCE"]
EVENT = ["CLICKED", "MOVING", "RELEASED"]
MAX_FORCE = 170
TEAM_SIZE = 4


class ButtonSoccer(World):

    def __init__(self):
        World.__init__(self)
        self.add(Scene())
        self.force = Vec2(0, 0)
        self.current_state = "ACTIVE"
        self.current_event = None
        self.add_bounds(width=10)
        self.button_list = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(TEAM_SIZE):
            button = Button('blue')
            button.pos = (random.randint(20, SCREEN_WIDTH),
                          random.randint(20, SCREEN_HEIGHT))
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
