from typing import List

import torch

from src.car_detectors.car_detector import CarDetector
from src.data_structures import Frame, Rectangle, Video


class YoloDetector(CarDetector):
    """Car detector based on YOLOv5 model.

    Args:
        yolo_model: the YOLOv5 model to use. Can be one of 'yolov5s', 'yolov5m', 'yolov5l', 'yolov5x'.
    """

    def __init__(self, yolo_model: str = 'yolov5s'):
        self.model = torch.hub.load('ultralytics/yolov5', yolo_model, pretrained=True)

    @staticmethod
    def _parse_results(results) -> List[Rectangle]:
        rectangles = []
        for x_min, y_min, x_max, y_max, _, _, name in results.pandas().xyxy[0].to_numpy():
            w = round(x_max - x_min)
            h = round(y_max - y_min)
            rectangles.append(Rectangle(round(x_min), round(y_min), w, h,
                                        label=f"{name}"))

        return rectangles

    def detect(self, video: Video) -> List[List[Rectangle]]:
        """Detects cars in a video.

        Args:
            video: the video to detect cars in.

        Returns:
            A list of lists of rectangles. Each list of rectangles represents a frame.
        """
        images = [frame.image for frame in video.frames]
        results = self.model.forward(images)
        return [self._parse_results(result) for result in results]

    def detect_frame(self, frame: Frame) -> List[Rectangle]:
        results = self.model(frame.image)
        return self._parse_results(results)
