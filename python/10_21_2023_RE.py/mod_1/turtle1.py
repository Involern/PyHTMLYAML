import turtle # Imports turtle module

t = turtle.Pen() # Creates an object with the turtle pen object

# Creates a square using t turtle object

t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

#t.clear() # resets the canvas but leaves the turtle object at where it is
t.reset() # resets the canvas and turtle position back to starting position

# Creates parallel lines using the t turtle object
t.backward(100)
t.up()
t.right(90)
t.forward(20)
t.left(90)
t.down()
t.forward(100)
t.reset()
# 

## Challenge 1 (Rectangle)
t.forward(50)
t.right(90)
t.forward(30)
t.right(90)
t.forward(50)
t.right(90)
t.forward(30)
t.reset()

## Challenge 2 (Triangle)
t.forward(50)
t.right(120)
t.forward(50)
t.right(120)
t.forward(50)
t.reset()

## Challenge 3 (Box without corners)
t.forward(80)
t.up()
t.forward(10)
t.right(90)
t.forward(10)
t.down()
t.forward(80)
t.up()
t.forward(10)
t.right(90)
t.forward(10)
t.down()
t.forward(80)
t.up()
t.forward(10)
t.right(90)
t.forward(10)
t.down()
t.forward(80)





#

turtle.done() # Keeps the turtle window open til its manually closed