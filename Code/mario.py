import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math
import numpy as np
from per import *
import time
# Clean the canvas
def Canvas_Empty():
	glClearColor(0.7,0.7,0.7,1.0) #backgraund color, silver
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glFlush()
# Clear part of the canvas
def Canvas_Box(x,y,r,g,b):
	for i in range(5):
		for j in range(5):
			Pixel(y+j-4,x-i,r,g,b,6)
			glFlush()
# Traslate a Pixel
def Traslate(point, tx, ty):
	T = [[1, 0, tx], 
		[0, 1, ty], 
		[0, 0, 1]]
	solve = np.dot(T,point)
	return solve
# Filled in Mario
def Filled_Mario(matrix,percent,i,x,y,r,g,b):
	m , n = percent,13
	r,g,b = 0,1,1
	# Drawing pixel by pixel
	for i in range(i,m):
		for j in range(n):
			if matrix[i][j] != 0:
				Pixel(y-j,x-i,r,g,b,8)
				glFlush()
	percent += 1
	return percent
#  Show number of attempts
def Attempt(number,x,y,r,g,b):
	N1 = [
		[0,0,1,0,0],
		[0,1,1,0,0],
		[0,0,1,0,0],
		[0,0,1,0,0],
		[0,1,1,1,0]]
	N2 = [
		[0,1,1,1,0],
		[0,0,0,1,0],
		[0,1,1,1,0],
		[0,1,0,0,0],
		[0,1,1,1,0]]
	N3 = [
		[0,1,1,1,0],
		[0,0,0,1,0],
		[0,1,1,1,0],
		[0,0,0,1,0],
		[0,1,1,1,0]]
	N4 = [
		[0,1,0,1,0],
		[0,1,0,1,0],
		[0,1,1,1,0],
		[0,0,0,1,0],
		[0,0,0,1,0]]
	N5 = [
		[0,1,1,1,0],
		[0,1,0,0,0],
		[0,1,1,1,0],
		[0,0,0,1,0],
		[0,1,1,1,0]]
	if number == 1: Pixel_Number(N1,x,y,r,g,b)
	elif number == 2: Pixel_Number(N2,x,y,r,g,b)
	elif number == 3: Pixel_Number(N3,x,y,r,g,b)
	elif number == 4: Pixel_Number(N4,x,y,r,g,b)
	elif number == 5: Pixel_Number(N5,x,y,r,g,b)
# Drawing the number
def Pixel_Number(Matrix,x,y,r,g,b):
	Canvas_Box(20,20,0.7,0.7,0.7)
	for i in range(5):
		for j in range(5):
			if Matrix[i][j] == 1:
				Pixel(y+j-4,x-i,r,g,b,6)
				glFlush()
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
		[1,1,1,1,0]]
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
		[0,0,1,0,0]]
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
				Pixel(y+j-4,x-i,r,g,b,6)
				glFlush()
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
	return Matrix
# Drawing a pixel by color at pygame's windows
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
	return word
# Genering the words for the game in the array
def Words():
	# split words by category and adding in a single array
	words = []
	fruits = ["pera", "manzana", "frutilla", "naranja", "ciruela","mango",
	"mandarina","coco","platano","sandia"]
	words.append(fruits)
	countries = ["alemania","australia","peru","argentina","chile",
	"china","japon","colombia","finlandia","hungria"]
	words.append(countries)
	colors = ["rojo", "azul", "ambar", "amarillo", "crema",
	"lacre","cobre","zafiro","oliva","menta"]
	words.append(colors)
	sports = ["futbol" , "voley" , "basquet" , "box" , "tenis",
	"golf" , "natacion" , "atletismo", "ciclismo", "surf" ]
	words.append(sports)
	clothes = ["blusa","chaqueta","falda","vestido","gorra",
	"short","pantalon","sombrero","zapatilla","traje"]
	words.append(clothes)
	#choose a random word
	idx = random.randint(0,4)
	rdm = random.randint(0,len(words[idx])-1)
	return words[idx][rdm]
# Show the Lose message
def Message(txt,r,g,b):
	Canvas_Empty()
	for i in range(len(txt)):
		Alphabet(txt[i].lower(),0,-16+6*i,r,g,b)
	glFlush()
# Check if character is in the word
def Again(x,y):
	Canvas_Empty()
	ans = Traslate([x,y,1],20,25)
	matrix = Mario(ans[1],ans[0],8)
	M_x, M_y = -20 , -20
	word = Spot(M_x, M_y,8)
	print(word)
	Attempts = 4
	r = random.random()
	g = random.random()
	b = random.random()					
	Attempt(Attempts,20,20,r,g,b)
	picture = "Mario"
	price = 0
	glFlush()
