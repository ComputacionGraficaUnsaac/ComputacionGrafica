from utils import *
def P2():
	
	verticeslente = [(-50, 35), (-40, 40), (0, 40),(0,10),(-40,10),(-50,15)]
	verticescuerpo = [(-20,60), (20, 60), (20, 50),(30,50),(30,-40),(10,-40),(10,-30),(-10,-30),(-10,-40),(-30,-40),(-30,10),(0,10),(0,40),(-30,40),(-30,50),(-20,50)]
	verticesmochila = [(30,40), (50, 40), (50,-10), (30,-10)]
	DrawPolygon(verticescuerpo,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticeslente,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticesmochila,  255/255, 255/255, 255/255, 3)
	print("Finish...")
	glFlush()

def P1():
	x = 0
	y = 0
	set_pixel(x, y, 255/255, 255/255, 255/255, 3)
	verticeslente = [[-50, 35, 1], [-40, 40, 1], [0, 40, 1],[0,10, 1],[-40,10, 1],[-50,15, 1]]
	verticesmochila=[[30,40, 1], [50, 40, 1], [50,-10, 1],[30,-10, 1]]
	verticescuerpo=[[-20,60, 1], [20, 60, 1], [20, 50, 1],[30,50, 1],[30,-40, 1],[10,-40, 1], [10,-30, 1], [-10,-30, 1],[-10,-40, 1],[-30,-40, 1],[-30,10, 1], [0,10, 1], [0,40, 1],[-30,40, 1],[-30,50, 1],[-20,50, 1]]
	tx = -210
	ty = 0
	verticeslente2 = Traslate(verticeslente, tx, ty)
	verticescuerpo2 = Traslate(verticescuerpo, tx, ty)
	verticesmochila2 = Traslate(verticesmochila, tx, ty)
	print(verticeslente2)
	print(verticescuerpo2)
	print(verticesmochila2)
	DrawPolygon_(verticeslente2, 0/255, 255/255, 0/255,3)
	DrawPolygon_(verticescuerpo2, 0/255, 255/255, 0/255, 3)
	DrawPolygon_(verticesmochila2, 0/255, 255/255, 0/255, 3)
	glFlush()
def P3():
	x = 0
	y = 0
	set_pixel(x, y, 255/255, 255/255, 255/255, 3)
	verticeslente = [[-50, 35, 1], [-40, 40, 1], [0, 40, 1],[0,10, 1],[-40,10, 1],[-50,15, 1]]
	verticesmochila=[[30,40, 1], [50, 40, 1], [50,-10, 1],[30,-10, 1]]
	verticescuerpo=[[-20,60, 1], [20, 60, 1], [20, 50, 1],[30,50, 1],[30,-40, 1],[10,-40, 1], [10,-30, 1], [-10,-30, 1],[-10,-40, 1],[-30,-40, 1],[-30,10, 1], [0,10, 1], [0,40, 1],[-30,40, 1],[-30,50, 1],[-20,50, 1]]
	tx = 210
	ty = 0
	verticeslente2 = Traslate(verticeslente, tx, ty)
	verticescuerpo2 = Traslate(verticescuerpo, tx, ty)
	verticesmochila2 = Traslate(verticesmochila, tx, ty)
	print(verticeslente2)
	print(verticescuerpo2)
	print(verticesmochila2)
	DrawPolygon_(verticeslente2, 0/255, 255/255, 0/255,3)
	DrawPolygon_(verticescuerpo2, 0/255, 255/255, 0/255, 3)
	DrawPolygon_(verticesmochila2, 0/255, 255/255, 0/255, 3)
	glFlush()
def P11():
	x = 0
	y = 0
	set_pixel(x, y, 255/255, 255/255, 255/255, 3)
	verticeslente = [[-50, 35, 1], [-40, 40, 1], [0, 40, 1],[0,10, 1],[-40,10, 1],[-50,15, 1]]
	verticesmochila=[[30,40, 1], [50, 40, 1], [50,-10, 1],[30,-10, 1]]
	verticescuerpo=[[-20,60, 1], [20, 60, 1], [20, 50, 1],[30,50, 1],[30,-40, 1],[10,-40, 1], [10,-30, 1], [-10,-30, 1],[-10,-40, 1],[-30,-40, 1],[-30,10, 1], [0,10, 1], [0,40, 1],[-30,40, 1],[-30,50, 1],[-20,50, 1]]
	tx = -210
	ty = 0
	verticeslente2 = Traslate(verticeslente, tx, ty)
	verticescuerpo2 = Traslate(verticescuerpo, tx, ty)
	verticesmochila2 = Traslate(verticesmochila, tx, ty)
	print(verticeslente2)
	print(verticescuerpo2)
	print(verticesmochila2)
	DrawPolygon_(verticeslente2, 0/255, 255/255, 0/255,3)
	DrawPolygon_(verticescuerpo2, 0/255, 255/255, 0/255, 3)
	DrawPolygon_(verticesmochila2, 0/255, 255/255, 0/255, 3)
	#punto (40,20) dentro de la figura --> pixel semilla de la mochila
	xi2 = -170
	yi2 = 20
	SimpleSeedFill(600, 600, 1, verticesmochila2,xi2, yi2, 0/255, 255/255, 255/255)
	print("Finish...")
	glFlush()
