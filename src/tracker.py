from typing import List

from src.data_structures import Rectangle


class Tracker:
    """This class keeps track of the objects that are in the action zone."""

    def __init__(self, action_zone: Rectangle):
        self.action_zone = action_zone
        self.tracked_objects = []
        self.frame_counter = 0
        self.car_counter = 0

    def rectangles_in_action_zone(self, rectangles: List[Rectangle]) -> List[Rectangle]:
        """Returns the rectangles that are in the action zone and adds them to the tracked objects.

        A rectangle is in the action zone if its top left corner and bottom right corner are in the action zone.

        Args:
            rectangles: the rectangles to check
        """
        rectangles = [rectangle for rectangle in rectangles if self._rectangle_in_action_zone(rectangle)]
        self.tracked_objects.extend(rectangles)
        return rectangles

    def _rectangle_in_action_zone(self, rectangle: Rectangle) -> bool:
        """A rectangle is in the action zone if its top left corner and bottom right corner are in the action zone."""
        x, y, w, h = rectangle
        return (x, y) in self.action_zone and (x + w, y + h) in self.action_zone