def Validate(edges,key,word,r,g,b,x,y,attempts,matrix,picture,price):
	key = key.lower()
	if price == len(word):
		Message("YOU WIN",r,g,b)
		return attempts,edges,price
	elif key in word:
		for i in range(len(word)):
			if word[i] == key:
				price += 1		
				Alphabet(key,x,y+6*i,r,g,b)
		return attempts,edges,price
	elif attempts > 1:
		Attempt(attempts-1,20,20,r,g,b)
		if picture == "Mario":
			#validate Mario
			edges = Filled_Mario(matrix,edges,edges-4,x+21,y+8,r,g,b)
			edges += 3
		else:
			#validate Amog
			None
		return attempts - 1,edges,price
	else:
		if picture == "Mario":
			edges = Filled_Mario(matrix,edges,edges-4,x+21,y+8,r,g,b)
		Message("YOU LOSE",r,g,b)
		time.sleep(0.10)
		Again(x,y)
		edges = 0
		price = 0
		attempts = 4
		return attempts,edges,price
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
	width, height = 640, 640
	pygame.init()
	pygame.display.set_caption('Hangman')
	display_openGL(width, height, scale)
	# our game start here
	# calling the first picture
	matrix = Mario(5,-12,scale)
	P1()
	#spot after drawing mario
	M_x, M_y = -20 , -20
	#draw spots for each character
	word = "" 
	#genering a random color for the words
	r = random.random()
	g = random.random()
	b = random.random()
	# Number of attempts
	Attempts = 4
	edges = math.ceil(16/4)
	glFlush()
	pygame.display.flip()
	#creating events to display
	while True:
		for event in pygame.event.get():# While we don't end the game
			if event.type == QUIT:
				return
			elif event.type == pygame.MOUSEBUTTONDOWN:# choose a character to start the game
				pos = pygame.mouse.get_pos()
				print(pos)
				if pos[0] > 61 and pos[0] < 198 and pos[1] < 426 and pos[1] > 261:
					# Choose a Mario
					ans = Traslate([0,0,1],-12,5)
					Canvas_Empty()
					matrix = Mario(ans[1],ans[0],scale)
					M_x, M_y = -20 , -20
					word = Spot(M_x, M_y,scale)
					print(word)					
					Attempt(Attempts,20,20,r,g,b)
					picture = "Mario"
					price = 0
				elif pos[0] > 404 and pos[0] < 535 and pos[1] > 430 and pos[1] < 264:
					# Choose a Amog
					None
			elif event.type == pygame.KEYDOWN:# define what happend when we press the keys
				if event.key == pygame.K_a:Attempts,edges,price  = Validate(edges,"A",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_b:Attempts,edges,price = Validate(edges,"B",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_c:Attempts,edges,price = Validate(edges,"C",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_d:Attempts,edges,price = Validate(edges,"D",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_e:Attempts,edges,price = Validate(edges,"E",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_f:Attempts,edges,price = Validate(edges,"F",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_g:Attempts,edges,price = Validate(edges,"G",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_h:Attempts,edges,price = Validate(edges,"H",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_i:Attempts,edges,price = Validate(edges,"I",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_j:Attempts,edges,price = Validate(edges,"J",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_k:Attempts,edges,price = Validate(edges,"K",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_l:Attempts,edges,price = Validate(edges,"L",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_m:Attempts,edges,price = Validate(edges,"M",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_n:Attempts,edges,price = Validate(edges,"N",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_o:Attempts,edges,price = Validate(edges,"O",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_p:Attempts,edges,price = Validate(edges,"P",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_q:Attempts,edges,price = Validate(edges,"Q",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_r:Attempts,edges,price = Validate(edges,"R",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_s:Attempts,edges,price = Validate(edges,"S",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_t:Attempts,edges,price = Validate(edges,"T",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_u:Attempts,edges,price = Validate(edges,"U",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_v:Attempts,edges,price = Validate(edges,"V",word,r,g,b,-16,-20,Attempts,matrix,picture,price) 
				elif event.key == pygame.K_w:Attempts,edges,price = Validate(edges,"W",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_x:Attempts,edges,price = Validate(edges,"Y",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_y:Attempts,edges,price = Validate(edges,"X",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				elif event.key == pygame.K_z:Attempts,edges,price = Validate(edges,"Z",word,r,g,b,-16,-20,Attempts,matrix,picture,price)
				else:print("Wrong key, try again")
# Calling main menu
if __name__ == '__main__':
	main()