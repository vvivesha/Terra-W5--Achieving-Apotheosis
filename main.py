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

def randomizer():
    global x
    global y
    global v
    global c
    x = random.randint(int(n_max), int(p_max))
    y = random.randint(int(d_max), int(u_max))
    v = random.randint(2, 50)
    c = random.randint(2, 50)

#x_co = p_max - random()
#going to assume that a safe screen-size for most users will be -3000 to -250 and 300 to 250 ish.

level = 0
level_complete = False  #marks whether or not you finished the level. (so players can move on to the next one!!)
realm = "Colorless Realm"
died = False
survive = False
level_over = False
next_b = False

screen.title(str(level) + " | Acheiving Apotheosis | " + realm)
screen.bgcolor("black")

z = turtle.Turtle()  #zenith-turtle (aka pen-turtle)
p = turtle.Turtle()  #player-turtle
s = turtle.Turtle()  #stats-turtle
b = turtle.Turtle()  #boost-turtle
p.shapesize(stretch_wid = 5, stretch_len = 5, outline = 1) #had to research this!
z.hideturtle()
s.hideturtle()
b.hideturtle()
b.penup()
b.goto(n_max, u_max)
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
rebound_trigger = False
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
    died = False
    survived = False

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
    global level_over
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
    level_over = False
    obstacles_moving()

def obstacles_moving():  #while True'ed
    global header_y
    global x
    global y
    global v
    global c
    global survive
    global died
    global level
    global level_over
    global next_b
    screen.tracer(0)
    b.goto(0, header_y)
    b.setheading(0)
    b.right(90)
    ##commented out bc it's too complex for now, but might use later!
    b.shape("square")
    b.shapesize(5, 5)
    #b.pendown()
    #b.forward(50)
    #b.right(90)
    #b.forward(25)
    #b.right(90)
    #b.forward(50)
    #b.right(90)
    #b.forward(25)
    #b.penup()
    ##next
    for obstacles in range(5):
        if next_b == True:
            randomizer()
            b.goto(x, y)
            b.shapesize(v, v)
            b.color("red")
            b.shape("square")
        #b.shape("square")
        #b.shapesize(v, v)
        #b.goto(x, y)
        #b.setheading(0)
        #b.right(90)
        #b.pendown()
        #b.forward(50)
        #b.right(90)
        #b.forward(25)
        #b.right(90)
        #b.forward(50)
        #b.right(90)
        #b.forward(25)
        #b.penup()
            if p.distance(b) > v:
                next_b = True
            if p.distance(b) < v:
                next_b = False
            if next_b == False:
                died = True
                survive = False
                level_over = False
                b.clear()
                z.clear()
                p.clear()
                player_spawn()
                #may or may not need the parts below..?
            if level_over == True:
                if p.distance(b) > v:
                    survive = True
                    died = False
                    level_up()
                    level += 1
                if p.distance(b) < v:
                    died = True
                    survive = False
                    b.clear()
                    z.clear()
                    p.clear()
                    player_spawn()

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
screen.tracer(0)

#def boost_timer_time():  #while True'ed
    #global boost_timer
    #s.clear()
    #s.write(".b." + str(bounds_timer) + ".t." + str(clear_timer) + ".s." + str(boost_timer), align = "right", font = ("Courier New", 5, "bold"))
    #if boost_timer == 0:
        #s.clear()
        #s.write(".b." + str(bounds_timer) + ".t." + str(clear_timer) + ".s." + str(boost_timer), align = "right", font = ("Courier New", 5, "bold"))

#def bounds_timer_time():  #while True'ed
    #global bounds_timer
    #if bounds_timer < 0:
        #bounds_timer = 0
    #if bounds_timer >= 0:
        #s.clear()
        #s.write(".b." + str(bounds_timer) + ".t." + str(clear_timer) + ".s." + str(boost_timer), align = "right", font = ("Courier New", 5, "bold"))

def rebound():
    global rebound_trigger
    if rebound_trigger == True:
        p.pencolor("red")
        p.backward(80)
        #p.pencolor("orange")
        #bounds_error = False #error-able

def bounds_error_check():
    global bounds_timer
    global bounds_error
    global n_max
    global p_max
    global player_x
    global z_timer
    global rebound_trigger
    z.color("red")
    #left-side:
    if player_x <= n_max:
        rebound_trigger = True
        bounds_error = True
        z.write("Too far out!", align = "left", font = ("Consolas", 15, "underline"))
        bounds_timer += 3
        #rebound()
        #time.sleep(3)
        z_clear()
    #else:
        #bounds_error = False
        #p.pencolor("orange")
    #right-side:
    elif player_x >= p_max:
        rebound_trigger = True
        bounds_error = True
        z.write("Too far out!", align = "left", font = ("Consolas", 15, "underline"))
        bounds_timer += 3
        #rebound()
        #time.sleep(3)
        z_clear()
    else:
        bounds_error = False
        p.pencolor("orange")
    if bounds_error == True:
        p.fillcolor("red")
        rebound()
        z.write("Too far out!", align = "left", font = ("Consolas", 15, "underline"))
        z_timer += 3
        bounds_timer -= 1

def z_clear(): #script-clearing (z-turtle's doing/write cmds) while True'ed
    global z_timer
    if z_timer <= 0:
        z.clear()

def trail_clear():  #while True'ed
    global move
    global clear_timer
    if move == True:
        if clear_timer > 0:
            clear_timer -= 1
            if clear_timer == 0:
                move = False
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
    global move
    global n_max
    global player_x
    global bounds_timer
    global boost
    global boost_timer
    p.fillcolor("orange")
    p.setheading(0) #right (positioner/angler/directional stability!!)
    if boost == False:
        p.pencolor("orange")
        p.left(180)  #left
        p.forward(10) #might need to change
        move = True
        bounds_error_check()
    else: #boost == True:
        p.pencolor("green")
        p.left(180)  #left
        p.forward(30) #also might need to change, but should stay x3 of non-boosted's move-distance.
        move = True
        bounds_error_check()
        boost = False
        boost_timer += 3
        
def right():
    global move
    global p_max
    global player_x
    global bounds_timer
    global boost
    global boost_timer
    p.fillcolor("orange")
    p.setheading(0) #right
    #p.forward(10) #also might need to change
    if boost == False:
        p.pencolor("orange")
        p.forward(10)
        bounds_error_check()
    else:  #boost == True:
        p.pencolor("green")
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

def timer_manager():
    global bounds_timer
    global boost_timer
    global clear_timer
    global z_timer
    if boost_timer > 0:
        boost_timer -= 1
    if bounds_timer > 0:
        bounds_timer -= 1
    if clear_timer > 0:
        clear_timer -= 1
    if z_timer > 0:
        z_timer -= 1
    s.clear()
    s.write(".b." + str(bounds_timer) + ".t." + str(clear_timer) + ".s." + str(boost_timer), align = "right", font =("Courier New", 5, "bold"))
    screen.ontimer(timer_manager, 1000)

def bounds_check_runner():
    global move
    global bounds_timer
    global bounds_error
    screen.ontimer(bounds_error_check, 1000)

timer_manager()
bounds_check_runner()

while True:
    #screen.title(level + " | Acheiving Apotheosis | " + realm)
    player_coordinates()
    trail_clear()  #ig this could also go under left() and right() and still function the same, but any weird movement-related glitches will be caught under this locations, so the cmd will be living over here :>
    bounds_error_check()
    obstacles_moving()
    #bounds_timer_time()
    #boost_timer_time()
    z_clear()
    screen.update()