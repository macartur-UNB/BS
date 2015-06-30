# -*- coding utf-8 -*-
from FGAme import Vec2, Circle, listen
from scene import SCREEN_MIDDLE, SCALE
import state

MAX_VEL = 300
RADIUS = 2 * SCALE
coef_friction = 11 ** 5

class Ball(Circle):

    def __init__(self):
        super(Ball, self).__init__(RADIUS, color='black')
        self.current_state = state.STATE_AVAILABLE
        self.pos = SCREEN_MIDDLE
        self.ball_force = Vec2(0, 0)

    def reset(self):
        self.vel = Vec2(0,0)
        self.pos = SCREEN_MIDDLE

    def update_forces(self):
 #       if self.current_state & STATE_STOPPED:
        friction = - coef_friction * self.vel.normalize()
        self.apply_force(friction, 1.0 / 60)

        if self.vel.norm() > MAX_VEL:
            self.vel = self.vel.normalize() * MAX_VEL

        if self.vel.norm() < 2.5:
            self.vel = Vec2(0, 0)
#                self.current_state = state.STOPPED

#    @listen('collision')
    def change_status(self, col):
        for button in col:
            button.current_state = state.STOPPED
