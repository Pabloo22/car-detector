from typing import List, Protocol

from src.data_types import Frame, LabeledRectangle


class CarDetector(Protocol):

    def detect(self, frame: Frame) -> List[LabeledRectangle]:
        pass
