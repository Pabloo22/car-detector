from typing import List

import cv2
from copy import deepcopy
import numpy as np

from . import CarDetector
from src.data_structures import Frame, Rectangle, Video


class ClassicDetector(CarDetector):
    """Classical car detector based on difference between two frames.

    Args:
        min_area: minimum area of a rectangle to be considered a car
    """

    def __init__(self, min_area: int = 800):
        self.min_area = min_area
        self.last_frame = None

    def detect(self, video: Video) -> List[List[Rectangle]]:
        """Detects cars in a video.

        Args:
            video: the video to detect cars in.

        Returns:
            A list of lists of rectangles. Each list of rectangles represents a frame.
        """
        return [self.detect_frame(frame) for frame in video.frames]

    def detect_frame(self, frame: Frame) -> List[Rectangle]:
        """Detects cars in a frame.

        Args:
            frame: the frame to detect cars in.

        Returns:
            A list of rectangles.
        """
        rectangles = self._detect(self.last_frame.image, frame.image) if self.last_frame is not None else []
        self.last_frame = deepcopy(frame)
        return rectangles

    def _detect(self, frame1: np.ndarray, frame2: np.ndarray) -> List[Rectangle]:
        """
        Primero, hemos tomado dos frames del video, los pasamos a escala de grises y realizamos la diferencia entre
        estos fotogramas. De esta forma capturamos el movimiento de un frame a otro.
        Luego, con el resultado de esa diferencia apreciamos los coches en blanco, por lo que con un filtro de unos
        de dimensiones 5x5 realizamos una dilatación a la imagen para obtener estructuras cuadradas en vez de coches,
        y capturamos de esta forma todos los píxeles separados y que queden unidos. A continuación, aplicamos un blur
        a la imagen para eliminar los píxeles diminutos que existan en la imagen y suavizar los bordes. Por último,
        detectamos el contorno de las 'manchas blancas' y dibujamos un cuadrado alrededor.
        """
        gray_a = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray_b = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        diff_image = cv2.absdiff(gray_b, gray_a)
        ret, thresh = cv2.threshold(diff_image, 40, 255, cv2.THRESH_BINARY)
        kernel = np.ones((5, 5), np.uint8)
        dilated = cv2.dilate(thresh, kernel, iterations=4)
        filtered = cv2.medianBlur(dilated, 9)
        contours, hierarchy = cv2.findContours(filtered.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        rectangles = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < self.min_area:
                continue
            rectangles.append(Rectangle(x, y, w, h, label="car"))
        return rectangles
