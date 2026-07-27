from turtle import Turtle

class Ball(Turtle):
    def __init__(self, x, y):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.goto(x, y)

    def move(self):
        self.seth(45)
        self.fd(10)