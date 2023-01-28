# import cv2

from src.car_detectors import YoloDetector
# from src.data_structures import Frame
from src import Processor


def main():

    car_detector = YoloDetector()

    # # read image with numpy
    # image = cv2.imread("data/highway.jpg")
    # frame = Frame(image)
    #
    # # detect cars
    # cars = car_detector.detect(frame)
    #
    # # draw rectangles
    # frame.draw_rectangles(cars)
    #
    # # show image
    # frame.show()

    processor = Processor(car_detector, video_path="data/video.avi")
    video = processor.process_video(n_jobs=-1)
    video.visualize()
    video.save("data/new_video_yolo_counting.avi")


if __name__ == "__main__":
    main()