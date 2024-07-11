import turtle as tur
import colorsys as cs

tur.setup(800, 800)
tur.speed(0)
tur.tracer(10)
tur.width(2)
tur.bgcolor('white')  # Set a valid background color

for j in range(25):
    for i in range(15):
        color = cs.hsv_to_rgb(i/15, 1, 1)  # Adjusted color generation
        tur.color(color)
        
        tur.right(90)
        tur.circle(200 - j*8, 90)  # Adjusted radius multiplier
        tur.left(90)
        tur.circle(200 - j*8, 90)  # Adjusted radius multiplier
        tur.right(180)
        tur.circle(50, 24)

tur.hideturtle()
tur.done()
