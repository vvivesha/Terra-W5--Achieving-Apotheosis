import time
import random
print("Welcome to Acheiving Apotheosis, where you will get to ascend to the zenith of the world, or as high as you can get.")
time.sleep(0.3)
print("Continuing to game... ")
time.sleep(0.2)
print("Your eyelids flutter as you regain your consciousness...")
time.sleep(0.1)
import turtle
screen = turtle.Screen()

width = screen.window_width()
height = screen.window_height()
n_max = (width/2) * -1  #negative max coordinate x-axis/horizontal
p_max = width/2  #positive max coordinate x-axis/horizontal
u_max = height/2
d_max = (height/2) * -1
spawn_y = (d_max / 10) * 8
spawn_dist = (d_max / 10) * 2
spawn = (0, spawn_y)
header_y = (u_max / 10 ) * 8  #now quarter_spawn_anim has to go from 8/10 aka 4/5 down to spawn.
header_dist = (u_max / 10) * 2
header = (0, header_y)
#quarter_spawn_anim = (height - (2/10 * d_max)) / 4
#header
quarter_spawn_anim = (height - (header_dist + spawn_dist)) / 4
#going to assume that a safe screen-size for most users will be -3000 to -250 and 300 to 250 ish.

level = 0
level_complete = False  #marks whether or not you finished the level. (so players can move on to the next one!!)
realm = "Colorless Realm"

screen.title(str(level) + " | Acheiving Apotheosis | " + realm)
screen.bgcolor("black")

z = turtle.Turtle()  #zenith-turtle (aka pen-turtle)
p = turtle.Turtle()  #player-turtle
s = turtle.Turtle()  #stats-turtle
p.shapesize(stretch_wid = 5, stretch_len = 5, outline = 1) #had to research this!
z.hideturtle()
s.hideturtle()
s.penup()
p.penup()
z.penup()
s.goto(p_max, u_max)  #basically, "always go to user's upper-right corner." (Will always right-align text)
p.hideturtle()
p.goto(0, -200)
p.shape("turtle")
p.fillcolor("orange")

#to see if the things work!
#p.showturtle()
#time.sleep(2)
#screen.tracer(1)
#p.goto(0, u_max)
#time.sleep(2)
#p.goto(header)
#time.sleep(2)
#p.goto(0, u_max)
#screen.tracer(1)
#p.speed(3)
#p.goto(spawn)
#time.sleep(2)

def player_coordinates():
    global player_x
    global player_y
    player_x = p.xcor()
    player_y = p.ycor()

move = False  #apparently I've been using "true" and "false" wrong (inside of strings) <-- reminder to use it properly, now and onwards.
clear_timer = 0
bounds_timer = 0
z_timer = 0 #scripts' disappearing-cue-timer.
boost_timer = 0 #spacebar's booster-timer
boost = False
#def player_coordinates():
    #global player_x
    #global player_y
    

z.pencolor("orange") #orange = script
z.write("... where am I?", align = "center", font = ("Consolas", 20, "italic"))
time.sleep(1.5)
z.penup()
#z.goto(-300, -250)
z.goto(0, 0)
z.dot(10, "gray")
time.sleep(1) #this part
z.dot(25, "gray")
time.sleep(0.09)
z.dot(50, "gray")
time.sleep(0.08)
z.dot(100, "gray")
time.sleep(0.07)
z.dot(150, "gray")
time.sleep(0.065)
z.dot(200, "gray")
time.sleep(0.06)
z.dot(250, "gray")
time.sleep(0.06)
z.dot(280, "gray")
time.sleep(0.06)
z.clear()
screen.bgcolor("gray")
time.sleep(0.01)
z.write("Woah", align = "center", font = ("Consolas", 20, "italic"))
screen.tracer(0) #instant drawings w/ turtle!! Hopefully!! :D    #MOVED from ABOVE!!!!!!!!!  #moved screen.tracer(0) from here.  *disregard these comments pls*

def intro_scene():
    for intro_scene_loop in range(4):
        #player_spawn_anim()
        p.showturtle()   #might be a bit redundant..?
        p.pencolor("white")
        time.sleep(0.1)
        p.pencolor("orange")
        time.sleep(0.8)
        p.pencolor("white")
        time.sleep(0.1)
        #p.fillcolor("gray") #or white; we'll see which looks cooler :>
        #time.sleep(0.1)

def player_spawn_anim():  #CALLING ONCE MOVES ONLY 1/4 OF WAY DOWN THE SCREEN!!!  <-- DISREGARD THAT!
    screen.tracer(0)
    p.hideturtle()
    p.setheading(0)
    p.left(90)
    p.penup()
    p.goto(header)
    p.showturtle()
    #intro_scene()
    #p.backward(quarter_spawn_anim)  #or (d_max - spawn_y) + u_max / 4     prob not that one..
    ##OR: [height - (2/10 * d_max)] / 4  <-- THISS!
    #time.sleep(0.25)  #1 second / 4    XD
    screen.tracer(1)
    p.speed(3)
    p.goto(spawn)
    intro_scene()

