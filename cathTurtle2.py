import turtle
import random

game_over =False
#screen turtle

screen = turtle.Screen()
screen.title("catch the Turtle 2")
screen.bgcolor("light blue")
FONT = ('Arial' , 30 , 'normal')
score= 0




x_cordinates = [-20,-10,0 ,10,20]
y_cordinates = [20,10,0,-10]

turtle_list = []

#count_Down
count_down_turtle = turtle.Turtle()


#score turtle

score_turtle= turtle.Turtle()

def setup_score_turtle():
    score_turtle.color("dark blue")
    score_turtle.hideturtle()
    score_turtle.penup()

    top_height = screen.window_height()/2
    y= top_height *0.9
    score_turtle.setpos(0,y-12)
    score_turtle.write("Score : 0" , False , align="center" , font=FONT)



gridSize = 10

def make_turtle(x,y):
    t= turtle.Turtle()


    def handle_click(x,y):
        global score
        score+=1
        score_turtle.clear()
        score_turtle.write("Score : {0}".format(score) , False , align='center' , font=FONT)
        print(x,y) # kordinatları yazdırır

    t.shape("turtle")
    t.onclick(handle_click)
    t.penup()
    t.color("green")
    t.shapesize(2,2)
    t.goto(x*gridSize , y*gridSize)
    turtle_list.append(t)

def setup_turtles():
    for x in x_cordinates:
        for y in y_cordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def count_Down(time):
    global game_over
    count_down_turtle.color("dark blue")
    count_down_turtle.hideturtle()
    count_down_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9
    count_down_turtle.setposition(0,y-45)
    count_down_turtle.clear()

    if time >0 :
        count_down_turtle.clear()
        count_down_turtle.write("Time : {0}".format(time) ,False , align='center', font=FONT)
        screen.ontimer(lambda :count_Down(time-1) , 1000)

    else:
        game_over = True
        count_down_turtle.clear()
        hide_turtles()
        count_down_turtle.write("Game Over !" , False , align='center' , font=FONT)











turtle.tracer(0)
setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles_randomly()
count_Down(10)

turtle.tracer(1)
turtle.mainloop()
