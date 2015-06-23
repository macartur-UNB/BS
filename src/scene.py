from FGAme import *
from FGAme import conf
from FGAme.draw import RenderTree


SCALE = 6
TAM_TABULEIRO = (0, 184 * SCALE, 0,  124 * SCALE)

conf.set_resolution(TAM_TABULEIRO[1], TAM_TABULEIRO[3])

LARGURA_PISTA_LATERAL = 8 * SCALE
LARGURA_PISTA_FUNDO = 10 * SCALE

TAM_GRANDE_AREA_ESQUERDA = (
	LARGURA_PISTA_FUNDO,
	LARGURA_PISTA_FUNDO + 30 * SCALE,
	(TAM_TABULEIRO[1] / 3) - (30 * SCALE),
	(TAM_TABULEIRO[1] / 3) + 30 * SCALE
)

TAM_GRANDE_AREA_DIREITA = (
	TAM_TABULEIRO[1] - LARGURA_PISTA_FUNDO - 30 * SCALE,
	TAM_TABULEIRO[1] - LARGURA_PISTA_FUNDO,
	(TAM_TABULEIRO[1] / 3) - (30 * SCALE),
	(TAM_TABULEIRO[1] / 3) + 30 * SCALE
)

TAM_PEQ_AREA_DIREITA = (30 * SCALE, 11 * SCALE)

TAM_PEQ_AREA_ESQUERDA = (
	LARGURA_PISTA_FUNDO,
	LARGURA_PISTA_FUNDO + 11 * SCALE,
	(TAM_TABULEIRO[1] / 3) - (15 * SCALE),
	(TAM_TABULEIRO[1] / 3) + 15 * SCALE
)

TAM_PEQ_AREA_DIREITA = (
	TAM_TABULEIRO[1] - LARGURA_PISTA_FUNDO - 11 * SCALE,
	TAM_TABULEIRO[1] - LARGURA_PISTA_FUNDO,
	(TAM_TABULEIRO[1] / 3) - (15 * SCALE),
	(TAM_TABULEIRO[1] / 3) + 15 * SCALE
)

RAIO_CIRCULO_CENTRAL = 16 * SCALE
RAIO_CIRCULO_MEIA_LUA = 16 * SCALE
RAIO_ESCANTEIO = 3 * SCALE
DIST_PENALTU = 20.5 * SCALE


class Scene(RenderTree):
	def __init__(self):
		RenderTree.__init__(self)
		self.tabuleiro = Rectangle(TAM_TABULEIRO, color = 'green')
		
		self.garea_esquerda = Rectangle(TAM_GRANDE_AREA_ESQUERDA, color = 'red')
		self.garea_direita = Rectangle(TAM_GRANDE_AREA_DIREITA, color = 'red')
		
		self.peq_area_esquerda = Rectangle(TAM_PEQ_AREA_ESQUERDA, color = 'blue')
		self.peq_area_direita = Rectangle(TAM_PEQ_AREA_DIREITA, color = 'blue')
		
		self.circulo_central = Circle(RAIO_CIRCULO_CENTRAL, pos= (TAM_TABULEIRO[1]/2, TAM_TABULEIRO[3]/2), color = 'red')
		self.circulo_esquerda = Circle(RAIO_CIRCULO_CENTRAL, pos= (TAM_GRANDE_AREA_ESQUERDA[1], TAM_TABULEIRO[3]/2), color = 'white')
		self.circulo_direita = Circle(RAIO_CIRCULO_CENTRAL, pos= (TAM_GRANDE_AREA_DIREITA[0], TAM_TABULEIRO[3]/2), color = 'white')

		
		self.add(self.tabuleiro)
		self.add(self.circulo_esquerda)
		self.add(self.circulo_direita)
		self.add(self.garea_esquerda)
		self.add(self.garea_direita)
		self.add(self.peq_area_esquerda)
		self.add(self.peq_area_direita)
		self.add(self.circulo_central)

if __name__ == '__main__':
	game = World()
	game.add(Scene())
	game.run()
