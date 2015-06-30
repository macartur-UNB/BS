# -*- coding utf-8 -*-
from FGAme import listen, World, color
from button import Button
from ball import Ball
from pointer import Pointer
from mathtools import Vec2
from scene import *
from goal import Goal
from random import randint
from state import *
from team import Team

MOVES = 3

TEAM_SIZE = 4
team_red_POSITIONS = ((SCREEN_MIDDLE[0] - 20 * SCALE, SCREEN_MIDDLE[1] + 40 * SCALE),
                    (SCREEN_MIDDLE[0] - 20 * SCALE, SCREEN_MIDDLE[1] - 40 * SCALE),
                    (SCREEN_MIDDLE[0] - 46 * SCALE, SCREEN_MIDDLE[1] + 14 * SCALE),
                    (SCREEN_MIDDLE[0] - 46 * SCALE, SCREEN_MIDDLE[1] - 14 * SCALE))

team_blue_POSITIONS = ((SCREEN_MIDDLE[0] + 20 * SCALE, SCREEN_MIDDLE[1] + 40 * SCALE),
                    (SCREEN_MIDDLE[0] + 20 * SCALE, SCREEN_MIDDLE[1] - 40 * SCALE),
                    (SCREEN_MIDDLE[0] + 46 * SCALE, SCREEN_MIDDLE[1] + 14 * SCALE),
                    (SCREEN_MIDDLE[0] + 46 * SCALE, SCREEN_MIDDLE[1] - 14 * SCALE))
CHECK_IDLE = 1
CHECK_ACTIVE = 2

class ButtonSoccer(World):

    def __init__(self):
        World.__init__(self)
        self.add(Scene())
        self.add_bounds(width=(W_DIFF, H_DIFF, W_DIFF, H_DIFF))
        
        
        self.force = Vec2(0, 0)

        self.create_teams()
        self.create_goal()
        self.moves = 0
        
        self.ball = Ball()
        self.add(self.ball)
        
        self.movement_check = CHECK_IDLE
    
    def create_teams(self):
        self.team_red = Team(self, 'Red Team', 'red', team_red_POSITIONS, True)
        self.team_blue = Team(self, 'Blue Team', 'blue', team_blue_POSITIONS, False)
        self.current_team = self.team_red
        self.teams = (self.team_red, self.team_blue)
        
        self.team_red.add_listener('released', self.movement_started)
        self.team_blue.add_listener('released', self.movement_started)

    def create_goal(self):
        self.goal_red = Goal("LEFT")
        self.goal_red.team_owner = self.team_red
        self.goal_red.team_enemy = self.team_blue
        self.goal_blue = Goal("RIGHT")
        self.goal_blue.team_owner = self.team_blue
        self.goal_blue.team_enemy = self.team_red
        
        self.goals = (self.goal_red, self.goal_blue)
        
        for goal in self.goals:
            for dash in goal.elements():
                self.add(dash)

    def check_turn(self):
        print('Turn -> ' + str(self.current_team))
        if self.moves + 1 >= MOVES:
            self.change_turn()
            self.current_team = self.team_red if self.team_red.turn else self.team_blue
            self.moves = 0
        else:
            self.moves += 1
    
    def change_turn(self):
        self.team_red.change_turn()
        self.team_blue.change_turn()

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
    
    def check_goal(self, goal):
        if goal.is_goal(self.ball.pos):
            goal.team_enemy.points += 1
            self.moves = 0
            self.ball.reset()
            
            if self.current_team != goal.team_owner:
                self.change_turn()
        
    @listen('frame-enter')
    def process(self):
        # bolinha
        self.ball.update_forces()
        
        # botões
        for team in self.teams:
            team.update_forces()

        # verificar se houve gol
        self.check_goal(self.goal_red)
        self.check_goal(self.goal_blue)
        
        if self.movement_check == CHECK_ACTIVE:
            if self.team_red.is_stopped() and self.team_blue.is_stopped():
                self.movement_check = CHECK_IDLE
                self.check_turn()


if __name__ == '__main__':
    game = ButtonSoccer()
    game.run()
