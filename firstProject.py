#THIS SHOULD ALWAYS BE THE FIRST LINE!
from Myro import *
init("sim") #If not already open. SHOULD ALWAYS BE SECOND COMMAND.
def draw(shape):
    return shape
 
square = [penDown(), forward(2,1), turnBy(90), forward(2,1), turnBy(90), forward(2,1), turnBy(90), forward(2,1), penUp()]
draw(square)

forward(1,1)

triangle = [penDown(), forward(2,1), turnBy(120), forward(2,1), turnBy(118), forward(2,1), penUp()]
draw(triangle)

