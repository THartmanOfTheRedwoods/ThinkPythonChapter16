#!/usr/bin/env python3
from line import Line
from point import Point
import turtle

class Circle:
    """Represents a circle.

    attributes: radius, center
    """

    def __init__(self, radius, center:Point, t:turtle.Turtle=None):
        self.t = t if t else turtle.Turtle()
        self.radius = radius
        self.center = center

    def draw(self):
        start_y = self.center.y - self.radius
        self.t.penup()
        self.t.goto(self.center.x, start_y)
        self.t.pendown()
        self.t.circle(self.radius)  # I chose not to go find the arc methods from our early days of coding.

    def __str__(self):
        return f'Circle({self.radius}, {self.center})'

    def __getstate__(self):  # This method is defined to tell Python not to pickle/serialize the turtle object.
        state = self.__dict__.copy()
        del state["t"]
        return state


def main():
    # Create a window to draw in
    # Create a new turtle screen and set its background color
    screen = turtle.Screen()
    screen.bgcolor( "white" )
    # Set the width and height of the screen
    screen.setup( width=600, height=600 )
    # Create the turtle
    turt = turtle.Turtle()
    turt.speed(5)
    turt.clear()

    # Create a new circle
    circle1 = Circle(50, Point(-20, -20), t=turt)
    circle1.draw()

    # Close the turtle graphics window when clicked
    turtle.exitonclick()


if __name__ == '__main__':
    main()