from typing import List, Tuple

import cv2

from .frame import Frame


class Video:

    def __init__(self, path: str):
        self.path = path
        self.video_capture: cv2.VideoCapture = cv2.VideoCapture(path)
        self.fps = self.video_capture.get(cv2.CAP_PROP_FPS)
        self.frames = None
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
        self.create_video(self.frames, path, self.fps, self.size)

    def visualize(self) -> None:
        for frame in self.frames:
            cv2.imshow("frame", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cv2.destroyAllWindows()

    @staticmethod
    def create_video(frames: List[Frame], path: str, fps: int, size: Tuple[int, int] = None) -> None:
        size = size if size is not None else (frames[0].width, frames[0].height)
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        out = cv2.VideoWriter(path, fourcc, fps, size)
        for frame in frames:
            out.write(frame)
        out.release()

    def __iter__(self):
        return iter(self.frames)
