from typing import Tuple, Optional

from src.car_detectors.car_detector import CarDetector
from src.data_types import Video, Rectangle
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
                 action_zone: Optional[Tuple[int, int, Optional[int], Optional[int]]] = None):
        self.car_detector = car_detector
        self.action_zone = action_zone

    def process_video(self, video_path: str) -> Video:
        """Processes video and returns new video with detected cars.

        Args:
            video_path: the path to the video to process
        """
        video = Video(video_path)
        for frame in video:
            if self.action_zone is None:
                self.action_zone = Rectangle(0, 0, frame.width, frame.height - 125)
            if isinstance(self.action_zone, tuple):
                x, y, w, h = self.action_zone
                w = w if w is not None else frame.width - x
                h = h if h is not None else frame.height - y
                self.action_zone = Rectangle(x, y, w, h)

            cars_rectangles = self.car_detector.detect(frame.image)
            tracker = Tracker(self.action_zone)

            cars_in_action_zone = tracker.rectangles_in_action_zone(cars_rectangles)
            frame.draw_rectangles(cars_in_action_zone)
            frame.draw_rectangle(self.action_zone, color=(0, 255, 0))

            frame.draw_text(f"Car counter: {len(cars_in_action_zone)}", (70, 20))

        return video
