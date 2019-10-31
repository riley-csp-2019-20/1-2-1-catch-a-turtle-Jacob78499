# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import turtle as score_writer
import turtle as counter
#-----game configuration----
shape = "arrow"
size = 5
color = "red"
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False



#-----initialize turtle-----
Randy = trtl.Turtle(shape =shape)
Randy.color(color)
Randy.shapesize(size)
score = 0
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.ht()
score_writer.speed(0)
score_writer.goto(-410, 370)
font = ("Arial", 20, "bold")
score_writer.write(score, font=font)

counter =  trtl.Turtle()
counter.ht()
counter.speed(0)
counter.penup()
counter.goto(360,370)


#-----game functions--------
def turtle_clicked(x,y):
    print("Randy was clicked")
    change_position()
    score_counter()

def turtle_size():
  global size
  if(size > 1):
    size - .5



def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.goto(0,0)
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    Randy.hideturtle()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def change_position():
    Randy.penup()
    Randy.speed(0)
    Randy.ht()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-300,300)
    Randy.goto(new_xpos, new_ypos)
    Randy.st()

def score_counter():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)


#-----events----------------
Randy.onclick(turtle_clicked)



wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
wn.bgcolor()