from turtle import *

class Pixel():
    def __init__(self):
        self.tortuga = Turtle()
        bgcolor("#282c34")
        setup(410,450,100,100)
        title("pixel graphic")
        self.tortuga.pensize(2)
        self.tortuga.penup()
        self.tortuga.speed(0)
        self.tortuga.hideturtle()

    def cuadrado(self):
        self.tortuga.begin_fill()
        self.tortuga.pendown()
        self.tortuga.forward(10)
        self.tortuga.left(90)
        self.tortuga.forward(10)
        self.tortuga.left(90)
        self.tortuga.forward(10)
        self.tortuga.left(90)
        self.tortuga.forward(10)
        self.tortuga.left(90)
        self.tortuga.penup()
        self.tortuga.end_fill()

    def draw(self, coordenada, colorbg):
        self.tortuga.color(colorbg)
        for i in coordenada:
            self.tortuga.goto(i)
            self.cuadrado()

    def finish(self):
        done()
            
            
        
