from FGAme import *
from FGAme import init_canvas


WIDTH = 800
HEIGTH = 600

class Button_Soccer(World):                                                          
                                                                                 
    def __init__(self):                                         
        World.__init__(self, background='blue')  
        self.test = Circle(50, color='red')
        self.add(self.test)
    
    @listen("long-press","left")
    def space(self):
        x,y = self.test.pos
        self.test.move(x-0.5,y)

    @listen("long-press","right")
    def space(self):
        x,y = self.test.pos
        self.test.move(x+0.5,y)

    @listen("long-press","up")
    def space(self):
        x,y = self.test.pos
        self.test.move(x,y+0.5)
    @listen("long-press","down")
    def space(self):
        x,y = self.test.pos
        self.test.move(x,y-0.5)

if __name__ == '__main__':                                                       
    game = Button_Soccer()                                                           
    game.run() 
