from typing import Tuple, Optional, List, Union

import tqdm
from copy import deepcopy

from src.car_detectors.car_detector import CarDetector
from src.data_structures import Video, Rectangle, Frame
from src.tracker import Tracker


class Processor:
    """Facade class to simplify the use of the application.

    Args:
        car_detector: the car detector to use
        action_zone: the action zone to use. If not specified, the whole frame is used. If specified, it must be a
            tuple of 4 integers, where the first two integers are the top left corner of the action zone, and the
            last two integers are the width and height of the action zone. These two last integers can be set to None
            to use the whole width or height of the frame until the right or bottom border of the frame.
    """

    def __init__(self,
                 car_detector: CarDetector,
                 video_path: str,
                 action_zone: Optional[Union[Tuple[int, int, Optional[int], Optional[int]], Rectangle]] = None):
        self.car_detector = car_detector
        self.video = Video(video_path)
        self.action_zone = action_zone

        if self.action_zone is None:
            self.action_zone = Rectangle(0, 125, self.video.frame_width, self.video.frame_height - 125)
        if isinstance(self.action_zone, tuple):
            x, y, w, h = self.action_zone
            w = w if w is not None else self.video.frame_width - x
            h = h if h is not None else self.video.frame_height - y
            self.action_zone = Rectangle(x, y, w, h)

        self.tracker = Tracker(self.action_zone)

    def _set_action_zone(self, video_dim: Tuple[int, int]):
        if self.action_zone is None:
            self.action_zone = Rectangle(0, 125, video_dim[0], video_dim[1] - 125)
        if isinstance(self.action_zone, tuple):
            x, y, w, h = self.action_zone
            w = w if w is not None else video_dim[0] - x
            h = h if h is not None else video_dim[1] - y
            self.action_zone = Rectangle(x, y, w, h)

    def _draw_scene(self, frame: Frame, cars_in_action_zone: List[Rectangle], traces: List[List[Rectangle]]):
        frame.draw_rectangles([car_in_action_zone for car_in_action_zone in cars_in_action_zone
                               if "car" in car_in_action_zone.label])
        frame.draw_rectangle(self.action_zone, color=(0, 255, 0))
        frame.draw_text(f"Car counter: {len(cars_in_action_zone)}", (70, 20))

        for trace in traces:
            points = [rectangle.center for rectangle in trace]
            for i, point in enumerate(points):
                if i == 0:
                    continue
                frame.draw_line(points[i - 1], point, color=(0, 0, 255))

    def process_video(self) -> Video:
        """Processes the video and returns new video with detected cars."""

        new_frames = [deepcopy(frame) for frame in self.video]
        rectangles_in_video = self.car_detector.detect(self.video)

        for idx, rectangles in enumerate(rectangles_in_video):
            rectangles_in_action_zone = [rectangle for rectangle in rectangles if rectangle in self.action_zone]
            car_rectangles = [rectangle for rectangle in rectangles_in_action_zone
                              if "car" in rectangle.label.lower()]
            traces: List[List[Rectangle]] = self.tracker.track_cars(car_rectangles)
            self._draw_scene(new_frames[idx], car_rectangles, traces)

        return Video(frames=new_frames, fps=self.video.fps)
