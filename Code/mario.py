import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
# Desing the alphabet pixel by pixel
def Alphabet(txt,x,y,r,g,b):
	A = [
		[1,1,1,1,0],
		[1,0,0,1,0],
		[1,1,1,1,0],
		[1,0,0,1,0],
		[1,0,0,1,0]]
	B = [
		[1,1,1,1,0],
		[0,1,0,1,0],
		[0,1,1,1,0],
		[0,1,0,1,0],
		[1,1,1,1,0]]
	C = [
		[1,1,1,1,0],
		[1,0,0,0,0],
		[1,0,0,0,0],
		[1,0,0,0,0],
		[1,1,1,1,0]]
	D = [
		[1,1,1,1,0],
		[0,1,0,1,0],
		[0,1,0,1,0],
		[0,1,0,1,0],
		[1,1,1,1,0]]
	E = [
		[1,1,1,1,0],
		[1,0,0,0,0],
		[1,1,1,1,0],
		[1,0,0,0,0],
		[1,1,1,1,0]]
	F = [
		[1,1,1,1,0],
		[1,0,0,0,0],
		[1,1,1,1,0],
		[1,0,0,0,0],
		[1,0,0,0,0]]
	G = [
		[1,1,1,1,0],
		[1,0,0,0,0],
		[1,0,1,1,0],
		[1,0,0,1,0],
		[1,1,1,1,0]]
	H = [
		[1,0,0,1,0],
		[1,0,0,1,0],
		[1,1,1,1,0],
		[1,0,0,1,0],
		[1,0,0,1,0]]
	I = [
		[1,1,1,1,1],
		[0,0,1,0,0],
		[0,0,1,0,0],
		[0,0,1,0,0],
		[1,1,1,1,1]]
	J = [
		[0,1,1,1,0],
		[0,0,1,0,0],
		[0,0,1,0,0],
		[1,0,1,0,0],
		[1,1,1,0,0]]
	K = [
		[1,0,0,1,0],
		[1,0,1,0,0],
		[1,1,0,0,0],
		[1,0,1,0,0],
		[1,0,0,1,0]]
	L = [
		[1,0,0,0,0],
		[1,0,0,0,0],
		[1,0,0,0,0],
		[1,0,0,0,0],
		[1,1,1,0,0]]
	M = [
		[1,0,0,0,1],
		[1,1,0,1,1],
		[1,0,1,0,1],
		[1,0,0,0,1],
		[1,0,0,0,1]]
	N = [
		[1,0,0,0,1],
		[1,1,0,0,1],
		[1,0,1,0,1],
		[1,0,0,1,1],
		[1,0,0,0,1]]
	O = [
		[1,1,1,1,0],
		[1,0,0,1,0],
		[1,0,0,1,0],
		[1,0,0,1,0],
		[1,1,1,1,0]]
	P = [
		[1,1,1,1,0],
		[1,0,0,1,0],
		[1,1,1,1,0],
		[1,0,0,0,0],
		[1,0,0,0,0]]
	Q = [
		[0,1,1,0,0],
		[1,0,0,1,0],
		[1,0,0,1,0],
		[1,0,0,1,0],
		[0,1,1,1,1]]
	R = [
		[1,1,1,1,0],
		[1,0,0,1,0],
		[1,1,1,1,0],
		[1,0,1,0,0],
		[1,0,0,1,0]]
	S = [
		[1,1,1,1,0],
		[1,0,0,0,0],
		[1,1,1,1,0],
		[0,0,0,1,0],
		[1,1,1,1,0]]
	T = [
		[1,1,1,1,1],
		[0,0,1,0,0],
		[0,0,1,0,0],
		[0,0,1,0,0],
		[0,0,1,0,0]]
	U = [
		[1,0,0,1,0],
		[1,0,0,1,0],
		[1,0,0,1,0],
		[1,0,0,1,0],
		[1,1,1,1,0]]
	V = [
		[1,0,0,0,1],
		[1,0,0,0,1],
		[1,0,0,0,1],
		[0,1,0,1,0],
		[0,0,1,1,0]]
	W = [
		[1,0,0,0,1],
		[1,0,0,0,1],
		[1,0,1,0,1],
		[1,1,0,1,1],
		[1,0,0,0,1]]
	X = [
		[1,0,0,0,1],
		[0,1,0,1,0],
		[0,0,1,0,0],
		[0,1,0,1,0],
		[1,0,0,0,1]]
	Y = [
		[1,0,0,0,1],
		[0,1,0,1,0],
		[0,0,1,0,0],
		[0,0,1,0,0],
		[0,0,1,0,0]]
	Z = [
		[1,1,1,1,0],
		[0,0,0,1,0],
		[0,0,1,0,0],
		[0,1,0,0,0],
		[1,1,1,1,0]]
	if txt == 'a': Pixel_Word(A,x,y,r,g,b)
	if txt == 'b': Pixel_Word(B,x,y,r,g,b)
	if txt == 'c': Pixel_Word(C,x,y,r,g,b)
	if txt == 'd': Pixel_Word(D,x,y,r,g,b)
	if txt == 'e': Pixel_Word(E,x,y,r,g,b)
	if txt == 'f': Pixel_Word(F,x,y,r,g,b)
	if txt == 'g': Pixel_Word(G,x,y,r,g,b)
	if txt == 'h': Pixel_Word(H,x,y,r,g,b)
	if txt == 'i': Pixel_Word(I,x,y,r,g,b)
	if txt == 'j': Pixel_Word(J,x,y,r,g,b)
	if txt == 'k': Pixel_Word(K,x,y,r,g,b)
	if txt == 'l': Pixel_Word(L,x,y,r,g,b)
	if txt == 'm': Pixel_Word(M,x,y,r,g,b)
	if txt == 'n': Pixel_Word(N,x,y,r,g,b)
	if txt == 'o': Pixel_Word(O,x,y,r,g,b)
	if txt == 'p': Pixel_Word(P,x,y,r,g,b)
	if txt == 'q': Pixel_Word(Q,x,y,r,g,b)
	if txt == 'r': Pixel_Word(R,x,y,r,g,b)
	if txt == 's': Pixel_Word(S,x,y,r,g,b)
	if txt == 't': Pixel_Word(T,x,y,r,g,b)
	if txt == 'u': Pixel_Word(U,x,y,r,g,b)
	if txt == 'v': Pixel_Word(V,x,y,r,g,b)
	if txt == 'w': Pixel_Word(W,x,y,r,g,b)
	if txt == 'x': Pixel_Word(X,x,y,r,g,b)
	if txt == 'y': Pixel_Word(Y,x,y,r,g,b)
	if txt == 'z': Pixel_Word(Z,x,y,r,g,b)
#drawing a single word
def Pixel_Word(Matrix,x,y,r,g,b):
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
	countries = ["Alemania","Australia","Peru","Argentina","Chile",
	"China","Japon","Colombia","Finlandia","Madagascar"]
	colors = ["rojo", "azul", "ambar", "amarillo", "crema",
	"lacre","cobre","zafiro","oliva","menta"]
	sports = ["fútbol" , "voley" , "basquet" , "box" , "tenis",
	"golf" , "natación" , "atletismo", "ciclismo", "surf" ]
	clothes = ["blusa","chaqueta","falda","vestido","gorra",
	"short","pantalon","sombrero","zapatillas","traje"]
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
	picture = Mario(5,5,scale)
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