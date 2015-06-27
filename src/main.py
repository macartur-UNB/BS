# -*- coding utf-8 -*-
from FGAme import listen, World, color
from button import Button
from ball import Ball
from mathtools import Vec2
from scene import Scene, SCREEN_MIDDLE
from goal import Goal 
import status
import state

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
        self.create_goal()
        self.register_listener()
        self.current_team = None

        self.ball = Ball()
        self.add(self.ball)

    def create_goal(self):
        self.goals = list()
        self.goals.append(Goal("RIGHT"))
        self.goals.append(Goal("LEFT")) 


        for gol in self.goals:
            self.add(gol.goal_area())
            for dash in gol.elements():
                self.add(dash)

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

    def change_turn(self):
        self.change_availability(self.buttons_team_a)
        self.change_availability(self.buttons_team_b)

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

    def get_current_team(self, button):
        if button in self.buttons_team_a:
            self.current_team = self.buttons_team_a
        else:
            self.current_team = self.buttons_team_b

    def end_turn(self):
        stopped = []
        for button in self.buttons_team_a + self.buttons_team_b:
            if button.current_state is state.MOVING:
                stopped.append(False)
            if button.current_state is state.STOPPED:
                stopped.append(True)

        if False not in stopped:
            self.change_turn()

    def register_listener(self):
        for button in self.buttons_team_a:
            button.listen('released', self.get_current_team, button)
            button.listen('stopped', self.end_turn)

        for button in self.buttons_team_b:
            button.listen('released', self.get_current_team, button)
            button.listen('stopped', self.end_turn)


if __name__ == '__main__':
    game = ButtonSoccer()
    game.run()
