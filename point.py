#!/usr/bin/env python3
from copy import copy

class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def translated(self, dx=0, dy=0):
        point = copy(self)  # Remember, this is a shallow copy, but since all attributes are primitive types, it works.
        point.translate( dx, dy )
        return point

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)