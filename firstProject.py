#THIS SHOULD ALWAYS BE THE FIRST LINE!
from Myro import *
init("sim") #If not already open. SHOULD ALWAYS BE SECOND COMMAND.
def draw(shape):
    return shape
 
square = [penDown(), forward(2,1), turnLeft(2.49,1), forward(2,1), turnLeft(2.49,1), forward(2,1), turnLeft(2.49,1), forward(2,1), penUp()]
draw(square)

forward(1,1)
turnLeft(2.5,1)
forward(1,.5)

triangle = [penDown(), forward(1.5,1), turnRight(3,1), forward(1.5,1), turnRight(3,1.25), forward(1.5,1), penUp()]
draw(triangle)

turnRight(2.5,1)
forward(2,1.2)