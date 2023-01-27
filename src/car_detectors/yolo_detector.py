from typing import List

import torch

from src.car_detectors.car_detector import CarDetector
from src.data_structures import Frame, Rectangle, Video


class YoloDetector(CarDetector):

    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    @staticmethod
    def _parse_results(results) -> List[Rectangle]:
        rectangles = []
        for x_min, y_min, x_max, y_max, confidence, _, name in results.pandas().xyxy[0].to_numpy():
            w = round(x_max - x_min)
            h = round(y_max - y_min)
            rectangles.append(Rectangle(round(x_min), round(y_min), w, h,
                                        label=f"class: {name} - {confidence * 100:.2f}%"))

        return rectangles

    def detect(self, video: Video) -> List[List[Rectangle]]:
        images = [frame.image for frame in video.frames]
        results = self.model.forward(images)
        return [self._parse_results(result) for result in results]

    def detect_frame(self, frame: Frame) -> List[Rectangle]:
        results = self.model(frame.image)
        return self._parse_results(results)
