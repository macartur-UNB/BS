# -*- coding utf-8 -*-
from FGAme import listen, World, color
from button import Button
from ball import Ball
from pointer import Pointer
from mathtools import Vec2
from scene import Scene, SCREEN_MIDDLE
from goal import Goal
from random import randint
from state import *
from team import Team

MOVES = 3

TEAM_SIZE = 4
TEAM_A_POSITIONS = ((SCREEN_MIDDLE[0] - 100, SCREEN_MIDDLE[1] + 200),
                    (SCREEN_MIDDLE[0] - 100, SCREEN_MIDDLE[1] - 200),
                    (SCREEN_MIDDLE[0] - 230, SCREEN_MIDDLE[1] + 70),
                    (SCREEN_MIDDLE[0] - 230, SCREEN_MIDDLE[1] - 70),)

TEAM_B_POSITIONS = ((SCREEN_MIDDLE[0] + 100, SCREEN_MIDDLE[1] + 200),
                    (SCREEN_MIDDLE[0] + 100, SCREEN_MIDDLE[1] - 200),
                    (SCREEN_MIDDLE[0] + 230, SCREEN_MIDDLE[1] + 70),
                    (SCREEN_MIDDLE[0] + 230, SCREEN_MIDDLE[1] - 70),)
CHECK_IDLE = 1
CHECK_ACTIVE = 2

class ButtonSoccer(World):

    def __init__(self):
        World.__init__(self)
        self.add(Scene())
        self.force = Vec2(0, 0)
        self.add_bounds(width=(20, 10, 20, 10))
        
        self.create_teams()
        self.moves = 0

        self.create_goal()

        self.ball = Ball()
        self.add(self.ball)
        
        self.movement_check = CHECK_IDLE
    
    def create_teams(self):
        self.team_a = Team(self, 'red', TEAM_A_POSITIONS, True)
        self.team_b = Team(self, 'blue', TEAM_B_POSITIONS, False)
        self.teams = (self.team_a, self.team_b)
        
        self.team_a.add_listener('released', self.movement_started)
        self.team_b.add_listener('released', self.movement_started)

    def create_goal(self):
        self.goals = list()
        self.goals.append(Goal("RIGHT"))
        self.goals.append(Goal("LEFT"))

        for gol in self.goals:
            for dash in gol.elements():
                self.add(dash)

    def check_turn(self):
        if self.moves >= MOVES:
            self.team_a.change_turn()
            self.team_b.change_turn()
            self.moves = 0
            print('Change turn.')
        else:
            self.moves += 1
            print('Move')

    @listen('mouse-long-press', 'left')
    def update_poiter(self, pos):
        self.clear_pointer()
        
        button = None
        for team in self.teams:
            if team.turn:
                button = team.get_clicked_button()
        
        if button != None:
            try:
                size = button.pos - Vec2(pos)
                p = Pointer(button.pos.as_tuple(), size.as_tuple())
                self.add(p)
            except ZeroDivisionError:
                pass
    
    def clear_pointer(self):
        for element in self.get_render_tree().walk():
            if isinstance(element, Pointer):
                self.remove(element)
                
    def movement_started(self):
        self.clear_pointer()
        self.movement_check = CHECK_ACTIVE
        
    @listen('frame-enter')
    def process(self):
        # bolinha
        self.ball.update_forces()
        
        # botões
        for team in self.teams:
            team.update_forces()

        # verificar se houve gol
        for goal in self.goals:
            if goal.is_goal(self.ball.pos):
                print("GOOOOOOOOOOOOOOOOL")
        
        if self.movement_check == CHECK_ACTIVE:
            if self.team_a.is_stopped() and self.team_b.is_stopped():
                self.movement_check = CHECK_IDLE
                self.check_turn()


if __name__ == '__main__':
    game = ButtonSoccer()
    game.run()
