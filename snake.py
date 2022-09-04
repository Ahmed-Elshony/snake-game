#simble snake game in python.
import turtle
import time
import random

delay = 0.1

#score
score = 0
high_score = 0

#set up the screen 
wn = turtle.Screen()
wn.title("snake by elshony sphinx")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)#ternes off the screen ubdates

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

#function
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction !="right":
        head.direction ="left"

def go_right():
    if head.direction !="left":
        head.direction ="right"

def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction =="down":
        y = head.ycor()
        head.sety(y - 20)  

    if head.direction =="left":
        x = head.xcor()
        head.sety(x - 20) 

    if head.direction =="right":
        x = head.xcor()
        head.sety(x + 20)     

#Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")          
wn.onkeypress(go_right, "d")

#Main game loop

while True:
    wn.update()

    #check for a collision with rhe border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop" 

        #Hiad the segments
        for segment in segments:
            segment.goto(1000, 1000)

            #clear the segments list
            segments.clear()

            #rest the score
            score = 0

            #Reset delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {} High Score: {}". format(score, high_score) ,align="center", font=("Couyrier", 24, "normal")) 

            #check for a collision with the food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y =  random.randint(-290, 290) 
        food.goto(x, y) 

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment) 

        # Shorten the delay
        delay -= 0.001

        score += 10
        
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Couyrier", 24, "normal")) 

        #move the end segments first in revese order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcore()
        y = segments[index - 1].ycore()  
        segments[index].goto(x, y)


    # Move
    if len(segments) > 0:
       x = head.xcor()
       y = head.ycor()
       segments[0].goto(x, y)

    move() 

    # Check
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop" 

            # Head the sements 
            for segment in segments:
                segment.goto(1000, 1000)
             
            segment.clear()


            score = 0

            delay = 0.1

            pen.clear()
            pen.write("Score: {} High Score: {}". format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)      
wn.mainloop()
