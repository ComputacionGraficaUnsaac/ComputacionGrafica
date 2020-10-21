import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
def Mario(x,y,size):
	#define colors
	#red = 1, blue = 2, black = 3, yellow = 4, brown = 5,coral = 6
	# blue = (0,0,1)
	# red = (1,0,0)
	# yellow = (1,1,0)
	# black = (0,0,0)
	# brown = (0.5,0,0)
	# coral = (1,127/255,80/255)

	Matrix = [
			[0,0,0,1,1,1,1,1,1,0,0,0,0],
			[0,0,1,1,1,1,1,1,1,1,1,1,0],
			[0,0,5,5,5,6,6,6,3,6,0,0,0],
			[0,5,6,5,6,6,6,6,3,6,6,6,0],
			[0,5,6,5,5,6,6,6,6,3,6,6,6],
			[0,5,5,6,6,6,6,6,3,3,3,3,0],
			[0,0,0,6,6,6,6,6,6,6,6,0,0],
			[0,0,1,1,2,1,1,1,1,0,0,0,0],
			[0,1,1,1,2,1,1,2,1,1,1,0,0],
			[1,1,1,1,2,2,2,2,1,1,1,1,0],
			[6,6,1,2,4,2,2,4,2,1,6,6,0],
			[6,6,6,2,2,2,2,2,2,6,6,6,0],
			[6,6,2,2,2,2,2,2,2,2,6,6,0],
			[0,0,2,2,2,0,0,2,2,2,0,0,0],
			[0,5,5,5,0,0,0,0,5,5,5,0,0],
			[5,5,5,5,0,0,0,0,5,5,5,5,0]]
	m , n = 16,13
	for i in range(m):
		for j in range(n):
			if Matrix[i][j] == 1:
				Pixel(y-j,x-i,1,0,0,size)
			elif Matrix[i][j] == 2:
				Pixel(y-j,x-i,0,0,1,size)
			elif Matrix[i][j] == 3:
				Pixel(y-j,x-i,0,0,0,size)
			elif Matrix[i][j] == 4:
				Pixel(y-j,x-i,1,1,0,size)
			elif Matrix[i][j] == 5:
				Pixel(y-j,x-i,0.5,0,0,size)
			elif Matrix[i][j] == 6:
				Pixel(y-j,x-i,1,127/255,80/255,size) 
def Pixel(x,y,r,g,b,size): 
	glColor3f(r, g, b)
	glPointSize(size)

	glBegin(GL_POINTS)
	glVertex2f(x, y)
	glEnd()

def display_openGL(width, height, scale):
	pygame.display.set_mode((width, height), pygame.OPENGL)

	glClearColor(0.7,0.7,0.7,1.0)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	# glScalef(scale, scale, 0)

	gluOrtho2D(-30, 30, -30 ,30)
def main():
	scale = 8
	width, height = scale * 80, scale * 80

	pygame.init()
	pygame.display.set_caption('C.G. I')
	
	display_openGL(width, height, scale)

	picture = Mario(0,0,scale) 

	glFlush()
	pygame.display.flip()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			elif event.type == pygame.MOUSEBUTTONDOWN:
				print(event)
if __name__ == '__main__':
	main()