def p12():
	x = 0
	y = 0
	set_pixel(x, y, 255/255, 255/255, 255/255, 3)
	verticeslente = [[-50, 35, 1], [-40, 40, 1], [0, 40, 1],[0,10, 1],[-40,10, 1],[-50,15, 1]]
	verticesmochila=[[30,40, 1], [50, 40, 1], [50,-10, 1],[30,-10, 1]]
	verticescuerpo=[[-20,60, 1], [20, 60, 1], [20, 50, 1],[30,50, 1],[30,-40, 1],[10,-40, 1], [10,-30, 1], [-10,-30, 1],[-10,-40, 1],[-30,-40, 1],[-30,10, 1], [0,10, 1], [0,40, 1],[-30,40, 1],[-30,50, 1],[-20,50, 1]]
	tx = -210
	ty = 0
	verticeslente2 = Traslate(verticeslente, tx, ty)
	verticescuerpo2 = Traslate(verticescuerpo, tx, ty)
	verticesmochila2 = Traslate(verticesmochila, tx, ty)
	print(verticeslente2)
	print(verticescuerpo2)
	print(verticesmochila2)
	DrawPolygon_(verticeslente2, 0/255, 255/255, 0/255,3)
	DrawPolygon_(verticescuerpo2, 0/255, 255/255, 0/255, 3)
	DrawPolygon_(verticesmochila2, 0/255, 255/255, 0/255, 3)
	#punto (40,20) dentro de la figura --> pixel semilla de la mochila
	xi2 = -170
	yi2 = 20
	#punto (0,0) dentro de la figura --> pixel semilla del cuerpo
	xi1 = -210
	yi1 = 0
	SimpleSeedFill(600, 600, 1, verticesmochila2,xi2, yi2, 0/255, 255/255, 255/255)
	SimpleSeedFill(600, 600, 1, verticescuerpo2,xi1, yi1, 0/255, 255/255, 255/255)
	print("Finish...")
	glFlush()
def P13():
	x = 0
	y = 0
	set_pixel(x, y, 255/255, 255/255, 255/255, 3)
	verticeslente = [[-50, 35, 1], [-40, 40, 1], [0, 40, 1],[0,10, 1],[-40,10, 1],[-50,15, 1]]
	verticesmochila=[[30,40, 1], [50, 40, 1], [50,-10, 1],[30,-10, 1]]
	verticescuerpo=[[-20,60, 1], [20, 60, 1], [20, 50, 1],[30,50, 1],[30,-40, 1],[10,-40, 1], [10,-30, 1], [-10,-30, 1],[-10,-40, 1],[-30,-40, 1],[-30,10, 1], [0,10, 1], [0,40, 1],[-30,40, 1],[-30,50, 1],[-20,50, 1]]
	tx = -210
	ty = 0
	verticeslente2 = Traslate(verticeslente, tx, ty)
	verticescuerpo2 = Traslate(verticescuerpo, tx, ty)
	verticesmochila2 = Traslate(verticesmochila, tx, ty)
	print(verticeslente2)
	print(verticescuerpo2)
	print(verticesmochila2)
	angle = 90
	verticeslente3 = Rotation(verticeslente2, angle)
	verticescuerpo3 = Rotation(verticescuerpo2, angle)
	verticesmochila3 = Rotation(verticesmochila2, angle)
	DrawPolygon_(verticeslente3, 0/255, 255/255, 0/255, 3)
	DrawPolygon_(verticescuerpo3, 0/255, 255/255, 0/255, 3)
	DrawPolygon_(verticesmochila3, 0/255, 255/255, 0/255, 3)
	print("Finish...")
	glFlush()

