from FGAme import *
from FGAme import conf
from FGAme.draw import RenderTree


SCALE = 5
TAM_TABULEIRO = (0, 184 * SCALE, 0,  124 * SCALE)
SCREEN_WIDTH = TAM_TABULEIRO[1]
SCREEN_HEIGHT = TAM_TABULEIRO[3]
SCREEN_MIDDLE = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

conf.set_resolution(SCREEN_WIDTH, SCREEN_HEIGHT)

LINHA_ESPESSURA = 5
LARGURA_PISTA_LATERAL = 8 * SCALE
LARGURA_PISTA_FUNDO = 10 * SCALE

TAM_GRANDE_AREA_ESQUERDA_LINHA = (
	LARGURA_PISTA_FUNDO,
	LARGURA_PISTA_FUNDO + 30 * SCALE,
	(SCREEN_WIDTH / 3) - (30 * SCALE),
	(SCREEN_WIDTH / 3) + 30 * SCALE
)

TAM_GRANDE_AREA_ESQUERDA = (
	LARGURA_PISTA_FUNDO,
	LARGURA_PISTA_FUNDO + 30 * SCALE - LINHA_ESPESSURA,
	(SCREEN_WIDTH / 3) - (30 * SCALE) + LINHA_ESPESSURA,
	(SCREEN_WIDTH / 3) + 30 * SCALE - LINHA_ESPESSURA
)

TAM_GRANDE_AREA_DIREITA_LINHA = (
	SCREEN_WIDTH - LARGURA_PISTA_FUNDO - 30 * SCALE,
	SCREEN_WIDTH - LARGURA_PISTA_FUNDO,
	(SCREEN_WIDTH / 3) - (30 * SCALE),
	(SCREEN_WIDTH / 3) + 30 * SCALE
)

TAM_GRANDE_AREA_DIREITA = (
	SCREEN_WIDTH - LARGURA_PISTA_FUNDO - 30 * SCALE + LINHA_ESPESSURA,
	SCREEN_WIDTH - LARGURA_PISTA_FUNDO,
	(SCREEN_WIDTH / 3) - (30 * SCALE) + LINHA_ESPESSURA,
	(SCREEN_WIDTH / 3) + 30 * SCALE - LINHA_ESPESSURA
)

TAM_LINHA_EXTERNA = (
	LARGURA_PISTA_FUNDO - LINHA_ESPESSURA,
	SCREEN_WIDTH - LARGURA_PISTA_FUNDO + LINHA_ESPESSURA,
	LARGURA_PISTA_LATERAL - LINHA_ESPESSURA,
	SCREEN_HEIGHT - LARGURA_PISTA_FUNDO + LINHA_ESPESSURA
)

TAM_LINHA_INTERNA = (
	LARGURA_PISTA_FUNDO,
	SCREEN_WIDTH - LARGURA_PISTA_FUNDO,
	LARGURA_PISTA_LATERAL,
	SCREEN_HEIGHT - LARGURA_PISTA_FUNDO
)

TAM_PEQ_AREA_DIREITA = (30 * SCALE, 11 * SCALE)

TAM_PEQ_AREA_ESQUERDA_LINHA = (
	LARGURA_PISTA_FUNDO,
	LARGURA_PISTA_FUNDO + 11 * SCALE,
	(SCREEN_WIDTH / 3) - (15 * SCALE),
	(SCREEN_WIDTH / 3) + 15 * SCALE
)

TAM_PEQ_AREA_ESQUERDA = (
	LARGURA_PISTA_FUNDO,
	LARGURA_PISTA_FUNDO + 11 * SCALE - LINHA_ESPESSURA,
	(SCREEN_WIDTH / 3) - (15 * SCALE) + LINHA_ESPESSURA,
	(SCREEN_WIDTH / 3) + 15 * SCALE - LINHA_ESPESSURA
)

TAM_PEQ_AREA_DIREITA_LINHA = (
	SCREEN_WIDTH - LARGURA_PISTA_FUNDO - 11 * SCALE,
	SCREEN_WIDTH - LARGURA_PISTA_FUNDO,
	(SCREEN_WIDTH / 3) - (15 * SCALE),
	(SCREEN_WIDTH / 3) + 15 * SCALE
)

TAM_PEQ_AREA_DIREITA = (
	SCREEN_WIDTH - LARGURA_PISTA_FUNDO - 11 * SCALE + LINHA_ESPESSURA,
	SCREEN_WIDTH - LARGURA_PISTA_FUNDO,
	(SCREEN_WIDTH / 3) - (15 * SCALE) + LINHA_ESPESSURA,
	(SCREEN_WIDTH / 3) + 15 * SCALE - LINHA_ESPESSURA
)

