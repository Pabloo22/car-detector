from typing import List, Tuple, Optional
import time
import cv2

from .frame import Frame


class Video:
    """Class for handling videos.

    It can be created from a path to a video or from a list of frames.

    Args:
        path: the path to the video. Defaults to "".
        frames: the frames to create the video from. Defaults to None.
        fps: the frames per second of the video. Only used if frames is not None. Defaults to 30.

    Raises:
        ValueError: if neither path nor frames is set
    """

    def __init__(self, path: str = "", frames: Optional[List[Frame]] = None, fps: int = 30):
        self.path = path
        if path:
            self.video_capture: cv2.VideoCapture = cv2.VideoCapture(path)
            self.fps = self.video_capture.get(cv2.CAP_PROP_FPS)
            self.frames: List[Frame] = None
            self.frame_width = int(self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.frame_height = int(self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self._set_frames()
        elif frames is not None:  # Create video from list of frames
            self.video_capture = None
            self.fps = fps
            self.frames = frames
            frame_0 = frames[0]
            self.frame_height = frame_0.height
            self.frame_width = frame_0.width
        else:
            raise ValueError("Either path or frames must be set.")

    @property
    def size(self):
        return self.frame_width, self.frame_height

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
            if cv2.waitKey(1) & 0xFF == ord("x") or cv2.getWindowProperty("frame", cv2.WND_PROP_VISIBLE) < 1:
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
        return iter(self.frames)

    def __getitem__(self, item: int) -> Frame:
        return self.frames[item]

    def __len__(self):
        return len(self.frames)
