from src.car_detectors.car_detector import CarDetector
from src.data_types import Video, Rectangle
from src.tracker import Tracker


class App:
    """
    Recommended zone action: Rectangle(0, 125, frame.width, frame.height - 125)
    """

    def __init__(self, car_detector: CarDetector, action_zone: Rectangle = None):
        self.car_detector = car_detector
        self.action_zone = action_zone

    def process_video(self, video_path: str):
        video = Video(video_path)
        for frame in video:
            if self.action_zone is None:
                self.action_zone = Rectangle(0, 0, frame.width, frame.height)

            cars_rectangles = self.car_detector.detect(frame.image)
            tracker = Tracker(self.action_zone)
            cars_in_action_zone = tracker.rectangles_in_action_zone(cars_rectangles)

            frame.draw_rectangles(cars_in_action_zone)
            frame.draw_rectangle(self.action_zone, color=(0, 255, 0))

            frame.draw_text(f"Car counter: {len(cars_in_action_zone)}", (70, 20))
