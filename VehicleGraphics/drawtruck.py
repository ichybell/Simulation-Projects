import turtle
import random
import math

colours = (random.random(),random.random(),random.random())

# Dimensions of rectangle
rec_length = len() # Length of car is randomly generated
# rec_length= 370
rec_height = rec_length / 10

# Dimensions of roof - trapezium shape with angle of 45 degrees
roof_height = rec_height * 1.48
roof_splitter = math.sin(math.radians(45)) * roof_height
# roof splitter has same values as y since angle is 45

# Ratio of areas of rectangle and roof is 1.475
rec_area = rec_length * rec_height
roof_area = rec_area / 1.475
roof_length = (roof_area - (roof_splitter * roof_splitter)) / roof_splitter

# Dimensions of tire.
# Ratio of areas of rectangle and tires is 14.75
tire_area = rec_area / 14.75
tire_radius = math.sqrt(tire_area / math.pi)

# Dimensions for semi-circle. Use larger ratio to make circle smaller
back_tire = rec_area / 25.75
back_tire_radius = math.sqrt(back_tire / math.pi)

# Various coordinates used to draw
rec_coords= [0,0]
roof_coords = [(rec_length/4),(rec_height)]
window_1_coords = [(roof_coords[0]*1.5),roof_coords[1]]
window_2_coords = [(roof_coords[0]*3.5),roof_coords[1]]
tire_1_coords = [(rec_length/6),-(rec_height/9)]
tire_2_coords = [(rec_length/1.121),-(rec_height/9)]
back_tire_coords = [(rec_length),(rec_height/8)]

# Below code for drawing rectangular upper body
turtle.fillcolor(colours)
turtle.penup()
turtle.goto(rec_coords[0],rec_coords[1]) # rec_coords
turtle.pendown()
turtle.begin_fill()
turtle.forward(rec_length)
turtle.left(90)
turtle.forward(rec_height)
turtle.left(90)
turtle.forward(rec_length)
turtle.left(90)
turtle.forward(rec_height)
turtle.end_fill()

colours = (random.random(),random.random(),random.random())


# Below code for drawing roof and window
turtle.penup()
turtle.goto(roof_coords[0],roof_coords[1]) # roof coords
turtle.pendown()
turtle.setheading(45)
turtle.forward(roof_height)
turtle.setheading(0)
turtle.forward(roof_length)

turtle.setheading(-45)
turtle.forward(roof_height)
turtle.setheading(90)
turtle.penup()
turtle.goto(window_1_coords[0],window_1_coords[1]) # window coords
turtle.pendown()
turtle.forward(roof_splitter)
turtle.setheading(90)
turtle.penup()
turtle.goto(window_2_coords[0],window_2_coords[1]) # window coords

turtle.pendown()
turtle.forward(roof_splitter)

# Below code for drawing two tires
turtle.penup()
turtle.goto(tire_1_coords[0],tire_1_coords[1])
turtle.pendown()
turtle.fillcolor(colours)
turtle.begin_fill()
turtle.circle(tire_radius)
turtle.end_fill()
turtle.penup()
turtle.goto(tire_2_coords[0],tire_2_coords[1])
turtle.pendown()
turtle.fillcolor(colours)
turtle.begin_fill()
turtle.circle(tire_radius)
turtle.end_fill()

# Drawing back tire
turtle.penup()
turtle.goto(back_tire_coords[0],back_tire_coords[1])
turtle.pendown()
turtle.setheading(360)
turtle.fillcolor(colours)
turtle.begin_fill()
turtle.circle(back_tire_radius,180)
turtle.end_fill()
turtle.done()


