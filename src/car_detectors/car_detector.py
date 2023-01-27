from typing import List, Protocol

from src.data_structures import Frame, Rectangle


class CarDetector(Protocol):

    def detect(self, frame: Frame) -> List[Rectangle]:
        pass
