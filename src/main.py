from FGAme import *
from FGAme import init_canvas
from mathtools import Vec2



RADIUS = 30 
coef_atrito = 10**5

STATE = ["ACTIVE","WAITING_FORCE","COMPUTING_FORCE", "APPLYING_FORCE"]
EVENT = ["CLICKED","MOVING","RELEASED" ]



class Button_Soccer(World):

    def __init__(self):
        World.__init__(self, background='blue')  
        self.test = Circle(RADIUS, color='red')
        self.test.pos = (400,300)
        self.add(self.test)
        self.current_state = "ACTIVE"
        self.current_event = None


    @listen('frame-enter')                                                       
    def force_bounds(self):
        print("POS_CIRCLE=")
        print(str(self.test.vel))
        if self.current_state is STATE[2]: 
            self.force = -2*self.force
            self.test.vel = self.force
            self.current_state = STATE[3]

        if self.current_state is STATE[3]:
            atrito = -coef_atrito * self.test.vel.normalize()
            self.test.apply_force(atrito,1./60)
            if self.test.vel.norm() < 0.5:
                self.test.vel = Vec2(0,0)
                self.current_state = STATE[0]




    def distance(self,a,b):
        return ( a - b ).norm()

    @listen('long-press','left')
    def left(self):
        self.test.move(-5,0)

    @listen('long-press','right')
    def right(self):
        self.test.move(5,0)

    @listen('long-press','up')
    def up(self):
        self.test.move(0,5)

    @listen('long-press','down')
    def down(self):
        self.test.move(0,-5)

    @listen('mouse-button-down','left')
    def mouse_click_down_left(self,pos):
        dist = self.distance(Vec2(pos),self.test.pos)

        if dist < RADIUS and self.current_state is STATE[0]:
            self.current_state = "WAITING_FORCE" 


    @listen('mouse-button-up','left')
    def mouse_click_up_left(self,pos):
        if self.current_state is STATE[1]:
            self.force = Vec2(pos) - self.test.pos
            self.current_state = STATE[2]
            


if __name__ == '__main__':
    game = Button_Soccer()
    game.run()
