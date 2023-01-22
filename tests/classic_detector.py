from src import Processor
from src.car_detectors import ClassicDetector


def main():
    car_detector = ClassicDetector()
    app = Processor(car_detector)
    new_video = app.process_video("video.avi")
    #new_video.save("new_video.avi")
    new_video.visualize()


if __name__ == "__main__":
    main()
