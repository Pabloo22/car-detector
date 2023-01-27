from typing import List

from src.data_structures import Rectangle


class Tracker:
    """This class keeps track of the objects that are in the action zone."""

    def __init__(self, action_zone: Rectangle, tol=10):
        self.action_zone = action_zone
        self.tracked_objects = []
        self.frame_counter = 0
        self.car_counter = 0
        self.tol = tol
        self.old_rectangle_set = None

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

    def _get_distance(self, rectangle1, rectangle2):
        return ((rectangle1.x - rectangle2.x)**2 + (rectangle1.y - rectangle2.y)**2)**0.5

    def track_cars(self, new_rectangles_set):
        # old_rectangles_set: Coches en frame anterior al actual
        # new_rectangles_set: Coches en frame actual
        relations = []
        if old_rectangle_set != None:
            for car in new_rectangles_set:
                distances = [self._get_distance(car, old_car) for old_car in old_rectangles_set]
                potential_candidates = list(filter(lambda x: x <= self.tol, distances))
                if potential_candidates != []:
                    potential_candidates.sort()
                    old_me = potential_candidates[0]
                    relations.append((old_me.center, car.center))

        self.old_rectangle_set = new_rectangles_set
        return relations