def P21():
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
	SimpleSeedFill(600, 600, 1, verticesmochila,xi2, yi2, 0/255, 255/255, 255/255)
	print("Finish...")
	glFlush()
def P22():
	#vertices de cada figura a utilizar para realizar personaje 
	verticeslente = [(-50, 35), (-40, 40), (0, 40),(0,10),(-40,10),(-50,15)]
	verticescuerpo = [(-20,60), (20, 60), (20, 50),(30,50),(30,-40),(10,-40),(10,-30),(-10,-30),(-10,-40),(-30,-40),(-30,10),(0,10),(0,40),(-30,40),(-30,50),(-20,50)]
	verticesmochila = [(30,40), (50, 40), (50,-10), (30,-10)]
	#punto (40,20) dentro de la figura --> pixel semilla de la mochila
	xi2 = 40
	yi2 = 20
	#punto (0,0) dentro de la figura --> pixel semilla del cuerpo
	xi1 = 0
	yi1 = 0
	DrawPolygon(verticescuerpo,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticeslente,  255/255, 255/255, 255/255, 3)
	DrawPolygon(verticesmochila,  255/255, 255/255, 255/255, 3)
	SimpleSeedFill(600, 600, 1, verticesmochila,xi2, yi2, 0/255, 255/255, 255/255)
	SimpleSeedFill(600, 600, 1, verticescuerpo,xi1, yi1, 0/255, 255/255, 255/255)
	print("Finish...")
	glFlush()
def P23():
	x = 0
	y = 0
	set_pixel(x, y, 255/255, 255/255, 255/255, 3)
	verticeslente = [[-50, 35, 1], [-40, 40, 1], [0, 40, 1],[0,10, 1],[-40,10, 1],[-50,15, 1]]
	verticesmochila=[[30,40, 1], [50, 40, 1], [50,-10, 1],[30,-10, 1]]
	verticescuerpo=[[-20,60, 1], [20, 60, 1], [20, 50, 1],[30,50, 1],[30,-40, 1],[10,-40, 1], [10,-30, 1], [-10,-30, 1],[-10,-40, 1],[-30,-40, 1],[-30,10, 1], [0,10, 1], [0,40, 1],[-30,40, 1],[-30,50, 1],[-20,50, 1]]
	angle = 90
	verticeslente2 = Rotation(verticeslente, angle)
	verticescuerpo2 = Rotation(verticescuerpo, angle)
	verticesmochila2 = Rotation(verticesmochila, angle)
	DrawPolygon_(verticeslente2, 0/255, 255/255, 0/255,3)
	DrawPolygon_(verticescuerpo2, 0/255, 255/255, 0/255,3)
	DrawPolygon_(verticesmochila2, 0/255, 255/255, 0/255, 3)
	print("Finish...")
	glFlush()
def P31():
	x = 0
	y = 0
	set_pixel(x, y, 255/255, 255/255, 255/255, 3)
	verticeslente = [[-50, 35, 1], [-40, 40, 1], [0, 40, 1],[0,10, 1],[-40,10, 1],[-50,15, 1]]
	verticesmochila=[[30,40, 1], [50, 40, 1], [50,-10, 1],[30,-10, 1]]
	verticescuerpo=[[-20,60, 1], [20, 60, 1], [20, 50, 1],[30,50, 1],[30,-40, 1],[10,-40, 1], [10,-30, 1], [-10,-30, 1],[-10,-40, 1],[-30,-40, 1],[-30,10, 1], [0,10, 1], [0,40, 1],[-30,40, 1],[-30,50, 1],[-20,50, 1]]
	tx = 210
	ty = 0
	verticeslente2 = Traslate(verticeslente, tx, ty)
	verticescuerpo2 = Traslate(verticescuerpo, tx, ty)
	verticesmochila2 = Traslate(verticesmochila, tx, ty)
	print(verticeslente2)
	print(verticescuerpo2)
	print(verticesmochila2)
	DrawPolygon_(verticeslente2, 0/255, 255/255, 0/255,3)
	DrawPolygon_(verticescuerpo2, 0/255, 255/255, 0/255, 3)
	DrawPolygon_(verticesmochila2, 0/255, 255/255, 0/255, 3)
	#punto (40,20) dentro de la figura --> pixel semilla de la mochila
	xi2 = 250
	yi2 = 20
	SimpleSeedFill(600, 600, 1, verticesmochila2,xi2, yi2, 0/255, 255/255, 255/255)
	print("Finish...")
	glFlush()
