import pygame as pg
# from os import path
from settings import *
from sprites import *
from tilemap import *

class Game:
	def __init__(self):
		pg.init()
		pg.display.set_caption(TITLE)
		self.screen = pg.display.set_mode((WIDTH,HEIGHT))
		self.clock = pg.time.Clock()
		self.loadData()

	def loadData(self):
		gameFolder = path.dirname(__file__)
		# self.map = Map(path.join(gameFolder,"data","maps","map.txt"))
		self.map = Map(path.join(MAP_FOLDER,"map.txt"))

	def newGame(self):
		self.allSprites = pg.sprite.Group()
		self.walls = pg.sprite.Group()

		for row,tiles in enumerate(self.map.data):
			for col,tile in enumerate(tiles):
				if tile == "1":
					Wall(self,col,row)
				if tile == "P":
					self.player = Player(self,col,row)
		self.camera = Camera(self.map.width,self.map.height)

	def run(self):
		self.playing = True
		while self.playing:
			self.dt = self.clock.tick(FPS)/1000
			self.events()
			self.update()
			self.draw()

	def quit(self):
		pg.quit()

	def update(self):
		self.allSprites.update()
		self.camera.update(self.player)

	def drawGrid(self):
		for x in range(0,WIDTH,TILESIZE):
			pg.draw.line(self.screen,LIGHTGREY,(x,0),(x,HEIGHT)) # vertical lines
		for y in range(0,HEIGHT,TILESIZE):
			pg.draw.line(self.screen,LIGHTGREY,(0,y),(WIDTH,y)) # horizontal lines

	def draw(self):
		self.screen.fill(BGCOLOR)
		self.drawGrid()
		for sprite in self.allSprites:
			self.screen.blit(sprite.image,self.camera.applyTo(sprite))
		pg.display.flip()

	def events(self):
		for ev in pg.event.get():
			if ev.type == pg.QUIT:
				self.quit()
			if ev.type == pg.KEYDOWN:
				if ev.key == pg.K_ESCAPE:
					self.quit()

	def showStartScreen(self):
		pass

	def showGameOverScreen(self):
		pass

if __name__ == '__main__':
	g = Game()
	g.showStartScreen()
	while True:
		g.newGame()
		g.run()
		g.showGameOverScreen()