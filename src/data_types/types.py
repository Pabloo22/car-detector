from typing import Tuple

from collections import namedtuple
from dataclasses import dataclass


Point = namedtuple("Point", ["x", "y"])


@dataclass
class Rectangle:
    """A rectangle defined by its top left corner and its width and height

    Args:
        x: x coordinate of the top left corner
        y: y coordinate of the top left corner
        w: width of the rectangle
        h: height of the rectangle

    Examples:
        >>> rectangle = Rectangle(0, 0, 100, 100)
        >>> rectangle.x
        0
        >>> rectangle.y
        0
        >>> point_in_rectangle = (50, 50)
        >>> point_not_in_rectangle = (150, 150)
        >>> point_in_rectangle in rectangle
        True
        >>> point_not_in_rectangle in rectangle
        False
    """

    x: int
    y: int
    w: int
    h: int

    def __iter__(self):
        return iter((self.x, self.y, self.w, self.h))

    def __getitem__(self, key):
        return (self.x, self.y, self.w, self.h)[key]

    def __len__(self):
        return 4

    def __contains__(self, item: Tuple[int, int]):
        x, y = item
        return self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h


class LabeledRectangle(Rectangle):
    """A rectangle defined by its top left corner and its width and height with a label

    Args:
        label: label of the rectangle
        x: x coordinate of the top left corner
        y: y coordinate of the top left corner
        w: width of the rectangle
        h: height of the rectangle

    Examples:
        >>> rectangle = LabeledRectangle("car", 0, 0, 100, 100)
        >>> rectangle.label
        'car'
        >>> rectangle.x
        0
        >>> rectangle.y
        0
        >>> point_in_rectangle = (50, 50)
        >>> point_not_in_rectangle = (150, 150)
        >>> point_in_rectangle in rectangle
        True
        >>> point_not_in_rectangle in rectangle
        False
    """

    def __init__(self, label: str, x: int, y: int, w: int, h: int):
        super().__init__(x, y, w, h)
        self.label = label


if __name__ == "__main__":
    import doctest

    doctest.testmod()
