from src import App
from src.car_detectors import ClassicDetector


def main():
    car_detector = ClassicDetector()
    app = App(car_detector)
    new_video = app.process_video("data/video.avi")
    new_video.save("data/new_video.avi")


if __name__ == "__main__":
    main()
