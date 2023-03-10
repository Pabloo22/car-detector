from typing import List, Union, Dict, Set

from collections import defaultdict

from src.data_structures import Rectangle


class Tracker:
    """This class keeps track of the objects that are in the action zone.

    In particular, it keeps track of the traces of the objects and assigns an id to each object.

    Args:
        tol: tolerance for the distance between the center of two rectangles to be considered the same object.
        min_trace_length: minimum length of a trace to be considered a car.
    """

    def __init__(self, tol: Union[float, int] = 10, min_trace_length: int = 10):
        self.last_id = 0
        self.min_trace_length = min_trace_length
        self.tol = tol
        self.traces: Dict[int, List[Rectangle]] = defaultdict(list)
        self.active_traces: Set[int] = set()

    @property
    def car_counter(self) -> int:
        return len([trace for trace in self.traces.values() if len(trace) >= self.min_trace_length])

    def _set_car_id(self, car: Rectangle) -> int:
        """Returns the id of the car."""
        old_cars = [self.traces[trace_id][-1] for trace_id in self.active_traces]
        distances = [car.distance_to(old_car) for old_car in old_cars]
        potential_candidates = [(trace_id, distance) for trace_id, distance in zip(self.active_traces, distances)
                                if distance <= self.tol]
        if not potential_candidates:
            self.last_id += 1
            return self.last_id
        trace_id, _ = min(potential_candidates, key=lambda x: x[1])
        return trace_id

    def track_cars(self, new_rectangles_set) -> List[List[Rectangle]]:
        """Returns a

        Args:
            new_rectangles_set: the new rectangles to track

        """
        active_traces = set()
        for car in new_rectangles_set:
            trace_id = self._set_car_id(car)
            active_traces.add(trace_id)
            self.traces[trace_id].append(car)

        self.active_traces = active_traces

        return [self.traces[trace_id] for trace_id in self.active_traces]
