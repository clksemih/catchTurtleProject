import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("python turtle")

turtle_instance = turtle.Turtle()

def turtleForward():

        turtle_instance.forward(100)

def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading() + 10)
    #turtle_instance.right(10)

def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading() - 10)
    #turtle_instance.left(10)

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_pen_up()
    turtle_instance.home()
    turtle_pen_down()

def turtle_pen_up():
    turtle_instance.penup() #çizim yapmayı durdur
def turtle_pen_down():
    turtle_instance.pendown() # çizim yap

drawing_board.listen() # dinlemeyi başlatır.
drawing_board.onkey(fun = turtleForward ,key= "space")
drawing_board.onkey(fun = rotate_angle_right ,key= "Down")
drawing_board.onkey(fun = rotate_angle_left,key= "Up")

drawing_board.onkey(fun=clear_screen , key= "c")

drawing_board.onkey(fun=turtle_return_home , key= "h")


drawing_board.onkey(fun=turtle_pen_down , key= "w")
drawing_board.onkey(fun=turtle_pen_up , key= "q")



turtle.mainloop()
