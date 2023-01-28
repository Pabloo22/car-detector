"""Contains the definition of the Rectangle class and of the Point and Color types"""
from typing import Tuple, Union

from dataclasses import dataclass


Point = Tuple[int, int]
Color = Tuple[int, int, int]


@dataclass(frozen=True)
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

    @property
    def center(self) -> Point:
        return self.x + self.width // 2, self.y + self.height // 2

    def __iter__(self):
        return iter((self.x, self.y, self.width, self.height))

    def __getitem__(self, key: int):
        return (self.x, self.y, self.width, self.height)[key]

    def __len__(self):
        return 4

    def __contains__(self, item: Union[Tuple[int, int], "Rectangle"]):
        if isinstance(item, Rectangle):
            x, y, w, h = item
            return (x, y) in self and (x + w, y + h) in self

        x, y = item
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def distance_to(self, other: "Rectangle") -> float:
        """Computes the distance between the center of this rectangle and the center of the other rectangle

        Args:
            other: the other rectangle

        Returns:
            the distance between the centers of the rectangles
        """
        x1, y1 = self.center
        x2, y2 = other.center
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


if __name__ == "__main__":
    import doctest

    doctest.testmod()
