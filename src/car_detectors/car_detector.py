from typing import List, Protocol

from src.data_structures import Rectangle, Video, Frame


class CarDetector(Protocol):

    def detect(self, video: Video) -> List[List[Rectangle]]:
        pass

    def detect_frame(self, frame: Frame) -> List[Rectangle]:
        pass

