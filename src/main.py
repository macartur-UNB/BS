from FGAme import *
from FGAme import init_canvas


class Button_Soccer(World):

    def __init__(self):
        World.__init__(self, background='blue')  
        self.test = Circle(50, color='red')
        self.test.pos = (400,300)
        self.add(self.test)

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

    @listen('mouse-motion')
    def mouse(self,pos):
        #print(str(pos))
        pass

    @listen('mouse-click')
    def mouse_click_l(self,button,pos):
        print("left")
        self.test.move(0,-5)

if __name__ == '__main__':
    game = Button_Soccer()
    game.run()
