from typing import List

import abc

from src.data_structures import Rectangle, Video, Frame


class CarDetector(abc.ABC):
    """Base class for car detectors"""

    def detect(self, video: Video) -> List[List[Rectangle]]:
        """Detects cars in a video.

        Args:
            video: the video to detect cars in.

        Returns:
            A list of lists of rectangles. Each list of rectangles represents a frame.
        """

    def detect_frame(self, frame: Frame) -> List[Rectangle]:
        """Detects cars in a frame.

        Args:
            frame: the frame to detect cars in.

        Returns:
            A list of rectangles.
        """
