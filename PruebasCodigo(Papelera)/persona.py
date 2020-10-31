from utils import *
from transform import *
def personaje():
	scale = 3
	width, height = scale * 200, scale * 200
	pygame.init()
	pygame.display.set_caption('AHOGADO')
	display_openGL(width, height, scale)
	verticeslente = [(-50, 35), (-40, 40), (0, 40),(0,10),(-40,10),(-50,15)]
	verticescuerpo = [(-20,60), (20, 60), (20, 50),(30,50),(30,-40),(10,-40),(10,-30),(-10,-30),(-10,-40),(-30,-40),(-30,10),(0,10),(0,40),(-30,40),(-30,50),(-20,50)]
	verticesmochila = [(30,40), (50, 40), (50,-10), (30,-10)]
	DrawPolygon(verticescuerpo,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticeslente,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticesmochila,  255/255, 255/255, 255/255, 3)
	print("Finish...")
	glFlush()
	pygame.display.flip()
	 
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
def avanzarIzquierdaPersonaje():
	scale = 3
	width, height = scale * 200, scale * 200
	pygame.init()
	pygame.display.set_caption('C.G. I')
	display_openGL(width, height, scale)
	x = 0
	y = 0
	set_pixel(x, y, 255/255, 255/255, 255/255, scale)
	verticeslente = [[-50, 35, 1], [-40, 40, 1], [0, 40, 1],[0,10, 1],[-40,10, 1],[-50,15, 1]]
	verticesmochila=[[30,40, 1], [50, 40, 1], [50,-10, 1],[30,-10, 1]]
	verticescuerpo=[[-20,60, 1], [20, 60, 1], [20, 50, 1],[30,50, 1],[30,-40, 1],[10,-40, 1], [10,-30, 1], [-10,-30, 1],[-10,-40, 1],[-30,-40, 1],[-30,10, 1], [0,10, 1], [0,40, 1],[-30,40, 1],[-30,50, 1],[-20,50, 1]]
	tx = -250
	ty = 0
	verticeslente2 = Traslate(verticeslente, tx, ty)
	verticescuerpo2 = Traslate(verticescuerpo, tx, ty)
	verticesmochila2 = Traslate(verticesmochila, tx, ty)
	print(verticeslente2)
	print(verticescuerpo2)
	print(verticesmochila2)
	DrawPolygon_(verticeslente2, 0/255, 255/255, 0/255, scale)
	DrawPolygon_(verticescuerpo2, 0/255, 255/255, 0/255, scale)
	DrawPolygon_(verticesmochila2, 0/255, 255/255, 0/255, scale)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
def avanzarDerechaPersonaje():
	scale = 3
	width, height = scale * 200, scale * 200
	pygame.init()
	pygame.display.set_caption('C.G. I')
	display_openGL(width, height, scale)
	x = 0
	y = 0
	set_pixel(x, y, 255/255, 255/255, 255/255, scale)
	verticeslente = [[-50, 35, 1], [-40, 40, 1], [0, 40, 1],[0,10, 1],[-40,10, 1],[-50,15, 1]]
	verticesmochila=[[30,40, 1], [50, 40, 1], [50,-10, 1],[30,-10, 1]]
	verticescuerpo=[[-20,60, 1], [20, 60, 1], [20, 50, 1],[30,50, 1],[30,-40, 1],[10,-40, 1], [10,-30, 1], [-10,-30, 1],[-10,-40, 1],[-30,-40, 1],[-30,10, 1], [0,10, 1], [0,40, 1],[-30,40, 1],[-30,50, 1],[-20,50, 1]]
	tx = 250
	ty = 0
	verticeslente2 = Traslate(verticeslente, tx, ty)
	verticescuerpo2 = Traslate(verticescuerpo, tx, ty)
	verticesmochila2 = Traslate(verticesmochila, tx, ty)
	print(verticeslente2)
	print(verticescuerpo2)
	print(verticesmochila2)
	DrawPolygon_(verticeslente2, 0/255, 255/255, 0/255, scale)
	DrawPolygon_(verticescuerpo2, 0/255, 255/255, 0/255, scale)
	DrawPolygon_(verticesmochila2, 0/255, 255/255, 0/255, scale)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