diff = LINHA_ESPESSURA / 2.0
TAM_RETA_CENTRO = (
	SCREEN_WIDTH / 2 - diff,
	SCREEN_WIDTH / 2 + diff,
	LARGURA_PISTA_LATERAL - diff,
	SCREEN_HEIGHT - LARGURA_PISTA_LATERAL - LINHA_ESPESSURA
)

RAIO_BOLINHA = LINHA_ESPESSURA * 2
RAIO_CIRCULO_CENTRAL = 16 * SCALE
RAIO_CIRCULO_MEIA_LUA = 16 * SCALE
RAIO_ESCANTEIO = 3 * SCALE
DIST_PENALTI = 20.5 * SCALE + LARGURA_PISTA_FUNDO

class Scene(RenderTree):
	def __init__(self):
		RenderTree.__init__(self)
		self.linha_externa = Rectangle(TAM_LINHA_EXTERNA, color = 'white')
		self.linha_interna = Rectangle(TAM_LINHA_INTERNA, color = 'green')

		self.tabuleiro = Rectangle(TAM_TABULEIRO, color = 'green')

		self.garea_esquerda_linha = Rectangle(TAM_GRANDE_AREA_ESQUERDA_LINHA, color = 'white')
		self.garea_esquerda = Rectangle(TAM_GRANDE_AREA_ESQUERDA, color = 'green')

		self.garea_direita_linha = Rectangle(TAM_GRANDE_AREA_DIREITA_LINHA, color = 'white')
		self.garea_direita = Rectangle(TAM_GRANDE_AREA_DIREITA, color = 'green')

		self.peq_area_esquerda_linha = Rectangle(TAM_PEQ_AREA_ESQUERDA_LINHA, color = 'white')
		self.peq_area_esquerda = Rectangle(TAM_PEQ_AREA_ESQUERDA, color = 'green')

		self.peq_area_direita_linha = Rectangle(TAM_PEQ_AREA_DIREITA_LINHA, color = 'white')
		self.peq_area_direita = Rectangle(TAM_PEQ_AREA_DIREITA, color = 'green')

		self.circulo_central_grande_linha = Circle(RAIO_CIRCULO_CENTRAL, pos= (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), color = 'white')
		self.circulo_central_grande = Circle(RAIO_CIRCULO_CENTRAL - LINHA_ESPESSURA, pos= (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), color = 'green')

		self.circulo_central_peq = Circle(RAIO_BOLINHA, pos= (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), color = 'white')

		self.circulo_esquerda_linha = Circle(RAIO_CIRCULO_CENTRAL, pos= (TAM_GRANDE_AREA_ESQUERDA[1], SCREEN_HEIGHT/2), color = 'white')
		self.circulo_esquerda = Circle(RAIO_CIRCULO_CENTRAL - LINHA_ESPESSURA, pos= (TAM_GRANDE_AREA_ESQUERDA[1], SCREEN_HEIGHT/2), color = 'green')

		self.circulo_direita_linha = Circle(RAIO_CIRCULO_CENTRAL, pos= (TAM_GRANDE_AREA_DIREITA[0], SCREEN_HEIGHT/2), color = 'white')
		self.circulo_direita = Circle(RAIO_CIRCULO_CENTRAL - LINHA_ESPESSURA, pos= (TAM_GRANDE_AREA_DIREITA[0], SCREEN_HEIGHT/2), color = 'green')

		self.reta_centro = Rectangle(TAM_RETA_CENTRO, color='white')

		self.marca_penalti_esquerda = Circle(RAIO_BOLINHA, pos=(DIST_PENALTI , SCREEN_HEIGHT/2), color='white')
		self.marca_penalti_direita = Circle(RAIO_BOLINHA, pos=(SCREEN_WIDTH - DIST_PENALTI, SCREEN_HEIGHT/2), color='white')

		self.add(self.tabuleiro)
		self.add(self.linha_externa)
		self.add(self.linha_interna)

		self.add(self.circulo_esquerda_linha)
		self.add(self.circulo_esquerda)

		self.add(self.circulo_direita_linha)
		self.add(self.circulo_direita)

		self.add(self.garea_esquerda_linha)
		self.add(self.garea_esquerda)

		self.add(self.garea_direita_linha)
		self.add(self.garea_direita)

		self.add(self.peq_area_esquerda_linha)
		self.add(self.peq_area_esquerda)

		self.add(self.peq_area_direita_linha)
		self.add(self.peq_area_direita)

		self.add(self.circulo_central_grande_linha)
		self.add(self.circulo_central_grande)
		self.add(self.circulo_central_peq)

		self.add(self.marca_penalti_esquerda)
		self.add(self.marca_penalti_direita)

		self.add(self.reta_centro)

if __name__ == '__main__':
	game = World()
	game.add(Scene())
	game.run()
