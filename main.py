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

width = screen.window_width() / 2
height = screen.window_height() / 2
n_max = width * -1  #negative max coordinate x-axis/horizontal
p_max = width  #positive max coordinate x-axis/horizontal
#going to assume that a safe screen-size for most users will be -3000 to -250 and 300 to 250 ish.

screen.Title(level + " | Acheiving Apotheosis | " + realm)
screen.bgcolor("black")

z = turtle.Turtle()
p = turtle.Turtle()
p.hideturtle()
p.goto(0, -200)
p.shape("turtle")
p.fillcolor("orange")

z.color("orange") #orange = script
z.write("... where am I?", align = "center", font = ("Consolas", 20, "italic"))
time.sleep(1.5)
z.penup()
#z.goto(-300, -250)
z.goto(0, 0)
screen.tracer(0)
z.dot(10, "gray")
time.sleep(0.1)
z.clear()
z.dot(25, "gray")
time.sleep(0.09)
z.clear()
z.dot(50, "gray")
time.sleep(0.08)
z.clear()
z.dot(100, "gray")
time.sleep(0.07)
z.clear()
z.dot(150, "gray")
time.sleep(0.06)
z.clear()
z.dot(200, "gray")
time.sleep(0.05)
z.clear()
z.dot(250, "gray")
time.sleep(0.04)
z.clear()
z.dot(300, "gray")
time.sleep(0.03)
z.clear()
screen.bgcolor("gray")
time.sleep(0.01)
z.write("Woah", align = "center", font = ("Consolas", 20, "italic"))
p.showturtle()

def left():
    global n_max
    
