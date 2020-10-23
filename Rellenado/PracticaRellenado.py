# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# Python 3.8
from utils import *

def main():
	scale = 3
	width, height = scale * 200, scale * 200

	pygame.init()
	pygame.display.set_caption('AHOGADO')
	
	display_openGL(width, height, scale)
	# glColor3f(1.0, 0, 0)
	x = 0
	y = 0
	set_pixel(x, y, 1, 1, 1, scale)

	



	#HEPTAGONO - 7 vertices
	#vertices = [(-20, -28), (-70, 0), (-35, 25), (0, 30), (40, 15), (50, -15), (20, -30)]
	
	#HEXAGONO - 6 vertices
	#vertices = [(-15, -33), (-45, 0), (-30, 30), (20, 30), (40, 0), (25, -30)]
	
	#PENTAGONO - 5 vertices
	#vertices = [(-30, -10), (-20, 20), (20, 15), (30, -20), (0, -30)]
	
	#CUADRILATERO - 4 vertices
	verticesoreja1 = [(-15, 50), (-20, 70), (-30, 65)]
	verticesoreja2 = [(15, 50), (20, 70), (30, 65)]
	verticescabeza = [(10, 20), (-10, 20), (-20, 30), (-10, 60), (10, 60), (20, 30)]
	verticesojo1 = [(10, 45), (5, 45), (5, 40), (10, 40)]
	verticesojo2 = [(-10, 45), (-5, 45), (-5, 40), (-10, 40)]
	verticesbarba =  [(-6, 30), (6, 30), (6, 33), (-6, 33)]
	verticesboca =  [(-10, 30), (10, 30), (5, 25), (-5, 25)]
	verticescuerpo = [(15, -40), (-15, -40),  (-30, -10), (-30, 10), (-15, 20), (15, 20), (30, 10), (30, -10)]
	verticesbolsillo =  [(-10, 0), (10, 0), (5, -10), (-5, -10)]
	verticesbrazo1 = [(-30, -10), (-30, 10), (-50, -10), (-50, -20)]
	verticesbrazo2 = [(30, -10), (30, 10), (50, -10), (50, -20)]
	verticespierna1 = [(15, -40), (5, -40), (5, -80), (20, -90), (15, -80)]
	verticespierna2 = [(-15, -40), (-5, -40), (-5, -80), (-20, -90), (-15, -80)]	
	
	#TRIANGULO - 3 vertices
	#vertices = [(-20, -10), (20, 20), (10, -20)]

	#POLIGONO - CHACANA
	#vertices = [(40, 20), (30, 20), (30, 30), (20, 30), (20, 40), (-20, 40), (-20, 30), (-30, 30), (-30, 20), (-40, 20),(-40, -20), (-30, -20), (-30, -30), (-20, -30), (-20, -40),(20, -40), (20, -30), (30, -30), (30, -20), (40, -20)]

	#punto (0,0) dentro de la figura --> pixel semilla
	xi = 0
	yi = -20
	xi1 = 0
	yi1 = -5

	xi2 = 10
	yi2 = -50
	xi3 = -10
	yi3 = -50

	xi4 = -40
	yi4 = 0
	xi5 = 40
	yi5 = 0
	
	DrawPolygon(verticescuerpo,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticescabeza,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticesbrazo1,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticesbrazo2,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticespierna1,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticespierna2,  255/255, 255/255, 255/255, 3)	
	DrawPolygon(verticesojo1, 255/255, 255/255, 255/255, 1)
	DrawPolygon(verticesojo2, 255/255, 255/255, 255/255, 1)
	DrawPolygon(verticesboca, 255/255, 255/255, 255/255, 1)
	DrawPolygon(verticesoreja1, 255/255, 255/255, 255/255, 3)
	DrawPolygon(verticesoreja2, 255/255, 255/255, 255/255, 3)
	DrawPolygon(verticesbolsillo, 255/255, 255/255, 255/255, 3)
	DrawPolygon(verticesbarba, 255/255, 255/255, 255/255, 1)

	SimpleSeedFillSimul(width, height, 1, verticespierna1, verticespierna2, xi2, yi2, xi3, yi3, 255/255, 255/255, 0/255)
	SimpleSeedFill(width, height, 1, verticescuerpo, xi, yi, 255/255, 255/255, 0/255)
	SimpleSeedFill(width, height, 1, verticesbolsillo, xi1, yi1, 255/255, 0/255, 0/255)
	SimpleSeedFillSimul(width, height, 1, verticesbrazo1, verticesbrazo2, xi4, yi4, xi5, yi5, 255/255, 255/255, 0/255)
	#SimpleSeedFill(width, height, 1, vertices, xi, yi, 0/255, 255/255, 255/255)
	#SimpleSeedFill(width, height, 1, vertices, xi, yi, 255/255, 255/255, 0/255)
	#SimpleSeedFill(width, height, 1, vertices1, xi1, yi1, 255/255, 255/255, 0/255)
	# rgb = glReadPixels(width/2 +x-1, height/2+y-1, scale, scale, GL_RGB, GL_UNSIGNED_BYTE, None)
	# print(list(rgb))

	# Fill Triangle
	#vertices = [(1, 1), (40, 40), (80, 1)]
	#FillTriangle(vertices, 255/255, 0/255, 0/255, scale)
	#DrawPolygon(vertices, 255/255, 0/255, 0/255, scale)
	print("Finish...")
	glFlush()
	pygame.display.flip()
	 
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

if __name__ == '__main__':
	main()