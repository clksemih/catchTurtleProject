import turtle
import random


#screen turtle
screen = turtle.Screen()
screen.title("Catch the turtle")
screen.bgcolor("light blue")
FONT = ('Arial', 30 ,'normal')
score =0

game_over = False


#make turtles properties
x_cordinates = [-20,-10 , 0, 10,20]
y_cordinates = [20,10,0,-10]


#turtle_list
turtle_list = []


#count_down turtle

countdown_turtle = turtle.Turtle()




#score_turtle
score_turtle = turtle.Turtle()
def setup_score_turtle():

    score_turtle.color("dark blue")
    score_turtle.hideturtle()
    score_turtle.penup()

    top_height = screen.window_height() / 2  #yazı yarıdan başladığı için 2 ye böldük
    y = top_height *0.9
    score_turtle.setpos(0,y-12)
    score_turtle.write("Score : 0 " ,False , align= "center" , font=FONT)


gridSize = 10
def make_turtle(x,y):

    t= turtle.Turtle()

    def handle_click(x,y):
        global score
        score+=1
        score_turtle.clear()
        score_turtle.write("Score : {0}".format(score), False, align="center", font=FONT)
        print(x,y)



    t.shape("turtle")
    t.onclick(handle_click)
    t.penup()
    t.color("green")
    t.shapesize(2,2)
    t.goto(x* gridSize,y *gridSize)
    turtle_list.append(t)




def setup_turtles():
    for x in x_cordinates:
        for y in y_cordinates:
            make_turtle(x,y)


def hide_turtle():
    for t in turtle_list:
        t.hideturtle()


#recursive function
def show_turtles_randomly():
    if not game_over :
        hide_turtle()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)


def count_Down(time):
    global game_over
    countdown_turtle.color("dark blue")
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = screen.window_height() / 2  # yazı yarıdan başladığı için 2 ye böldük
    y = top_height * 0.9
    countdown_turtle.setposition(0, y -45)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write("Time : {0} ".format(time), False, align="center", font=FONT)
        screen.ontimer(lambda : count_Down(time-1) , 1000)

    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtle()
        countdown_turtle.write("Game Over !", False, align="center", font=FONT)






turtle.tracer(0)
setup_turtles()
hide_turtle()
show_turtles_randomly()
setup_score_turtle()
count_Down(15)
turtle.tracer(1)
turtle.mainloop()