from tkinter import *

class Block():

    def __init__(self, x, y, mass, desiredFrameRate, size, vx = 0, vy = 0):
        self.size = size
        self.x = x
        self.y = y - size
        self.vx = vx
        self.vy = vy
        self.desiredFrameRate = desiredFrameRate
        self.mass = mass        
        #Linear density

    def setOld(self):
        self.oldX = self.x
        self.oldY = self.y

    def collide(self, other):
        a = (self.x - other.x)*(self.x - other.x)
        b = (self.y - other.y)*(self.y - other.y)
        c = (self.size / 2 + other.size / 2) * (self.size / 2 + other.size / 2)  
        if (a + b < c):
            return True
        else:
            return False

    def update(self):
        self.x += (self.vx / self.desiredFrameRate)
        self.y += (self.vy / self.desiredFrameRate)

    def move(self, canvas):        
        #canvas.config(self.id, x)
        canvas.move(self.id, self.x - self.oldX, self.y - self.oldY) 

    def show(self, canvas):
        self.id = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill="black")