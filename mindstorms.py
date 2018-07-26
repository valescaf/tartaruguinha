import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("purple")
    brad.speed(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #Create the turtle Angie - Draws a circle
    #angie = turtle.Turtle()
    #angie.shape("turtle")
    #angie.color("green")
    #angie.circle(100)

    window.exitonclick()
draw_art()
