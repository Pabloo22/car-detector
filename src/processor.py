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

    def _set_action_zone(self, video_dim: Tuple[int, int]):
        if self.action_zone is None:
            self.action_zone = Rectangle(0, 125, video_dim[0], video_dim[1] - 125)
        if isinstance(self.action_zone, tuple):
            x, y, w, h = self.action_zone
            w = w if w is not None else video_dim[0] - x
            h = h if h is not None else video_dim[1] - y
            self.action_zone = Rectangle(x, y, w, h)

    def _draw_scene(self, frame: Frame, cars_in_action_zone: List[Rectangle]):
        frame.draw_rectangles([car_in_action_zone for car_in_action_zone in cars_in_action_zone
                               if "car" in car_in_action_zone.label])
        frame.draw_rectangle(self.action_zone, color=(0, 255, 0))

        frame.draw_text(f"Car counter: {len(cars_in_action_zone)}", (70, 20))

    def process_video(self) -> Video:
        """Processes the video and returns new video with detected cars."""

        new_video = deepcopy(self.video)
        rectangles_in_video = self.car_detector.detect(new_video)

        for idx, rectangles in enumerate(tqdm.tqdm(rectangles_in_video)):
            car_rectangles = [rectangle for rectangle in rectangles.rectangles if "car" in rectangle.label.lower()]
            self._draw_scene(new_video[idx], car_rectangles)

        return new_video
