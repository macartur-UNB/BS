# -*- coding utf-8 -*-
from FGAme import listen, World, color
from button import Button
from ball import Ball
from mathtools import Vec2
from scene import Scene, SCREEN_MIDDLE
import status

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
        self.buttons_team_a = []
        self.buttons_team_b = []
        self.create_buttons()
        self.ball = Ball()
        self.add(self.ball)

    def create_buttons(self):
        self.buttons_team_a = self.create_team('blue', TEAM_A_POSITIONS)
        self.buttons_team_b = self.create_team('red', TEAM_B_POSITIONS)
        self.change_availability(self.buttons_team_b)

    def create_team(self, team_color, team_positions):
        buttons = []
        for position in team_positions:
            button = Button(team_color)
            button.pos = position
            buttons.append(button)
            self.add(button)
        return buttons

    def change_turn(self, team_a, team_b):
        self.change_availability(team_a)
        self.change_availability(team_b)

    def change_availability(self, team):
        for button in team:
            if button.current_status is status.AVAILABLE:
                button.current_status = status.UNAVAILABLE
                button.color = color.Color(100, 100, 100)
            elif button.current_status is status.UNAVAILABLE:
                button.current_status = status.AVAILABLE
                button.color = button.team_color

    @listen('frame-enter')
    def force_bounds(self):
        self.ball.update_forces()
        for button in self.buttons_team_a:
            button.update_forces()

        for button in self.buttons_team_b:
            button.update_forces()

    def distance(self, a, b):
        return (a - b).norm()

if __name__ == '__main__':
    game = ButtonSoccer()
    game.run()
