from typing import List, Protocol

from src.data_types import Frame, Rectangle


class CarDetector(Protocol):

    def detect(self, frame: Frame) -> List[Rectangle]:
        pass
