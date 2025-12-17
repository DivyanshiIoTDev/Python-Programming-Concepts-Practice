
import turtle

wn=turtle.Screen()
wn.bgcolor("yellow")
wn.title("Turtle")

skk=turtle.Turtle()

#for square
for i in range(4):
    skk.forward(50)
    skk.right(90)
i=0
#for star
skk.forward(100)
skk.right(161)
skk.right(71)
skk.forward(100)

for i in range(4):
    skk.right(144)
    skk.forward(100)
skk.skup()
skk.pendown()

wn=turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
mn=turtle.Turtle()
mn.goto(0,0)
mn.pendown()
s=int(input("Input the number of sides"))#For n sided polygon
angle=90-180/s
for i in range(s):
    mn.forward(100)
    mn.left(angle)

turtle.done()
"""
#Inside_Out squares pattern
import turtle 
wn = turtle.Screen() 
wn.bgcolor("light green") 
skk = turtle.Turtle() 
skk.color("blue") 

def sqrfunc(size): 
	for i in range(4): 
		skk.forward(size) 
		skk.left(90) 
		skk.forward(size) 
		skk.left(90)
		size = size + 5

for j in range(26,147,20):
  sqrfunc(j)  

 #Drawing and filling a circle  
import turtle 

# Set up the turtle screen and set the background color to white 
screen = turtle.Screen() 
screen.bgcolor("white") 

# Create a new turtle and set its speed to the fastest possible 
pen = turtle.Turtle() 
pen.speed(0) 

# Set the fill color to red 
pen.fillcolor("red") 
pen.begin_fill(100) 

# Draw the circle with a radius of 100 pixels 
pen.circle(100) 
pen.end_fill()
# End the fill and stop drawing 
pen.end_fill() 
pen.hideturtle() #hiding turtle

# Keep the turtle window open until it is manually closed 
turtle.done() 

import turtle
turtle.Screen().bgcolor("orange")
skk=turtle.Turtle()
skk.color("yellow")
skk.shape("turtle")
skk.pendown()
skk.speed(1)

skk.fillcolor("Yellow")
skk.begin_fill()

for i in range(2):
    skk.forward(200)
    skk.left(45)
    skk.forward(100)
    skk.left(135)
skk.penup()
skk.end_fill()
skk.hideturtle()

turtle.done()

#making panda
import turtle
wn=turtle.Screen()
wn.title("Turtle")
wn.bgcolor("blue")
sk=turtle.Turtle()

def circle1(color,radius):
    
    sk.fillcolor(color)
    sk.begin_fill()
    sk.circle(radius)
    sk.end_fill()
#for 1st ear
sk.up()
sk.goto(-35,95)
circle1("black",15)
sk.down()
#for 2nd ear
sk.up()
sk.goto(35,95)
circle1("black",15)
sk.down()
#for face
sk.up()
sk.goto(0,35)
circle1("white",40)
sk.down()
# Draw first eye
sk.up()
sk.goto(-18, 75)
sk.down
circle1('black', 8)
 
# Draw second eye
sk.up()
sk.goto(18, 75)
sk.down()
circle1('black', 8)
 
##### Draw eyes white #####
 
# Draw first eye
sk.up()
sk.goto(-18, 77)
sk.down()
circle1('white', 4)
 
# Draw second eye
sk.up()
sk.goto(18, 77)
sk.down()
circle1('white', 4)
 
##### Draw nose #####
sk.up()
sk.goto(0, 55)
sk.down
circle1('black', 5)
 
##### Draw mouth #####
sk.up()
sk.goto(0, 55)
sk.down()
sk.right(90)
sk.circle(5, 180)
sk.up()
sk.goto(0, 55)
sk.down()
sk.left(360)
sk.circle(5, -180)
sk.hideturtle()

turtle.done()


#gfg code
# import package and making objects
import turtle


sc=turtle.Screen()
trtl=turtle.Turtle()
trtl.speed(0)

# method to draw y-axis lines
def drawy(val):
	
	# line
	trtl.forward(300)
	
	# set position
	trtl.up()
	trtl.setpos(val,300)
	trtl.down()
	
	# another line
	trtl.backward(300)
	
	# set position again
	trtl.up()
	trtl.setpos(val+10,0)
	trtl.down()
	
# method to draw y-axis lines
def drawx(val):
	
	# line
	trtl.forward(300)
	
	# set position
	trtl.up()
	trtl.setpos(300,val)
	trtl.down()
	
	# another line
	trtl.backward(300)
	
	# set position again
	trtl.up()
	trtl.setpos(0,val+10)
	trtl.down()
	
# method to label the graph grid
def lab():
	
	# set position
	trtl.penup()
	trtl.setpos(155,155)
	trtl.pendown()
	
	# write 0
	
	
	# set position again
	trtl.penup()
	trtl.setpos(290,155)
	trtl.pendown()
	
	# write x
	trtl.write("x",font=("Verdana", 12, "bold"))
	
	# set position again
	trtl.penup()
	trtl.setpos(155,290)
	trtl.pendown()
	
	# write y
	trtl.write("y",font=("Verdana", 12, "bold"))
	

# Main Section
# set screen
sc.setup(800,800) 

# set turtle features
trtl.speed(100)
trtl.left(90) 
trtl.color('lightgreen')

# y lines
for i in range(30):
	drawy(10*(i+1))

# set position for x lines
trtl.right(90)
trtl.up()
trtl.setpos(0,0)
trtl.down()

# x lines
for i in range(30):
	drawx(10*(i+1))

# axis 
trtl.color('green')

# set position for x axis
trtl.up()
trtl.setpos(0,150)
trtl.down()

# x-axis
trtl.forward(300)

# set position for y axis
trtl.left(90)
trtl.up()
trtl.setpos(150,0)
trtl.down()

# y-axis
trtl.forward(300)

# labeling
lab()

# hide the turtle
trtl.hideturtle()
turtle.done()

#my code
import turtle
wn=turtle.Screen()
wn.bgcolor("white")
t=turtle.Turtle()
t.shape("turtle")
t.color("green")

t.speed(0)
t.penup()
t.goto(-300,150)
t.pendown()
for i in range(50):
    t.forward(500)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(500)
    t.left(90)
    t.forward(5)
    t.left(90)
t.forward(500)
for i in range(50):
    t.left(90)
    t.pendown()
    t.forward(5)
    t.left(90)
    t.penup()
    t.forward(500)
    t.right(90)
    t.pendown()
    t.forward(5)
    t.right(90)
    t.penup()
    t.forward(500)
t.goto(195,150)
t.forward(5)
t.right(90)
t.pendown()
for i in range(50):
    t.forward(500)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(500)
    t.left(90)
    t.forward(5)
    t.left(90)
t.forward(500)
for i in range(50):
    t.left(90)
    t.pendown()
    t.forward(5)
    t.left(90)
    t.penup()
    t.forward(500)
    t.right(90)
    t.pendown()
    t.forward(5)
    t.right(90)
    t.penup()
    t.forward(500)
t.goto(-50,-300)
t.pendown()
t.forward(500)

turtle.done()


# pen.width(10) attribute for deciding width of the pen
# Import turtle package
import turtle

# Creating a turtle screen object
sc = turtle.Screen()

# Creating a turtle object(pen)
pen = turtle.Turtle()

# Defining a method to form a semicircle
# with a dynamic radius and color
def semi_circle(col, rad, val):

	# Set the fill color of the semicircle
	pen.color(col)

	# Draw a circle
	pen.circle(rad, -180)

	# Move the turtle to air
	pen.up()

	# Move the turtle to a given position
	pen.setpos(val, 0)

	# Move the turtle to the ground
	pen.down()

	pen.right(180)


# Set the colors for drawing
col = ['violet', 'indigo', 'blue', 
	'green', 'yellow', 'orange', 'red']

# Setup the screen features
sc.setup(600, 600)

# Set the screen color to black
sc.bgcolor('black')

# Setup the turtle features
pen.right(90)
pen.width(10)
pen.speed(7)

# Loop to draw 7 semicircles
for i in range(7):
	semi_circle(col[i], 10*(
	i + 8), -10*(i + 1))

# Hide the turtle
pen.hideturtle()
turtle.done()


#midsem-2 question
# Import the turtle module
import turtle


# Create a turtle object
arrow= turtle.Turtle()

def triangle1():
    arrow.fillcolor('black')
    arrow.begin_fill()
    arrow.left(90)
    arrow.forward(2)
    arrow.right(120)
    arrow.forward(4)
    arrow.right(120)
    arrow.forward(4)
    arrow.right(120)
    arrow.forward(2)
    arrow.right(90)
    arrow.end_fill()
def triangle2():
    arrow.fillcolor('black')
    arrow.begin_fill()
    arrow.right(90)
    arrow.forward(2)
    arrow.left(120)
    arrow.forward(4)
    arrow.left(120)
    arrow.forward(4)
    arrow.left(120)
    arrow.forward(2)
    arrow.left(90)
    arrow.end_fill()
for i in range(6):
        if i%2==0:
            for j in range(i,6):
                 arrow.pendown()
                 arrow.forward(20)
                 triangle1()
                 arrow.penup()
                 arrow.forward(7)
            
            print()
            arrow.right(-180)
        else:
            for j in range(i,6):
                  arrow.pendown()
                  arrow.forward(20)
                  triangle2()
                  arrow.penup()
                  arrow.forward(5)   
           
            print()
            arrow.left(-180)
    

# Keep the window open
turtle.done()
"""
#turtle module does not support line break
#pyq end sem question
#hands of a clock
import turtle
t=turtle.Turtle()
t.shape("turtle")
t.speed(0)
for i in range(0,12):
    t.penup()
    t.forward(200)
    t.pendown()
    t.forward(20)
    t.stamp() #stamping or printing the arrow or cursor shape
    t.penup()
    t.right(-180)
    t.forward(220)
    t.right(-180)
    t.left(30)

#to write something
t.write('turtle',font=("Verdana", 12, "bold"))
turtle.done()
