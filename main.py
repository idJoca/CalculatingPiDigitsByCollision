from tkinter import *
from blocks import Block
import time
import math
desiredFrameRate = 30
#nrDigits = 3
width = 1280
height = 400

def nextDelay(): 
    global startTime
    end = (time.perf_counter())   
    elapsedTime = (end - startTime)
    delay = (1 / desiredFrameRate) - (elapsedTime) 
    startTime = (time.perf_counter())
    #print(delay)
    return delay if (delay >= 0) else 0

def calculate():
    global canvas, startTime   
    startTime = (time.perf_counter()) 
    const = 1 / (width)    
    k = 0.051
    collided = False
    canvas.delete(ALL)        
    nrCollisions = 0
    text = canvas.create_text(width/2, 72)
    nrDigits = int(digits.get())
    TimeSteps = 1
    block1 = Block(10, height, 1, desiredFrameRate, 50)
    block2 = Block(500, height, 100 **( nrDigits-1), desiredFrameRate, 100, (-100/TimeSteps))
    k = - 100
    block1.show(canvas)
    block2.show(canvas)       
    numerator = (width - block2.x + k) 
    oldNumerator = numerator
    firstTime = True
    #secondTime = False
    realNrCollisions = int(math.pi * 10 ** (nrDigits-1))
    previousNrCollisions = 0
    while(True):
        block1.setOld()
        block2.setOld()
        for i in range(0, TimeSteps):
            numerator = (width - block2.x + k)
            if (block1.x <= 0):            
                block1.vx *= -1
                #block1.x = block1.x * -1
                collided = True
            elif (block1.collide(block2)):
                collided = True
                sumOfMasses = block1.mass + block2.mass
                newV1 = (block1.mass - block2.mass) * block1.vx
                newV1 += (2 * block2.mass) * block2.vx
                newV1 /= sumOfMasses

                newV2 = (block2.mass - block1.mass) * block2.vx
                newV2 += (2 * block1.mass) * block1.vx
                newV2 /= sumOfMasses
                #block1.x -= block1.size - (x2 - x1) / 2
                #block2.x += block1.size - (x2 - x1) / 2
                block1.vx = newV1
                block2.vx = newV2
            
            if(nrCollisions == realNrCollisions and firstTime):    
                firstTime = False            
                block2.vx *= TimeSteps
                TimeSteps = 1
                break
            elif(numerator - oldNumerator > 100):
                #firstTime = False
                oldNumerator = numerator
                nrSteps = math.ceil(nrDigits * numerator * const)
                block2.vx *= TimeSteps
                block1.vx *= TimeSteps
                TimeSteps = nrSteps ** (nrSteps - 1)
                block2.vx /= TimeSteps
                block1.vx /= TimeSteps   
            if(collided):
                nrCollisions += 1          
                collided = False  
            block1.update()
            block2.update()            
        #print(block2.vx - block1.vx)
        canvas.itemconfig(text, text=str(nrCollisions))    
        canvas.itemconfig(text, font=("Courier", 72)) 
        block1.move(canvas)
        block2.move(canvas) 
        root.update()
        time.sleep(nextDelay())
    block1 = None
    block2 = None

root = Tk()
canvas = Canvas(root, width=width, height=height)
canvas.pack()


digits = Entry(root)
digits.pack()

button = Button(root, text="Simular", width=10, command=calculate)
button.pack()

root.mainloop()
