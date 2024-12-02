#!/usr/bin/env python3
# The turtle module requires the tk GUI libraries
# On Mac install for your version of Python, e.g. `brew install python-tk@3.12`
# On Debian/Ubuntu flavors of Linux `sudo apt-get install python3-tk`
# On Windows it should be included with your Python3 install.
import turtle
from point import Point

class Line:
    def __init__(self, p1, p2, t:turtle.Turtle=None):
        self.t = t if t else turtle.Turtle()
        self.p1 = p1
        self.p2 = p2

    def jumpto(self):
        self.t.penup()
        self.t.goto(self.p1.x, self.p1.y)
        self.t.pendown()

    def draw(self):
        self.jumpto()
        self.t.goto(self.p2.x, self.p2.y)

    # Exercise 3
    def midpoint(self) -> Point:
        """ Computes the midpoint of a line segment and returns the result as a Point object

        :return: Point
        """
        return Point((self.p1.x + self.p2.x)/2, (self.p1.y + self.p2.y)/2 )

    def __str__(self):
        return f'Line({self.p1}, {self.p2})'

    # Exercise 02
    def __eq__(self, other):
        # The __eq__ method of Point is already overridden, so we can pass the equivalence check to the Point class
        # simply by utilizing the overloaded == operator.
        return (self.p1 == other.p1 and self.p2 == other.p2) or (self.p1 == other.p2 and self.p2 == other.p1)

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
    turt.clear()

    # Create a line object.
    line1 = Line(Point(10,10), Point(100,100), t=turt)
    # Clear the screen

    # Draw a line
    line1.draw()

    line2 = Line(Point(100,100), Point(10,10), t=turt)
    # Compare for equivalence
    print(line1 == line2)  # Should be True

    line3 = Line(Point(101,100), Point(10,10), t=turt)
    # Compare for equivalence
    print(line1 == line3)  # Should be False


    line4 = Line(Point(3,0), Point(9, 0), t=turt)
    line5 = Line(Point(0,3), Point(0, 9), t=turt)
    line6 = Line(Point(3,3), Point(9, 9), t=turt)
    print(line4.midpoint())
    print(line5.midpoint())
    print(line6.midpoint())

    # Close the turtle graphics window when clicked
    turtle.exitonclick()

if __name__ == '__main__':
    main()