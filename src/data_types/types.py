from typing import Tuple

from dataclasses import dataclass


Point = Tuple[int, int]
Color = Tuple[int, int, int]


@dataclass
class Rectangle:
    """A rectangle defined by its top left corner and its width and height

    Args:
        x: x coordinate of the top left corner
        y: y coordinate of the top left corner
        width: width of the rectangle
        height: height of the rectangle
        label: label of the rectangle

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
        >>> rectangle[0]
        0
        >>> x, y, w, h = rectangle
        >>> x
        0
        >>> labeled_rectangle = Rectangle(0, 0, 100, 100, "car")
        >>> labeled_rectangle.label
        'car'
        >>> len(labeled_rectangle)
        4
    """

    x: int
    y: int
    width: int
    height: int
    label: str = ""

    def __iter__(self):
        return iter((self.x, self.y, self.width, self.height))

    def __getitem__(self, key):
        return (self.x, self.y, self.width, self.height)[key]

    def __len__(self):
        return 4

    def __contains__(self, item: Tuple[int, int]):
        x, y = item
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height


if __name__ == "__main__":
    import doctest

    doctest.testmod()
