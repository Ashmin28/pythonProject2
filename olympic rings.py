import turtle
#from encodings.johab import codec

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('tan')

t = turtle.Turtle()

# blue circle
t.pencolor("blue")
t.setheading(0)
t.penup()
t.goto(-80,15)
t.pendown()
t.circle(35)

# black circle
t.pencolor("black")
t.setheading(0)
t.penup()
t.goto(0,15)
t.pendown()
t.circle(35)

# red circle
t.pencolor("red")
t.setheading(0)
t.penup()
t.goto(80,15)
t.pendown()
t.circle(35)

# green circle
t.pencolor("green")
t.setheading(0)
t.penup()
t.goto(40,-15)
t.pendown()
t.circle(35)

# yellow circle
t.pencolor("yellow")
t.setheading(0)
t.penup()
t.goto(-45,-15)
t.pendown()
t.circle(35)

# writing
t.penup()
t.pencolor("purple")
t.goto(0,100)
t.write("Winter Olympics",font=("arial", 40, "bold italic"),align="center")

# writing
t.penup()
t.pencolor("purple")
t.goto(0,-100)
t.write("2026" ,font=("arial", 40, "bold italic"),align="center")



# THIS IS THE LAST LINE OF CODE
turtle.done()
