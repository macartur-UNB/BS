from FGAme import color
from button import Button
from state import *


INACTIVE_COLOR = color.Color(100, 100, 100)

class Team:
    def __init__(self, bs, team_name, team_color, team_position, turn = False):
        self.points = 0
        self.buttons = []
        self.team_color = team_color
        self.team_name = team_name
        self.team_position = team_position
        self.turn = not turn
        self._create_team()
        self.change_turn()
        
        for button in self.buttons:
            bs.add(button)
        
    def _create_team(self):
        self.buttons = []
        for position in self.team_position:
            button = Button(self.team_color, self.turn)
            button.pos = position
            self.buttons.append(button)

    def change_turn(self):
        self.turn = not self.turn
        for button in self.buttons:
            button.turn = self.turn
            if self.turn:
                button.color = self.team_color
            else:
                button.color = INACTIVE_COLOR
    
    def is_stopped(self):
        all_stopped = True
        for button in self.buttons:
            if button.current_state & STATE_MOVING:
               all_stopped = False
               break
        
        return all_stopped
    
    def get_clicked_button(self):
        for button in self.buttons:
            if button.current_state & STATE_CLICKED:
                return button
        
        return None
    
    def update_forces(self):
        for button in self.buttons:
            button.update_forces()
    
    def add_listener(self, signal, function):
        for button in self.buttons:
            button.listen(signal, function)
    
    def __str__(self):
        return self.team_name + ': ' + str(self.points)
    
    def __repr(self):
        return self.__str__()
