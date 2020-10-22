import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
# Desing the alphabet pixel by pixel
def Alphabet(txt,x,y,r,g,b):
	#creating the matrix of all words
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
	# drawing the word that was choose
	if txt == 'a': Pixel_Word(A,x,y,r,g,b)
	elif txt == 'b': Pixel_Word(B,x,y,r,g,b)
	elif txt == 'c': Pixel_Word(C,x,y,r,g,b)
	elif txt == 'd': Pixel_Word(D,x,y,r,g,b)
	elif txt == 'e': Pixel_Word(E,x,y,r,g,b)
	elif txt == 'f': Pixel_Word(F,x,y,r,g,b)
	elif txt == 'g': Pixel_Word(G,x,y,r,g,b)
	elif txt == 'h': Pixel_Word(H,x,y,r,g,b)
	elif txt == 'i': Pixel_Word(I,x,y,r,g,b)
	elif txt == 'j': Pixel_Word(J,x,y,r,g,b)
	elif txt == 'k': Pixel_Word(K,x,y,r,g,b)
	elif txt == 'l': Pixel_Word(L,x,y,r,g,b)
	elif txt == 'm': Pixel_Word(M,x,y,r,g,b)
	elif txt == 'n': Pixel_Word(N,x,y,r,g,b)
	elif txt == 'o': Pixel_Word(O,x,y,r,g,b)
	elif txt == 'p': Pixel_Word(P,x,y,r,g,b)
	elif txt == 'q': Pixel_Word(Q,x,y,r,g,b)
	elif txt == 'r': Pixel_Word(R,x,y,r,g,b)
	elif txt == 's': Pixel_Word(S,x,y,r,g,b)
	elif txt == 't': Pixel_Word(T,x,y,r,g,b)
	elif txt == 'u': Pixel_Word(U,x,y,r,g,b)
	elif txt == 'v': Pixel_Word(V,x,y,r,g,b)
	elif txt == 'w': Pixel_Word(W,x,y,r,g,b)
	elif txt == 'x': Pixel_Word(X,x,y,r,g,b)
	elif txt == 'y': Pixel_Word(Y,x,y,r,g,b)
	elif txt == 'z': Pixel_Word(Z,x,y,r,g,b)
# Drawing a single word
def Pixel_Word(Matrix,x,y,r,g,b):
	# draw the word by the color
	for i in range(5):
		for j in range(5):
			if Matrix[i][j] == 1:
				Pixel(y-j,x-i,r,g,b,4)
# Drawing mario by default
def Mario(x,y,size):
	#define colors
	#red = 1, blue = 2, black = 3, yellow = 4, brown = 5,coral = 6
	# blue = (0,0,1)
	# red = (1,0,0)
	# yellow = (1,1,0)
	# black = (0,0,0)
	# brown = (0.5,0,0)
	# coral = (1,127/255,80/255)
	# Mario's Matrix
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
	# Draw a pixel in the pygame's windows
	glColor3f(r, g, b)
	glPointSize(size)
	glBegin(GL_POINTS)
	glVertex2f(x, y)
	glEnd()
# Draw a single spot
def Draw_Spot(x,y,size):
	# array of number of lines
	line = [1,1,1,1,1]
	#drawing a spot in pygame's windows
	for i in range(5):
		Pixel(y-i,x-1, 0,0,0,size)
	y += 6
	return y 
# Drawing the spot for each character
def Spot(x,y,size):
	# Calling a word to draw a spot for each character
	word = Words()
	# drawing the spots
	for i in word:
		y = Draw_Spot(x,y,size)
# Genering the words for the game in the array
def Words():
	# split words by category and adding in a single array
	words = []
	fruits = ["pera", "manzana", "frutilla", "naranja", "ciruela","mango",
	"mandarina","coco","platano","sandia"]
	words.append(fruits)
	countries = ["Alemania","Australia","Peru","Argentina","Chile",
	"China","Japon","Colombia","Finlandia","Madagascar"]
	words.append(countries)
	colors = ["rojo", "azul", "ambar", "amarillo", "crema",
	"lacre","cobre","zafiro","oliva","menta"]
	words.append(colors)
	sports = ["fútbol" , "voley" , "basquet" , "box" , "tenis",
	"golf" , "natación" , "atletismo", "ciclismo", "surf" ]
	words.append(sports)
	clothes = ["blusa","chaqueta","falda","vestido","gorra",
	"short","pantalon","sombrero","zapatillas","traje"]
	words.append(clothes)
	#choose a random word
	idx = random.randint(0,4)
	rdm = random.randint(0,len(words[idx])-1)
	return words[idx][rdm]

# Start our world
def display_openGL(width, height, scale):
	#display the game's windows
	pygame.display.set_mode((width, height), pygame.OPENGL)
	glClearColor(0.7,0.7,0.7,1.0) #backgraund color, silver
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	#camara that we use
	gluOrtho2D(-30, 30, -30 ,30)
# Main, define the start point
def main():
	# inicial conditions
	scale = 8
	width, height = scale * 80, scale * 80
	pygame.init()
	pygame.display.set_caption('C.G. I')
	display_openGL(width, height, scale)
	# our game star here
	# calling the first picture
	picture = Mario(5,5,scale)
	#spot after drawing mario
	M_x, M_y = -20 , -20
	#draw spots
	Spot(M_x, M_y,scale)
	#drawing the spot for the words
	#genering a random color for the words
	r = random.random()
	g = random.random()
	b = random.random()
	#
	Alphabet("m",-16,-20,r,g,b)
	
	glFlush()
	pygame.display.flip()
	#creating events to display
	while True:
		for event in pygame.event.get():# While we don't end the game
			if event.type == QUIT:
				return
			elif event.type == pygame.MOUSEBUTTONDOWN:# choose a character to start the game
				print(event)
			elif event.type == pygame.KEYDOWN:# define what happend when we press the keys
				if event.key == pygame.K_a:print("A")
				elif event.key == pygame.K_b:print("B")
				elif event.key == pygame.K_c:print("C")
				elif event.key == pygame.K_d:print("D")
				elif event.key == pygame.K_e:print("E")
				elif event.key == pygame.K_f:print("F")
				elif event.key == pygame.K_g:print("G")
				elif event.key == pygame.K_h:print("H")
				elif event.key == pygame.K_i:print("I")
				elif event.key == pygame.K_j:print("J")
				elif event.key == pygame.K_k:print("K")
				elif event.key == pygame.K_l:print("L")
				elif event.key == pygame.K_m:print("C")
				elif event.key == pygame.K_n:print("C")
				elif event.key == pygame.K_o:print("C")
				elif event.key == pygame.K_p:print("C")
				elif event.key == pygame.K_q:print("C")
				elif event.key == pygame.K_r:print("C")
				elif event.key == pygame.K_s:print("C")
				elif event.key == pygame.K_t:print("C")
				elif event.key == pygame.K_u:print("C")
				elif event.key == pygame.K_v:print("C")
				elif event.key == pygame.K_w:print("C")
				elif event.key == pygame.K_x:print("C")
				elif event.key == pygame.K_y:print("C")
				elif event.key == pygame.K_z:print("C")
				else:print("Wrong key, try again")
# Calling main menu
if __name__ == '__main__':
	main()