def player_spawn():
    global header
    p.pensize(30)
    p.hideturtle()
    p.penup()
    p.goto(header)
    p.fillcolor("orange")  #or which other color??
    for intro_scene_loop in range(4):
        player_spawn_anim()
        p.showturtle()   #might be a bit redundant..?
        p.pencolor("white")
        time.sleep(0.1)
        p.pencolor("orange")
        time.sleep(0.8)
        p.pencolor("white")
        time.sleep(0.1)
        #p.fillcolor("gray") #or white; we'll see which looks cooler :>
        #time.sleep(0.1)
    p.hideturtle()
    p.goto(spawn)  #look back at this soon/later!!
    z.clear()

def level_up():
    global level
    global realm
    z.clear()
    z.goto(0, 0)
    z.fillcolor("orange")
    z.pencolor("white")
    z.write("LEVEL " + str(level), align = "center", font = ("Impact", 30, "bold"))
    level += 1
    time.sleep(2)
    p.fillcolor("white")
    p.color("orange")
    p.goto(spawn)
    p.hideturtle()
    p.setheading(0)
    p.left(90)
    p.showturtle()
    time.sleep(2)
    z.clear()

def spawn_animation():
    global header
    global header_y
    global level
    global level_complete
    player_spawn()
    #next level: 
    if level_complete == True:
        level_up()  #for whenever you actually move up in the game's levels:
    #same level (oof):
    
#player_spawn()
player_spawn_anim()
level_up()

def bounds_timer_time():  #while True'ed
    global bounds_timer
    if bounds_timer < 0:
        bounds_timer = 0
    if bounds_timer >= 0:
        s.clear()
        s.write(".b." + str(bounds_timer) + ".t." + str(clear_timer) + ".s." + str(boost_timer), align = "right", font = ("Courier New", 5, "bold"))

def bounds_error_check():
    global bounds_timer
    global bounds_error
    global n_max
    global p_max
    global player_x
    global z_timer
    z.color("red")
    #left-side:
    if player_x < n_max:
        bounds_error = True
        z.write("Too far out!", align = "left", font = ("Consolas", 15, "underline"))
        bounds_timer += 3
    else:
        bounds_error = False
    if bounds_error == True:
        p.fillcolor("red")
        z.write("Too far out!", align = "left", font = ("Consolas", 15, "underline"))
        z_timer += 3
        bounds_timer -= 1
    #right-side:
    if player_x > p_max:
        bounds_error = True
        z.write("Too far out!", align = "left", font = ("Consolas", 15, "underline"))
        bounds_timer += 3
    else:
        bounds_error = False

def z_clear(): #script-clearing (z-turtle's doing/write cmds)
    global z_timer
    if z_timer <= 0:
        z.clear()

def trail_clear():  #while True'ed
    global move
    global clear_timer
    if move == True:
        if clear_timer > 0:
            clear_timer -= 1
        else:
            p.clear()
            clear_timer += 3

def space_boost():
    global boost_timer
    global boost
    if boost_timer < 0:
        boost_timer = 0
    if boost_timer == 0:
        boost = True
    if boost_timer >= 0:
        s.clear()
        s.write(".b." + str(bounds_timer) + ".t." + str(clear_timer) + ".s." + str(boost_timer), align = "right", font =("Courier New", 5, "bold"))

def left():
    global n_max
    global player_x
    global bounds_timer
    global boost
    global boost_timer
    p.fillcolor("orange")
    p.setheading(0) #right (positioner/angler/directional stability!!)
    if boost == False:
        p.left(180)  #left
        p.forward(10) #might need to change
        bounds_error_check()
    else: #boost == True:
        p.left(180)  #left
        p.forward(30) #also might need to change, but should stay x3 of non-boosted's move-distance.
        bounds_error_check()
        boost = False
        boost_timer += 3
        
def right():
    global p_max
    global player_x
    global bounds_timer
    global boost
    global boost_timer
    p.fillcolor("orange")
    p.setheading(0) #right
    #p.forward(10) #also might need to change
    if boost == False:
        p.forward(10)
        bounds_error_check()
    else:  #boost == False:
        p.forward(30)
        bounds_error_check()
        boost = False
        boost_timer += 3

screen.onkey(left, "Left")
screen.listen()
screen.onkey(right, "Right")
screen.listen()
screen.onkey(space_boost, "space")
screen.listen()

while True:
    #screen.title(level + " | Acheiving Apotheosis | " + realm)
    player_coordinates()
    trail_clear()  #ig this could also go under left() and right() and still function the same, but any weird movement-related glitches will be caught under this locations, so the cmd will be living over here :>
    bounds_error_check()
    bounds_timer_time()
    screen.update()