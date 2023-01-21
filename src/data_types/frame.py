from typing import List, Tuple

import cv2
from dataclasses import dataclass
from collections import namedtuple
import numpy as np


Rectangle = namedtuple("Rectangle", ["x", "y", "w", "h"])
LabeledRectangle = namedtuple("LabeledRectangle", ["label", "x", "y", "w", "h"])
Point = Tuple[int, int]
Color = Tuple[int, int, int]


@dataclass
class Frame:

    image: np.ndarray
    width: int = None
    height: int = None

    def draw_rectangles(self,
                        rectangles: List[Rectangle],
                        color: Color = (0, 255, 0),
                        thickness: int = 2):
        for rectangle in rectangles:
            _, x, y, w, h = rectangle
            cv2.rectangle(self.image, (x, y), (x + w, y + h), color, thickness)

    def draw_text(self,
                  text: str,
                  position: Point,
                  color: Color = (0, 255, 0),
                  thickness: int = 2):
        cv2.putText(self.image, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, color, thickness)

    def draw_line(self,
                  start: Point,
                  end: Point,
                  color: Color = (0, 255, 0),
                  thickness: int = 2):
        cv2.line(self.image, start, end, color, thickness)
