# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# pip install numpy
# Python 3.8

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

import math
import random as rdn
import numpy as np

### Algorithm ###

def set_pixel(x, y, r, g, b, size):
	glColor3f(r, g, b)
	glPointSize(size)

	glBegin(GL_POINTS)
	glVertex2f(x, y)
	glEnd()


def color_pixel(width, height, x, y, size):
	rgb = glReadPixels(width / 2 + x , height / 2 + y, size ,size , 
						GL_RGB, GL_UNSIGNED_BYTE, None)
	return list(rgb)
	

def DDA(x0, y0, x1, y1, r, g, b, size):
	points = []
	dx = x1 - x0
	dy = y1 - y0
	x = x0
	y = y0
	if abs(dx) > abs(dy):
		steps = abs(dx)
	else:
		steps = abs(dy)
	xi = dx / steps
	yi = dy / steps
	set_pixel(round(x), round(y), r, g, b, size)
	points.append((round(x), round(y)))
	for k in range(int(steps)):
		x += xi
		y += yi
		set_pixel(round(x), round(y), r, g, b, size)
		points.append((round(x), round(y)))
	return points

def DrawPolygon(vertices, r, g, b, size):
	# vertices = [(x1, x2), (x2, y2), ..., (xn, yn)]
	vertices.append(vertices[0])
	for k in range(len(vertices) - 1):
		x0, y0 = vertices[k]
		x1, y1 = vertices[k + 1]
		DDA(x0, y0, x1, y1, r, g, b, size)

def DrawPolygon_(vertices, r, g, b, size):
	# vertices = [(x1, x2), (x2, y2), ..., (xn, yn)]
	vertices.append(vertices[0])
	for k in range(len(vertices) - 1):
		# print(vertices[k])
		x0, y0 = vertices[k][:2]
		x1, y1 = vertices[k + 1][:2]
		DDA(x0, y0, x1, y1, r, g, b, size)
	vertices.pop()		

def punto_en_poligono(x, y, vertices_poligono):
    #Comprueba si un punto se encuentra dentro de un polígono teniendo los vertices del
    i = 0
    j = len(vertices_poligono) - 1
    salida = False
    for i in range(len(vertices_poligono)):
        if (vertices_poligono[i][1] < y and vertices_poligono[j][1] >= y) or (vertices_poligono[j][1] < y and vertices_poligono[i][1] >= y):
            if vertices_poligono[i][0] + (y - vertices_poligono[i][1]) / (vertices_poligono[j][1] - vertices_poligono[i][1]) * (vertices_poligono[j][0] - vertices_poligono[i][0]) < x:
                salida = not salida
        j = i
    return salida

def SimpleSeedFill(width, height, size, vertices, xi, yi, r, g, b):
	r, g, b = 255 * r, 255 * g, 255 * b
	stack = []
	stack.append((xi, yi))
	while len(stack) > 0:
		x, y = stack.pop()

		if (color_pixel(width, height, x, y, size) != [r, g, b] and punto_en_poligono(x, y,vertices)):
			set_pixel(x, y, r, g, b, size)
			

		# examine surrounding pixels to see if they should be placed onto stack
		if (color_pixel(width, height, x + 1, y, size) != [r, g, b] and punto_en_poligono( x + 1, y,vertices)):
			stack.append((x + 1, y))
			

		if (color_pixel(width, height, x + 1, y + 1, size) != [r, g, b] and punto_en_poligono(x + 1, y + 1,vertices)):
			stack.append((x + 1, y + 1))
			

		if (color_pixel(width, height, x, y + 1, size) != [r, g, b] and punto_en_poligono(x, y + 1,vertices)) :
			stack.append((x, y + 1))

		if (color_pixel(width, height, x - 1, y + 1, size) != [r, g, b] and punto_en_poligono(x - 1, y + 1,vertices)) :
			stack.append((x - 1, y + 1))

		if (color_pixel(width, height, x - 1, y, size) != [r, g, b] and punto_en_poligono(x - 1, y,vertices)):
			stack.append((x - 1, y))

		if (color_pixel(width, height, x - 1, y - 1, size) != [r, g, b] and punto_en_poligono(x - 1, y - 1,vertices)):
			stack.append((x - 1, y - 1))

		if (color_pixel(width, height, x, y - 1, size) != [r, g, b] and punto_en_poligono(x, y - 1,vertices)):
			stack.append((x, y - 1))

		if (color_pixel(width, height, x + 1, y - 1, size) != [r, g, b] and  punto_en_poligono(x + 1, y - 1,vertices)):
			stack.append((x + 1, y - 1))

def Traslate(vertices, tx, ty):
	T = [
		[1, 0, tx], 
		[0, 1, ty], 
		[0, 0, 1]
	]
	result = []
	for item in vertices:
		point = np.dot(T, item)
		result.append(point)
	return result

def Rotation(vertices, angle):
	angle = math.radians(angle)
	R = [
		[math.cos(angle), -math.sin(angle), 0],
		[math.sin(angle), math.cos(angle), 0],
		[0, 0, 1]
	]
	result = []
	for item in vertices:
		point = np.dot(R, item)
		result.append(point)
	return result

def floatRgb(mag, cmin, cmax):
    """ Return a tuple of floats between 0 and 1 for R, G, and B. """
    # Normalize to 0-1
    try: x = float(mag-cmin)/(cmax-cmin)
    except ZeroDivisionError: x = 0.5 # cmax == cmin
    blue  = min((max((4*(0.75-x), 0.)), 1.))
    red   = min((max((4*(x-0.25), 0.)), 1.))
    green = min((max((4*math.fabs(x-0.5)-1., 0.)), 1.))
    return red, green, blue

### Draw
def display_openGL(width, height, scale):
	pygame.display.set_mode((width, height), pygame.OPENGL)

	glClearColor(0.0, 0.0, 0.0, 1.0)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	# glScalef(scale, scale, 0)

	gluOrtho2D(-1 * width / 2, width / 2, -1 * height / 2, height / 2)