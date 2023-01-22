from typing import List, Tuple
import time
import cv2

from .frame import Frame


class Video:

    def __init__(self, path: str):
        self.path = path
        self.video_capture: cv2.VideoCapture = cv2.VideoCapture(path)
        self.fps = self.video_capture.get(cv2.CAP_PROP_FPS)
        self.frames: List[Frame] = None
        self.frame_width = int(self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.size = (self.frame_width, self.frame_height)
        self._set_frames()

    def _set_frames(self) -> None:
        self.frames = []
        while self.video_capture.isOpened():
            ret, frame = self.video_capture.read()
            if not ret:
                break
            self.frames.append(Frame(frame))

        self.video_capture.release()

    def save(self, path: str) -> None:
        """Saves the video to the given path."""
        self.create_video(self.frames, path, self.fps, self.size)

    def visualize(self) -> None:
        """Visualizes the video."""
        for frame in self.frames:
            time.sleep((1/self.fps) - 0.021)
            cv2.imshow("frame", frame.image)
            if cv2.waitKey(1) & 0xFF == ord("x"):
                break
        cv2.destroyAllWindows()

    @staticmethod
    def create_video(frames: List[Frame], path: str, fps: int, size: Tuple[int, int] = None) -> None:
        """Creates a video from the frames.

        Args:
            frames: the frames to create the video from
            path: the path to save the video
            fps: the frames per second of the video
            size: the size of the video. Defaults to None.
        """
        size = size if size is not None else (frames[0].width, frames[0].height)
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        out = cv2.VideoWriter(path, fourcc, fps, size)
        for frame in frames:
            out.write(frame.image)
        out.release()

    def __iter__(self):
        for frame in self.frames:
            yield frame
