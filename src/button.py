# -*- coding utf-8 -*-
from FGAme import Vec2, Circle, listen, Signal, EventDispatcher
# from main import coef_friction
from state import *
from scene import *

RADIUS = 6 * SCALE
MAX_FORCE = 170
coef_friction = 15 ** 5


class Button(Circle, EventDispatcher):
    released = Signal('released')
    stopped = Signal('stopped')

    def __init__(self, color, turn=False):
        super(Button, self).__init__(RADIUS, color=color)
        self.team_color = color
        self.current_state = STATE_AVAILABLE
        self.button_force = Vec2(0, 0)
        self.turn = turn
        print(turn)

    @listen('mouse-button-down', 'left')
    def left_click_down(self, pos):
        distance = self.__distance(Vec2(pos), self.pos)
        if distance < self.radius and self.current_state == STATE_AVAILABLE and self.turn:
            self.current_state = STATE_CLICKED

    @listen('mouse-button-up', 'left')
    def left_click_up(self, pos):
        if self.current_state & STATE_CLICKED:
            self.button_force = self.pos - Vec2(pos)
            self.button_force = 2 * self.button_force
            self.vel = self.button_force

            if self.button_force.norm() > MAX_FORCE:
                self.button_force = self.button_force.normalize() * MAX_FORCE
            self.current_state = STATE_MOVING
            self.trigger_released()

    def update_forces(self):
    
        #if self.current_state is state.MOVING:
        friction = - coef_friction * self.vel.normalize()
        self.apply_force(friction, 1.0 / 60)

        if self.vel.norm() < 2.5:
            self.vel = Vec2(0, 0)
            self.current_state &= STATE_STOPPED
            self.trigger_stopped()

    @listen('collision')
    def change_status(self, col):
        for button in col:
            button.current_state = STATE_MOVING
    
    def reset(self):
        self.pos = self.init_pos
        self.current_state = STATE_AVAILABLE
        self.vel = Vec2(0,0)

    def __distance(self, a, b):
        return (a - b).norm()
