from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__('square')
        self.setpos(x, y)
        self.color("white")
        self.resizemode("user")
        self.penup()
        self.seth(90)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def paddle_up(self):
        self.fd(20)
        
    def paddle_down(self):
        self.fd(-20)