def P32():
	x = 0
	y = 0
	set_pixel(x, y, 255/255, 255/255, 255/255, 3)
	verticeslente = [[-50, 35, 1], [-40, 40, 1], [0, 40, 1],[0,10, 1],[-40,10, 1],[-50,15, 1]]
	verticesmochila=[[30,40, 1], [50, 40, 1], [50,-10, 1],[30,-10, 1]]
	verticescuerpo=[[-20,60, 1], [20, 60, 1], [20, 50, 1],[30,50, 1],[30,-40, 1],[10,-40, 1], [10,-30, 1], [-10,-30, 1],[-10,-40, 1],[-30,-40, 1],[-30,10, 1], [0,10, 1], [0,40, 1],[-30,40, 1],[-30,50, 1],[-20,50, 1]]
	tx = 210
	ty = 0
	verticeslente2 = Traslate(verticeslente, tx, ty)
	verticescuerpo2 = Traslate(verticescuerpo, tx, ty)
	verticesmochila2 = Traslate(verticesmochila, tx, ty)
	print(verticeslente2)
	print(verticescuerpo2)
	print(verticesmochila2)
	DrawPolygon_(verticeslente2, 0/255, 255/255, 0/255,3)
	DrawPolygon_(verticescuerpo2, 0/255, 255/255, 0/255, 3)
	DrawPolygon_(verticesmochila2, 0/255, 255/255, 0/255, 3)
	#punto (40,20) dentro de la figura --> pixel semilla de la mochila
	xi2 = 250
	yi2 = 20
	#punto (0,0) dentro de la figura --> pixel semilla del cuerpo
	xi1 = 210
	yi1 = 0
	SimpleSeedFill(600, 600, 1, verticesmochila2,xi2, yi2, 0/255, 255/255, 255/255)
	SimpleSeedFill(600, 600, 1, verticescuerpo2,xi1, yi1, 0/255, 255/255, 255/255)
	print("Finish...")
	glFlush()	
def P33():
	x = 0
	y = 0
	set_pixel(x, y, 255/255, 255/255, 255/255, 3)
	verticeslente = [[-50, 35, 1], [-40, 40, 1], [0, 40, 1],[0,10, 1],[-40,10, 1],[-50,15, 1]]
	verticesmochila=[[30,40, 1], [50, 40, 1], [50,-10, 1],[30,-10, 1]]
	verticescuerpo=[[-20,60, 1], [20, 60, 1], [20, 50, 1],[30,50, 1],[30,-40, 1],[10,-40, 1], [10,-30, 1], [-10,-30, 1],[-10,-40, 1],[-30,-40, 1],[-30,10, 1], [0,10, 1], [0,40, 1],[-30,40, 1],[-30,50, 1],[-20,50, 1]]
	tx = 210
	ty = 0
	verticeslente2 = Traslate(verticeslente, tx, ty)
	verticescuerpo2 = Traslate(verticescuerpo, tx, ty)
	verticesmochila2 = Traslate(verticesmochila, tx, ty)
	print(verticeslente2)
	print(verticescuerpo2)
	print(verticesmochila2)
	angle = 90
	verticeslente3 = Rotation(verticeslente2, angle)
	verticescuerpo3 = Rotation(verticescuerpo2, angle)
	verticesmochila3 = Rotation(verticesmochila2, angle)
	DrawPolygon_(verticeslente3, 0/255, 255/255, 0/255, 3)
	DrawPolygon_(verticescuerpo3, 0/255, 255/255, 0/255, 3)
	DrawPolygon_(verticesmochila3, 0/255, 255/255, 0/255, 3)
	print("Finish...")
	glFlush()

def mains(p,f):
	#p:es el numero de palabra ya sea palabra 1 2 3
	#f:es el numero de fallos
	# scale = 3
	# width, height = scale * 200, scale * 200
	# pygame.init()
	# pygame.display.set_caption('AHOGADO')
	# display_openGL(width, height, scale)
	# pygame.display.flip()
	if p==1:
		if f==0:
			P1()
		if f==1:
			P11()
		if f=2:
			P12()
		if f=3:
			P13()
    if p=2:
		if f=0:
			P2()
		if f=1:
			P21()
		if f=2:
			P22()
		if f=3:
			P23()
    if p=2:
		if f=0:
			P3()
		if f=1:
			P31()
		if f=2:
			P32()
		if f=3:
			P33()
	# while True:
	# 	for event in pygame.event.get():
	# 		if event.type == QUIT: