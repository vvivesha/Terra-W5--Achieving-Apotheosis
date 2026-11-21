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
screen.tracer(0) #instant drawings w/ turtle!! Hopefully!! :D

width = screen.window_width() / 2
height = screen.window_height() / 2
n_max = width * -1  #negative max coordinate x-axis/horizontal
p_max = width  #positive max coordinate x-axis/horizontal
u_max = height
d_max = height * -1
#going to assume that a safe screen-size for most users will be -3000 to -250 and 300 to 250 ish.

level = 0
realm = "Colorless Realm"

screen.title(str(level) + " | Acheiving Apotheosis | " + realm)
screen.bgcolor("black")

z = turtle.Turtle()  #zenith-turtle (aka pen-turtle)
p = turtle.Turtle()  #player-turtle
s = turtle.Turtle()  #stats-turtle
s.hideturtle()
s.penup()
s.goto(p_max, u_max)  #basically, "always go to user's upper-right corner." (Will always right-align text)
p.hideturtle()
p.goto(0, -200)
p.shape("turtle")
p.fillcolor("orange")

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
    

z.color("orange") #orange = script
z.write("... where am I?", align = "center", font = ("Consolas", 20, "italic"))
time.sleep(1.5)
z.penup()
#z.goto(-300, -250)
z.goto(0, 0)
z.dot(10, "gray")
time.sleep(1) #this part
z.clear()
z.dot(25, "gray")
time.sleep(0.9)
z.clear()
z.dot(50, "gray")
time.sleep(0.8)
z.clear()
z.dot(100, "gray")
time.sleep(0.7)
z.clear()
z.dot(150, "gray")
time.sleep(0.6)
z.clear()
z.dot(200, "gray")
time.sleep(0.5)
z.clear()
z.dot(250, "gray")
time.sleep(0.4)
z.clear()
z.dot(300, "gray")
time.sleep(0.3)
z.clear()
screen.bgcolor("gray")
time.sleep(0.2)
z.write("Woah", align = "center", font = ("Consolas", 20, "italic"))

def player_spawn():
    for intro_scene_loop in range(4):
        p.showturtle()
        p.fillcolor("gray")
        time.sleep(0.1)
        p.fillcolor("orange")
        time.sleep(0.8)
        p.fillcolor("gray") #or white; we'll see which looks cooler :>
        time.sleep(0.1)

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
    #left-side:
    if player_x < n_max:
        bounds_error = True
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
    boost = True
    if boost_timer < 0:
        boost_timer = 0
    if boost_timer >= 0:
        s.clear()
        s.write(".b." + str(bounds_timer) + ".t." + str(clear_timer) + ".s." + str(boost_timer), align = "right", font =("Courier New", 5, "bold"))

def left():
    global n_max
    global player_x
    global bounds_timer
    p.fillcolor("orange")
    p.setheading(0) #right (positioner/angler/directional stability!!)
    if boost == True:
        p.left(180)
        p.forward(30) #also might need to change, but should stay x3 of non-boosted's move-distance.
        bounds_error_check()
        boost = False
    elif boost == False:
        p.left(180) #left
        p.forward(10) #might need to change
        bounds_error_check()
        
def right():
    global p_max
    global player_x
    global bounds_timer
    p.fillcolor("orange")
    p.setheading(0) #right
    p.forward(10) #also might need to change
    if boost == True:
        p.forward(30)
        bounds_error_check()
        boost = False
    elif boost == False:
        p.forward(10)
        bounds_error_check()

screen.onkey(left, "Left")
screen.listen()
screen.onkey(right, "Right")
screen.listen()
screen.onkey(space_boost, "space")
screen.listen()

while True:
    #screen.title(level + " | Acheiving Apotheosis | " + realm)
    trail_clear()  #ig this could also go under left() and right() and still function the same, but any weird movement-related glitches will be caught under this locations, so the cmd will be living over here :>
    bounds_error_check()
    bounds_timer_time()
    screen.update()