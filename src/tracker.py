from typing import List

from src.data_types import Frame, LabeledRectangle, Rectangle


class Tracker:

    def __init__(self, action_zone: Rectangle):
        self.action_zone = action_zone
        self.tracked_objects = []
        self.frame_counter = 0
        self.car_counter = 0

    def rectangles_in_action_zone(self, rectangles: List[LabeledRectangle]) -> List[LabeledRectangle]:
        rectangles = [rectangle for rectangle in rectangles if self._rectangle_in_action_zone(rectangle)]
        return rectangles

    def _rectangle_in_action_zone(self, rectangle: LabeledRectangle) -> bool:
        _, x, y, w, h = rectangle
        return (x, y) in self.action_zone or (x + w, y + h) in self.action_zone
