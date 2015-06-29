from FGAme import Poly, World
from FGAme.draw import RenderTree


class Pointer(RenderTree):

    def __init__(self, button_center, mouse_pos):
        RenderTree.__init__(self)
        vertices = []
        x = button_center[0]
        y = button_center[1]
        vertices.append((x, y + 1))
        vertices.append((x + mouse_pos[0], y + mouse_pos[1]))
        vertices.append((x + mouse_pos[0], y + mouse_pos[1] - 2))
        vertices.append((x, y - 1))

        self.pointer = Poly(vertices, color='white')
        self.add(self.pointer)


if __name__ == '__main__':
    game = World()
    game.add(Pointer())
    game.run()
