import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
#Drawing mario by default
def Mario(x,y,size):
	#define colors
	#red = 1, blue = 2, black = 3, yellow = 4, brown = 5,coral = 6
	# blue = (0,0,1)
	# red = (1,0,0)
	# yellow = (1,1,0)
	# black = (0,0,0)
	# brown = (0.5,0,0)
	# coral = (1,127/255,80/255)
	#mario Matrix
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
	# Drawing pixel by pixel
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
# Pixel drawing by color
def Pixel(x,y,r,g,b,size): 
	glColor3f(r, g, b)
	glPointSize(size)

	glBegin(GL_POINTS)
	glVertex2f(x, y)
	glEnd()
#draw a single spot
def Draw_Spot(x,y,size):
	line = [1,1,1]
	for i in range(3):
		Pixel(y-i,x-1, 0,0,0,size)
	y += 5
	return y 
# Drawing the spot for each character
def Spot(x,y,size):
	word = Words()
	for i in word:
		y = Draw_Spot(x,y,size)
# Genering the words for the game in the array
def Words():
	fruits = ["pera", "manzana", "frutilla", "naranja", "ciruela","mango",
	"mandarina","coco","platano","sandia"]
	rdm = random.randint(0,len(fruits)-1)
	return fruits[rdm]

# start our world
def display_openGL(width, height, scale):
	pygame.display.set_mode((width, height), pygame.OPENGL)

	glClearColor(0.7,0.7,0.7,1.0) #backgraund color, silver
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

	gluOrtho2D(-30, 30, -30 ,30)
def main():
	scale = 8
	width, height = scale * 80, scale * 80
	pygame.init()
	pygame.display.set_caption('C.G. I')
	display_openGL(width, height, scale)
	# our game star here
	# calling the first picture
	picture = Mario(0,0,scale)
	#spot after drawing mario
	M_x, M_y = -20 , -10
	#draw spots
	Spot(M_x, M_y,scale)
	#drawing the spot for the words
	# creatin events to display

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