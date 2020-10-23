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
	
	#CUADRILATERO - 4 vertices
	verticeslente = [(-50, 35), (-40, 40), (0, 40),(0,10),(-40,10),(-50,15)]
	verticescuerpo = [(-20,60), (20, 60), (20, 50),(30,50),(30,-40),(10,-40),(10,-30),(-10,-30),(-10,-40),(-30,-40),(-30,10),(0,10),(0,40),(-30,40),(-30,50),(-20,50)]
	verticesmochila = [(30,40), (50, 40), (50,-10), (30,-10)]
	#TRIANGULO - 3 vertices
	#vertices = [(-20, -10), (20, 20), (10, -20)]
	#POLIGONO - CHACANA
	#vertices = [(40, 20), (30, 20), (30, 30), (20, 30), (20, 40), (-20, 40), (-20, 30), (-30, 30), (-30, 20), (-40, 20),(-40, -20), (-30, -20), (-30, -30), (-20, -30), (-20, -40),(20, -40), (20, -30), (30, -30), (30, -20), (40, -20)]

	#punto (0,0) dentro de la figura --> pixel semilla
	xi = -30
	yi = 25
	xi1 = 0
	yi1 = 0
	xi2 = 40
	yi2 = 20
	DrawPolygon(verticescuerpo,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticeslente,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticesmochila,  255/255, 255/255, 255/255, 3)
	SimpleSeedFill(width, height, 1, verticescuerpo, xi1, yi1, 255/255, 0/255, 0/255)
	SimpleSeedFill(width, height, 1, verticesmochila,xi2, yi2, 255/255, 0/255, 0/255)
	SimpleSeedFill(width, height, 1, verticeslente, xi, yi, 204/255, 229/255, 255/255)

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