from typing import List

import cv2
from dataclasses import dataclass, field
import numpy as np

from .types import Point, Color, Rectangle


@dataclass
class Frame:

    image: np.ndarray
    width: int = field(init=False)
    height: int = field(init=False)

    def __post_init__(self):
        self.height, self.width, _ = self.image.shape

    def draw_rectangles(self,
                        rectangles: List[Rectangle],
                        color: Color = (205, 255, 0),
                        thickness: int = 2):
        """Draws the rectangles on the frame.

                Args:
                    rectangles: the rectangles to draw
                    color: the color of the rectangles. Defaults to (205, 255, 0) (blue).
                    thickness: the thickness of the rectangles. Defaults to 2.
        """
        for rectangle in rectangles:
            x, y, w, h = rectangle
            cv2.rectangle(self.image, (x, y), (x + w, y + h), color, thickness)

    def draw_rectangle(self,
                       rectangle: Rectangle,
                       color: Color = (0, 255, 0),
                       thickness: int = 1):
        """Draws the rectangle on the frame.

        Args:
            rectangle: the rectangle to draw
            color: the color of the rectangle. Defaults to (0, 255, 0) (green).
            thickness: the thickness of the rectangle. Defaults to 1.
        """
        x, y, w, h = rectangle
        cv2.rectangle(self.image, (x, y), (x + w, y + h), color, thickness)

    def draw_text(self,
                  text: str,
                  position: Point,
                  color: Color = (0, 255, 0),
                  thickness: int = 2):
        """Draws the text on the frame.

        Args:
            text: the text to draw
            position: the position of the text
            color: the color of the text. Defaults to (0, 255, 0) (green).
            thickness: the thickness of the text. Defaults to 2.
        """
        cv2.putText(self.image, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, color, thickness)

    def draw_line(self,
                  start: Point,
                  end: Point,
                  color: Color = (0, 255, 0),
                  thickness: int = 2):
        """Draws the line on the frame.

        Args:
            start: the start of the line
            end: the end of the line
            color: the color of the line. Defaults to (0, 255, 0) (green).
            thickness: the thickness of the line. Defaults to 2.
        """
        cv2.line(self.image, start, end, color, thickness)
