from typing import Tuple, Optional

from src.car_detectors.car_detector import CarDetector
from src.data_types import Video, Rectangle
from src.tracker import Tracker


class Processor:
    """Facade class to simplify the use of the application.

    Args:
        car_detector: the car detector to use
        action_zone: the action zone to use. If not specified, the whole frame is used. If specified, it must be a
            tuple of 2 to 4 integers, where the first two integers are the top left corner of the action zone, and the
            last two integers are the width and height of the action zone. If only 2 integers are specified, the action
            zone is a square with the frame's width and height at the left and behind the given point.
    """

    def __init__(self, car_detector: CarDetector, action_zone: Optional[Tuple[int, ...]] = None):
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
            if isinstance(self.action_zone, tuple) and len(self.action_zone) == 2:
                x, y = self.action_zone
                self.action_zone = Rectangle(x, y, frame.width - x, frame.height - y)
            if isinstance(self.action_zone, tuple) and len(self.action_zone) == 4:
                x, y, w, h = self.action_zone
                self.action_zone = Rectangle(x, y, w, h)

            cars_rectangles = self.car_detector.detect(frame.image)
            tracker = Tracker(self.action_zone)

            cars_in_action_zone = tracker.rectangles_in_action_zone(cars_rectangles)
            frame.draw_rectangles(cars_in_action_zone)
            frame.draw_rectangle(self.action_zone, color=(0, 255, 0))

            frame.draw_text(f"Car counter: {len(cars_in_action_zone)}", (70, 20))

        return video
