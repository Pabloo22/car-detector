from src import Processor
from src.car_detectors import ClassicDetector


def main():

    car_detector = ClassicDetector()
    app = Processor(car_detector, video_path="video.avi")
    new_video = app.process_video(n_jobs=1)
    #new_video.save("data/new_video_classic_detector.avi")
    new_video.visualize()

if __name__ == "__main__":
    main()
