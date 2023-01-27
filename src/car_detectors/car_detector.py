from typing import List, Protocol

from src.data_structures import Rectangle, Video


class CarDetector(Protocol):

    def detect(self, video: Video) -> List[List[Rectangle]]:
        pass