def rotarPersonaje():
	scale = 3
	width, height = scale * 200, scale * 200
	pygame.init()
	pygame.display.set_caption('C.G. I')
	display_openGL(width, height, scale)
	x = 0
	y = 0
	set_pixel(x, y, 255/255, 255/255, 255/255, scale)
	verticeslente = [[-50, 35, 1], [-40, 40, 1], [0, 40, 1],[0,10, 1],[-40,10, 1],[-50,15, 1]]
	verticesmochila=[[30,40, 1], [50, 40, 1], [50,-10, 1],[30,-10, 1]]
	verticescuerpo=[[-20,60, 1], [20, 60, 1], [20, 50, 1],[30,50, 1],[30,-40, 1],[10,-40, 1], [10,-30, 1], [-10,-30, 1],[-10,-40, 1],[-30,-40, 1],[-30,10, 1], [0,10, 1], [0,40, 1],[-30,40, 1],[-30,50, 1],[-20,50, 1]]
	angle = 90
	verticeslente2 = Rotation(verticeslente, angle)
	verticescuerpo2 = Rotation(verticescuerpo, angle)
	verticesmochila2 = Rotation(verticesmochila, angle)
	DrawPolygon_(verticeslente2, 0/255, 255/255, 0/255, scale)
	DrawPolygon_(verticescuerpo2, 0/255, 255/255, 0/255, scale)
	DrawPolygon_(verticesmochila2, 0/255, 255/255, 0/255, scale)
	#punto (-30,25) dentro de la figura --> pixel semilla del lente
	xi = -30
	yi = 25
	#punto (0,0) dentro de la figura --> pixel semilla del cuerpo
	xi1 = 0
	yi1 = 0
	#punto (40,20) dentro de la figura --> pixel semilla de la mochila
	xi2 = 40
	yi2 = 20
	SimpleSeedFill(width, height, 1, verticescuerpo2, xi1, yi1, 0/255, 225/255, 225/255)
	SimpleSeedFill(width, height, 1, verticesmochila2,xi2, yi2, 0/255, 225/255, 225/255)
	SimpleSeedFill(width, height, 1, verticeslente2, xi, yi, 0/255, 255/255, 255/255)
	print("Finish...")
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
def rellenaragua1():
	scale = 3
	width, height = scale * 200, scale * 200
    #iniciando pantalla
	pygame.init()
	pygame.display.set_caption('AHOGADO')
	
	display_openGL(width, height, scale)

	#vertices de cada figura a utilizar para realizar personaje 
	verticeslente = [(-50, 35), (-40, 40), (0, 40),(0,10),(-40,10),(-50,15)]
	verticescuerpo = [(-20,60), (20, 60), (20, 50),(30,50),(30,-40),(10,-40),(10,-30),(-10,-30),(-10,-40),(-30,-40),(-30,10),(0,10),(0,40),(-30,40),(-30,50),(-20,50)]
	verticesmochila = [(30,40), (50, 40), (50,-10), (30,-10)]
	#punto (40,20) dentro de la figura --> pixel semilla de la mochila
	xi2 = 40
	yi2 = 20
	DrawPolygon(verticescuerpo,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticeslente,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticesmochila,  255/255, 255/255, 255/255, 3)
	SimpleSeedFill(width, height, 1, verticesmochila,xi2, yi2, 0/255, 255/255, 255/255)
	print("Finish...")
	#glFlush()
	pygame.display.flip()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return	
def rellenaragua3():
	scale = 3
	width, height = scale * 200, scale * 200
    #iniciando pantalla
	pygame.init()
	pygame.display.set_caption('AHOGADO')
	
	display_openGL(width, height, scale)

	#vertices de cada figura a utilizar para realizar personaje 
	verticeslente = [(-50, 35), (-40, 40), (0, 40),(0,10),(-40,10),(-50,15)]
	verticescuerpo = [(-20,60), (20, 60), (20, 50),(30,50),(30,-40),(10,-40),(10,-30),(-10,-30),(-10,-40),(-30,-40),(-30,10),(0,10),(0,40),(-30,40),(-30,50),(-20,50)]
	verticesmochila = [(30,40), (50, 40), (50,-10), (30,-10)]
	
	#punto (-30,25) dentro de la figura --> pixel semilla del lente
	xi = -30
	yi = 25
	#punto (0,0) dentro de la figura --> pixel semilla del cuerpo
	xi1 = 0
	yi1 = 0
	#punto (40,20) dentro de la figura --> pixel semilla de la mochila
	xi2 = 40
	yi2 = 20
	DrawPolygon(verticescuerpo,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticeslente,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticesmochila,  255/255, 255/255, 255/255, 3)
	SimpleSeedFill(width, height, 1, verticescuerpo, xi1, yi1, 0/255, 225/255, 225/255)
	SimpleSeedFill(width, height, 1, verticesmochila,xi2, yi2, 0/255,225/255, 225/255)
	SimpleSeedFill(width, height, 1, verticeslente, xi, yi, 0/255, 225/255, 225/255)

	print("Finish...")
	#glFlush()
	pygame.display.flip()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
def rellenaragua2():
	scale = 3
	width, height = scale * 200, scale * 200
    #iniciando pantalla
	pygame.init()
	pygame.display.set_caption('AHOGADO')
	
	display_openGL(width, height, scale)

	#vertices de cada figura a utilizar para realizar personaje 
	verticeslente = [(-50, 35), (-40, 40), (0, 40),(0,10),(-40,10),(-50,15)]
	verticescuerpo = [(-20,60), (20, 60), (20, 50),(30,50),(30,-40),(10,-40),(10,-30),(-10,-30),(-10,-40),(-30,-40),(-30,10),(0,10),(0,40),(-30,40),(-30,50),(-20,50)]
	verticesmochila = [(30,40), (50, 40), (50,-10), (30,-10)]
	#punto (0,0) dentro de la figura --> pixel semilla del cuerpo
	xi1 = 0
	yi1 = 0
	#punto (40,20) dentro de la figura --> pixel semilla de la mochila
	xi2 = 40
	yi2 = 20
	DrawPolygon(verticescuerpo,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticeslente,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticesmochila,  255/255, 255/255, 255/255, 3)
	SimpleSeedFill(width, height, 1, verticescuerpo, xi1, yi1, 0/255, 225/255, 225/255)
	SimpleSeedFill(width, height, 1, verticesmochila,xi2, yi2, 0/255,225/255, 225/255)

	print("Finish...")
	#glFlush()
	pygame.display.flip()
	 
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
if __name__ == '__main__':
	rellenaragua1()