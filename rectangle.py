#!/usr/bin/env python3
from line import Line
from point import Point
import turtle

class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner.
    """

    def __init__(self, width, height, corner:Point, t:turtle.Turtle=None):
        self.t = t if t else turtle.Turtle()
        self.width = width
        self.height = height
        self.corner = corner

    def make_points(self) -> tuple[Point]:
        p1 = self.corner
        p2 = p1.translated( self.width, 0 )
        p3 = p2.translated( 0, self.height )
        p4 = p3.translated( -self.width, 0 )
        return p1, p2, p3, p4  # Returning a tuple (i.e. immutable type, but the points are mutable object references).

    def make_lines(self) -> tuple[Line]:
        p1, p2, p3, p4 = self.make_points()
        return Line( p1, p2, t=self.t ), Line( p2, p3, t=self.t ), Line( p3, p4, t=self.t ), Line( p4, p1, t=self.t )

    def draw(self):
        lines = self.make_lines()
        for line in lines:
            line.draw()

    def grow(self, dwidth, dheight):
        self.width += dwidth
        self.height += dheight

    def translate(self, dx, dy):
        self.corner.translate( dx, dy )

    # Exercise 4
    def midpoint(self) -> Point:
        """Finds the point in the center of a rectangle and returns the result as a Point object.

        :return: Point
        """
        return Point(self.corner.x + self.width / 2, self.corner.y + self.height / 2)

    def make_cross_v2(self) -> tuple[Line]:
        midpoints = []

        for line in self.make_lines():
            midpoints.append( line.midpoint() )

        p1, p2, p3, p4 = midpoints
        return Line( p1, p3, t=self.t ), Line( p2, p4, t=self.t )

    # Exercise 5
    def make_cross(self) -> list[Line]:
        """ 1. Uses make_lines to get a list of Line objects that represent the four sides of the rectangle.
            2. Computes the midpoints of the four lines.
            3. Makes and returns a list of two Line objects that represent lines connecting opposite midpoints,
               forming a cross through the middle of the rectangle."""
        cross_lines = []
        lines = self.make_lines()
        mp1 = mp2 = 0
        for i, line in enumerate(lines):
            if i == 0:
                mp1 = line.midpoint()
            elif i == 1:
                mp2 = line.midpoint()
            elif i == 2:
                cross_lines.append(Line(mp1, line.midpoint(), t=self.t))
            elif i == 3:
                cross_lines.append(Line(mp2, line.midpoint(), t=self.t))
        return cross_lines

    def __str__(self):
        return f'Rectangle({self.width}, {self.height}, {self.corner})'

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
    turt.speed(10)
    turt.clear()

    corner = Point( 20, 20 )
    rect1 = Rectangle( 100, 50, corner, t=turt)
    print( rect1 )
    rect1.draw()
    print(f"{rect1} midpoint: {rect1.midpoint()}")

    rect2 = Rectangle( 100, 50, corner, t=turt)
    print( f"Rect 2 before {rect2}" )

    from copy import deepcopy  # This will allow us to copy nested objects even.
    rect3 = deepcopy( rect2 )
    rect3.t = turt  # Have to set this since the deep copy uses __getstate__ and it ignores the turtle.
    print( f"Rect 3 before {rect3}" )

    rect2.translate( 50, 30 )
    print( f"Rect 2 after translate {rect2}" )
    rect3.grow( 100, 60 )
    print( f"Rect 3 after grow {rect3}" )

    rect2.draw()
    rect3.draw()

    print(f"{rect1} midpoint: {rect1.midpoint()}")  # rect2 was not deep-copied, so rect1's point was also translated.
    print(f"{rect2} midpoint: {rect2.midpoint()}")
    print(f"{rect3} midpoint: {rect3.midpoint()}")

    line1, line2 = rect3.make_cross()
    print(line1, line2)
    line1, line2 = rect3.make_cross_v2()
    print(line1, line2)

    line1.draw()
    line2.draw()

    # Close the turtle graphics window when clicked
    turtle.exitonclick()


if __name__ == '__main__':
    main()