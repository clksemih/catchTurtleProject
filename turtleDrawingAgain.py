import turtle


turtle_drawing=turtle.Screen()
turtle_drawing.bgcolor("light blue")
turtle_drawing.title("python turtle")

turtle_instance = turtle.Turtle()


def turtleForward():
    turtle_instance.forward(100)

def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading() +10)

def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading() -10)

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.home()

def turtle_penup():
    turtle_instance.penup()

def turtle_pendown():
    turtle_instance.pendown()

turtle_drawing.listen()

turtle_drawing.onkey(fun = turtleForward , key = "space")
turtle_drawing.onkey(fun= rotate_angle_left , key ="Left")
turtle_drawing.onkey(fun = rotate_angle_right , key = "Right")
turtle_drawing.onkey(fun = turtle_penup , key = "q")
turtle_drawing.onkey(fun= turtle_pendown , key = "w")
turtle_drawing.onkey(fun=turtle_return_home , key="h")
turtle_drawing.onkey(fun=clear_screen , key="c")


turtle.mainloop()
